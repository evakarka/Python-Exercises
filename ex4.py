# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data  # Node's data
        self.next = None  # Pointer to the next node, initially set to None

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None  # Initialize an empty linked list (head is None)

    # Method to append a new node at the end of the list
    def append(self, data):
        new_node = Node(data)  # Create a new node with the given data
        if not self.head:
            self.head = new_node  # If the list is empty, set new_node as the head
            return
        last_node = self.head
        while last_node.next:  # Traverse to the last node
            last_node = last_node.next
        last_node.next = new_node  # Set the last node's next to the new node

    # Method to insert a new node at a specific position
    def insert(self, position, data):
        new_node = Node(data)  # Create a new node with the given data
        if position == 0:  # If position is 0, insert at the beginning
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        count = 0
        while current_node and count < position - 1:
            current_node = current_node.next
            count += 1
        if not current_node:
            print("Position out of range")
            return
        new_node.next = current_node.next  # Point new node to the next node
        current_node.next = new_node  # Point current node to the new node

    # Method to delete the first node containing the specified data
    def delete(self, data):
        current_node = self.head
        if current_node and current_node.data == data:
            self.head = current_node.next  # If the head node is the one to be deleted
            current_node = None
            return
        prev_node = None
        while current_node and current_node.data != data:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:  # If data not found in the list
            print(f"Data {data} not found in the list")
            return
        prev_node.next = current_node.next  # Remove the node by linking previous node to the next one
        current_node = None

    # Method to display the list
    def display(self):
        current_node = self.head
        if not current_node:
            print("The list is empty.")
            return
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")  # End of the list

# Testing the linked list implementation
if __name__ == "__main__":
    linked_list = LinkedList()

    # Perform append operations
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    print("After appending 10, 20, 30:")
    linked_list.display()

    # Perform insert operation at position 1
    linked_list.insert(1, 15)
    print("After inserting 15 at position 1:")
    linked_list.display()

    # Perform delete operation
    linked_list.delete(20)
    print("After deleting 20:")
    linked_list.display()

    # Perform delete operation where element doesn't exist
    linked_list.delete(100)
    
    # Perform insert operation at the beginning
    linked_list.insert(0, 5)
    print("After inserting 5 at the beginning:")
    linked_list.display()
