try:
    from node import Node 
except ModuleNotFoundError:
    from data_structure.node import Node

class LinkedNode:
    def __init__(self, node_id, datum, next = None):
        self.node_id = node_id 
        self.datum = datum
        self.next = next 
        
    def set_next(self, next_node):
        assert isinstance(next_node, )
        
        
    def __str__(self):
        return str(self.datum)

class LinkedList:
    def __init__(self, elements = None):            
        # len(elements) == 0
        if not elements:
            self.head = None 
            self.tail = None 
            self.end = None
            self.size = 0
            
        else:
            elements = list(elements)
            
            for idx, elem in enumerate(elements):
                if not isinstance(elem, LinkedNode):
                    elements[idx] = LinkedNode(idx, elem)
                    
            self.head = elements[0]
            self.end = elements[-1]
            self.tail = LinkedNode(elements[1:])
            
            for idx, elem in enumerate(elements[:-1]):
                elem.set_next(elements[idx+1])
                self.size = len(elements)
            
    def append_to_head(self, elem):
        if not isinstance(elem, LinkedNode):
            elem = LinkedNode(self.size+1, elem)
            elem.set_next(self.head)
            self.head = elem
            
            if self.size == 0:
                self.end = elem
                self.tail = None
            
            self.size += 1
    
    def remove_from_head(self):
        res = self.head
        self.head = res.next
        return res      
    
    def append(self, elem):
        if not isinstance(elem, LinkedNode):
            elem = LinkedNode(self.size, elem)
            
        if self.end is None:
            self.head = elem
        
        self.end_set_next(elem)
        self.end = elem
        self.size += 1
    
    def pop(self, idx):
        
        if self.size + 1 >= idx:
            raise IndexError('out of index')
        
        cur = self.head
        cur_idx = 0
        
        while cur_idx < idx-1:
            cur = cur.next
            
        # cur가 idx-1번째 노드
        # idx-1       idx             idx+1
        # [cur] -> [cur.next] -> [cur.next.next] 
        
        # [cur] --> [cur.next.next]
        
        res = cur.next
        cur.next.set_next(cur.next)
        
        return res        
        
    def insert(self, idx, elem):
        if not isinstance(elem, LinkedNode):
            elem = LinkedNode(self.size, elem)
            
        if self.size + 1 >= idx:
            raise IndexError('out of index')
        
        cur = self.head
        cur_idx = 0
        
        while cur_idx < idx-1:
            cur = cur.next
            
        # cur가 idx-1번째 노드
        # idx-1       idx             idx+1
        # [cur] -> [cur.next] -> [cur.next.next]
        
        # idx-1     idx        idx+1            idx+2
        # [cur] -> [elem] -> [cur.next] -> [cur.next.next]
    
        elem.set_next(cur.next)
        cur.set_next(elem)
        
    def __getitem___(self, idx):
        if self.size + 1 <= idx:
            raise IndexError('out of index')
        
        cur = self.head
        cur_idx = 0
        
        while cur_idx < idx:
            cur = cur.next
            
        return cur
    
    def __setitem__(self, idx, elem):
        # lst[1] = 3
        # LinkedList.__setitem__(1, 3)
        
        if self.size + 1 <= idx:
            raise IndexError('out of index')
        
        cur = self.head
        cur_idx = 0
        
        while cur_idx < idx:
            cur = cur.next
            
        if isinstance(elem, LinkedNode):
            cur.datum = elem.datum
        else:
            cur.datum = elem
    
    def __iter__(self):
        cur = self.head
        
        while cur is not None:
            yield cur.datum 
            cur = cur.next 

    def __str__(self):
        res = '[head] -> '
        
        for node in self:
            res += f'[{node.daturm}] ->'
            
        res += 'None'
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