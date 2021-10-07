### Design Consideration:

- Trie Data structure has best time complexity for Auto Complete and This problem description specifically asked to implement Auto complete using Trie Data Structure.
- TrieNode Children : HashMap(Dict), which has constant Time Complexity O(1) for search(Each Character will have key) Although 52 asci length index array can achieve same result as Dict However dict can support any language character utf also.

### Complexity Analysis

-  insert: O(n) worst cast (n = no of character in one word)
- find: Which will call suffix of TrieNode. O(n): n = no of Characters
- Trie Space Complexity: O(n) 
