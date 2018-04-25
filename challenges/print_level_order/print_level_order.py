def breadth_first_traversal(self, func):
       '''Perform func on each node breadth first'''
       
    def recurse(nodelist):
        new_list = []
            for node in nodelist:
                string.append(node.val + ', ') 
                for child in node.children:
                    new_list.append(child)
                print(string + '\b\b')
            if len(new_list) > 0:
                recurse(new_list)

        if self.root:
        recurse([k_tree.root])
