# n = int(input())
# character = []
# for _ in range(n):
#     character.append(int(input()))

dictionary = {0: 45, 1: 13, 2: 12, 3: 16, 4: 9, 5: 5}
# ch = 'a'
# for i in enumerate(character):
#     dictionary[i[0]] = i[1]
# print(dictionary) 


class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        # probability of symbol
        self.prob = prob

        # symbol 
        self.symbol = symbol

        # left node
        self.left = left

        # right node
        self.right = right

        # tree direction (0/1)
        self.code = ''

codes = dict()

def Calculate_Codes(node, val=''):
    newVal = val + str(node.code)
    if(node.left):
        Calculate_Codes(node.left, newVal)
    if(node.right):
        Calculate_Codes(node.right, newVal)

    if(not node.left and not node.right):
        codes[node.symbol] = newVal
    return codes 

def Huffman_Encoding(dictionary):
    symbol_with_probs = dictionary
    symbols = symbol_with_probs.keys()
    nodes = []
    
    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))
    
    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.prob)
        right = nodes[0]
        left = nodes[1]
        print(right.prob, left.prob)
        left.code = 0
        right.code = 1
        newNode = Node(left.prob+right.prob, left.symbol+right.symbol, left, right)
    
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
            
    for value in nodes:
        print(value.prob)

    print(nodes[0].prob)
    huffman_encoding = Calculate_Codes(nodes[0])
    return huffman_encoding  

result = Huffman_Encoding(dictionary)
for value in result.values():
    print(value)