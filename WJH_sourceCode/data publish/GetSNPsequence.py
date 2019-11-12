#-*- coding: utf-8 -*-

import csv
"""
	construct noisy published sequence from noisy significant SNPs
"""
## srcfile: store SNPs (srcfile.bim)， snpfile: store noisy SNPs
def get_snp_allele(srcfile, snpfile):


	try:
		sfile = open(str(srcfile), 'rb')
		# construct a data dictionary
		srcdict = {}
		posdict = {}
		if sfile:
			spamreader = csv.reader(sfile, delimiter=',') # The file separator is ,
			for line in spamreader:
				srcdict[line[1]] = line[4]	## allele: key is the location of the SNP, and value is the allele
				posdict[line[1]] = line[3]	## physical location: key is the location of the SNP, and value is the physical location
	except IOError as e:
		print(e)
	else:
		if sfile:
			sfile.close()
	
	ret = []	# store the allele returned by the corresponding location
	chromosome = [None] * 250000000	# initialize a list of length len
	try:
		snfile = open(snpfile, 'rb')
		if snfile:
			for line in snfile.readlines():
				line = line.strip()			# remove the space character at the beginiing and end of each line
				if srcdict.has_key(line):	# determine whether the key is in the list
					#ret.append(srcdict.get(line)) # if yes, return the corresponding value
					#chromosome.insert(int(posdict.get(line))-1, srcdict.get(line))
					chromosome[int(posdict.get(line))-1] = srcdict.get(line)
	except IOError as e:
		print(e)
	else:
		if snfile:		
			snfile.close()
	#print('len(ret) = %s' % len(ret))
	print('len(chromosome) = %s' % len(chromosome))
	#print(chromosome)
	print(ret)
	return ret
