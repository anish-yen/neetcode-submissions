class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None #need key value, prev, next
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #cahce holds keys and nodes
        self.head = ListNode(0,0) #iniatlize hashmap, head, tail capcity
        self.tail = ListNode(0,0)
        self.tail.prev = self.head
        self.head.next = self.tail
        

    def insert(self, node): #always insert at tail
        node.prev= self.tail.prev
        self.tail.prev.next = node
        node.next= self.tail
        self.tail.prev =node
        

    def remove(self, node):
        node.prev.next= node.next
        node.next.prev = node.prev  #remove before and after links
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        
        self.cache[key] = ListNode(key, value)
        self.insert(self.cache[key]) 

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key] # remove from hashamp

             #find length of dict directly
        
