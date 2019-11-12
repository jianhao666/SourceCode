# -*- encoding: utf-8 -*-
import re
import sys
import numpy as np
from scipy.stats import f
import scipy.stats as stats
import matplotlib.pyplot as plt
import pandas as pd

def ANOVA_1(data):
    """
    """
    alpha = 0.05
    group_num = len(data)     # calculate the total number of values in two groups (N)
    ingroup_num = len(data[0])   # calculate the toal number of values in each group (n1, n2)
    ingroup_sum=[sum(data[0]), sum(data[1])] #calculate the sum of values in each group (T1, T2)
    ingroup_mean=[ingroup_sum[0]/ingroup_num, ingroup_sum[1]/ingroup_num] # calculate the mean value of each group
    
    
    group_sum=sum(ingroup_sum)  #calculate the sum of all values in two groups (T)
    group_mean=group_sum/(group_num*ingroup_num)  #calculate the mean value of groups
    


    I=group_sum**2 / (group_num*ingroup_num)    
    II = 0
    for i in range(group_num):
        for j in range(ingroup_num):
            II += (data[i][j]) ** 2

    III=0
    
    for i in range(group_num):
        III+=(ingroup_sum[i]**2)/ingroup_num

    SS_between = III-I # calculate the sum of squares between groups
    print('Between-groups sum of Squared Differences: {}'.format(SS_between))

    
    SS_within = II-III # calculate the sum of squares within groups
    print('Within-groups sum of Squared Differences: {}'.format(SS_within))

    Df_between =group_num-1    # calculate the degree of freedom between groups

    Df_within = 0
    for i in range(group_num):
        Df_within+=ingroup_num-1    #calculate the degree of freedom within groups
    
    
    MS_between = SS_between/Df_between  #calculate the Mean Square value of Between-groups


    print('Between-groups Mean Square Value: {}'.format(MS_between))

    
    MS_within = SS_within/Df_within   #calculate the Mean Square value of Within-groups

    print('Within-groups Mean Square Value: {}'.format(MS_within))
    
    
    F = MS_between/MS_within
    
    print('F-score: {}'.format(F))

    #check the value of F_practical

    f1, p=stats.f_oneway(data)
    

    print('double-check F_check value: {}'.format(f1))
    print('double-check P_check value: {}'.format(p))
    
    p_expected = f.ppf(alpha, Df_between, Df_within)

    F_real_score=f(Df_between, Df_within).ppf(1-alpha)
    
    print F_real_score, F, p_expected
    
    fig, ax= plt.subplots(1, 1)
    x2 = np.linspace(f.ppf(0.01, Df_between,  Df_within),f.ppf(0.99, Df_between,  Df_within), 100)
    ax.plot(x2, f.pdf(x2, Df_between,  Df_within),'r-', lw=5, alpha=0.6, label='f pdf')
    plt.axvline(x=F_real_score, lw=3, label='Critical value for alpha=0.05', color='g')
    plt.axvline(x=F, lw=3, label='F-score')
    plt.legend()
    plt.show()

    
    A=[SS_between, Df_between, MS_between, F, p, SS_within, Df_within, MS_within, SS_between+SS_within, Df_between+Df_within, alpha, F_real_score]
    return A

def print_ANOVA_1(d, maxedg = 90 ):
    '''
    print the table of ANOVA_1
    input：d - dict，contains the data that is need by ANOVA_1;
    maxedg - print output separator maximum
    '''
    title = 'The table of ANOVA_1'
    print( title.center( maxedg ))
    print( '=' *  maxedg )
    print( '{:^12s}|{:^16s}|{:^6s}|{:^16s}|{:^12s}|{:^10s}|'.format('Error Source  ','Sum of square      ','Freedom  ','Mean Square        ','F','p-value'))
    print( '-' *  maxedg )
    print( '{:8s}|{:>18,.4f} |{:>8d} |{:>18,.4f} |{:>11.6f} |{:>10.3%} |'.format( 'Between-groups',d[0],d[1],d[2],d[3],d[4]))
    print( '{:10s}|{:>18,.4f} |{:>8d} |{:>18,.4f} |'.format( 'Within-group  ',d[5],d[6],d[7]))
    print( '{:14s}|{:>18,.4f} |{:>8d} |'.format( 'Sum',d[8],d[9]))
    print( '-' *  maxedg )
    print('Remarks：When the significant level is {:.2%}, the critical value of F is {:.6f}。'.format(d[10],d[11]))

     
     
