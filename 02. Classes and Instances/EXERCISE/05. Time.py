# https://judge.softuni.bg/Contests/Practice/Index/1937#4
# 87/100


class Time:
    max_hours = 24
    max_minutes = 60
    max_seconds = 60

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        if self.hours >= 10:
            hh = self.hours
        else:
            hh = "0" + str(self.hours)

        if self.minutes >= 10:
            mm = self.minutes
        else:
            mm = "0" + str(self.minutes)

        if self.seconds >= 10:
            ss = self.seconds
        else:
            ss = "0" + str(self.seconds)

        return f"{hh}:{mm}:{ss}"

    def next_second(self):
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes >= 60:
                self.minutes = 0
                self.hours += 1
                if self.hours == 25:
                    self.hours = 1

        return self.get_time()


time = Time(9, 30, 60)
print(time.next_second())


