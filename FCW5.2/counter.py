class Counter:
    def __init__(self):
        self.count = 0
        self.open = True

    def add(self):
        if self.open:
            self.count += 1
        else:
            raise Exception("Counter is closed.")

    def rem(self):
        if self.open:
            self.count -= 1
        else:
            raise Exception("Counter is closed.")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.open = False
        if exc_type or traceback or exc_value:
            raise

    def get_count(self):
        return self.count

    def set_count(self, count):
        self.count = count
