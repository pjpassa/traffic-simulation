
class Road:

    def __init__(self, length, deceleration_ratios=[(0, 1)]):
        self.length = length
        self.deceleration_ratios = deceleration_ratios

    def get_decel_ratio(self, location):
        for max_location, ratio in self.deceleration_ratios:
            if location < max_location:
                return ratio
        return 1
