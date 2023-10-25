#!/usr/bin/python3
"""class Node that defines a node of a singly linked list by"""


class Node:
    """Represents a node in a singly linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The reference to the next node in the linked list.

    """

    def __init__(self, data, next_node=None):
        """Initialize a new node with the given data and an optional next node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The next node in the linked list. Defaults to None.

        """
        self._data = None
        self._next_node = None
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data stored in the node.

        Returns:
            int: The data stored in the node.

        """
        return self._data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value (int): The data to be stored in the node.

        Raises:
            TypeError: If the provided value is not an integer.

        """
        if not isinstance(value, int):
            raise TypeError("Data must be an integer.")
        self._data = value

    @property
    def next_node(self):
        """Get the next node in the linked list.

        Returns:
            Node: The next node in the linked list, or None if it's the end of the list.

        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node in the linked list.

        Args:
            value (Node, optional): The next node in the linked list. Set to None to indicate the end of the list.

        Raises:
            TypeError: If the provided value is not a Node object.

        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object.")
        self._next_node = value

    def __str__(self):
        """Get a string representation of the node's data.

        Returns:
            str: A string representation of the node's data.

        """
        return str(self.data)



class SinglyLinkedList:
    """
    Represents a singly linked list.

    Attributes:
        head (Node): The head of the linked list, which points to the first node in the list.

    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node with the specified value into the list in ascending order.

        Args:
            value: The value to be inserted into the list.

        """
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        elif value <= self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node and current_node.next_node.data < value:
                current_node = current_node.next_node

            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list, with one node per line.

        Returns:
            str: A string containing the values of the nodes in the list, each on a separate line.

        """
        result = []
        current_node = self.head
        while current_node:
            result.append(str(current_node.data))
            current_node = current_node.next_node
        return '\n'.join(result)
