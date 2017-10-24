import json


class Party:
    def __init__(self, **entries):
        self.__dict__.update(entries)


with open('election.json') as json_data:
    d = json.load(json_data)

for i in range(0, len(d)):
    # print(d[i])
    p = Party(**d[i])
    print(p.name)
