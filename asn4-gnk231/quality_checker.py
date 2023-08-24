#!/usr/bin/env python

#Rubana Syeda
#gnk231
#11317615
#BINF 351
#Jin Lingling


import sys

"""
Function returns true if the seq consists of only actg or ACTG
Returns False otherwise
@param seq is the sequence to evaluate
"""
def seq_isValid(seq):
    ref = "acgtACGT"
    for s in seq:
        if s not in ref:
            return False

    return True

"""
Funtion evaluates a quality score and returns its average if it is a valid score
; QUality score is valid if the characters' ascii value minus 33 is >= 0 and <=40
@returns a tuple (False,0) if score is not valid; (True, *avg*) if score is valid
@param word the score to evaluate
"""
def quality_isValid_avg(word):
    count=0
    avg=0
    for w in word:
        if (ord(w)-33) < 0 or (ord(w)-33) > 40:
            return False,0
        count+= 1
        avg+= ord(w)
    return True,avg/count



if __name__ == "__main__":
    
    inputfile = sys.argv[1]
    threshold = int(sys.argv[2])
    
    # terminate program if file cannot be opened
    try:
        infile = open(inputfile,"r")
    except:
        print("File provided in command line arg %s cannot be opened" % inputfile)
        sys.exit()

    # evaluating the sequence
    infile = infile.readlines()
    if(not seq_isValid(infile[1].rstrip())):
        print("Sequence in %s is not valid"% inputfile)
        sys.exit()

    # evaluating score
    q_valid,avg = quality_isValid_avg(infile[3].rstrip())
    if(not q_valid):
        print("Quality score in %s is not valid"% inputfile)
        sys.exit()

    if(avg >= threshold):
        print("%s meets the specified quality threshold" % inputfile)
    else:
        print("%s does not meet the specified quality threshold" % inputfile)











































