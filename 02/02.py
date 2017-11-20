import re  # regular expressions
import sqlite3


# This is a base class for objects that represent database items. It implements
# the store() method in terms of fetch_id and do_store, which need to be
# implemented in every derived class (see Person below for an example).


class DBItem:
    def __init__(self, connection):
        self.id = None
        self.cursor = connection.cursor()

    def store(self):
        self.fetch_id()
        if self.id is None:
            self.do_store()
            self.cursor.execute("select last_insert_rowid()")
            self.id = self.cursor.fetchone()[0]


# Example of a class which represents a single row of a single database table.
# This is a very simple example, since it does not contain any references to
# other objects.


class Person(DBItem):
    def __init__(self, connection, string):
        super().__init__(connection)
        if string is None:
            return

        self.name = re.sub('\([0-9+-]+\)', '', string)
        self.born = None
        self.died = None

        born_die_regex = re.compile(r".* \(([0-9]+)--([0-9]+).*\)")
        years = born_die_regex.match(string)

        if years is not None:

            born = years.group(1).strip()
            died = years.group(2).strip()

            if born:
                self.born = int(born)
            if died:
                self.died = int(died)

    def fetch_id(self):
        self.cursor.execute("SELECT id FROM person WHERE name = ? AND born = ? AND died = ?",
                            (self.name, self.born, self.died))
        self.id = self.cursor.fetchone()

    def do_store(self):
        self.cursor.execute("INSERT INTO person (name, born, died) VALUES (?, ?, ?)",
                            (self.name, self.born, self.died))


if __name__ == '__main__':

    conn = sqlite3.connect('scorelib.dat')

    keyValueRegex = re.compile(r"(.*): (.*)")

    for line in open('scorelib.txt', 'r', encoding='utf-8'):
        matchComposersWithYear = keyValueRegex.match(line)
        if matchComposersWithYear is None:
            continue

        key = matchComposersWithYear.group(1)
        value = matchComposersWithYear.group(2)

        if key == 'Composer':

            for composerWithYear in value.split(";"):
                p = Person(conn, composerWithYear.strip())
                p.store()

    conn.commit()
