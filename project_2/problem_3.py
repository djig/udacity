import heapq
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        # this will hold code
        self.code = None

import sys

def huffman_encoding(data):
    if data == None or len(data) == 0:
        return '', None
    l = len(data)
    char_map = dict()
    min_heap = []
    for char in data:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1
    for key in char_map:
        node = Node(key)
        heapq.heappush(min_heap,( char_map[key], id(node), node))

    #  this is to handle only one char input. i.e. AAAA
    if len(min_heap) == 1:
        # set only one char frequency as left node to parent none
        parent_node = Node(None)
        min_heap[0][2].code = 0
        parent_node.left = min_heap[0][2]
        min_heap[0] = None, id(parent_node),parent_node
    # heapq.heappop(min_heap)
    while len(min_heap)> 1:
        left_node_tuple = heapq.heappop(min_heap)
        left_node_fre = left_node_tuple[0]
        left_node = left_node_tuple[2]
        right_node_tuple = (0,0, None)
        right_node = None
        if min_heap:
            right_node_tuple = heapq.heappop(min_heap)
            right_node = right_node_tuple[2]
            right_node_tuple[2].code = 1
            right_node_fre = right_node_tuple[0]
        
        left_node.code = 0
        parent_node = Node(None)
        parent_node.code = left_node.code + right_node.code
        parent_node.left = left_node
        parent_node.right = right_node
        parent_node_fre = left_node_fre + right_node_fre
        heapq.heappush(min_heap,(parent_node_fre, id(parent_node), parent_node))


    dict_code = dict()
    tree = min_heap[0][2]
    
    root = tree
    def traverse(node, val, isRoot=False):
        new_val = ''
        if isRoot == False:
            new_val = val +str(node.code)
        if node.left == None and node.right == None:
            node.code = new_val
            dict_code[node.value] = node.code
        if node.left:
            traverse(node.left, new_val)
        if node.right:
            traverse(node.right, new_val)
    traverse(root, '', True)
    ans = []
    for char in data:
        ans.append(dict_code[char])
    # print("dict_code")
    # print(dict_code)
    return ("".join(ans), tree)
    

def huffman_decoding(data,tree):
    
    list_chars = list(data)
    if len(list_chars) == 0:
        return ''
    #  result buffer
    ans = []
    def traverse(node, i):
        if node == None:
            return i
        if i >= len(list_chars):
            ans.append(node.value)
            return i+1
        if node.left == None and node.right == None:
            ans.append(node.value)
            return i
        bit = list_chars[i]
        if bit == "0":
            return traverse(node.left, i+1)
        if bit == "1":
           return traverse(node.right, i+1)

    i = 0
    curr = tree
    while i <= len(list_chars):
        i = traverse(curr, i)
        curr= tree
        
    return "".join(ans)

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"
   
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    # huffman_encoding(a_great_sentence)
    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    a_great_sentence = "AAAABBBBKJJKKKAJAJKJK"
   
    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    # Empty input
    a_great_sentence = ""
   
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)


    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The content of the encoded data is: {}\n".format(decoded_data))


    a_great_sentence = "AAA"
   
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)


    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The content of the encoded data is: {}\n".format(decoded_data))