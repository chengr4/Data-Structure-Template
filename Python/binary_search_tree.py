'''
Reference
[1] https://stackoverflow.com/questions/44090304/binary-search-tree-recursive-implementation-in-python
[2] https://medium.com/@Kadai/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E5%A4%A7%E4%BE%BF%E7%95%B6-binary-search-tree-3c40be3204e
'''
class Node(object):
  def __init__(self, key: int):
    self.left_node = None
    self.right_node = None
    self.parent_node = None
    self.key = key


class BinarySearchTree(object):
  # 先 init 一個 root
  def __init__(self, root):
    self.root = Node(root)
    
  def add_node(self, key:int):
    node = Node(key)
    current_node = self.root # 必要，因為 init 的值不能動
    while True:
      if node.key == current_node.key:
        raise Exception('same key value not allow')
      elif node.key < current_node.key:
        if current_node.left_node: # 若左 subtree 有值，進行下一輪比較
          current_node = current_node.left_node
        else:
          node.parent_node = current_node
          current_node.left_node = node
          break
      elif node.key > current_node.key:
        if current_node.right_node:
          current_node = current_node.right_node
        else:
          node.parent_node = current_node
          current_node.right_node = node
          break

  def check_node_by_key(self, key:int, node=None): 
    current_node = self.root
    while True:
      if key == current_node.key:
        return 'exist'
      elif key < current_node.key:
        if current_node.left_node:
          current_node = current_node.left_node
        else:
          raise Exception('node not found')
      elif key > current_node.key:
        if current_node.right_node:
          current_node = current_node.right_node
        else:
          raise Exception('node not found') 

BST = BinarySearchTree(50)
BST.add_node(3)
BST.add_node(33)
BST.add_node(34)
BST.add_node(22)
BST.add_node(360)
BST.add_node(-1)
print(BST.check_node_by_key(-1))
