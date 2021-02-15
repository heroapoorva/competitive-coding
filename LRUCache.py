class Node:
    def __init__(self, val=None, prev=None, next= None):
        self.val= val
        self.prev= prev
        self.next= next
        
class Dlist:
    def __init__(self):
        self.head=Node()
        self.end=Node()
        self.head.next=self.end
        self.end.prev=self.head
        self.len=0
        
    def add(self, n):
        self.head.next.prev=n
        n.next=self.head.next
        n.prev=self.head
        self.head.next=n
        self.len+=1
    
    def eject(self):
        if(self.len>0):
            op=self.end.prev.val
            self.end.prev.prev.next=self.end
            self.end.prev=self.end.prev.prev
            self.len-=1
            return op
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.values={}
        self.ls=Dlist()

    def get(self, key: int) -> int:
        if key not in self.values: return -1
        t=self.values[key]
        t.next.prev=t.prev
        t.prev.next=t.next
        self.ls.len-=1
        self.ls.add(t)
        return self.values[key].val[0]

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            t=self.values[key]
            t.next.prev=t.prev
            t.prev.next=t.next
            self.ls.len-=1
        else:
            if self.capacity==self.ls.len :
                t=self.ls.eject()
                del self.values[t[1]]
        t=Node((value,key))
        self.values[key]=t
        self.ls.add(t)
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
