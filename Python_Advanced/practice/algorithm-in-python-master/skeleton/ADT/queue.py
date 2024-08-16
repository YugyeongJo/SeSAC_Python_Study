import sys 
# sys.path.append('./skeleton/data_structure')
sys.path.append('../data_structure')

try:
    from linked_list import LinkedList, LinkedNode, DoublyLinkedNode, DoublyLinkedList
except ModuleNotFoundError:
    from data_structure.linked_list import LinkedList, LinkedNode, DoublyLinkedNode, DoublyLinkedList

class Queue:
    def __init__(self, *elements, backend = list):
        assert isinstance(elements, list) or isinstance(elements, tuple)

        self.backend = backend
        if self.backend == list:
            self.list = list(elements)
        elif self.backend == LinkedList:
            self.linked_list = LinkedList(list(elements))
            # import code 
            # code.interact(local = locals())

    def elements(self):
        if self.backend == list:
            return self.list 
        elif self.backend == LinkedList:
            # res = []
            # cur = self.linked_list.head
            # while cur is not None:
            #     cur = cur.next 
            # return res
            
            # return self.linked_list.to_list()
            
            return list(self.linked_list)[::-1]

    def enqueue(self, elem):
        if self.backend == list:
            self.list = [elem] + self.list
        elif self.backend == LinkedList:
            # self.linked_list.size += 1
            # self.linked_list.LinkedNode(self.size(), elem) 
            # print(self.linked_list.size) # n 
            self.linked_list.append_to_tail(elem)
            # print(self.linked_list.size) # n+1 

    def dequeue(self):
        if self.backend == list:
            return self.list.pop()
        elif self.backend == LinkedList:
            return self.linked_list.pop_from_head()
        
    # 가장 먼저 들어온 애가 누구야?
    def front(self):
        if self.backend == list:
            return self.list[-1]
        elif self.backend == LinkedList:
            return self.linked_list.head.datum

    def size(self):
        if self.backend == list:
            return len(self.list)
        elif self.backend == LinkedList:
            return self.linked_list.size
    
    def is_empty(self):
        return len(self.elements()) == 0
        # if self.backend == list:
        #     return self.list == []
        # elif self.backend == LinkedList:
        #     return self.linked_list.head == None and self.linked_list.end == None

    def __str__(self):
        return str(self.elements())

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.elements == other.elements 
        return False 

class PriorityQueue:
    def __init__(self, *elements_with_priority, backend = list):
        """Get list of 2-tuple containing (obj, number), which denotes object and its priority. Higher the number, the element have hight priority. 
        """
        self.backend = backend
        
        sorted_list = sorted(elements_with_priority, key = lambda x:x[1])
        if self.backend == list:
            self.list = list(sorted_list)
        elif self.backend == LinkedList:
            self.linked_list = LinkedList(list(sorted_list))


    def elements(self):
        if self.backend == list:
            return self.list 
        elif self.backend == LinkedList:
            return list(self.linked_list)[::-1]
    
    def enqueue(self, elem):
        if self.backend == list:
            for idx, x in enumerate(self.list):
                if elem[1] <= x[1]:
                    self.list.insert(idx, elem)
                    break
            else:
                self.list.append(elem)
        elif self.backend == LinkedList:
            self.linked_list.insert(elem)

    def dequeue(self):
        if self.backend == list:
            return self.list.pop()
        elif self.backend == LinkedList:
            return self.linked_list.pop_from_head()
                
    def front(self):
        if self.backend == list:
            return self.list[-1]
        elif self.backend == LinkedList:
            return self.linked_list.head.datum

    def size(self):
        if self.backend == list:
            return len(self.list)
        elif self.backend == LinkedList:
            return self.linked_list.size
    
    def is_empty(self):
        return len(self.elements()) == 0
        # if self.backend == list:
        #     return self.list == []
        # elif self.backend == LinkedList:
        #     return self.linked_list.size == 0

    def __str__(self):
        return str(self.elements())

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.elements == other.elements 
        return False

if __name__ == '__main__':
    from code import interact 
    available_backends = [LinkedList]
    # available_backends = [list, LinkedList, DoublyLinkedList]

    for backend in available_backends:
        
        # q1 = Queue(1,2,3,4, backend = backend)
        
        # assert q1.elements() == [1,2,3,4]  #, interact(local = locals())
        # assert q1.size() == 4
        
        # q1.enqueue(5)
        # assert q1.elements() == [5,1,2,3,4]
        # assert q1.size() == 5
        # assert q1.dequeue() == 4
        # assert q1.size() == 4
        # assert q1.elements() == [5,1,2,3]
        # assert q1.front() == 3 

        # q2 = Queue(backend = backend)

        # assert q2.elements() == []
        # assert q2.size() == 0
        # assert q2.is_empty()
        
        # q2.enqueue(1)

        # assert q2.elements() == [1]
        # assert q2.size() == 1  
        # assert not q2.is_empty()
        
        # if backend == LinkedList:
        #     print(q1.linked_list, "///", q2.linked_list)
    
        q2 = PriorityQueue(('c',1), ('d',4), ('e',2), ('b',3), backend = backend)

        assert q2.elements() == [('c',1), ('e',2), ('b',3), ('d',4)]
        assert q2.size() == 4 
        assert q2.front() == ('d', 4) 
        assert not q2.is_empty()
        q2.dequeue()
        
        assert q2.elements() == [('c',1), ('e',2), ('b',3)]
        assert q2.size() == 3 
        assert q2.front() == ('b', 3) 
        assert not q2.is_empty()
        
        print(q2)
        q2.enqueue(('f', 5))
        print(q2)
        q2.enqueue(('g', 3))
        print(q2)
        q2.enqueue(('h', -1))
        print(q2, q2.linked_list.end.datum)


        assert q2.elements() == [('h',-1), ('c',1), ('e',2), ('g', 3), ('b',3), ('f', 5)]
        
        q2.dequeue()
        print(q2)
        q2.dequeue()
        print(q2)
        q2.dequeue()
        print(q2)
        q2.dequeue()
        print(q2)
        q2.dequeue()
        print(q2)
        q2.dequeue()
        print(q2)

        assert q2.is_empty()