# javaSyntax
basic java syntax that I wrote in Y2 and some leetcode solution

# building table for revision: (Incompleted)
Question + link + most intuitive thought about this question. You can find the answer under [LeetCode/src](https://github.com/jinwei14/java-PythonSyntax-Leetcode/tree/master/LeetCode/src)   

## Array
   [35. Search Insert Position.](https://leetcode.com/problems/search-insert-position/)   
   [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/)&nbsp;[-2,2,3,5]->1 wrong O(n^2) solution. O(n) is so hard.    
   [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)  
   [243. Shortest Word Distance](https://leetcode.com/problems/shortest-word-distance/)&nbsp; given word list find shorest dis between two words. one pass. need to define the shortest to max len first   
   [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) &nbsp; array deletion by element/index    
   [463. Island Perimeter](https://leetcode.com/problems/island-perimeter/)&nbsp; easy 2D array   
   [448. Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)&nbsp;check which number is missing from 1 to n. brilliant sol by converting index num to neg.      
   [605. Can Place Flowers](https://leetcode.com/problems/can-place-flowers/)&nbsp; single scan easy    
   [628. Maximum Product of Three Numbers](https://leetcode.com/problems/maximum-product-of-three-numbers/)&nbsp;find the biggest product of 3 nums in array   
   [704. Binary Search](https://leetcode.com/problems/binary-search/) &nbsp; binary search in array implementation right/left = mid +- 1    
   [766. Toeplitz Matrix](https://leetcode.com/problems/toeplitz-matrix/)&nbsp;2D array that all diagonal are the same    
   [904. Fruit Into Baskets](https://leetcode.com/problems/fruit-into-baskets/)&nbsp; two item basket, find the largest range in array. Slicing window classic   
   [944. Delete Columns to Make Sorted](https://leetcode.com/problems/delete-columns-to-make-sorted/)&nbsp; pool descripted delete X column to make it alway ascending.   
   [Two Sum - Closest to target ](https://yeqiuquan.blogspot.com/2017/04/lintcode-533-two-sum-closest-to-target.html)&nbsp;Lintcode533 Amazon OA2 TwoSumClosest.py        

## String manipulation (addition, replace(deletion)):
   [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)&nbsp; classic palindrome number but used a werid amazing number reverse method.   
   [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)&nbsp; classic Palindrome number (two pointer/reversed)  
   [443. String Compression](https://leetcode.com/problems/string-compression/) &nbsp; easy,String    
   [482. License Key Formatting](https://leetcode.com/problems/license-key-formatting/)  
   [520. Detect Capital](https://leetcode.com/problems/detect-capital/)&nbsp; substring    
   [680. Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii/)&nbsp; two pointer solution. s==s[::-1].   
   [844. Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)  
   [917. Reverse Only Letters](https://leetcode.com/problems/reverse-only-letters/)&nbsp;two pointer sol, string is immutable. convert to list then join.   

## HashTable/Counter:
   [number of substring with exact k distinct element](https://drive.google.com/drive/folders/1zfwa-4YmDQkF8B7QoYvo80lu3xqgkqPI) amazon OA2  NumOfSubstringwithExactKDistinctCharacters.py   
   [159. Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) &nbsp; usnig hashMap but was shit. slicing windiw is better.   
   [169. Majority Element](https://leetcode.com/problems/majority-element/) &nbsp; most basic hashMap  
   [170. Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/)&nbsp; same as two sum, but not good enough   
   [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) &nbsp; I use two arrays one check against two. Two check against one.  
   [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/)&nbsp; easy hashMap    
   [246. Strobogrammatic Number](https://leetcode.com/problems/strobogrammatic-number/) &nbsp;hashtable + two pointer easy   
   [266. Palindrome Permutation](https://leetcode.com/problems/palindrome-permutation/)&nbsp; a word turn to palindrome after permu    
   [350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)&nbsp; easy classic hashMap  
   [389. Find the Difference](https://leetcode.com/problems/find-the-difference/) classic hashtable !   
   [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)&nbsp; classic slicing window problem !two hashtables + dictionary deletion  
   [532. K-diff Pairs in an Array](https://leetcode.com/problems/k-diff-pairs-in-an-array/) &nbsp; easy hashtable classic bloomberg interview.   
   [697. Degree of an Array](https://leetcode.com/problems/degree-of-an-array/) &nbsp; minLength of subarray with maxdegree.3 hashMaps    
   [706. Design HashMap](https://leetcode.com/problems/design-hashmap/)&nbsp; implementation of hashmap, easy   
   [760. Find Anagram Mappings](https://leetcode.com/problems/find-anagram-mappings/) &nbsp; different version of Anagram   
   [811. Subdomain Visit Count](https://leetcode.com/problems/subdomain-visit-count/)  
   [961. N-Repeated Element in Size 2N Array](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/) &nbsp; very easy hashMap   

## LinkedList:
   [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)&nbsp; classic linkedlist plus Math plus  
   [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) &nbsp; keep track a previous node and keep updating prev.next, also recurrsive<img height="400" width="500" alt="21" src="https://user-images.githubusercontent.com/26280459/56148273-d0dc9080-5fa1-11e9-854f-ed77c119e0e6.PNG">

   [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)  
   [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)  
   [146. LRU Cache](https://leetcode.com/problems/lru-cache/)&nbsp; LRU linkedlist + hashmap/ dequeue + hashmap. classic    
   [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/)&nbsp; using two pointer to solove linkedlist, classic   
   [203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)  
   [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)&nbsp;reverse(iteratively or recursively)  
   [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) &nbsp; same as 9/125 Palindrome  
   [445. Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/) &nbsp; 1.reverse and reverse back. 2.using stack    
   [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

## Recursive:
Things to know:
1. The base case: this is the hardest to define. we need to figure out the boundury condition and return type
2. the recursion rules: the return type should be the same as base case, some time we need to keep an eye on whether it is a pre-order, post-order or in-order traversal.
3. write some easy example to run through. It is fine if the first two step are wrong, write some cases to figure which part is wrong.     
[Big O](https://stackoverflow.com/questions/13467674/determining-complexity-for-recursive-functions-big-o-notation)    

   [24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/) &nbsp; use iterative or recurrsive

   <img src="https://user-images.githubusercontent.com/26280459/56078275-2bc58a80-5dde-11e9-9ebe-2dea5bc90852.JPG" alt="24" height="400px" width="500px">   

   [50. Pow(x, n)](https://leetcode.com/problems/powx-n/) &nbsp; brute force search TLE, recussive and iteration works<img  height="400px" width="500" alt="50" src="https://user-images.githubusercontent.com/26280459/56144416-3b89ce00-5f9a-11e9-8e52-f5fe14f4eb75.PNG">

   [95. Unique Binary Search Trees II](https://leetcode.com/problems/unique-binary-search-trees-ii/) &nbsp; break down and G(n) = G(i-1)G(n-i)       
   <img height="300" width="200" alt="95" src="https://user-images.githubusercontent.com/26280459/56367090-63707000-61ec-11e9-905d-80b908d5009c.PNG">


   [118. Pascal's Triangle](https://leetcode.com/problems/pascals-triangle/) &nbsp; TLE using recursion. use iterative approach instead.<img height="400px" width="500px" alt="500" src="https://user-images.githubusercontent.com/26280459/56081115-7e646e00-5e01-11e9-91bd-6857519d9967.PNG">

   [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)&nbsp;reverse lnkedlist (iteratively or recursively).<img height="400px" width="500" alt="206" src="https://user-images.githubusercontent.com/26280459/56091506-b0301000-5ea7-11e9-8f9e-b585e2adb8d3.PNG">

   [779. K-th Symbol in Grammar](https://leetcode.com/problems/k-th-symbol-in-grammar/) &nbsp; find the kth element by recussion.   
   <img height="400" width="282" alt="779" src="https://user-images.githubusercontent.com/26280459/56198580-16956980-6033-11e9-89c9-8ec19d6f45ec.PNG">



## Stack:
   [682. Baseball Game](https://leetcode.com/problems/baseball-game/) &nbsp; classic stack problem easy  
   [716. Max Stack](https://leetcode.com/problems/max-stack/) &nbsp; tuple in stack similar to MinStack but adding popMax!   
   [844. Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)  

## Queue:
   [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/) &nbsp; using two stack to implement this   
   [346. Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream/)&nbsp; Queue implementation dequeue python.   

## Math
   [168. Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/)&nbsp; math same as 171, base 26 num.   
   [171. Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/)&nbsp; ASCII num + math   
   [202. Happy Number](https://leetcode.com/problems/happy-number/) &nbsp;loop + hashMap check existance. easy.   
   [204. Count Primes](https://leetcode.com/problems/count-primes/)  &nbsp; isPrime() find common facter of n from 0 to sqrt(n). Convert it to DP!    
   [231. Power of Two](https://leetcode.com/problems/power-of-two/) &nbsp; math problem, can be solved as bit manipulation as well. (bit count)  
   [258. Add Digits](https://leetcode.com/problems/add-digits/)    
   [263. Ugly Number](https://leetcode.com/problems/ugly-number/) &nbsp; easy math    
   [412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz/)  
   [415. Add Strings](https://leetcode.com/problems/add-strings/) &nbsp; addition bit by bit plus carries   
   [888. Fair Candy Swap](https://leetcode.com/problems/fair-candy-swap/)&nbsp; sum(left)-x+y = sum(right)-y+x Math   
   [942. DI String Match](https://leetcode.com/problems/di-string-match/)&nbsp; Brilliant math problem   
   [970. Powerful Integers](https://leetcode.com/problems/powerful-integers/)&nbsp; attention to notes. x^i + y^j < bound    

## DFS/BFS:
   [SubtreewithMaximumAverage](https://yeqiuquan.blogspot.com/2017/03/lintcode-597-subtree-with-maximum.html)&nbsp; lintcode Amazon OA2 SubtreewithMaximumAverage.py   
   [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)&nbsp; DFS post-order traversal to find the maximum depth.    
   <img height="400" width="500" alt="104" src="https://user-images.githubusercontent.com/26280459/56094776-28a9c780-5ece-11e9-9c94-93fa5b65a728.PNG">

   [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)  
   [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)&nbsp;BFS/DFS all can solved this   
   [339. Nested List Weight Sum](https://leetcode.com/problems/nested-list-weight-sum/)&nbsp; DFS but using a new function everytime, classic!   
   [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)&nbsp; DFS, classic one   
   [965. Univalued Binary Tree](https://leetcode.com/problems/univalued-binary-tree/)&nbsp; easy DFS BFS using back tracking.    

## Dynamic Programming:
   [MaximumMinimumPath](https://drive.google.com/drive/folders/1zfwa-4YmDQkF8B7QoYvo80lu3xqgkqPI)Amazon OA2 MaximumMinimumPath.py   
   [5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)&nbsp; Brute used need to be rewrite.   
   [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)&nbsp; given arrry of num represent of height, maximum trapped water, Brute force-> DP-> stack.   
   [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)&nbsp; classic DP    
   [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)  
   [174. Dungeon Game](https://leetcode.com/problems/dungeon-game/) very hard DP backwords DP.   
   [198. House Robber](https://leetcode.com/problems/house-robber/) &nbsp; current optimal = max(previousprevious opt + now, previous opt)    
   [509. Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)&nbsp; Fibonacci number    
   [674. Longest Continuous Increasing Subsequence](https://leetcode.com/problems/longest-continuous-increasing-subsequence/)&nbsp; simple DB by store the previous result   

## Search
   ```python
   def binarySearch(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if len(nums) == 0:
        return -1

    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # End Condition: left > right
    return -1
   ```
   [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)&nbsp; Binary search      
   [33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) &nbsp; binarySearch case starting point not at index 0, find the starting point First    
   [374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/) &nbsp; Binary search    

## Min Max Heap
   [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)&nbsp; this can literally done by sorting but MinMax heap is better (dont understand)   
   [703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)&nbsp; minHeap with len(k) using heapq, pushpop()   

## Bash
   [195. Tenth Line](https://leetcode.com/problems/tenth-line/) &nbsp; print 10th line of a .txt  

## Bit  
   [190. Reverse Bits](https://leetcode.com/problems/reverse-bits/) &nbsp; reverse bits and convert to integer.   
   [191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)&nbsp; hamming weight   
