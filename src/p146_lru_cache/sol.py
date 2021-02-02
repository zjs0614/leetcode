class LinkedNode:
    def __init__(self, value: int, key: int):
        self.value = value
        self.prev = None
        self.next = None
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {}
        self.rootNode = None
        self.tailNode = None

    def topNode(self, node):
        if self.rootNode is not None and node.key == self.rootNode.key:
            return
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if self.tailNode is not None and node.key == self.tailNode.key:
            self.tailNode = node.prev
        node.prev = None
        node.next = self.rootNode
        if self.rootNode is not None:
            self.rootNode.prev = node
        self.rootNode = node
        if self.tailNode is None:
            self.tailNode = node

    def get(self, key: int) -> int:
        if key in self.nodes:
            node = self.nodes[key]
            self.topNode(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.nodes and len(self.nodes) == self.capacity:
            self.nodes.pop(self.tailNode.key)
            self.tailNode = self.tailNode.prev
            if self.tailNode is not None:
                self.tailNode.next = None
        if key in self.nodes:
            self.nodes[key].value = value
            self.topNode(self.nodes[key])
        else:
            node = LinkedNode(value, key)
            self.nodes[key] = node
            self.topNode(node)
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)