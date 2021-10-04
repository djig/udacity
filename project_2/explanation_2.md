This problem can be solved by recursively as well as Iteratively.
Since it's require to scan all sub directories , DFS is best way to solve this problem.
Recursive solution checks for path is directory then list all resources(files+directories)
It's add files to Results and calls again for directory with modified path using path join.
 
Iterative solution uses Queue data structure.
For both Solutions,
Time Complexity (n), space complexity(n) when n = no of all files
