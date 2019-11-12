# coding=utf-8
import sys   
#sys.setrecursionlimit(30000)
import time
import pdb
class LCS():
    def input(self, x, y):
    #read the matched two sequences
        if type(x) != str or type(y) != str:
            print 'input error'
            return None
        self.x = x
        self.y = y

    def Compute_LCS(self):
        xlength = len(self.x)
        ylength = len(self.y)
        self.direction_list = [None] * xlength #initialize a two-dimensional table
        for i in xrange(xlength):
            self.direction_list[i] = [None] * ylength
        self.lcslength_list = [None] * (xlength + 1)
        #store a list of the longest commen subsequence
        for j in xrange(xlength + 1):
            self.lcslength_list[j] = [None] * (ylength + 1)

        for i in xrange(0, xlength + 1):
            self.lcslength_list[i][0] = 0
        for j in xrange(0, ylength + 1):
            self.lcslength_list[0][j] = 0

        #calculate the backtracking direction
        for i in xrange(1, xlength + 1):
            for j in xrange(1, ylength + 1):
                if self.x[i - 1] == self.y[j - 1]:
                    self.lcslength_list[i][j] = self.lcslength_list[i - 1][j - 1] + 1
                    self.direction_list[i - 1][j - 1] = 0  # upper left direction
                elif self.lcslength_list[i - 1][j] > self.lcslength_list[i][j - 1]:
                    self.lcslength_list[i][j] = self.lcslength_list[i - 1][j]
                    self.direction_list[i - 1][j - 1] = 1  # up direction
                elif self.lcslength_list[i - 1][j] < self.lcslength_list[i][j - 1]:
                    self.lcslength_list[i][j] = self.lcslength_list[i][j - 1]
                    self.direction_list[i - 1][j - 1] = -1  # left direction
                else:
                    self.lcslength_list[i][j] = self.lcslength_list[i - 1][j]
                    self.direction_list[i - 1][j - 1] = 2  # left or up direction
        self.lcslength = self.lcslength_list[-1][-1]
        return self.direction_list, self.lcslength_list

    def printLCS(self, curlen, i, j, s):
        if i == 0 or j == 0:
            return None
        I=[]
        if self.direction_list[i - 1][j - 1] == 0:
            if curlen == self.lcslength:
                s += self.x[i - 1]
                for i in range(len(s)-1,-1,-1):
                    print s[i]
                    for k in range(0,len(self.y)):
                        if self.y[k]==s[i]:
                            I.append(k)
                            break
                #print '\n'
                #print s
                I=set(I)
                print I 
            elif curlen < self.lcslength:
                s += self.x[i-1]
                self.printLCS(curlen + 1, i - 1, j - 1, s)
        elif self.direction_list[i - 1][j - 1] == 1:
            self.printLCS(curlen,i - 1, j,s)
        elif self.direction_list[i - 1][j - 1] == -1:
            self.printLCS(curlen,i, j - 1,s)
        else:
            self.printLCS(curlen,i - 1, j,s)
            self.printLCS(curlen,i, j - 1,s)
        
    def returnLCS(self):
        #start backtracking
        self.printLCS(1,len(self.x), len(self.y),'')



def calcu_data_utility (rea_matc_seq, noisy_match_seq):
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
