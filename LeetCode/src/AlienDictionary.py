class Solution:
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS1 BFS
        BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS BFS1

        """
        ################ this part I build the dictionary of each words initialise as 0##########################
        Map = collections.defaultdict(set)
        degree = dict()

        if words == None or len(words) == 0: return result
        for s in words:
            for ch in s:
                degree[ch] = 0

        print("degree  ", degree)
        print("Map  ", Map)

        # this part I ordered the words by the order from up to down (only for the first differnet pair)
        for i in range(len(words) - 1):
            cur = words[i]
            nex = words[i + 1]
            length = min(len(cur), len(nex))
            for j in range(length):
                c1 = cur[j]
                c2 = nex[j]
                if c1 != c2:
                    Set = set()
                    if c1 in Map:
                        Set = Map.get(c1)
                    if c2 not in Set:
                        Set.add(c2)
                        Map[c1] = Set;
                        degree[c2] = degree.get(c2) + 1
                    break
        print("degree  ", degree)
        print("Map  ", Map)

        ##########################
        result = ''
        q = collections.deque()
        for c in degree.keys():
            if degree.get(c) == 0:
                q.append(c)

        print("queue  ", q)

        while (len(q) > 0):
            c = q.popleft()
            result += c
            if c in Map:  # vertical map before:after
                for c2 in Map.get(c):
                    degree[c2] = degree.get(c2) - 1
                    if degree.get(c2) == 0:
                        q.append(c2)
        print("last degree---------  ", degree)
        print("last Map ------------  ", Map)
        print("result ------------  ", result)

        if len(result) != len(degree): return ''

        return result

# class Solution {
#     public String alienOrder(String[] words) {
#     Map<Character, Set<Character>> map=new HashMap<Character, Set<Character>>();
#     Map<Character, Integer> degree=new HashMap<Character, Integer>();
#     String result="";
#     if(words==null || words.length==0) return result;
#     for(String s: words){
#         for(char c: s.toCharArray()){
#             degree.put(c,0);
#         }
#     }
#     for(int i=0; i<words.length-1; i++){
#         String cur=words[i];
#         String next=words[i+1];
#         int length=Math.min(cur.length(), next.length());
#         for(int j=0; j<length; j++){
#             char c1=cur.charAt(j);
#             char c2=next.charAt(j);
#             if(c1!=c2){
#                 Set<Character> set=new HashSet<Character>();
#                 if(map.containsKey(c1)) set=map.get(c1);
#                 if(!set.contains(c2)){
#                     set.add(c2);
#                     map.put(c1, set);
#                     degree.put(c2, degree.get(c2)+1);
#                 }
#                 break;
#             }
#         }
#     }
#     Queue<Character> q=new LinkedList<Character>();
#     for(char c: degree.keySet()){
#         if(degree.get(c)==0) q.add(c);
#     }
#     while(!q.isEmpty()){
#         char c=q.remove();
#         result+=c;
#         if(map.containsKey(c)){
#             for(char c2: map.get(c)){
#                 degree.put(c2,degree.get(c2)-1);
#                 if(degree.get(c2)==0) q.add(c2);
#             }
#         }
#     }
#     if(result.length()!=degree.size()) return "";
#     return result;
# }
# }
