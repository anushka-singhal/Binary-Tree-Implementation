class tree:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None
        
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if data < self.key:
            if self.lchild is None:
                self.lchild = tree(data)
            else:
                self.lchild.insert(data)
        else:
            if self.rchild is None:
                self.rchild = tree(data)
            else:
                self.rchild.insert(data)
    def search(self, data):
        if self.key == data:
            print("found")
            return 
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("not found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("not found")
    def preorder(self):
        print(self.key)
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    def postorder(self):
        print(self.key)
        if self.rchild:
            self.rchild.postorder()
        if self.lchild:
            self.lchild.postorder()
    def Inorder(self):
        print(self.key)
        if self.lchild:
            self.lchild.Inorder()
        if self.rchild:
            self.rchild.Inorder()

    def delete(self,data):
        if self.lchild is None:
            print("empty")
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("not present")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("not present")  
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        
root = tree(10)
list = [10,20,30,4,6,1]
for i in list:
    root.insert(i)
root.search(1)
root.preorder()
root.postorder()
root.Inorder()
root.delete(10)
