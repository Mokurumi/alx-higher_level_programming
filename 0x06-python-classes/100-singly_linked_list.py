#!/usr/bin/python3
"""singly linked list clases"""


class Node:
    """A class that defines a node of a singly linked list.

    Private instance attributes:
        _data (int): The data stored in the node.
        _next_node (Node): Reference to the next node.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): Reference to the next node.

    Raises:
        TypeError: If data is not an integer or next_node is not a Node object.
    """

    def __init__(self, data, next_node=None):
        """Initialize a node with data and next_node.

        Args:
            data (int): The data to store in the node.
            next_node (Node, optional): The next node in the linked list.
                                    Defaults to None.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self._data = data
        self._next_node = next_node

    @property
    def data(self):
        """Get the data stored in the node.

        Returns:
            int: The data stored in the node.
        """
        return self._data

    @data.setter
    def data(self, value):
        """Set the data stored in the node.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self._data = value

    @property
    def next_node(self):
        """Get the next node.

        Returns:
            Node: The next node.
        """
        return self._next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node.

        Args:
            value (Node): The new next node.

        Raises:
            TypeError: If value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self._next_node = value


class SinglyLinkedList:
    """A class that defines a singly linked list.

    Private instance attribute:
        _head (Node): The first node in the linked list.

    Attributes:
        head (Node): The first node in the linked list.
    """

    def __init__(self):
        """Initialize an empty singly linked list."""
        self._head = None

    def sorted_insert(self, value):
        """Insert a new Node into the sorted position in the linked list.

        Args:
            value (int): The value of the new Node to insert.
        """
        new_node = Node(value)
        if self._head is None or self._head.data >= new_node.data:
            new_node.next_node = self._head
            self._head = new_node
            return

        current = self._head
        while current.next_node is not None \
                and current.next_node.data < new_node.data:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Return a string representation of the linked list.

        Returns:
            str: The linked list as a string, with one node value per line.
        """
        values = []
        current = self._head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
