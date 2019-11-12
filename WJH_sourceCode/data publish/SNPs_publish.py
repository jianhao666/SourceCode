####################
##return the noisy significant SNPs and calculate the data utility

import sys;
import loadFile as ld;
from EIGNSTRAT import *;
from DP_process import PickTop as pt;

##
def inter(a,b):
        return len([i for i in a if i in b])/float(len(a));


##
##For making pics!
##
def NoisySig(mret,eps,filename,savename=""):
        if len(savename)==0:
                savename="Output/res_top_"+str(eps)+"_"+str(mret)+".txt"
        epsilons=[eps*i for i in range(1,11)];
        print "load Data"
        [y,BED]=ld.getData(filename);
        print "calc EIGN!"
        EIGN=EIGN_STRAT(BED,2);
        sc=EIGN.prod(y);
        sc=[abs(s) for s in sc];
        sc=sorted(sc,reverse=True);
        print "get True!";
        truSNPs=pt(y,EIGN,mret,-1,algor="noise");
        our=[0.0 for i in range(1,11)];
        score=[0.0 for i in range(1,11)];
        noise=[0.0 for i in range(1,11)];
        neighbor=[0.0 for i in range(1,11)];
        reps=20;
        for i in range(0,10):
                e=epsilons[i];
                print e;
                for j in range(0,reps):
                        print j;
                        nosySNPs=pt(y,EIGN,mret,e,algor="DPE",reuse=True);
                        our[i]=our[i]+inter(truSNPs,noisySNPs)/float(reps);
                        
                        noisySNPs=pt(y,MU,mret,e,algor="score");
                        score[i]=score[i]+inter(truSNPs,noisySNPs)/float(reps);
                        
                        noisySNPs=pt(y,MU,mret,e,algor="noise");
                        noise[i]=noise[i]+inter(truSNPs,noisySNPs)/float(reps);
                        
                        noisySNPs=pt(y,MU,mret,e,algor="neighbor");
                        neighbor=neighbor[i]+inter(truSNPs,noisySNPs)/float(reps);
                


