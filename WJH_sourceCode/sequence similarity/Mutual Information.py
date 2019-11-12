import math
import numpy as np
from sklearn import metrics

def string_digital_conversion(seq):  #The DNA sequence is conversted into a numerical sequence
    Seq_DNA=np.zeros(len(seq))
    for k in range (0, len(seq)-1):
        if seq[k]=='A':
            Seq_DNA[k]=2
        elif seq[k]=='C':
            Seq_DNA[k]=1
        elif seq[k]=='G':
            Seq_DNA[k]=3
        elif seq[k]=='T':
            Seq_DNA[k]=0
        elif seq[k]=='-':
            Seq_DNA[k]=-1
    return Seq_DNA

def NoMI(Seqm,Seqn):
    #the number of sample points
    total = len(Seqm)
    Seqm_ids = set(Seqm)
    Seqn_ids = set(Seqn)
    # calculate the mutual information between sequence n and sequence m, denoted by MImn
    MImn = 0
    eps = 1.4e-45
    for idSeqm in Seqm_ids:
        for idSeqn in Seqn_ids:
            idSeqm_Occur = np.where(Seqm==idSeqm)
            idSeqn_Occur = np.where(Seqn==idSeqn)
            idSeqmn_Occur = np.intersect1d(idSeqm_Occur,idSeqn_Occur)
            pm = 1.0*len(idSeqm_Occur[0])/total #
            pn = 1.0*len(idSeqn_Occur[0])/total
            pmn = 1.0*len(idSeqmn_Occur)/total
            MImn = MImn + pmn*math.log(pmn/(pm*pn)+eps,2)
    # calculate the normalized mutual information between n and m, denoted by NoMImn
    Hm = 0
    for idSeqm in Seqm_ids:
        idSeqm_OccurCount = 1.0*len(np.where(Seqm==idSeqm)[0])
        Hm = Hm - (idSeqm_OccurCount/total)*math.log(idSeqm_OccurCount/total+eps,2)
    Hn = 0
    for idSeqn in Seqn_ids:
        idSeqn_OccurCount = 1.0*len(np.where(Seqn==idSeqn)[0])
        Hn = Hn - (idSeqn_OccurCount/total)*math.log(idSeqn_OccurCount/total+eps,2)
    NoMImn = MImn/np.sqrt(Hm*Hn+eps)
    return NoMImn

def getline(thefilepath,line_num):
    if line_num < 1 :return '' # if the length of lines in a file, return null
    for currline,line in enumerate(open(thefilepath,'rU')): 
        if currline == line_num -1 :return line      #read each line in a file
    return ''

