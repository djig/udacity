#### Design Choice:
- Since Array is sorted We know Binary search will provide O(logn) time complextity compare to Linear search
However Input is rotated array Which means we need to modify binary search direction based on part of array where it's sort direction is ascending or descending.

- This solution requires special handling of left and right pointers of Binary search,

### Complexity Analysis
- Time Complexity: O(logn)
- Space Complexity: O(1)
