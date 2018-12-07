import re
from datetime import datetime
from enum import Enum


class RecordType(Enum):
    SHIFT_BEGINS = 1
    FALLS_ASLEEP = 2
    WAKES_UP = 3


class Record:
    def __init__(self, s, guard_number=0):
        match = re.search('\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] (.*)', s)

        self.time = datetime.strptime(match.group(1), "%Y-%m-%d %H:%M")
        text = match.group(2)

        shift_begins_match = re.search('Guard #(\d+) begins shift', text)
        if shift_begins_match is not None:
            self.type = RecordType.SHIFT_BEGINS
            self.guard_number = int(shift_begins_match.group(1))
        else:
            if text == 'wakes up':
                self.type = RecordType.WAKES_UP
                self.guard_number = guard_number
            else:
                self.type = RecordType.FALLS_ASLEEP
                self.guard_number = guard_number
