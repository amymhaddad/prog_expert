

class Range:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    def __iter__(self):
        self.current = self.start
        return self 

    def __next__(self):
        if self.step > 0 and self.current >= self.stop:
            raise StopIteration

        elif self.step < 0 and self.current <= self.stop:
            raise StopIteration
        
        self.current += self.step
        return self.current - self.step

 