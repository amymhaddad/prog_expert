
def new_range(start, stop, step):
    current = start 
   
    while current != stop:
        #import pdb; pdb.set_trace() 
       
        if (step > 0 and current >= stop) or (start < 0 and step > 0):
        #if (step > 0 and current >= stop) or (step < 0 and start > 0):
            raise StopIteration
     
        current += step
        yield current - step 

x = new_range(2, 5, 1)
#rint(next(x))
for num in x:
    print(num)

