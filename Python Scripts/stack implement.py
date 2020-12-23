class Stack:
	def __init__(self):
		self.stack = list()
	def push(self, item):
		self.stack.append(item)
		return(self.stack)
	def pop(self):
		if len(self.stack) == 0:
			return None
		else:
			self.stack.pop()
			return self.stack
	def peek(self):
		if len(self.stack) == 0:
			return None
		else:
			return(self.stack[len(self.stack) - 1])
		self.stack
	def __str__(self):
		str(self.stack)
