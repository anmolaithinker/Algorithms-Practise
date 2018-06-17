
# Min Heap

class minHeap:

	# Initalized
	def __init__(self , capacity = False , capacity_value = 10):
		if capacity:
			self.capacity_value = capacity_value
			self.capacity = self.capacity
		self.heap = []
		self.heap_size = 0


	# Finding out parent	
	def parent(index):
		return (i-1)/2

	def MakeMinHeapAfterChange(index):
		while index != 0 and (self.heap[self.parent(index)] > self.heap[index]):
			self.heap[parent(index)] , self.heap[index] = self.heap[index] , self.heap[self.parent(index)] 
			index = parent(index)
		

	# MinHeapify	
	# Insert in min heap
	def insert(self , key):
		if self.capacity:
			if self.capacity_value == self.heap_size:
				print '------------------------------'
				print 'Overflow Error !!'
				print '------------------------------'
				return
		
		heap_size = heap_size + 1
		self.heap.append(key)
		# Make min heap again after change
		self.MakeMinHeapAfterChange(heap_size - 1)


					
