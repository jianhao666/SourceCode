# -*- coding: UTF-8 -*-
import numpy as np
def goal_bidui(str1, str2):
    len_str1 = len(str1) + 1
    print len_str1
    len_str2 = len(str2) + 1
    print len_str2
    newstr1 = newstr2 = ""
    matrix = np.zeros([len_str1, len_str2]) #initialize the matrix
    matrix[0] = np.arange(len_str2)
    matrix[:, 0] = np.arange(len_str1)
    print matrix[:, 0]
    for i in range(1, len_str1):
        for j in range(1, len_str2):
            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1,
                               matrix[i - 1][j - 1] + 2*(int)(str1[i - 1] != str2[j - 1])) # set the matric[i][j] to the minimum value
    i = len_str1-1
    j = len_str2-1
    print i, j
    while i != 0 or j != 0:
        if (matrix[i][j] == matrix[i - 1][j - 1] and str1[i - 1] == str2[j - 1]) or matrix[i][j] == matrix[i - 1][j - 1] + 2:
            newstr1 = str1[i-1].__add__(newstr1)   #str1[i-1] is added to the newstr1
            newstr2 = str2[j - 1].__add__(newstr2) # #str2[j-1] is added to the newstr2
            i = i-1
            j = j-1
            print i, j
        elif matrix[i][j] == matrix[i - 1][j] + 1:
            newstr1 = str1[i-1].__add__(newstr1) #str1[i-1] is added to the newstr1
            newstr2 = "-".__add__(newstr2) # add a '-' to the newstr2
            i = i-1
            print "get flase!";
        elif matrix[i][j] == matrix[i][j - 1] + 1:
            newstr1 = "-".__add__(newstr1) # add a '-' to the newstr1
            newstr2 = str2[j - 1].__add__(newstr2)  #str2[j-1] is added to the newstr2
            j = j-1
            print "get True!";
    print(matrix)
    print(newstr1)
    print(newstr2)
    print len(newstr1)
    print len(newstr2)
    


def getline(thefilepath,line_num):
    if line_num < 1 :return '' # if the length of lines in a file, return null
    for currline,line in enumerate(open(thefilepath,'rU')): 
        if currline == line_num -1 :return line      #read each line in a file
    return ''






    
