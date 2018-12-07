import unittest
from datetime import datetime

from src.day04.Record import Record, RecordType


class WhenParseRecord(unittest.TestCase):
    def test_that_it_populates_attributes_of_shift_begins(self):
        record = Record("[1518-05-08 00:02] Guard #2719 begins shift\n")

        self.assertEqual(datetime(1518, 5, 8, 0, 2), record.time)
        self.assertEqual(RecordType.SHIFT_BEGINS, record.type)
        self.assertEqual(2719, record.guard_number)

    def test_that_it_populates_attributes_of_wakes_up(self):
        record = Record("[1518-04-12 00:57] wakes up")

        self.assertEqual(datetime(1518, 4, 12, 0, 57), record.time)
        self.assertEqual(RecordType.WAKES_UP, record.type)

    def test_that_it_populates_attributes_of_falls_asleep(self):
        record = Record("[1518-11-12 00:30] falls asleep")

        self.assertEqual(datetime(1518, 11, 12, 0, 30), record.time)
        self.assertEqual(RecordType.FALLS_ASLEEP, record.type)
