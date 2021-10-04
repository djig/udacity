LRU Cache will have following Member variable
Capacity: Integer
entries: Haspmap(dict) key and value: [usage_frequency_counter, value]

Method: get
Time Complexity: O(1) because Haspmap
Method : set
Time Complexity: O(1) Constant time Although we are looping through entries keys However Our haspmap will not grow beyond 5 entries. Which means O(5) == O(1)

Space Complexity : O(n) because of Hashmap(dict)
