from datetime import timedelta

from src.day04.Record import RecordType


class Guard:
    def __init__(self, number):
        self.number = number
        self.records = []
        self._minutes_asleep = None
        self._minutes = {}

    def append(self, record):
        self.records.append(record)
        self._invalidate()

    @property
    def minutes_asleep(self):
        if self._minutes_asleep is None:
            self._minutes_asleep = 0
            fallen_asleep_at = None
            for record in self.records:
                if record.type == RecordType.FALLS_ASLEEP:
                    fallen_asleep_at = record.time
                if record.type == RecordType.WAKES_UP:
                    was_asleep = record.time - fallen_asleep_at
                    self._minutes_asleep += was_asleep.seconds / 60
        return self._minutes_asleep

    @property
    def minutes(self):
        if self._minutes is None:
            self._minutes = {}
            for minute in range(0, 60):
                self._minutes[minute] = 0

            fallen_asleep_at = None
            for record in self.records:
                if record.type == RecordType.FALLS_ASLEEP:
                    fallen_asleep_at = record.time
                if record.type == RecordType.WAKES_UP:
                    wakes_up_at = record.time
                    time = fallen_asleep_at
                    while time < wakes_up_at:
                        if time.hour == 0:
                            self._minutes[time.minute] += 1
                        time += timedelta(minutes=1)

        return self._minutes

    @property
    def most_frequent_sleep_minute(self):
        max_frequency = 0
        max_frequency_minute = 0
        for m in self.minutes.keys():
            if max_frequency < self.minutes[m]:
                max_frequency = self.minutes[m]
                max_frequency_minute = m
        return max_frequency_minute

    def _invalidate(self):
        self._minutes_asleep = None
        self._minutes = None
