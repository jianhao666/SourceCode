Jianao Wei, Yaping Lin, Xin Yao and Ji Zhang, ¡°Differential Privacy-based Genetic Matching in Personalized Medicine¡±

To securely perform personzlized midicine, this paper proposed a differential privacy-based genetic matching (DPGM) scheme to achieve effective genetic matching and protect
genetic privacy inclusing pubilshed data privacy and query privacy.


This source code filie contains five subfiles, such as data publish, query, gene matching, ANOVA 1 test and sequence similarity.


In the data publish subfile:
     loadfile: read the dataset.
     EIGNSTART: the original dataset is processing. 
     DP_process and EIGN: the original dataset is added noise based on different DP methods.
     SNPs_publishe: significantly noisy SNPs publication.
     GetSNPsequence: construct the noisy published sequence from the significantly noisy SNPs 

In the query subfile:
     Hamdistance: the Hamming distance is used to construct a similar sequence dataset. The Hamming error between constrcted seqeunce and real query sequence is smaller than 2.
     Markov model generation: use DP to generate noisy (N-1)-order and N-order MArkov models.
     build noisy sequence: use a quadtree to build noisy query sequence.

In the genetic matching subfile:
    genetic_matching: use the dynamic planning method to calculate the longest common subsequence.

In the ANOVA 1 test subfile:
    ANOVA1 test: use the ANOVA 1 test to calculate the F-values of different methods.

In the sequence similarity subfile:
    global alignment: two sequences with different lengths are translated into the sequences with the same length.
    Mutual Information: calculate the normalized mutual information of sequence-pairs.
    Pearson Information: calculate the Pearson information of sequence-pairs.
    TOPSIS: use an information entropy-based TOPSIS to identify the top five highly correlated sequence-pairs. 

 

    