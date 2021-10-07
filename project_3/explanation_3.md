Design Consideration:
THis problem specifically ask to provide solution with timecomplextity O(nlogn)
To acheive solution We will need sorted array.
Althought Bubble sort, selection sort or Insertion sort will able to get array sorted However all 3 sorted algorithms have O(n*n) time complexity. All three have better space complexity because of swaping input array.
Only Merge sort and Quicksort provides TimeComplexity O(nlogn):
Merge sort uses extra space while quick sort swaps array and it's more efficient for space complexity also.
Hence this solution is using both Merge and Quicksort to provide TimeComplexity O(nlogn)

Solution of this problem can be achieved by sorting Array using divide solve recursively

Time Complexity : O(nlog(n))
Space Complexity : constant(Inplace using pivot/partitioning)
