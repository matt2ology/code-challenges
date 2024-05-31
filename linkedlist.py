class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head  # Traverse to the last node
        while last_node.next:  # While there is a next node
            last_node = last_node.next  # Move to the next node
        last_node.next = new_node  # Assign the new node to the next node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        current_node = self.head
        # If the data is in the head node itself
        if current_node and current_node.data == data:
            # Skip the head node and assign the next node as the head
            self.head = current_node.next
            current_node = None  # Delete the head node by assigning None
            return
        prev = None  # Keep track of the previous node to the current node
        # Traverse to the node to be deleted and keep track of the previous
        while current_node and current_node.data != data:
            prev = current_node
            current_node = current_node.next
        # If the data is not found in the linked list at all
        if current_node is None:
            return
        prev.next = current_node.next  # Skip the current node
        current_node = None  # Delete the current node by assigning None

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next
        print("None")


# Example Usage
if __name__ == "__main__":
    # Create a new linked list
    linked_list = LinkedList()

    # Append some elements
    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.append(40)
    linked_list.append(50)
    linked_list.append(60)

    # Display the linked list
    linked_list.display()  # Output: 10 -> 20 -> 30 -> None

    # Prepend an element
    linked_list.prepend(0)

    # Display the linked list again
    linked_list.display()  # Output: 0 -> 10 -> 20 -> 30 -> None

    # Delete an element
    linked_list.delete(20)

    # Display the linked list after deletion
    linked_list.display()  # Output: 0 -> 10 -> 30 -> None
