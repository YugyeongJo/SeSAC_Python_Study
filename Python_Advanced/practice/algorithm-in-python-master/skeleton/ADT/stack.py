import sys 
sys.path.append('../data_structure')

try:
    from linked_list import LinkedList, LinkedNode, DoublyLinkedNode, DoublyLinkedList
except ModuleNotFoundError:
    from data_structure.linked_list import LinkedList, LinkedNode, DoublyLinkedNode, DoublyLinkedList

class Stack:
    def __init__(self, *elements, backend = list):
        assert isinstance(elements, list) or isinstance(elements, tuple)
        self.backend = backend
        if self.backend == list:
            self.list = list(elements)
        elif self.backend == LinkedList:
            self.linked_list = LinkedList(list(elements))
    
    def elements(self):
        if self.backend == list:
            return self.list
        elif self.backend == LinkedList:
            return self.linked_list
        
    def push(self, elem):
        if self.backend == list:
            self.list.append(elem)
        elif self.backend == LinkedList:
            return self.linked_list.append_to_tail()

    def pop(self):
        if self.backend == list:
            return self.list.pop()
        elif self.backend == LinkedList:
            return self.linked_list.pop_from_head()

    def top(self):
        if self.backend == list:
            return self.list[-1]
        elif self.backend == LinkedList:
            return self.linked_list.elements()[-1]

    def is_empty(self):
        return len(self.elements()) == 0
        # if self.backend == list:
        #     return self.list == []
        # elif self.backend == LinkedList:
        #     return self.linked_list

    def size(self):
        if self.backend == list:
            return len(self.list)
        elif self.backend == LinkedList:
            return len(self.linked_list.elements())
        
    def __str__(self):
        return str(self.elements())

if __name__ == '__main__':
    # available_backends = [list, LinkedList, DoublyLinkedList]
    available_backends = [LinkedList]

    for backend in available_backends:
        s1 = Stack(3,2,1,4)
        assert s1.top() == 4 
        assert not s1.is_empty()
        assert s1.pop() == 4
        
        assert s1.top() == 1 
        
        s1.push(5) 
        assert s1.top() == 5
        assert s1.size() == 4

        assert s1.pop() == 5
        assert s1.pop() == 1
        assert s1.pop() == 2
        assert s1.pop() == 3

        assert s1.is_empty()