class Tree:
    def __init__(self, root, children = []):
        
        assert isinstance(children, list)
        self.root = root
        self.children = children
    
    def __str__(self):
        res = str(self.root)
        newline = '\n'
        
        for idx, child in enumerate(self.children):
            res += newline
            
            if idx < len(self.children)-1:
                res += '├── '
                res += str(child).replace(newline, newline + '|   ')
            else: 
                res += '└── '
                res += str(child).replace(newline, newline + '    ')
        
        return res
    
print(\
    Tree (1, [\
        Tree(2, [\
            Tree(3)
            , Tree(4)
            , Tree(5, [\
                        Tree(6)
                        , Tree(7)
                        ])                        
            , Tree(8)
            ])
        , Tree(9, [\
                 Tree(10)
                 , Tree(11)
                 ])
        ])
    )