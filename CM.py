class CM:
    def __init__(self, Place, Ground, Distance, DistanceType, Direction, Season, Weather, GroundCondition):
        self.Place = Place
        self.Ground = Ground
        self.Distance = Distance
        self.DistanceType = DistanceType
        self.Direction = Direction
        self.Season = Season
        self.Weather = Weather
        self.GroundCondition = GroundCondition

    def __str__(self) -> str:
        return f"{self.Place} {self.Ground} {self.Distance} {self.DistanceType} {self.Direction} {self.Season} {self.Weather} {self.GroundCondition}"