class maxHeap:
	'''
	needs public and private classes
	public classes like pop, push, peek
	private classes like swap, floatup, bubbledown
	'''

	def __init__(self, items = []):
		super().__init__()
		self.heap = [0]
		for item in items:
			self.heap.append(item)
			self.__floatUp(len(self.heap)-1)
			print(self.heap)
	def push(self, data):
		self.heap.append(data)
		self.__floatUp(len(self.heap)-1)
		return self.heap

	def peek(self):
		if len(self.heap) == 0:
			return None
		else:
			return self.heap[0]
	def pop(self):
		if len(self.heap) > 2:
			self.__swap(0, len(self.heap)-1)
			max = self.heap.pop()
			self.__bubbleDown(1)
		elif len(self.heap) == 2:
			max = self.heap.pop()
		else:
			max = False
		return max
	def __swap(self, i, j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
	def __floatUp(self,val):
		parent = val//2
		if self.heap[val] > self.heap[parent]:
			self.__swap(val, parent)
			self.__floatUp(parent)
		elif val == 1:
			return
	def __bubbleDown(self, index):
		left = index * 2
		right = index * 2 +1
		largest = index
		if left < (len(self.heap) -1) and self.heap[left] > self.heap[largest]:
			largest = left
		if right < (len(self.heap) -1) and right > largest:
			largest =right
		if largest != index:
			self.__swap(index, largest)
			self.__bubbleDown(largest)
	def __str__(self):
		return str(self.heap)
