
from simhash import Simhash

def set_simhash(old_lines, new_lines):
    # Test code
    #lines = preprocess.preprocess()
    #old_lines = lines[0]
    #new_lines = lines[1]

    #intilises the arrays
    old_simhash = []
    new_simhash = []

    #Sets simhashes for each line in old file
    i = 0
    while(i < len(old_lines)):
        old_simhash.append(Simhash(old_lines[i]))
        i = i + 1

    #Sets simhashes for each line in new file
    i = 0
    while(i < len(new_lines)):
        new_simhash.append(Simhash(new_lines[i]))
        i = i + 1

    #prints the arrays for testing
    #print(old_simhash)
    #print("\n ---- \n")
    #print(new_simhash)
    
    return [old_simhash, new_simhash]

