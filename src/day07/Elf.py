class Elf:
    def __init__(self):
        self.work_in_progress = None
        self.completed_work = None
        self.remaining_seconds = 0

    def has_work_to_do(self):
        return self.work_in_progress is not None

    def assign(self, node):
        self.work_in_progress = node
        self.completed_work = None
        self.remaining_seconds = 60 + (ord(node.name) - ord('A') + 1)

    def work(self):
        if not self.has_work_to_do():
            return

        self.remaining_seconds -= 1

        if self.remaining_seconds == 0:
            self.completed_work = self.work_in_progress
            self.work_in_progress = None
