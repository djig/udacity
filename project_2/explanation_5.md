Starts with Helper Static method for generating hash code based on input string.
and get utc value for now

Class Block Datastructure to hold block data, hash value and previous hash

Class Blockchain is linked list of Blocks with hashmap-disctionary for O(1) serach look up for block

Blockchain Operations and Big O complexity:
Method: append
Time Complexity : O(1),  it changes tail, dictionary and size
Method: Size
Time Complexity: O(1)
Method: get_block
Time Complexity: O(1) based on Hashmap(dict),
Method : delete_block
Time Complexity: O(n) because it loops through linked list to search for previous hash of deleted node to change to deleted node's previous hash. 

Method : traverse
Time Complexity: O(n)

Space Complexity O(n): Linked list, Hashmap grows linearly 