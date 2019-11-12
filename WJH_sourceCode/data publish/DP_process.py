#-*-coding: utf-8 -*-
from EIGN import EIGN_Mat;
from scipy.stats import chi2;
import numpy as np;
import scipy as sp;
from numpy.random import multinomial as mult;
import random as rand;
import math;
from numpy.random import laplace as Lap;



## select significant noisy SNPs using our DPE method
def PickSigDPE(y,EIGN,mret,epsilon,reuse=False,snpList=""):
    n=len(y); # calculate the data owners' number

    bnd=mret; #threshold
    print "Calculating the locations of noisy significant SNPs"
    
    SigSNPs=EIGN.DPE(y,bnd,epsilon,reuse=reuse); #our DPE method

    sc = [nei for nei in SigSNPs];
  
    print('len(sc) = ' + str(len(sc)))

    print('locations of noisy significant SNPs based on our DPE method: {}'.format(sc))

    return EIGN.snp_Names(sc);     #return the names of noisy significant SNPs



#Picks noisy significant SNPs using Score method
#
def PickSigScore(y,EIGN,mret,epsilon):
    n=len(y);
    sc=EIGN.prod(y);
    sc=[abs(s) for s in sc]
    m=len(sc);
    sens=EIGN.sens(mret);
    ms=max(sc);
    sc=[s-ms for s in sc];
        
    sc2=[s*epsilon/(2.0*sens) for s in sc]; #adds noise based on the Score method
    
    sc=np.abs(sc2);
    I=[i for i in range(0,len(sc)) if chi2(sc[i], n-K-1)< bnd ]; # select the noisy significant SNPs whose P-value < bnd
    I=set(I)
    index_Ret=I;

    print('locations of noisy significant SNPs based on Score method: {}'.format(index_Ret))

    return EIGN.snp_Names(index_Ret);

##
##Picks noisy significant SNPs using Laplacian method
##
def PickSigLap(y,EIGN,mret,epsilon):
    bnd=mret;
    n=len(y);
    sc=EIGN.prod(y);
    sc=[abs(s) for s in sc]
    m=len(sc);
    sens=EIGN.sens(mret);
    if epsilon<0:
        sc=sc;
    else:
        sc=[s+Lap(0,2*sens/epsilon) for s in sc];
    sc=np.abs(sc);
    I=[i for i in range(0,len(sc)) if chi2(sc[i], n-K-1) < bnd ]; # select the noisy significant SNPs whose P-value < bnd
    I=set(I)
    index_Ret=I;
    
    print('locations of noisy significant SNPs based on Laplace method: {}'.format(index_Ret))
    
    return EIGN.snp_Names(index_Ret);


##Picks noisy significant SNPs using Neighbor distance method
def PickSigNeigh(y,EIGN,mret,epsilon,reuse=False,snpList=""):
    n=len(y);
 
    ep1=.1*epsilon;
    ep2=.9*epsilon;
    bnd= mret;
    sc=EIGN.prod(y);
    sc=[abs(s) for s in sc]
                
    bnd=sum(sorted(sc,reverse=True)[1:n])/2.0;
    
    bnd=bnd+Lap(0,np.max(np.abs(EIGN.EIGN))/ep1);
    bnd=abs(bnd);
    print "Calculating Distance"
    neighDist=EIGN.neighDist(y,bnd,reuse=reuse);
    
    
    sc=[nei*ep2/(2.0*n) for nei in neighDist];
        

    SNPS=[];
    if len(snpList)>0:
        fil=open(snpList)
        lines=fil.readlines();
        fil.close();
        SNPS=[l.strip() for l in lines];
        I=EIGN.snp_index(SNPS);
        sc=[sc[i] for i in I];

    index_Ret=[i for i in range(0,len(sc)) if chi2(sc[i], n-K-1) < bnd ];  # select the noisy significant SNPs whose P-value < bnd

    print('locations of noisy significant SNPs based on Neighbor distance method: {}'.format(index_Ret))
    
    if len(snpList)>0:
        return [SNPS[i] for i in index_Ret]
    return EIGN.snp_Names(index_Ret);





##algorithms: our DPE method, Score method, Laplace method and Neighbor distance method

def PickTop(y,EIGN,mret,epsilon,algor="noise",reuse=False,snpList=""):
    if algor=="noise":
        return PickSigLap(y,EIGN,mret,epsilon);
    elif algor=="neighbor":
        return PickSigNeigh(y,EIGN,mret,epsilon,reuse=reuse,snpList=snpList);
    elif algor=="score":
        return PickSigScore(y,EIGN,mret,epsilon);
    elif algor=="DPE":
        return PickSigDPE(y,EIGN,mret,epsilon);
    else:
        raise ValueError("The algorithm "+algor+" is a wrong choice.");












