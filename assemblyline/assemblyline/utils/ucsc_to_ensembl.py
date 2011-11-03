'''
Created on Nov 1, 2011

@author: mkiyer
'''
import sys

chrom_names = [["chr1", "1"],
               ["chr2", "2"],
               ["chr3", "3"],
               ["chr4", "4"],
               ["chr5", "5"],
               ["chr6", "6"],
               ["chr7", "7"],
               ["chr8", "8"],
               ["chr9", "9"],
               ["chr10", "10"],
               ["chr11", "11"],
               ["chr12", "12"],
               ["chr13", "13"],
               ["chr14", "14"],
               ["chr15", "15"],
               ["chr16", "16"],
               ["chr17", "17"],
               ["chr18", "18"],
               ["chr19", "19"],
               ["chr20", "20"],
               ["chr21", "21"],
               ["chr22", "22"],
               ["chrX", "X"],
               ["chrY", "Y"],
               ["chrM", "MT"]]

ucsc_to_ensembl_dict = dict(chrom_names)

for line in open(sys.argv[1]):
    fields = line.strip().split('\t')
    if fields[0] not in ucsc_to_ensembl_dict:
        print >>sys.stderr, "skipped line %s" % line
        continue
    fields[0] = ucsc_to_ensembl_dict[fields[0]]
    print '\t'.join(fields)
