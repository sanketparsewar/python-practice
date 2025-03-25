# -------Tree
'''
It is a collection of Nodes and every nodes are connected with the edges
Non linear data structure
relashionship betwenn nodees are parent-child sibling 
'''

# ---- Types of Tree Data structure
'''
1.General Tree
2.Binary Tree

'''

# ----------General Tree -----
'''
Any number of child nodes
No limitations on how many child node each node can have
'''

# -------Binary Tree--------
'''
Each node can contain 0 child or 1 child node or 2 children node but not more than two child node
EX:    O                       O
      / \                    /   \                   
     O   O                  O     O
    / \   \                / \   / \ 
   O   O   O              O   O O   O
                         /
                        O
Binary tree is divided in 5 types:
a.Full binary tree
b.Complete Binary tree
c.Perfect Binary tree
d.Balanced Binary tree
e.Pathological or Degenarate Binary tree
'''

# -----a. Full Binary Tree -------
'''
It is also called as strict or strictly binary tree
Every node can have o child nodes or 2 children nodes but not 1 child node
EX:    O                       O
      / \                    /   \                   
     O   O                  O     O
    / \                    / \   / \ 
   O   O                  O   O O   O
'''

# -----b.Complete Binary tree----
'''
All the levels except last level are completely filled by nodes.
For last level either it can be comletely filled or the nodes need to be filled from left to right
             O                       O
           /   \                   /   \                   
          O     O                 O     O
         / \   / \               / \   / \ 
        O   O O   O             O   O O   O
       /                       / \
      O                       O   O  

'''

# -----c.Perfect Binary tree----
'''
All the Internal nodes contain 2 children node and all the leaf nodes are present in same level
                                         O
                                       /   \
                                      /     \
             O                       /       \       
           /   \                    /         \                   
          O     O                  O           O
         / \   / \               /   \       /   \ 
        O   O O   O             O     O     O     O
                               / \   / \   / \   / \
                              O   O O   O O   O O   O  

'''

# -----d.Balanced Binary tree----
'''
Height of the left and the right sub tree of every node may differ by at most 1.
                                         1(2-1)
                                         O
                                       /   \
             1(1-0)                   /     \
             O                       /       \       
          0/   \0                  0/         \1                   
          O     O                  O           O
        0/ \0                   0/   \0     1/   \0 
        O   O                   O     O     O     O
                              0/ \0 0/ \0 0/  
                              O   O O   O O     
Not a balance binary tree:
jya node che value kadaiche ahe tya node che child node pasun te last node madle edges mojaiche
           2(2-0)
           O
          / \
         O   O
        / 
       O 
      /
     O
'''

# -----e.Degenerate Binary tree----
'''
Every parent node has only one child node
           O     O
          /       \
         O         O
        /         / 
       O         O
      /
     O
'''


# ------------Implementation of General Tree
# Tree is recursive data structure. We have a child node and on child node we can again call same print refunction and it will do the same thing
# Electronics
#   |__Laptop
#      |__Mac
#      |__Dell
#      |__Asus
#   |__Cellphone
#      |__iphone
#      |__Samsung
#      |__Oppo
#   |__TV
#      |__LG
#      |__Sony
'''
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

  # method for adding child in tree
  # when ever we add a child we add child to self object and that self will become parent of this child
    def add_child(self, child):
        child.parent = self  # This means child is in stance of tree node class it will have parent property and that parent property we want to set it as self
        self.children.append(child)

    # this function is for adding space prefixes according to levels
    # for root level is zero
    # for child level is 1
    # for leaves node level is 2
    # we will find out levels by couting ancestors
    def get_level(self):
        level = 0  # initialize a variable
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    # In this function we will go through all the children one by one and printing data element

    def print_tree(self):
        spaces = ' ' * self.get_level()*4  # we add 3 more space for clear visualization
        prefix = spaces+'|__' if self.parent else ''
        # infront of self.data we need to print prefix based on levels
        print(prefix+self.data)
        if self.children:
            for child in self.children:
                # print(child.data)  #this prints only three child of root nodes not other childs
                child.print_tree()  # this recursively calls the function and prints the sub trees
                # the issue arises here is when we are at leaf node li will not have self.children that is it will be an empty array
                # so we can apply if condition


# def build_product_tree():
#     root=TreeNode("Electronics")    #the root node is Electronics
#     #this 'Electronics' will be stored in self.data of that particular root node


#     # for electronics laptop is one of the category
#     # we created an object as laptop and stored 'laptop' as string
#     laptop= TreeNode('Laptop')

#     root.add_child(laptop)
#     # we created electronics as parent and adding root as a child for laptop
#     return root


def build_product_tree():
    root = TreeNode("Electronics")  # main node
    laptop = TreeNode("Laptop")  # 1st child node creating a treenode object
    # child che child node each child are instance of tree node so we are creating object here and appending as a child
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Dell'))
    laptop.add_child(TreeNode('Asus'))

    cellphone = TreeNode("Cellphone")  # 2nd child node
    cellphone.add_child(TreeNode('iphone'))
    cellphone.add_child(TreeNode('Samsung'))
    cellphone.add_child(TreeNode('Oppo'))

    tv = TreeNode('TV')
    tv.add_child(TreeNode('LG'))
    tv.add_child(TreeNode('Sony'))

    # once we ceated three tree node we need to add it to root category that is electronics category will have laptop,cellphone and tv as subcategory
    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    return root


if __name__ == '__main__':
    root = build_product_tree()
    root.print_tree()  # on root we call print function
    pass

'''


# ---Simple binary tree
#     2
#    / \
#   3   5
'''
class tree:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
        
node0=tree(2)
node1=tree(3)
node2=tree(5)

root=node0.key
node0.left=node1
node0.right=node2

print(root)
print(node0.left.key)
print(node0.right.key)
'''


# ------Binary tree creating parse tuple function
#         2
#        / \
#       /   \
#      3     5 
#     /     / \
#    1     /   \
#         3     7
#          \   / \
#           4 6   8
'''
class Tree:
    def __init__(self,key):
        self.key=key
        self.right=None
        self.left=None
    
def Parse_tuple(data):
    if isinstance(data,tuple) and len(data) == 3:
        node = Tree(data[1])
        node.left = Parse_tuple(data[0])
        node.right = Parse_tuple(data[2])
    elif data is None:
        node=None
    else:
        node=Tree(data)
    return node

# tuple=Tree()
tree_tuple=((1,3,None),2,((None,3,4),5,(6,7,8)))
tree1=Parse_tuple(tree_tuple)
print(tree1)
'''

class Tree():
    def  __init__ (self,key):
        self.key=key
        self.right=None
        self.left=None

def parse_tuple(data):
    if isinstance(data,tuple) and len(data)==3:
        node = Tree(data[1])











