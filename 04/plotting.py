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

p = figure(x_range=([x.name for x in parties]))

p.vbar(x=[x.name for x in parties],
       top=[x.share for x in parties],
       width=0.7,
       color=[x.color for x in parties],
       )
show(p)


# PART 2

share_sum_below_one = sum(x.share for i, x in enumerate(parties) if x.share < 1)

parties_above_one = []

for i in range(0, len(parties)):
    if parties[i].share > 1:
        parties_above_one.append(parties[i])

print(len(parties_above_one))

p = figure(x_range=(-1, len(parties_above_one)))
p.vbar(x=list(range(0, len(parties_above_one))),
       top=[x.share for x in parties_above_one],
       width=0.7,
       color=[x.color for x in parties_above_one],
       )
# show(p)


