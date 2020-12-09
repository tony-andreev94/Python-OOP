class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @staticmethod
    def format_time(digit):
        if digit < 10:
            return f"0{digit}"
        return digit

    def get_time(self):
        hh = self.format_time(self.hours)
        mm = self.format_time(self.minutes)
        ss = self.format_time(self.seconds)
        return f"{hh}:{mm}:{ss}"

    def next_second(self):
        self.seconds += 1
        if self.seconds > Time.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > Time.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > Time.max_hours:
                    self.hours = 0
        return self.get_time()


time = Time(9, 30, 59)
print(time.next_second())
print()
time = Time(10, 59, 59)
print(time.next_second())
print()
time = Time(23, 59, 59)
print(time.next_second())
