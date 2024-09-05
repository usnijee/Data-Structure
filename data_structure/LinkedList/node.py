class Node:
	def __init__(self, value = 0, next = None):
		self.value = value
		self.next = next
		
first = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)

first.next = second
second.next = third
third.next = fourth
first.value = 6