# -*- coding: utf-8 -*-

#'''
#   buld query sequence
#'''
import numpy as np
import linecache
import string
import re
import os


# build noisy query sequences based on noisy Markov models
def buldNoisyQuey(Seq, Markov_N_1, MArkov_N, n):
    seq_leveltwo = Markov_N_1[0] # obtain the sequences of (N-1)-order Markov models
    seq_levelthree = MArkov_N[0] # obtain the sequences of N-order Markov models

    fre_leveltwo= Markov_N_1[1];   # obtain the noisy counts of (N-1)-order Markov models
    fre_levelthree= Markov_N[1];   # obtain the noisy counts of N-order Markov models

    result = [] # store all sequences
    proba = [] # store the noisy counts of all sequences
    pro = []  # frequencies of sequences
    seq = 'AAA'
    index_j = seq_levelthree.index(seq)
    value_j = pro_levelthree[index_j]
    pro = value_j

    i = N
    while (i < n):
        seq_i = linecache.getline(seq_leveltwo, i+1).strip()    # read the data of i-th row 
        pro = linecache.getline(seq_levelthree,i+1).strip()    # read the data of i-th row
        print pro
        print('seq:' + seq_i)

        P=[pro1, pro2, pro3, pro4];
        a=max(P);
        k = [i for i in range (0, len(P)) if a==P[i]]   
        seq_i=P[k]
        
        if len(seq_i) < n:
            seq_1= seq_i + 'A'
            seq_tmp1 = seq[len(seq)-3:len(seq)]
            seq_tmp2 = seq[len(seq)-3:len(seq)-1]
            #print('seq_tmp:' + seq_tmp)
            value_i1 = seq_levelthree.index(seq_tmp1);
            value_i2 = seq_leveltwo.index(seq_tmp2);
            pro1 = float(pro)*float(pro_levelthree[value_i1])/float(pro_leveltwo[value_i2]);
 

        if len(seq_i) < n:
            seq2 = seq_i + 'G'
            seq2_tmp1 = seq2[len(seq2)-3:len(seq2)]
            seq2_tmp2=seq2[len(seq2)-3:len(seq2)-1]
            #print('seq_tmp:' + seq_tmp)
            value_i1 = seq2_levelthree.index(seq2_tmp1);
            value_i2 = seq2_leveltwo.index(seq2_tmp2);

            pro2 = float(pro) * float(pro_levelthree[value_i1])/float(pro_leveltwo[value_i2]);



        if len(seq_i) < n:
            seq3= seq_i + 'C'
            seq3_tmp1 = seq3[len(seq3)-3:len(seq3)]
            seq3_tmp2=seq3[len(seq3)-3:len(seq3)-1]
            #print('seq_tmp:' + seq_tmp)
            value_i1 = seq3_levelthree.index(seq3_tmp1);
            value_i2 = seq3_leveltwo.index(seq3_tmp2);

            pro3 = float(pro) * float(pro_levelthree[value_i1])/float(pro_leveltwo[value_i2]);
            

        if len(seq_i) < n:
            seq4 = seq_i + 'T'
            seq4_tmp1 = seq4[len(seq)-3:len(seq4)]
            seq4_tmp2=seq4[len(seq)-3:len(seq4)-1]
            #print('seq_tmp:' + seq_tmp)
            value_i1 = seq4_levelthree.index(seq4_tmp1);
            value_i2 = seq4_leveltwo.index(seq4_tmp2);

            pro4 = float(pro) * float(pro_levelthree[value_i1])/float(pro_leveltwo[value_i2]);
   
        # linecache.checkcache('result.txt')
        linecache.clearcache()
        i = i + 1
    
    return seq



def data_utility (rea_query_seq, noisy_query_seq):
    S1=[s for s in a];
    print S1

    #S2=[s.strip() for s in b];
    S2=[s for s in b];
    print S2

    sm=0;
    print len(S1)
    for i in range(0,len(S1)):
        if S1[i]==S2[i]:
            sm=sm+1;
    c=sm/float(len(S1));
    print c

