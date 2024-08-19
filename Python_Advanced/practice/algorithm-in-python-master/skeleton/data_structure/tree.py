try:
    from node import Node 
except ModuleNotFoundError:
    from data_structure.node import Node

class TreeNode:
    def __init__(self, node_id, datum):
        self.node_id = node_id
        self.datum = datum 

class Tree:
    def __init__(self, root, children = []):
        if not isinstance(root, TreeNode):
            root = TreeNode('0', root) 
        self.root = root
        
        children = list(children)
        for idx, child in enumerate(children):
            if not isinstance(child, Tree):
                children[idx] = Tree(root=TreeNode(str(idx), child))
                
        self.children = children

    def iter_nodes(self):
        yield self.root 

        for child in self.children:
            for n in child.iter_nodes():
                yield n 

    def iter_nodes_with_address(self):
        yield [], self.root
        
        for idx, child in enumerate(self.children):
            for loc, n in child.iter_nodes_with_address():
                yield [idx] + loc, n
                
        # res = []
        
        # res.append(([], self.root))
        # for idx, child in enumerate(self.children):
        #     for addr, n in child.iter_nodes_with_address():
        #         res.append(([idx] + addr, n))
        
        # return res 

    def __iter__(self):
        yield self.root.datum

        for child in self.children:
            for n in child:
                yield n  

    def insert(self, address, elem):
        if not isinstance(elem, Tree):
            elem = Tree(elem) 
            
        cur = self
        for loc in address[:-1]:
            cur = cur.children[loc]
            
        cur.children.insert(address[-1], elem)

    def delete(self, address):
        cur = self
        cur = self
        for loc in address[:-1]:
            cur = cur.children[loc]
        
        res_tree = cur.children[address[-1]]
        res = cur.children[address[-1]].root.datum
        
        del cur.children[address[-1]]

        return res_tree, res
    
    def search(self, elem):
        for loc, node in self.iter_nodes_with_address():
            if node.datum == elem:
                return loc 

    def root_datum(self):
        return self.root.datum 

    def height(self):
        # for i in self.iter_nodes_with_address():
        #     h = len(i)+1 
        #     print(h)
        # return h
    
        # x = self.iter_nodes_with_address()
        # print(x)
        # h = len(x)+1
        # print(h)
        # print(max(x, key = lambda x:len(x[0])))
        h=0
        
        for loc, node in self.iter_nodes_with_address():
            if len(loc) + 1 > h:
                h = len(loc) +1

        return h

    def __str__(self):
        res = str(self.root.datum)
        
        for idx, child in enumerate(self.children):
            res += '\n'
            if idx < len(self.children) -1:
                res += '├── '
                res += str(child).replace('\n', '\n│    ')
            else:
                res += '└── '
                res += str(child).replace('\n', '\n     ')
        
        return res


if __name__ == '__main__':
    t1 = Tree(1, [
                Tree(11, [Tree(111,), Tree(112)],), 
                Tree(12, [Tree(121), Tree(122), Tree(123),])
             ]
         )
    print("/////Tree/////")
    print(t1)
    
    assert t1.root_datum() == 1 
    assert t1.height() == 3

    for addr, n in t1.iter_nodes_with_address():
        assert [int(e)-1 for e in list(str(n.datum))[1:]] == addr 
        assert t1.search(n.datum) == addr

    # for e in t1:
    #     print(e)
    
    print("/////Tree insert/////")
    t1.insert([2], Tree(13, [Tree(131), Tree(132), Tree(133)]))
    print(t1)
    t1.insert([1, 1], Tree(122, [Tree(1221), Tree(1222)]))
    print(t1)    
        
    print("/////Tree first delete/////")
    a, b = t1.delete([1,1])
    print(a)
    # print(type(a))
    assert 122 == b
    print(t1)
    
    print("/////Tree first second/////")
    a, b = t1.delete([1,2])
    print(a)
    assert 123 == b
    print(t1)

    for addr, n in t1.iter_nodes_with_address():
        assert [int(e)-1 for e in list(str(n.datum))[1:]] == addr 
        assert t1.search(n.datum) == addr 

    print(t1)