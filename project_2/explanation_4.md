Class Group has member variables groups and users
groups are list and users are haspmap(dict)
Using Hashmap for users will provide O(1) time for searching user within one group.
Overall Complexity of Finding user in group is
O(N) +  Nested Group levels + No. of Total Groups at all levels (worst case)
Space Complexity: O(n). No of Users + No of Groups (For all levels)
