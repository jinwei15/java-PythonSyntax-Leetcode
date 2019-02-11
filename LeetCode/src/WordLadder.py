class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, begin, end, bank):
        if begin == end: return 1
        if end not in bank: return 0

        beginSet, endSet = {begin}, {end}  # Note: set not dict
        d = {b: 1 for b in bank}  # either remove visted or hash
        print(d)
        steps = 1
        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet  # balance
            temp = set()
            for x in beginSet:
                for i in range(len(x)):
                    for t in string.ascii_lowercase:
                        if x[i] == t: continue
                        y = x[:i] + t + x[i + 1:]
                        if y in endSet: return steps + 1
                        if d.get(y, 0):
                            d[y] = 0
                            temp.add(y)
            beginSet = temp
            steps += 1
        return 0

    # ##########################version 2 copied java######################################
# public class Solution {

# public int ladderLength(String beginWord, String endWord, Set<String> wordList) {
# 	Set<String> beginSet = new HashSet<String>(), endSet = new HashSet<String>();

# 	int len = 1;
# 	int strLen = beginWord.length();
# 	HashSet<String> visited = new HashSet<String>();

# 	beginSet.add(beginWord);
# 	endSet.add(endWord);
# 	while (!beginSet.isEmpty() && !endSet.isEmpty()) {
# 		if (beginSet.size() > endSet.size()) {
# 			Set<String> set = beginSet;
# 			beginSet = endSet;
# 			endSet = set;
# 		}

# 		Set<String> temp = new HashSet<String>();
# 		for (String word : beginSet) {
# 			char[] chs = word.toCharArray();

# 			for (int i = 0; i < chs.length; i++) {
# 				for (char c = 'a'; c <= 'z'; c++) {
# 					char old = chs[i];
# 					chs[i] = c;
# 					String target = String.valueOf(chs);

# 					if (endSet.contains(target)) {
# 						return len + 1;
# 					}

# 					if (!visited.contains(target) && wordList.contains(target)) {
# 						temp.add(target);
# 						visited.add(target);
# 					}
# 					chs[i] = old;
# 				}
# 			}
# 		}

# 		beginSet = temp;
# 		len++;
# 	}

# 	return 0;
# }
# }


# from collections import *

##########################version 1 copied######################################
# class Solution():
#     def ladderLength(self, beginWord, endWord, wordList):

#         def construct_dict(word_list):
#             d = collections.defaultdict(list)
#             for word in word_list:
#                 for i in range(len(word)):
#                     s = word[:i] + "_" + word[i+1:]
#                     d[s].append(word)
#             return d

#         def bfs_words(begin, end, dict_words):
#             queue, visited = deque([(begin, 1)]), set()
#             while queue:
#                 word, steps = queue.popleft()
#                 if word not in visited:
#                     visited.add(word)
#                     if word == end:
#                         return steps
#                     for i in range(len(word)):
#                         s = word[:i] + "_" + word[i+1:]
#                         neigh_words = dict_words.get(s, [])
#                         for neigh in neigh_words:
#                             if neigh not in visited:
#                                 queue.append((neigh, steps + 1))
#             return 0

#         d = construct_dict(wordList)
#         return bfs_words(beginWord, endWord, d)


