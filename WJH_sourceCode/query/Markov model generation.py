# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import string
import re
from numpy.random import laplace as Lap;



def Markov_N_1(a, b, eps):
    epsilons=[eps*i for i in range(1,11)];
    line1=str(a.readline());
    line2=str(b.readline());
    le=len(line1.strip());
    m=[0.0 for i in range(0,20)];
    reps=20;
    for j in range(0,reps):
        line2=str(b.readline());
        while line2:
            sm=0;
            c1=line2.strip();
            line1=str(a.readline());
            while line1:
                a1=line1.strip();
                a1=a1+'0'
                idx=re.compile("(?=" + c1 + ")")
                idx=len(idx.findall(a1))
                sm=sm+idx;
                line1=str(a.readline());
                line1=line1.strip();
            
        line2=str(b.readline());
        line2=line2.strip();
        d_N_1=sm;
        d_N_1=d+Lap(float(2*(le-N+2))/epsilons)
        return d_N_1



def Markov_N(a, b, eps):
    epsilons=[eps*i for i in range(1,11)];
    line1=str(a.readline());
    line2=str(b.readline());
    le=len(line1.strip());
    m=[0.0 for i in range(0,20)];
    reps=20;
    for j in range(0,reps):
        line2=str(b.readline());
        while line2:
            sm=0;
            c1=line2.strip();
            line1=str(a.readline());
            while line1:
                a1=line1.strip();
                a1=a1+'0'
                idx=re.compile("(?=" + c1 + ")")
                idx=len(idx.findall(a1))
                sm=sm+idx;
                line1=str(a.readline());
                line1=line1.strip();
            
        line2=str(b.readline());
        line2=line2.strip();
        d_N=sm;
        d_N=d+Lap(float(2*(le-N+1))/epsilons)
        return d_N
 
         


        

