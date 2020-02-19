import numpy as np

class Portfolio:
    
    def __init__(self, value, eqs):
        self.positions = []
        self.total_value = value
        self.allocated_resources = 0

        for i in range(0, len(eqs) - 1):
            new_pos = Position(eqs[i])
            self.positions.insert(new_pos)

    def today(self):
        today = self.positions[0].eq.dates[0]
        return today

    def getWeight(self, pos, date = self.today(), type = 'O'):
        amt = pos.get_price(date, type) * pos.num_shares
        return amt/allocated_resources

    def realloc(self, date = self.today()):

        predictions = np.zeros((len(self.positions), 10))

        for i,position in enumerate(positions):
            ### RUN MODEL FOR PARTICULAR EQUITY
            predictions[i, :] = ## MODEL WOULD GO HERE

        recommended_allocation = selectAssets(predictions)

        for i, position in enumerate(positions):

            curr_alloc = position.value / self.value

            diff = recommended_allocation[i] - curr_alloc

            amt = diff * self.value

            position.trade_value(amt, date)
                
    def selectAssets(o, short=False):

        evs = []

        for pred in o:
            evs.append(expected_value(pred))

        total = 0
        for i in range(len(evs)):
            if evs[i] < 0:
                evs[i] = 0
            total = total + evs[i]

        evs = evs/total

        return evs

    def expected_value(x):

        ev = 0
        bounds = [-0.9, -0.4, -0.085, -.045, -0.01, 0.01, 0.035, 0.065,
                  0.095, 0.13]

        for i in range(len(bounds)):
            ev = ev + (bounds[i] * x[i])

        return ev

    #ISSUE WITH NEEDING DATES THROUGHOUT NOW
    def variance(self, date = self.today(), days = 500, start = 'O', stop = 'C'):
        var = 0
        for i in range(0,len(positions)-1):
            var = var + (positions[i].getWeight(date, start)^2)*(Finance.variance(positions[i].eq,days, start, stop))

        return var