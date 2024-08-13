try:
    from node import Node 
except ModuleNotFoundError:
    from data_structure.node import Node

class LinkedNode:
    def __init__(self, node_id, datum, next = None):
        self.node_id = node_id 
        self.datum = datum
        self.next = next 

class LinkedList:
    def __init__(self, elements):
        if elements == []:
            self.head = None 
            self.tail = None 
            self.end = None
            self.size = 0
            
        else:
        
            for idx, element in enumerate(elements):
                if not isinstance(element, LinkedNode):
                    elements[idx] = LinkedNode(idx, element)
            for idx, element in enumerate(elements):
                if idx+1 > idx:
                    element.next = None
                else:
                    element.next = elements[idx+1]
                
            self.head = elements[0] 
            self.tail = elements[1:]
            self.end = elements[-1]
            self.size = len(elements)
            
    def to_list(self):
        return [x for x in self]
        
    def __iter__(self):
        yield None 

    def __str__(self):
        res = ''

        return res 
        

class DoublyLinkedNode(Node):
    def __init__(self, node_id, datum, prev = None, next = None):
        self.node_id = node_id 
        self.datum = datum
        self.next = next 
        self.prev = prev 

class DoublyLinkedList:
    def __init__(self, elements):
        if elements == []:
            self.head = None 
            self.tail = None 
            self.end = None
            self.size = 0
        else:
            self.head = None 
            self.tail = None 
            self.end = None
            self.size = 0

    def __iter__(self):
        yield None 

    def __str__(self):
        res = ''

        return res 

