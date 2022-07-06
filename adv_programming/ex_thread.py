from imp import load_compiled
from threading import Lock, Thread 
from time import sleep

# mutex = Lock()
# mutex.aquire() #wait for lock to become available. If mutex is already acquired by something else, we have to wait for it to be released 
# mutex.release()

"""
join - multiple threads doing work and want to ensure all threads are done before resuming 
acquire/release - (single thread) single resource that can only be used by 1 thread at a time; need to acurie and release so there are not any colisions

deadlock - can't do anything -- no thread is able to run; each thread is waiting on each other 

-join threads at the end of file 

"""
