# -*- coding: utf-8 -*-
import numpy as np
import xlrd
import pandas as pd

#read the data from the excel file
def read(file):
    wb = xlrd.open_workbook(filename=file)#open the file
    sheet = wb.sheet_by_index(0) #obtain the table data from the index
    rows = sheet.nrows # calculate the number of rows
    all_content = []        #store the readed data
    for j in range(2, 4):       #select the 3-th column data (matual information) and 4-th column (pearson correlation cofficient).
        temp = []
        for i in range(1,rows):
            cell = sheet.cell_value(i, j)   #obtain the data
            temp.append(cell)           
        all_content.append(temp)    #add the results into the array according to the column
        temp = []
    return np.array(all_content)
    #print np.array(all_content)

#Calculate the very small measure
def dataDirection_1(datas):         
        return np.max(datas)-datas     

#calculate the intermediate measure
def dataDirection_2(datas, X_max, X_min):
    answer_list = []
    for i in datas:
        if (X_Min<= i <= (X_max+X_min)/2):
            answer_list.append(2*(i-X_min)/(X_max - X_min))
        elif ((X_max+X_min)/2<= i <= X_max):
            answer_list.append(2*(X_man-i)/(X_max - X_min))
        elif i<=X_min or i>=X_max:
            return 0
    return np.array(answer_list)
    
#calculate the interval type measure
def dataDirection_3(datas, X_min, X_max):
    M_min = X_min - np.min(datas)
    M_max = np.max(datas) - X_max
    answer_list = []
    for i in datas:
        if(i < X_min):
            answer_list.append(1 - (X_min-i) /M_min)      
        elif( X_min <= i <= X_max):
            answer_list.append(1)
        else:
            answer_list.append(1 - (i - X_max)/M_max)
    return np.array(answer_list)   
 
#Normalize the forward matrix
def temp2(datas):
    K = np.power(np.sum(pow(datas,2),axis =1),0.5)
    for i in range(0,K.size):
        for j in range(0,datas[i].size):
            datas[i,j] = datas[i,j] / K[i]      
    #print datas
    return datas
     

#calculate the weights of measures by using the information entropy 
def EntropyWeight(answer2):
    
    #anwser2 = np.array(anwser2)
    #anormalized processing
    a=[]
    wei=[]
    for k in range(0,2):        #go through each row
        Z = answer2[k,:] / answer2[k,:].sum(axis=0)
        entropy = np.sum(-Z * np.log(Z) / np.log(len(answer2[k,:])), axis=0)
        a.append(1-entropy)
    b=a[0]+a[1]
    wei=a/b
    return wei



#calculate the scores and normalize them
def TOPSIS(answer2, weight=None):
    list_max = np.array([np.max(answer2[0,:]),np.max(answer2[1,:])])  #calculate the maximum value of each column
    list_min = np.array([np.min(answer2[0,:]),np.min(answer2[1,:])])  #calculate the minimum value of each column
    max_list = []       #store the maximum distance between i-th object and maximum value
    min_list = []       #store the minimum value between i-th object and minimum value
    answer_list=[]      #strore the un-normalized scores of objects
    
    weight = EntropyWeight(answer2) if weight is None else np.array(weight)
    #print weight
    
    for k in range(0,np.size(answer2,axis = 1)):        #traversing each column of data
        max_sum = 0
        min_sum = 0
        for q in range(0,2):         #have two measures
            #print np.power(answer2[q,k]-list_max[q],2)
            max_sum += np.power(answer2[q,k]-list_max[q],2)  #calculate the Di+ by column
            min_sum += np.power(answer2[q,k]-list_min[q],2)  #*weight[k]  #calculate the Di- by column
        max_sum=max_sum*weight[0]
        min_sum=min_sum*weight[1]
        max_list.append(pow(max_sum,0.5))
        min_list.append(pow(min_sum,0.5))
        answer_list.append(min_list[k]/ (min_list[k] + max_list[k]))    #according tothe fomula: Si = (Di-) / ((Di+) +(Di-))
        max_sum = 0
        min_sum = 0
    answer = np.array(answer_list)      #normalize the socres
    #answer = answer / np.sum(answer)
    #print answer
    rank=sorted(answer, reverse=True)
    print answer
    A=rank[0:len(rank)]
    I = []
    for i in range(0,len(A)):
        for k in range(0,len(answer)):
            if answer[k] == A[i]:
                I.append(k)
    print rank[0:len(rank)]
    print I[0:len(I)]
    rank=[I, rank]
    rank=list(map(list, zip(*rank)))
    return rank


