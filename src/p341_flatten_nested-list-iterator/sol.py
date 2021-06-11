# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class MyTreeNode:
  def __init__(self, val, parent, children):
    self.val = val
    self.parent = parent
    self.children = children
    self.child_index = 0

class NestedIterator:
  def __init__(self, nestedList: [NestedInteger]):
    self.root = MyTreeNode(None, None, [])
    self.populateTree(nestedList, self.root)
    self.current = self.resetCurrent()
  
  def findNext(self, current):
    parent = current.parent
    while parent is not None and parent.child_index == len(parent.children) - 1:
      parent = parent.parent
    if parent is None:
      return None
    else:
      node = parent
      node.child_index = node.child_index + 1
      while node.val is None:
        node = node.children[node.child_index]
      return node
  
  def resetCurrent(self):
    current = self.root
    while current.val is None and current.child_index < len(current.children):
      current = current.children[current.child_index]
    return current if current.val is not None else None
    
  def populateTree(self, nestedList, node):
    for item in nestedList:
      if not item.isInteger():
        sub_node = MyTreeNode(None, node, [])
        self.populateTree(item.getList(), sub_node)
        if sub_node.children:
          node.children.append(sub_node)
      else:
        node.children.append(MyTreeNode(item.getInteger(), node, []))
    return node
  
  def next(self) -> int:
    if self.current is not None:
      val = self.current.val
      self.current = self.findNext(self.current)
      return val
    else:
      return -1
      
  
  def hasNext(self) -> bool:
    return True if self.current is not None else False
  