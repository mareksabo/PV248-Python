import requests
import xml.etree.cElementTree as etree
from dateutil import parser
from datetime import timezone

def main():
    ICAO_CODE = 'LKTB'
    DATA_SOURCE = 'https://aviationweather.gov/adds/dataserver_current/httpparam?' \
                  'dataSource=metars&requestType=retrieve&format=xml&stationString={}&hoursBeforeNow=2' \
        .format(ICAO_CODE)

    r = requests.get(DATA_SOURCE)

    root = etree.fromstring(r.content)

    for element in root.findall('.//data/METAR'):
        time = element.find('./observation_time').text
        temp = element.find('./temp_c').text
        print('{} - {}'.format(time, temp))

        utc_datetime = parser.parse(time)
        # utc_datetime.replace(tzinfo=timezone.utc).astimezone(tz=None)
        # print(utc_datetime)


if __name__ == '__main__':
    main()
