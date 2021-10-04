For Huffman Encoding:
As suggested on problem description Data structure used for this solutions are
Binary Tree, Hashmap(dict),
and min_heap where each values are tuple( frequecy and tree node)
Time Complexity : we are using min heap with heapq library. it is Olog(n)
Space Complexity: Big O O(n)
we are using minHeap O(n) + HaspMap(Asci or UTF codes )Constant O(256 for Asci) + tree(n)

For Decoding:
TimeComplexity: O(n*log(n))
n = no of resulted encoded  characters 
logn for traversing each characters from tree.

