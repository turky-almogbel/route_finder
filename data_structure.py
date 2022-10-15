from collections import deque

class Stack:
    """a class to represent stack(LIFO) data structure with no redundant values"""
    stack = []

    def unique_push(self, item):
        """push a node into stack if it's not there

        :parameter item : the node to add to stack
        """
        if item not in self.stack:
            self.stack.append(item)

    def pop(self):
        """:return item at the top of stack or declare error."""
        return self.stack.pop()

    def is_empty(self) -> bool:
        """:return boolean : True or False """
        return not self.stack

    def display(self):
        """display the content of stack in CLI"""
        print("stack:", self.stack, ">top")


class Queue:
    """a class to represent queue(FIFO) data structure with no redundant values"""
    queue = deque()

    def unique_enqueue(self, item):
        """push a node into queue if it's not there

        :parameter item : the node to add to queue
        """
        if item not in self.queue:
            self.queue.append(item)

    def dequeue(self):
        """:return first item in queue or declare error."""
        return self.queue.popleft()

    def is_empty(self) -> bool:
        """:return boolean : True or False """
        return not self.queue

    def display(self):
        """display the content of queue in CLI"""
        print("queue:", list(self.queue))


class Graph:
    """a class to represent graph using adjacency list -dictionary of list-"""
    graph = {}  # adjacency list  |   dictionary of list
    def __init__(self, graph = {}):
        self.graph = graph


    def add_node(self, node, connected_nodes):
        """add node into graph

        if node is repeated, previous node is removed

        :param connected_nodes: list of connected nodes
        :param node: the node to be added"""
        self.graph[node] = connected_nodes

    def get_all_nodes(self):
        """:return list of all nodes in graph"""
        return [node for node in self.graph.keys()]

    def get_children_of_node(self, node):
        """:return list of connected nodes to the given node"""
        return self.graph[node]