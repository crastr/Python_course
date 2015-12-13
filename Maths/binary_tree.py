__author__ = 'Alex'
class BSTNode():

    def __init__(self, data = None):
        self.value = data
        self.left = None
        self.right = None
        self.parent = None
    def get_data(self):
        return self.value
    def get_left(self):
        return self.next_node
    def get_right(self):
        return self.prev_node
    def set_left(self, next_new):
        self.next_node = next_new
    def set_right(self, prev_new):
        self.prev_node = prev_new

class BST:

    def __init__(self, Data = None):
        self.root = Data
        self.string = []

    def Add(self, value):
        if not self.root:
            self.root = BSTNode(value)
        else:
            self.further_add(value, self.root)

    def further_add (self, new_value, current_node):
        if new_value < current_node.value:
            if not current_node.left:
                current_node.left = BSTNode(new_value)
                current_node.left.parent = current_node
            else:
                self.further_add (new_value, current_node.left)
        elif new_value > current_node.value:
            if not current_node.right:
                current_node.right = BSTNode(new_value)
                current_node.right.parent = current_node
            else:
                self.further_add (new_value, current_node.right)
        else:
            return ('Element already in tree!')

    def find(self, smt):
        if self.root:
            return self.further_find(self.root, smt)
        else:
            return ('The tree is empty!')

    def further_find(self, node, smt):

        if node == None:
            return 'Not found!'
        elif node.value == smt:
            return node
        elif node.value > smt:
            return self.further_find(node.left, smt)
        elif node.value < smt:
            return self.further_find(node.right, smt)

    def FindMax(self):
        if self.root:
            return self.find_max_further(self.root)
        else:
            return ('The tree is empty!')

    def find_max_further(self, node):
        max = None
        while node:
            max = node
            node = node.right
        return max

    def FindMin(self):
        if self.root:
            return self.find_min_further(self.root)
        else:
            return ('The tree is empty!')

    def find_min_further(self, node):
        min = None
        while node:
            min = node
            node = node.left
        return min

    def GetNext(self, node):
        node = self.find(node)
        if node.right:
            return self.find_min_further(node.right)
        else:
            parent = node.parent
            while parent:
                if parent.left == node:
                    return parent
                node = parent
                parent = node.parent
            return None

    def GetPrevious(self, node):
        node = self.find(node)
        if node.left:
            return self.find_max_further(node.left)
        else:
            parent = node.parent
            while parent:
                if parent.right == node:
                    return parent
                node = parent
                parent = node.parent
            return None

    def Print(self):
        if self.root:
            self.print_node_tree(self.root)
        else:
            print ('Tree is empty!')

    def print_node_tree(self, node):
        if node:
            self.print_node_tree(node.left)
            print (node.value, end=' ')
            self.print_node_tree(node.right)

    def Remove(self, value):
        a = self.find(value)
        if a == 'Not found!':
            print(a)
        elif a == 'Tree is empty':
            print ('Tree is empty!')
        elif a:
            self.remove_further(a)

    def remove_further(self, node):
        if node == self.root:
            if node.left == None and node.right != None:
                self.root = None
                print('Tree now empty')
            if node.left != None and node.right != None:
                minimum = self.GetNext(node.value)
                minimum.left = node.left
                if node.right == minimum:
                    node.right = None
                minimum.right = node.right
                minimum.parent.left = None
                self.root = minimum
                node = None
            elif node.left != None and node.right == None:
                self.root = node.left
            elif node.left == None and node.right != None:
                self.root = node.right

        else:
            if node.right == None and node.left == None:
                if node.parent.left == node:
                    node.parent.left = None
                elif node.parent.right == node:
                    node.parent.right = None
            elif node.left != None and node.right != None:
                if node.parent.left == node:
                    minimum = self.GetNext(node.value)
                    minimum.left = node.left
                    if node.right == minimum:
                        node.right = None
                    minimum.right = node.right
                    minimum.parent.left = None
                    node.parent.left = minimum
                    node = None
                elif node.parent.right == node:
                    minimum = self.GetNext(node.value)
                    minimum.left = node.left
                    if node.right == minimum:
                        node.right = None
                    minimum.right = node.right
                    minimum.parent.left = None
                    node.parent.right = minimum
                    node = None
            elif node.left != None and node.right == None:
                if node.parent.left == node:
                    node.parent.left = node.left
                    node.left.parent = node.parent
                elif node.parent.right == node:
                    node.parent.right = node.left
                    node.left.parent = node.parent

            elif node.left == None and node.right != None:
                if node.parent.left == node:
                    node.parent.left = node.right
                    node.right.parent = node.parent
                elif node.parent.right == node:
                    node.parent.right = node.right
                    node.right.parent = node.parent

    def linearise(self):
        if self.root:
            self.linearise_further(self.root)
        else:
            print('The tree is empty!')

    def linearise_further(self, node):
        if node:
            self.string.append (node.value)
            self.linearise_further(node.left)
            self.linearise_further(node.right)
            self.string = sorted(self.string)
    def Rebuild(self):
        self.linearise()
        self.root = None
        self.further_rebuild(self.string, 0, (len(self.string)-1))

    def further_rebuild(self, linear_tree, begin, end):
            if begin == 0 and end == len(linear_tree)-1:
                mid_point = begin + (end - begin)//2
                middle_value = linear_tree[mid_point]
                node = BSTNode(middle_value)
                self.root = node
                node.left = self.further_rebuild(linear_tree, begin, (mid_point - 1))
                node.left.parent = node
                node.right = self.further_rebuild(linear_tree, (mid_point + 1), end)
                node.right.parent = node
            if begin > end:
                return None
            mid_point = begin + ((end - begin) // 2)
            middle_value = linear_tree[mid_point]
            node = BSTNode(middle_value)
            node.left = self.further_rebuild(linear_tree, begin, (mid_point - 1))
            if node.left:
                node.left.parent = node
            node.right = self.further_rebuild(linear_tree, (mid_point + 1), end)
            if node.right:
                node.right.parent = node
            return node


tree = BST()
a = ()
i = 1
b = []
while i < 15:
    a = range(-10, 1000, 2)[i]
    b.append(a)
    i += 1

b = sorted(b, reverse = True)

for i in range(len(b)):
    tree.Add(b[i])
    i += 1


# print(tree.root.value)
# print(tree.print())
# print(tree.string())
tree.Rebuild()
tree.Print()
tree.Remove(8)
print('\n')
tree.Print()