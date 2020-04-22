import priority_queue_base
import random
import string

class Priority_Queue(priority_queue_base.PriorityQueueBase):
    class Item(priority_queue_base.PriorityQueueBase._Item):
        def getkey(self):
            return self._key

        def getvalue(self):
            return self._value

        def changekey(self,k):
            self._key = k

        def changevalue(self,v):
            self._Value = v

    def __init__(self):
        self._array = []
        self._root = None

    def search(self,item):
        return item in self._array

    #gets index counting from last
    def getindex(self,item):
        if self.search(item) == True:
            lent = len(self._array)
            LIST = self._array
            LIST.reverse()
            c = lent - 1
            for i in LIST:
                if i == item:
                    LIST.reverse()
                    return c
                else:
                    c -= 1
        else:
            print(item.__repr__(),"does not exist in Heap")

    def swap(self,itema,itemb):
        if self.search(itema) == True or self.search(itemb) == True:
            indexa = self.getindex(itema)
            indexb = self.getindex(itemb)
            self._array[indexa] = itemb
            self._array[indexb] = itema
        else:
            print(itema.__repr__(),'or',itemb.__repr__(),"does not exist in Heap")
            
    def print(self):
        for i in self._array:
            print(i.__repr__())

    #Searches from start of Array
    def getparent(self,item):
        if self.search(item) == True:
            indexitem = self.getindex(item)
            indexparent = int((indexitem - 1) / 2)
            return self._array[indexparent]
        else:
            print(item.__repr__(),"does not exist in Heap")
           
    def getleft(self,item):
        if self.search(item) == True:
            indexitem = self.getindex(item)
            indexleft = int((2 * indexitem) + 1)
            if indexleft >= len(self._array):
                return None
            else:
                return self._array[indexleft]
        else:
            print(item.__repr__(),"does not exist in Heap")
           
    def getright(self,item):
        if self.search(item) == True:
            indexitem = self.getindex(item)
            indexright = int((2 * indexitem) + 2)
            if indexright >= len(self._array):
                return None
            return self._array[indexright]
        else:
            print(item.__repr__(),"does not exist in Heap")
           
    def haschild(self,item):
        if self.search(item) == True:
            if self.getleft(item) != None or self.getright(item) != None:
                return True
            else:
                return False
        else:
            print(item.__repr__(),"does not exist in Heap")
            
    def minchild(self,item):
        if self.haschild(item) == True:
            if self.getright(item) == None:
                return self.getleft(item)
            if self.getleft(item).__lt__(self.getright(item)):
                return self.getleft(item)
            else:
                return self.getright(item)
        else:
            return None

    def insert(self,k,v):
        item = self.Item(k,v)
        self._array.append(item)
        if self._array[0] != item:
            while item.__lt__(self.getparent(item)):
                self.swap(self.getparent(item),item)
        self._root = self._array[0]

    def delete(self,item):
        if self.search(item) == True:
            initialindex = self.getindex(item)
            arraylength = len(self._array)
            self.swap(item,self._array[arraylength-1])
            del self._array[arraylength-1]
            if len(self._array) != 0:
                node = self._array[initialindex]
                while self.minchild(node) != None and node.__lt__(self.minchild(node)) == False:
                    self.swap(node,self.minchild(node))
                self._root = self._array[0]
            else:
                self._root = None
        else:
            print(item.__repr__(),"does not exist in Heap")
            
    def heapsort(self):
        LIST = []
        while len(self._array) != 0:
            LIST.append(self._root)
            self.delete(self._root)
        return LIST

    def heapify(self,LIST):
        for i in LIST:
            self.insert(i.getkey(),i.getvalue()) 

    def __len__(self):
        return len(self._array)

    def add(self,key,value):
        self.insert(key,value)

    def min(self):
        return self._root.__repr__()

    def remove_min(self):
        self.delete(self._root)
        print(self.min())

################################################################################

P = Priority_Queue()
for i in range(10):
    P.insert(random.randint(0,100),string.ascii_lowercase[i-1])
P.print()

