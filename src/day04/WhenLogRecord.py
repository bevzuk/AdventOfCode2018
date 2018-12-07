import unittest

from src.day04.Log import Log
from src.day04.Record import Record


class WhenLogRecords(unittest.TestCase):
    def test_records_are_sorted_by_time(self):
        log = Log()
        log.add(Record("[1518-12-01 00:30] wakes up"))
        log.add(Record("[1518-12-01 00:20] falls asleep"))
        log.add(Record("[1518-12-01 00:10] Guard #2719 begins shift"))

        self.assertEqual([10, 20, 30], list(map(lambda x: x.time.minute, log.records)))

    def test_guard_calculates_minutes_asleep(self):
        log = Log()
        log.add(Record("[1518-12-01 00:10] Guard #2719 begins shift"))
        log.add(Record("[1518-12-01 00:20] falls asleep", 2719))
        log.add(Record("[1518-12-01 00:25] wakes up", 2719))

        self.assertEqual(5, log.guards[2719].minutes_asleep)

    def test_guard_calculates_minutes_asleep_for_multiple_sleeps(self):
        log = Log()
        log.add(Record("[1518-12-01 00:10] Guard #2719 begins shift"))
        log.add(Record("[1518-12-01 00:20] falls asleep", 2719))
        log.add(Record("[1518-12-01 00:25] wakes up", 2719))
        log.add(Record("[1518-12-01 00:30] falls asleep", 2719))
        log.add(Record("[1518-12-01 00:40] wakes up", 2719))

        self.assertEqual(5 + 10, log.guards[2719].minutes_asleep)

    def test_guard_calculates_minutes_asleep_for_multiple_guards(self):
        log = Log()
        log.add(Record("[1518-12-01 00:10] Guard #1 begins shift"))
        log.add(Record("[1518-12-01 00:20] falls asleep", 1))
        log.add(Record("[1518-12-01 00:25] wakes up", 1))
        log.add(Record("[1518-12-01 01:10] Guard #2 begins shift"))
        log.add(Record("[1518-12-01 01:30] falls asleep", 2))
        log.add(Record("[1518-12-01 01:40] wakes up", 2))

        self.assertEqual(5, log.guards[1].minutes_asleep)
        self.assertEqual(10, log.guards[2].minutes_asleep)

    def test_guard_calculates_minutes(self):
        log = Log()
        log.add(Record("[1518-12-01 00:10] Guard #1 begins shift"))
        log.add(Record("[1518-12-01 00:20] falls asleep", 1))
        log.add(Record("[1518-12-01 00:25] wakes up", 1))

        self.assertEqual(0, log.guards[1].minutes[19])
        self.assertEqual(1, log.guards[1].minutes[20])
        self.assertEqual(1, log.guards[1].minutes[21])
        self.assertEqual(1, log.guards[1].minutes[22])
        self.assertEqual(1, log.guards[1].minutes[23])
        self.assertEqual(1, log.guards[1].minutes[24])
        self.assertEqual(0, log.guards[1].minutes[25])

    def test_guard_calculates_minutes_after_midnight(self):
        log = Log()
        log.add(Record("[1518-12-01 23:50] Guard #1 begins shift"))
        log.add(Record("[1518-12-01 23:59] falls asleep", 1))
        log.add(Record("[1518-12-02 00:01] wakes up", 1))

        self.assertEqual(1, log.guards[1].minutes[0])
        self.assertEqual(0, log.guards[1].minutes[1])
        self.assertEqual(0, log.guards[1].minutes[59])

    def test_guard_calculates_minutes_for_two_days(self):
        log = Log()
        log.add(Record("[1518-12-01 00:00] Guard #1 begins shift"))
        log.add(Record("[1518-12-01 00:00] falls asleep", 1))
        log.add(Record("[1518-12-01 00:02] wakes up", 1))
        log.add(Record("[1518-12-02 00:00] falls asleep", 1))
        log.add(Record("[1518-12-02 00:01] wakes up", 1))

        self.assertEqual(2, log.guards[1].minutes[0])
        self.assertEqual(1, log.guards[1].minutes[1])

    def test_guard_calculates_most_frequent_sleep_minute(self):
        log = Log()
        log.add(Record("[1518-12-01 00:00] Guard #1 begins shift"))
        log.add(Record("[1518-12-01 00:00] falls asleep", 1))
        log.add(Record("[1518-12-01 00:02] wakes up", 1))
        log.add(Record("[1518-12-02 00:01] falls asleep", 1))
        log.add(Record("[1518-12-02 00:02] wakes up", 1))

        self.assertEqual(1, log.guards[1].most_frequent_sleep_minute)
