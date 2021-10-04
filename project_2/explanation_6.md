DataStructure used for this Problem
LinkedList
Hashmap(Dict)
Hashset(Set)

First solution for Union and Intersection includes duplicate elements and creates new result link list
Time Complexity: O(n+m) n=list1 length m = list2 length
Space Complexity: O(n+m) result linked list + O(n) for Hash set = O(n+m)

Second solution without duplicated
Time Complexity: O(n+m) n=list1 length m = list2 length
Space Complexity: O(n+m) result linked list + O(n) for Hash set = O(n+m)

Third solution Inplace modification of existing Linked List (No Extra space for result)
Time Complexity: O(n+m) n=list1 length m = list2 length
Space Complexity: O(n) hashmap/set
