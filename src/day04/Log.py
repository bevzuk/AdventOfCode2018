from src.day04.Guard import Guard
from src.day04.Record import Record, RecordType


class Log:
    def __init__(self, file_name=None):
        self._guards = None
        if file_name is None:
            self._records = []
            return

        text_file = open(file_name, "r")
        self._records = list(map(lambda x: Record(x), text_file.readlines()))
        text_file.close()

        guard_number = 0
        for record in self.records:
            if record.type == RecordType.SHIFT_BEGINS:
                guard_number = record.guard_number
            else:
                record.guard_number = guard_number

    def add(self, record):
        self._records.append(record)

    @property
    def records(self):
        self._records.sort(key=lambda x: x.time)
        return self._records

    @property
    def guards(self):
        if self._guards is None:
            self._guards = self.create_guards()
        return self._guards

    def create_guards(self):
        _guards = {}

        for record in self.records:
            if _guards.__contains__(record.guard_number):
                _guards[record.guard_number].append(record)
            else:
                guard = Guard(record.guard_number)
                guard.append(record)
                _guards[record.guard_number] = guard

        return _guards
