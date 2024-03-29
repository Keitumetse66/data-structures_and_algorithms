

class node:
	def __init__(self, data=None):
		self.data = data
		self.next = None

class linked_list:
	def __init__(self):
		self.head = node()

	def append(self, data):
		new_node = node(data)
		current = self.head
		while current.next!=None:
			current = current.next
		current = new_node

	def length(self):
		current = self.head
		total = 0
		while current.next!=None:
			total+=1
			current = current.next
		return total

	def display(self):
		elements = []
		current_node = self.head
		while current_node.next != None:
			current_node = current_node.next
			elements.append(current_node.data)
		print(elements)

new_list = linked_list()
new_list.display()

