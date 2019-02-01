import collections
class HackerlandElection:
    def Election(self, votes):
        map = dict()
        for name in votes:
            map[name] = map.get(name, 0) + 1

        orderedDict = collections.OrderedDict(sorted(map.items()))

        return max(orderedDict.keys(), key=lambda k: orderedDict[k])

    def Election2(self,votes):

        winner = collections.Counter(votes).most_common(1)

        return winner

a  = HackerlandElection()
print(a.Election(['jinwei','marry','Alex','marry']))
print(a.Election2(['jinwei','marry','Alex']))
print(a.Election(['jinwei','marry','Alex']))
