
from simhash import Simhash, SimhashIndex
import preprocess
import set_simhash
import candidates
import match

lists = preprocess.preprocess()
simhashlist = set_simhash.set_simhash(lists[0],lists[1])
can = candidates.createCandidates2(simhashlist[0],simhashlist[1])
result = match.compare(lists[0], lists[1], can)
print(result)
#i = 0
#while(i < len(can)):
#    print(i+1, can[i])
#    i = i + 1