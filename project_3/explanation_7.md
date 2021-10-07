### Design Consideration:

- HTTP router functionality specifically ask to use Trie Datastructure 
- RouteTrieNode 
    - children : Haspmap(Dict) for better Search Time Complexity
    - is_final_handler: to keep track of end is it leaf node or not.



Since this solution is based on Trie structure 
### Complexity Analysis
- RouteTrie:
   - **insert**
    O(n) n =  length of subpath that has been inserted.. for example /home/about n=2 ... 
    Although we can say constant complexity also because Subpaths may not exceed to max lenght because 
    Browser can n't support large subpaths.
    Unlike Autocomplete trie Here We are storing word as key for RouteTrie Node Which means it will not group like Charater based Trie.
 
**Space Complexity** : Space complexity of trie in general will require more space.
O(n)
- n: Total no of subpaths. If we have 10 route handlers and each route has average 5 subpaths then It will be 50. Which means It will require more space.

**Router**:
**add_handler**:  It's wrapper on top of RouteTrie Insert method . Same as RouterTrie Insert

**lookup**: O(n): n=  length of subpath that has to be found.. for example /home/about n=2
