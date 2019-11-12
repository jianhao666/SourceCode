# -*- coding: utf-8 -*-
######################
##Loads Plink file
import numpy as np;
from pysnptools.snpreader import Bed;
from pysnptools.snpreader import Pheno;
from os.path import isfile;

##
##gets phenotypic data y, 
##
def getData(filename):
	mph=3;
	sFil=Bed(filename, count_A1=False); # Bed object
	yFil=Pheno(filename+".fam");
	
	y=yFil.read().val[:,mph];
	y=[i-1 for i in y] # the last column of .fam file is the disease states of data owners
	return [y,sFil];
	


