try:
    from node import Node 
except ModuleNotFoundError:
    from data_structure.node import Node

class LinkedNode:
    def __init__(self, node_id, datum, next = None):
        self.node_id = node_id 
        self.datum = datum
        self.next = next 
        
    def __str__(self):
        return str(self.datum)

class LinkedList:
    def __init__(self, elements = None):            
        # len(elements) == 0
        if elements == []:
            self.head = None 
            self.tail = None 
            self.end = None
            self.size = 0
            
        else:
            size = 0
            for idx, element in enumerate(elements):
                if not isinstance(element, LinkedNode):
                    elements[idx] = LinkedNode(idx, element)
                size += 1
            for idx, element in enumerate(elements[:-1]):
                elements[idx+1].next = element
                # print(f'{elements[idx+1]} --> {element}')
            elements[0].next = None
                
            self.head = elements[-1] 
            self.tail = LinkedList(elements[:-1])
            self.end = elements[0]
            self.size = size
            
    def to_list(self):
        # cur = self.head 
        # res = []
        
        # while cur is not None:
        #     res.append(cur.datum)
        #     cur = cur.next 

        # return res 
        return [x for x in self]
        # return list(self)
        # return [x for x in LinkedList.__iter__(self)]
        # 
        
    def __iter__(self):
        cur = self.head
        
        while cur is not None:
            yield cur.datum 
            cur = cur.next 

    def __str__(self):
        res = ''
        current = self.head
        while current:
            res += str(current.datum) + ' -> '
            current = current.next
        return res.rstrip(' -> ')
    
    def append_to_tail(self, element):
        if not isinstance(element, LinkedNode):
            element = LinkedNode(self.size+1, element)
        
        if self.size == 0:
            self.head = element
            self.tail = element
            self.end = element
        else:
            self.end.next = element
        self.size += 1
    
    def insert(self, element):
        if not isinstance(element, LinkedNode):
            element = LinkedNode(self.size+1, element)
            
        if self.size == 0:
            pass
        else:
            last = self.head 
            cur = self.head 
            
            while cur is not None:
                if cur.datum[1] >= element.datum[1]:
                    last = cur
                    cur = cur.next 
                else:
                    # print('last', last, element, self.head)
                    break
            if last == self.head:
                element.next = self.head 
                self.head = element 
            elif last == self.end:
                last.next = element 
                self.end = element
            else:
                element.next = last.next 
                last.next = element
            
            self.size += 1     
            
    def pop_from_head(self):
        res = self.head.datum
        self.head = self.head.next
        self.size -= 1
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

if __name__ == '__main__':
    lst = LinkedList([1,2,3,4])
    
    assert lst.head.datum == 1 
    assert lst.head.next.next.datum == 3