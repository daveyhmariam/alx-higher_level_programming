#!/usr/bin/python3

"""class node"""


class Node:
    """defnition of Node class"""
    def __init__(self, data, next_node=None):
        """instantiate Node object

        Args:
            data: data element
            next_node: next node object
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data property getter/setter"""

        return self.__data

    @data.setter
    def data(self, value):
        """data property getter/setter"""
        if (not isinstance(value, int)):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter"""
        if (value is not None and
                not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """class to creat linked list"""
    def __init__(self):
        """instantiate instance attribute"""

        self.__head = None

    def sorted_insert(self, value):
        """create and insert Node in the linked list

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value: value to be inserted
        """

        new = Node(value)

        if self.__head is None:
            new.next_node = None
            self.__head = new
            new = None
        elif self.__head.data >= new.data:
            new.next_node = self.__head
            self.__head = new
            new = None
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                   tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new
            new = None

    def __str__(self):

        """str representation of a SinglyLinkedList"""

        values = []
        tmp = self.__head
        while (tmp is not None):
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
