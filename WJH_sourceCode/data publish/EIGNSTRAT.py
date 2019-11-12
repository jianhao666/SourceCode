###########
##Implements the EIGN matrix class

from EIGN import EIGN_Mat;
from EIGN import EIGN_Mem;
from sklearn.decomposition import TruncatedSVD as svdt; 
import math;
import numpy as np;
from numpy.linalg import eigh;

class EIGNSTRAT(EIGN_Mem):
   
    ##Calulates an exact PCA
    ##
    def exactSVD(self):
        Mat=np.dot(self.X,(self.X).T);
        [w,v]=eigh(Mat);
        return np.asarray(v[:,:self.k])
        


    ##
    ##Implementation of calc EIGN matrix for DPE
    ##

    def calcEIGN(self,k,exact=False):
        self.k=k

        if not exact:
            uk_temp=svdt(n_components=k);
            u=np.asarray(uk_temp.fit_transform(self.X)); 
        else:
            u=self.exactSVD();
        bot=np.sum(u**2,axis=0);
        bot=[math.sqrt(i) for i in bot]
        self.Uk=u/bot;
    
        EIGN_temp=self.X-np.dot(self.Uk,np.dot((self.Uk).T,self.X));
    
        self.EIGN=EIGN_temp.T;
    
        sd=np.sum(self.EIGN**2,axis=1);
        sd=[math.sqrt(s) for s in sd];
        self.EIGN=self.EIGN/np.asarray(sd)[:,np.newaxis];
    
        

    ##
    ##Returns list of scores
    ##
    def score(self,y):
        EIGNy=prod(y);
        bot=1.0;
        return [my**2/bot**2 for my in EIGNy];

    ##
    ##mean centering and projecting out U_j to normalizes U,
    ##
    def normY(self,y):
        n=len(y);
        mn=sum(y)/float(len(y));
        y_st=[i-mn for i in y];
        y_st=np.asarray(y_st)-np.dot(self.Uk,np.dot(self.Uk.T,y_st));
        return [y_st,math.sqrt(sum([i**2 for i in y_st])),math.sqrt(float(n-1)/float(n))]
