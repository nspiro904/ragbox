
# type TreeNode = TreeNode

class TreeNode():
  value: str
  left = None
  right = None

  def __init__(self, value: str):
    self.value = value

class BinaryTree():
  root: TreeNode = None

  def __insert__(self, value: str, node: TreeNode,):

    if (value < node.value):
      if(node.left == None):
        node.left = TreeNode(value)
        return
      else:
        self.__insert__(value, node.left)

    if ( value > node.value):
      if(node.right == None):
        node.right = TreeNode(value)
        return
      else:
        self.__insert__(value, node.right)

  def insert(self, value: str):
    if(self.root == None):
      self.root = TreeNode(value)
    else:
      self.__insert__(value, self.root)

  def __trace__(self, node: TreeNode, value: str):
    if(value > node.value):
      print(f" > {node.value}")
      self.__trace__(node.right, value)
    elif(value < node.value):
      print(f" < {node.value}")
      self.__trace__(node.left, value)

  def trace(self, value: str):
    if(self.root.value != value):
      self.__trace__(self.root, value)
    else:
      print(value)
