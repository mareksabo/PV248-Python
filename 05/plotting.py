import json
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from math import pi


class Party:
    def __init__(self, **entries):
        self.color = None
        self.short = None
        self.__dict__.update(entries)


with open('election.json') as json_data:
    d = json.load(json_data)

parties = []

for i in range(0, len(d)):
    party = Party(**d[i])
    parties.append(party)


# PART 1

p = figure(x_range=(-1, 31))
p.vbar(x=[x.number for x in parties],
       top=[x.share for x in parties],
       width=0.7,
       color=[x.color for x in parties],
       )
show(p)


