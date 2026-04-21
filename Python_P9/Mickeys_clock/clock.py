import time

class Clock:
    def get_time(self):
        t = time.localtime()
        minutes = t.tm_min
        seconds = t.tm_sec
        return minutes, seconds
