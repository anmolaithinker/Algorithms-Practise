
# Node
class Node:
	def __init__(self,key):
		self.key = key
		self.left = None
		self.right = None


# Defining a queue class
class queue:
	def __init__(self):
		self.q = []

	def push(self,key):
		self.q.push(key)

	def empty(self):
		if self.q == []:
			return True		
		else:
			return False

	def front(self):
		return self.q[0]

	def pop():
		que = self.q
		a = que[0]
					

			
# Tree
# Inorder	
def inorder(root):
	if root:
		inorder(root.left)
		print root.key
		inorder(root.right)
	
# Preorder
def preorder(root):
	if root:
		print root.key
		preorder(root.left)
		preorder(root.right)

# Postorder	
def postorder(root):
	if root:
		postorder(root.left)
		postorder(root.right)
		print root.key





root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
inorder(root)
