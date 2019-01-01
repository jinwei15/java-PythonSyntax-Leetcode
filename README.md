# javaSyntax
basic java syntax that I wrote in Y2 and some leetcode solution 

# building table for revision: (Incompleted)
Question + link + most intuitive thought about this question. You can find the answer under [LeetCode/src](https://github.com/jinwei14/java-PythonSyntax-Leetcode/tree/master/LeetCode/src)

## Array:
   [35. Search Insert Position.](https://leetcode.com/problems/search-insert-position/)   
   [64. Minimum Path Sum](https://leetcode.com/problems/minimum-path-sum/)  
   [283. Move Zeroes](https://leetcode.com/problems/move-zeroes/) &nbsp; array deletion by element/index  
   [605. Can Place Flowers](https://leetcode.com/problems/can-place-flowers/)&nbsp; single scan easy    
   [Two Sum - Closest to target ](https://yeqiuquan.blogspot.com/2017/04/lintcode-533-two-sum-closest-to-target.html)&nbsp;Lintcode533 Amazon OA2 TwoSumClosest.py        
        
## HashTable/Counter:
   [number of substring with exact k distinct element](https://drive.google.com/drive/folders/1zfwa-4YmDQkF8B7QoYvo80lu3xqgkqPI) amazon OA2  NumOfSubstringwithExactKDistinctCharacters.py   
   [159. Longest Substring with At Most Two Distinct Characters](https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/) &nbsp; usnig hashMap but was shit. slicing windiw is better.   
   [169. Majority Element](https://leetcode.com/problems/majority-element/) &nbsp; most basic hashMap  
   [170. Two Sum III - Data structure design](https://leetcode.com/problems/two-sum-iii-data-structure-design/)&nbsp; same as two sum, but not good enough   
   [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/) &nbsp; I use two arrays one check against two. Two check against one.  
   [350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)&nbsp; easy classic hashMap  
   [438. Find All Anagrams in a String](https://leetcode.com/problems/find-all-anagrams-in-a-string/)&nbsp; classic slicing window problem !two hashtables + dictionary deletion  
   [760. Find Anagram Mappings](https://leetcode.com/problems/find-anagram-mappings/) &nbsp; different version of Anagram   
   [811. Subdomain Visit Count](https://leetcode.com/problems/subdomain-visit-count/)  
   [961. N-Repeated Element in Size 2N Array](https://leetcode.com/problems/n-repeated-element-in-size-2n-array/) &nbsp; very easy hashMap   

## LinkedList:
   [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)&nbsp; classic linkedlist plus Math plus  
   [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)  
   [83. Remove Duplicates from Sorted List](https://leetcode.com/problems/remove-duplicates-from-sorted-list/)  
   [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)  
   [203. Remove Linked List Elements](https://leetcode.com/problems/remove-linked-list-elements/)  
   [206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)&nbsp; classic linked list reverse  
   [234. Palindrome Linked List](https://leetcode.com/problems/palindrome-linked-list/) &nbsp; same as 9/125 Palindrome  
   [445. Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/) &nbsp; 1.reverse and reverse back. 2.using stack    
   [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

## Stack:
   [682. Baseball Game](https://leetcode.com/problems/baseball-game/) &nbsp; classic stack problem easy  
   [716. Max Stack](https://leetcode.com/problems/max-stack/) &nbsp; tuple in stack similar to MinStack but adding popMax!   
   [844. Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)  

## String manipulation (addition, replace(deletion)):
   [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)&nbsp; classic palindrome number but used a werid amazing number reverse method.   
   [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)&nbsp; classic Palindrome number (two pointer/reversed)  
   [482. License Key Formatting](https://leetcode.com/problems/license-key-formatting/)  
   [844. Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/)  
    
## Math
   [202. Happy Number](https://leetcode.com/problems/happy-number/) &nbsp;loop + hashMap check existance. easy.   
   [204. Count Primes](https://leetcode.com/problems/count-primes/)  &nbsp; isPrime() find common facter of n from 0 to sqrt(n). Convert it to DP!    
   [231. Power of Two](https://leetcode.com/problems/power-of-two/) &nbsp; math problem, can be solved as bit manipulation as well. (bit count)  
   [258. Add Digits](https://leetcode.com/problems/add-digits/)    
   [412. Fizz Buzz](https://leetcode.com/problems/fizz-buzz/)  
   [415. Add Strings](https://leetcode.com/problems/add-strings/) &nbsp; addition bit by bit plus carries   

## DFS/BFS:
   [SubtreewithMaximumAverage](https://yeqiuquan.blogspot.com/2017/03/lintcode-597-subtree-with-maximum.html)&nbsp; lintcode Amazon OA2 SubtreewithMaximumAverage.py   
   [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)  
   [339. Nested List Weight Sum](https://leetcode.com/problems/nested-list-weight-sum/)&nbsp; DFS but using a new function everytime, classic!   
   [543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)&nbsp; DFS, classic one   
   [965. Univalued Binary Tree](https://leetcode.com/problems/univalued-binary-tree/)&nbsp; easy DFS BFS using back tracking.    

## Dynamic Programming:
   [MaximumMinimumPath](https://drive.google.com/drive/folders/1zfwa-4YmDQkF8B7QoYvo80lu3xqgkqPI)Amazon OA2 MaximumMinimumPath.py   
   [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)&nbsp; classic DP    
   [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)  
   [174. Dungeon Game](https://leetcode.com/problems/dungeon-game/) very hard DP backwords DP.   
   [198. House Robber](https://leetcode.com/problems/house-robber/) &nbsp; current optimal = max(previousprevious opt + now, previous opt)  

## Min Max Heap
   [215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)&nbsp; this can literally done by sorting but MinMax heap is better (dont understand)  

## Bash
   [195. Tenth Line](https://leetcode.com/problems/tenth-line/) &nbsp; print 10th line of a .txt  



