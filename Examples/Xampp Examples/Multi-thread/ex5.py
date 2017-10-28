#!C:\Users\RAJ\AppData\Local\Programs\Python\Python36\python
import queue
import threading
import time

class producer(threading.Thread):
	def __init__(self,threadid,name,q):
		threading.Thread.__init__(self)
		self.q=q
		self.threadid=threadid
		self.name=name
		self.start()
	def run(self):
		print("starting ",self.name)
		i=0
		while not stop:
				queueLock.acquire()
				if not working.full():
					self.q.put(i)
					print ("%s put %s" % (self.name, i))
					i+=1
				queueLock.release()
		
		print ("Existing producer")
			
class consumer(threading.Thread):
	def __init__(self,threadid,name,q):
		threading.Thread.__init__(self)
		self.q=q
		self.threadid=threadid
		self.name=name
		self.start()
	def run(self):
		print("starting ",self.name)
		while not stop:
				queueLock.acquire()
				if not working.empty():
					data = self.q.get()
					print ("%s got %s" % (self.name, data))
				queueLock.release()	
		print ("Existing consumer")
			
stop=0		
valueset=1
queueLock = threading.Lock()
working=queue.Queue(10)
thread1=producer(1,"producer",working)
thread2=consumer(2,"consumer",working)

time.sleep(2)
stop=1