class Queue:
	def __init__(self):
		self.queue = list()
	def enqueue(self,item):
		self.queue.append(item)
		return self.queue
	def dequeue(self):
		if len(self.queue) > 0:
			del(self.queue[0])
			return self.queue
		else:
			return None
