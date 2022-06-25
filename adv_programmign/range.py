# class Nums:
#     def __init__(self, num1, num2, num3):
#         self.num1 = num1
#         self.num2 = num2
#         self.num3 = num3

#     def __iter__(self):
#         return Range(self.num1, self.num2, self.num3)


class Range:
    def __init__(self, start, stop, step):
        self.start = abs(start)
        self.stop = abs(stop)
        self.step = abs(step)
        self.current = abs(start)

    def __iter__(self):
        self.current = self.start
        return self 

    def __next__(self):
        #import pdb; pdb.set_trace()
        if  self.current + self.step > self.stop:
            raise StopIteration

        if abs(self.current) == abs(self.start):
            self.current += self.step
            return self.start
        
        elif self.current >= self.start and self.current <= self.stop:
            #import pdb; pdb.set_trace()
            self.current += self.step
            return self.current - self.step


nums = Range(-2, -5, -1)

for num in nums:
    print(num)

