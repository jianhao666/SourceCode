import math
import numpy as np


def string_digital_conversion(seq):   #The DNA sequence is conversted into a numerical sequence
    Seq_DNA=np.zeros(len(seq))
    for k in range (0, len(seq)-1):
        if seq[k]=='A':
            Seq_DNA[k]=2   #if Seq_DNA[k]='A', we set Seq_DNA[k] to be 2
        elif seq[k]=='C':
            Seq_DNA[k]=1   #if Seq_DNA[k]='C', we set Seq_DNA[k] to be 1
        elif seq[k]=='G':
            Seq_DNA[k]=3   #if Seq_DNA[k]='G', we set Seq_DNA[k] to be 3
        elif seq[k]=='T':
            Seq_DNA[k]=0   #if Seq_DNA[k]='T', we set Seq_DNA[k] to be 0
        elif seq[k]=='-':
            Seq_DNA[k]=-1   #if Seq_DNA[k]='-', we set Seq_DNA[k] to be -1
    return Seq_DNA


def multipl(a,b):
    sumofab=0.0
    for i in range(len(a)-1):
        temp=a[i]*b[i]
        sumofab+=temp
    return sumofab
 
def Pearson_corrcoef(x,y):
    n=len(x)
    #calculate the sum of x and y
    sum1=sum(x)
    sum2=sum(y)
    #calculate the sum of product between x and y
    sumofxy=multipl(x,y)
    #compute the sum of square between x and y
    sumofx2 = sum([pow(i,2) for i in x])
    sumofy2 = sum([pow(j,2) for j in y])
    num=sumofxy-(float(sum1)*float(sum2)/n)
    #compute the Pearson's correlation coefficient
    den=math.sqrt((sumofx2-float(sum1**2)/n)*(sumofy2-float(sum2**2)/n))
    return abs(num/den)

def getline(thefilepath,line_num):
    if line_num < 1 :return '' # if the length of lines in a file, return null
    for currline,line in enumerate(open(thefilepath,'rU')): 
        if currline == line_num -1 :return line      #read each line in a file
    return ''

