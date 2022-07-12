class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
            
        return self


    def contains(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(value)
        else:
            return True


    def getMin(self):
        if self.left is None:
            return self.value
        else:
            return self.left.getMin()

    def getMax(self):
        if self.right is None:
            return self.value
        else:
            return self.right.getMax()


    def remove(self, value, parent=None):
        if value <  self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value:
            if self.left is not None:
                self.right.remove(value, self)

        else:
            if self.left is not None and self.right is not None:
                self.value = self.right.getMin()
                self.right.remove(self.value, self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.right = self.right.right
                    self.left = self.right.left
                else:
                    self.value = None
                
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right
        return self

bst = BST(15)
bst.insert(5)
bst.insert(17)
bst.insert(7)
bst.insert(3)
bst.insert(2)
bst.insert(1)
print(bst.contains(2))
print(bst.contains(4))
print(bst.getMin())
print(bst.getMax())
bst.remove(3)
bst.remove(1)
bst.getMin()
print(bst.getMin())
print(bst.left.left.value)
print(bst.left.value)
print(bst.left.right.value)
print(bst.left.value)
print(bst.value)