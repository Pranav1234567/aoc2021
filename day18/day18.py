class BinTree():
  def __init__(self, val, parent, left, right, t=None):
    self.val = val
    self.parent = parent
    self.left = left
    self.right = right
    self.t = t

def push(obj, l, depth):
    while depth:
        l = l[-1]
        depth -= 1
    if obj != []:
        obj = int(obj)
    l.append(obj)

def convert(s):
    groups = []
    depth = 0
    for char in s:
        if char == '[':
            push([], groups, depth)
            depth += 1
        elif char == ']':
            depth -= 1
        else:
            if char != ',':
                push(char, groups, depth)
    return groups

def printTree(node, level=0):
    if node != None:
        printTree(node.left, level + 1)
        print(' ' * 4 * level + '->', node.val)
        printTree(node.right, level + 1)

# only has leaves with values, rest are 0s
def convert_to_bintree(sn, parent=None, t=None):
    if sn != []:
        left = sn[0]
        right = sn[1]
        parent = BinTree(0, None, None, None, None)
        if type(left) == int:
            leftTree = BinTree(left, parent, None, None, t)
        else:
            leftTree = convert_to_bintree(left, parent, t)
        if type(right) == int:
            rightTree = BinTree(right, parent, None, None, t)
        else:
            rightTree = convert_to_bintree(right, parent, t)

        leftTree.parent = parent
        rightTree.parent = parent
        leftTree.t = 'left'
        rightTree.t = 'right'

        parent.left = leftTree
        parent.right = rightTree
        return parent
    return None

def convert_to_snailfish(bt):
    if bt.left and bt.right:
        return [convert_to_snailfish(bt.left), convert_to_snailfish(bt.right)]
    elif bt.left:
        return convert_to_snailfish(bt.left)
    elif bt.right:
        return convert_to_snailfish(bt.right)
    else:
        return bt.val

def find_nested_pairs(sn):
    result = []
    find_nested_pair_helper(sn, 0, result)
    if result:
        return result[0]
    return None

def find_nested_pair_helper(sn, depth, result):
    if type(sn) != int:
        if depth == 4:
                if type(sn[0]) == int and type(sn[1]) == int:
                    result.append(sn)
        else:
            find_nested_pair_helper(sn[0], depth + 1, result)
            find_nested_pair_helper(sn[1], depth + 1, result)

def explode_pair(bt, pair, root):
    if bt:
        if bt.left and bt.right:
            if bt.left.val == pair[0] and bt.right.val == pair[1]:
                # do
                if bt.t == 'left':
                    # left most element in right subtree
                    if bt.parent:
                        rightSubTree = bt.parent.right
                        while rightSubTree.left:
                            rightSubTree = rightSubTree.left
                        rightSubTree.val += pair[1]

                elif bt.t == 'right':
                    # right most element in left subtree
                    if bt.parent:
                        leftSubTree = bt.parent.left
                        while leftSubTree.right:
                            leftSubTree = leftSubTree.right
                        leftSubTree.val += pair[0]
        if bt.left:
            bt.left = explode_pair(bt.left, pair, root)
        if bt.right:
            bt.right = explode_pair(bt.right, pair, root)
        return bt
    return None

def add(sn1, sn2):
    return [sn1, sn2]

# binary operations - explode & split
def reduce(sn):
    return None

def magnitude(sn):
    return None

with open('day18_input.txt') as f:
    lines = f.readlines()
    snailfish_nums = []
    for line in lines:
        snailfish_num = convert(line.rstrip())
        snailfish_nums.append(snailfish_num[0])

    tree = convert_to_bintree(snailfish_nums[0])
    # printTree(tree)
    snailfish_back = convert_to_snailfish(tree)

    # i = 0
    # first = None
    # while i < len(snailfish_nums):
    #     if not first:
    #         first = snailfish_nums[i]
    #         second = snailfish_nums[i+1]
    #         first = reduce(add(first, second))
    #         i += 2
    #     else:
    #         second = snailfish_nums[i]
    #         first = reduce(add(first, second))
    #         i += 1
    #
    # return magnitude(first)
