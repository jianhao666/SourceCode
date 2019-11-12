#-*-coding: utf-8 -*-
##calculate the EIGN matrix
import pysnptools;
import numpy as np;
import scipy as sp;
import math
from numpy.random import laplace as Lap;
from scipy.stats import chi2;




##EIGN_Mat class represents the EIGN matrix required for our method

class EIGN_Mat:
        ##Initialize
        ##
        def __init__(self,BED,par,binSize=1):
                self.BED=BED;
                self.binSize=binSize;

        
        ##
        ##Returns the product of EIGN with y
        ##
        def prod(self,y):
                raise NotImplementedError("calculate the product!");
        
        ##
        ##Returns a list the \chi^2 stat for all SNPs
        ##
        def score(self,y):
                raise NotImplementedError("calculate the Score!");
        
        ##Returns [b_i(c) i a SNP]
        ##
        def neighDist(self,y,cepsilon,):
                raise NotImplementedError("calculate the neighbor distance!");

        def DPE(self,y,cepsilon,):
                raise NotImplementedError("calculate the Noisy EIGENSTRAT Satistic!");
        ##Given mret, returns the associated sensitivity value
        ##
        def sens(self,mret):
                raise NotImplementedError("calculate the query sensitivity!");


        ##Returns a list of max_j|mu_{ij}| for all i
        def maxEIGN(self):
                raise NotImplementedError("calculate the product!");


        ##
        ##returns a normalization constant and sensitivity
        ##
        def normY(self,y):
                return [1.0,-1.0]


        ##
        ##Get the names of SNPs at specified indices
        ##
        def snp_Names(self,ind):
                return [self.BED.sid[i] for i in ind];


        ##
        ##Gets indices of SNPs with specified names
        ##
        def snp_index(self,snps):
                return self.BED.sid_to_index(snps);


##
##An extension of EIGN_Mat that assumes that MU and X can fit in memory
##
class EIGN_Mem(EIGN_Mat):       
        ##
        ##Initialize, where BED is an EIGN used if already calculated EIGN
        ##
        def __init__(self,BED,par,binSize=1):
                self.BED=BED
                self.X=BED.read().standardize().val  #normalized genotype data
                self.sensit=-1.0;       
                self.EIGNn=[];
                self.EIGNp=[];
                self.y=[];
                self.calcEIGN(par);
                

        ##Used to calculate the actual array EIGN
        ##
        def calcEIGN(self,par):
                self.EIGN=[];


        ##Returns the product of MU with y
        ##where y is a 
        ##
        def prod(self,y):
                return np.dot(self.EIGN,y);     # calculate the product of the matrixs       
        

        def DPE(self,y,c,epsilon,reuse=False):
                bnd=c;
                m=len(self.EIGN); # calculate the number of SNPs
                n=len(self.EIGN[0]); # calculate the number of data owners
                [y1,nm,sen]=self.normY(y);
                print 'nm=%s'% n
                print 'm=%s' % m
                sc2=np.dot(self.EIGN,y1); # calculate the product of the matrixs 
                sc2=[float(s) for s in sc2]
                sc2 = [s for s in sc2 if not math.isnan(s)]
                J=[j for j in range(0,len(sc2))];
                mxEIGN=self.maxEIGN();
                mxEIGN= [s for s in maxEIGN if not math.isnan(s)]
                
                if epsilon<0:
                        bot=nm**2;
                        sc2=[(n-self.k-1)*(sc2[i]**2)/bot for i in range(0,len(sc2))];
                else:
                        
                        sc2=[sc2[j]+Lap(0.0,2*maxEIGN[j]/epsilon) for j in J];   # genetopic data is added laplace nose
                        bot=nm+Lap(0.0,2/epsilon);                               #  phenotypic data is added laplace noise
                        bot=bot**2;
                        sc2=[(n-self.k-1)*(sc2[i]**2)/bot for i in range(0,len(sc2))]; 
                sc=np.abs(sc2);
                #print sc
                I=[i for i in range(0,len(sc)) if chi2(sc[i], n-K-1) < bnd ];  # select the noisy significant SNPs whose P-value < bnd
                I=set(I)
                #sc3 = []
                
                length = len(I)
                print length
                
                return I; # return the locations of noisy significant SNPs 

        def neighDist(self,y,mret,reuse=False):
                bnd=mret;
                m=len(self.EIGN);
                n=len(self.EIGN[0]);
                sc2=np.dot(self.EIGN,y);  # calculate the product of the matrixs    
                sc=np.abs(sc2);
                if reuse and len(self.EIGNn)>0:
                        EIGNn=self.EIGNn;
                        EIGNp=self.EIGNp;
                else:
                        EIGNz=self.EIGN*(1-2*np.asarray(y));
                        EIGNp=np.maximum(EIGNz,0);
                        EIGNn=np.minimum(EIGNz,0);
                        EIGNp=np.sort(-EIGNp,axis=1);
                        EIGNn=np.sort(EIGNn,axis=1);
                        EIGNp=-np.cumsum(EIGNp,axis=1);
                        EIGNn=np.cumsum(EIGNn,axis=1);
                        if reuse:
                                self.EIGNn=EIGNn;
                                self.EIGNp=EIGNp;
                cntp=[np.searchsorted(EIGNp[i],bnd-sc2[i]) for i in range(0,m)];
                cntn=[np.searchsorted(-EIGNn[i],bnd+sc2[i]) for i in range(0,m)];
                neigh=-np.minimum(cntp,cntn);
                neigh=[i for i in neigh];
                I=[i for i in range(0,m) if chi2(sc[i], n-K-1) < bnd];  
                for i in I:
                        mu=[]
                        if sc2[i]>bnd:
                                mu=EIGNn[i];
                                j=np.searchsorted(-mu,-bnd+sc2[i]);
                                neigh[i]=j+1;
                        if sc2[i]<-bnd:
                                mu=EIGNp[i];
                                j=np.searchsorted(mu,-bnd-sc2[i]);
                                neigh[i]=j+1
                return neigh;



        ##
        ##Given mret, returns the associated sensitivity value
        ##
        def sens(self,mret):

                EIGN2=np.absolute((self.EIGN).T)                                
                EIGN2=np.sort(-EIGN2)[:,:mret];
                sens=min(np.sum(EIGN2,axis=1));
                sens=-sens;
                self.sensit=sens;
                print sens;
                return sens;
        

        ##Returns a list of max_j|eign_{ij}| for all i
        ##
        def maxEIGN(self):
                return np.max(np.absolute(self.EIGN),axis=1)



