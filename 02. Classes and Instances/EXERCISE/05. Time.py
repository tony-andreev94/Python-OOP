# https://judge.softuni.bg/Contests/Practice/Index/1937#4

class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):  # method name could be change_time
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def hours_formatter(self):
        if self.hours < 10 or self.hours == 0:
            return f'0{self.hours}'
        return self.hours

    def minutes_formatter(self):
        if self.minutes < 10 or self.minutes == 0:
            return f'0{self.minutes}'
        return self.minutes

    def seconds_formatter(self):
        if self.seconds < 10 or self.seconds == 0:
            return f'0{self.seconds}'
        return self.seconds

    def get_time(self):
        return f"{self.hours_formatter()}:{self.minutes_formatter()}:{self.seconds_formatter()}"

    def next_second(self):
        self.seconds += 1
        if self.seconds <= self.max_seconds:
            return self.get_time()

        self.seconds = 0
        self.minutes += 1
        if self.minutes <= self.max_minutes:
            return self.get_time()

        self.minutes = 0
        self.hours += 1
        if self.hours <= self.max_hours:
            return self.get_time()

        self.hours = 0
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())
