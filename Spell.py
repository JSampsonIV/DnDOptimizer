class Spell:
    def __init__(self, name, level, casting_time, range_, duration, description):
        if not isinstance(name, str):
            raise TypeError("Spell name must be a string")
        self.name = name
        if not isinstance(level, int) or level < 0:
            raise ValueError("Spell level must be a non-negative integer, got {}".format(level))
        self.level = level
        if not isinstance(casting_time, str):
            raise TypeError("Casting time must be a string")
        self.casting_time = casting_time
        if not isinstance(range_, str):
            raise TypeError("Range must be a string")
        self.range = range_
        if not isinstance(duration, str):
            raise TypeError("Duration must be a string")
        self.duration = duration
        self.description = description

    def get_name(self):
        return self.name
    def get_level(self):
        return self.level
    def get_casting_time(self):
        return self.casting_time
    def get_range(self):
        return self.range
    def get_duration(self):
        return self.duration
    def get_description(self):
        return self.description
    def __str__(self):
        return f"{self.name} (Level {self.level}): {self.casting_time}, {self.range}, {self.duration}"
    def __repr__(self):
        return f"Spell(name={self.name}, level={self.level}, casting_time={self.casting_time}, range={self.range}, duration={self.duration})"
        