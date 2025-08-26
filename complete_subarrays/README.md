# Count Complete Subarrays in an Array


## Idea

My first idea was to enumerate all possible subarrays and then eliminate the ones that didn't respect the completude criteria, this solution was naive and it's complexity was O(n^3) which can be impracticable in practice, so i used a "sliding window" approach to construct the subarrays.


## Note

Interesting operations: len(set(list)) = #distinct element of list
