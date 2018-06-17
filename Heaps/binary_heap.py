
# Min Heap

class minHeap:

	# Initalized
	def __init__(self , capacity = False , capacity_value = 10):
		if capacity:
			self.capacity_value = capacity_value
			self.capacity = capacity
		self.heap = []
		self.heap_size = 0
		print '\n'
		print '-------------------------------------------'
		print 'Initializing Heap Successfulled'
		print '-------------------------------------------'


	# Finding out parent	
	def parent(self,index):
		return (index-1)/2

	def MakeMinHeapAfterChange(self,index):
		while index != 0 and (self.heap[self.parent(index)] > self.heap[index]):
			self.heap[self.parent(index)] , self.heap[index] = self.heap[index] , self.heap[self.parent(index)] 
			index = self.parent(index)
		

	
	#Debugging heap list
	def debug(self):
		print '----------------------DEBUGGING---------------'
		print 'Heap List : '
		for i in self.heap:
			print str(i)


	# Left Child

	def leftChild(self,index):
		return (2*index) + 1

	# Right Child
	def rightChild(self,index):
		return (2*index) + 2

	# MinHeapify after extracting min node	
	def MinHeapify(self,index):
		print 'Starting MinHeapify :)'

		# Take left child index
		l = self.leftChild(index)

		# Take right child index
		r = self.rightChild(index)

		# Take current element Index
		smallest = index

		if (l<self.heap_size and self.heap[l] < self.heap[smallest]):
			smallest = l

		if (r<self.heap_size and self.heap[r] < self.heap[smallest]):
			smallest = r	

		if (smallest != index):
			self.heap[index] , self.heap[smallest] = self.heap[smallest] , self.heap[index]
			self.MinHeapify(smallest)

	def extractMin(self):
		if self.heap_size <= 0:
			print '####################    Nothing to extract :( #####################'
		
		if self.heap_size == 1:
			self.heap_size = self.heap_size - 1
			element = self.heap.pop()
			return element

		element = self.heap[0]
		self.heap_size = self.heap_size - 1
		last_element = self.heap.pop()
		self.heap[0] = last_element
		self.MinHeapify(0)
		return element				

	# Insert in min heap
	def insert(self , key):
		if self.capacity:
			if self.capacity_value == self.heap_size:
				print '------------------------------'
				print 'Overflow Error !!'
				print '------------------------------'
				return
		
		self.heap_size = self.heap_size + 1
		self.heap.append(key)
		# Make min heap again after change
		heap_s = self.heap_size - 1
		self.MakeMinHeapAfterChange(heap_s)


heap = minHeap(capacity = True)
heap.insert(10)
heap.insert(9)
heap.insert(3)
heap.insert(20)
heap.insert(11)
heap.insert(4)
heap.insert(30)
heap.insert(4)
heap.debug()
print 'Min : ' + str(heap.extractMin())
heap.debug()					
print 'Min : ' + str(heap.extractMin())
heap.debug()					
print 'Min : ' + str(heap.extractMin())
heap.debug()					
print 'Min : ' + str(heap.extractMin())
heap.debug()					
