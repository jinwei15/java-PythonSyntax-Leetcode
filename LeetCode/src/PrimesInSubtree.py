# You will be given a description of a tree rooted at node 1, with each node having an
# associated value. After you construct the tree,
# there will be a number of queries in the form of
# a node number. For each query, determine the number of elements in the subtree rooted at
# the query node that have values that are prime numbers.
#
#
# As an example, the following tree has been created. The labels are in the form [data]/[node
# number]. Assuming the query is 3, we analyze the blue subtree and determine there are 2
# prime values in the subtree: 2 and 3 located in nodes 5 and 6. The value in node 3, i.e. 6, is
# not prime.

# Complete the function primeQuery in the editor below. The function must return an array of
# integers, each the result of a query, aligned by index.
# primeQuery has the following parameter(s):
# n: an integer denoting the number of nodes in the tree to be labeled 1 to n
# u[u[0],...u[n-1]]: an array of integers denoting start node of each edge[i]
# v[v[0],...v[n-1]]: an array of integers denoting end node of each edge[i]
# values[values[1],...values[n]]: an array of integers denoting the data value for each node[i]

class PrinesInSubtree:
    def isPrime(self, n):
        if n <= 3 : return True
        if n % 2 == 0: return  False

        i = 2
        while(i * i <= n):
            if n % i == 0: return False
            i += 1

        return True

    def primeQuery(self, number, starts, ends, values, queries):
        countDict = [None for _ in range(number)]
        indexDict = [None for _ in range(number)]

        for i in range(len(values)):
            if self.isPrime(values[i]):
                countDict[i] = 1
            else:
                countDict[i] = 0

        for i in range(len(indexDict)):
            indexDict[i] = i

        for i in range(len(starts)):
            idx = ends[i] - 1
            ptr = starts[i] - 1
            indexDict[idx] = ptr

        for i in range(len(countDict)):
            temp = i
            while(indexDict[temp] != temp):
                temp = indexDict[temp]
                countDict[temp] += countDict[i]


        res = [None for _ in range(len(queries))]
        for i in range(len(queries)):
            res[i] = countDict[queries[i] - 1]

        return res

n = 6
startNode = [1,2,2,1,3]
endNodes = [2, 4, 5, 3, 6]
values = [2, 2, 6, 5, 4, 3]
queries = [1, 4, 5, 6, 2]

print(PrinesInSubtree().primeQuery(n, startNode, endNodes, values, queries))
