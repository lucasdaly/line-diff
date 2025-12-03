from simhash import Simhash, SimhashIndex

def createCandidates(old_simhash, new_simhash):

    #test code
    #lines = preprocess.preprocess()
    #sim_lines = set_simhash.set_simhash(lines[0], lines[1])
    #old_simhash = sim_lines[0]
    #new_simhash = sim_lines[1]

    i = 0
    candidatelist = []
    while(i < len(old_simhash)):
        j = 0
        closest = 9999999999999 # gets a large number for comparing can be adjusted for accuracy
        pos_closest = 0
        #loops through all new lines for each old line
        while(j < len(new_simhash)):
            dst = old_simhash[i].distance(new_simhash[j])
            #comparing the disctance of old simhash and new simhash
            if( dst < closest):
                print(dst)
                closest = dst
                pos_closest = j + 1
            j = j + 1
        print("--")
        i = 1 + i
        candidatelist.append(pos_closest)
        new_simhash[pos_closest-1] = Simhash(0)
        
    return candidatelist
    


