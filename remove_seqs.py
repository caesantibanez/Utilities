#!/usr/bin/env python3
# -*- coding: utf-8 -*- 

import os
import Bio
import argparse

from Bio import SeqIO
#Function definitions
def remove_long_sequences(input_file, output_file, max_length):

  with open(input_file, "r") as f, open(output_file, "w") as out:
    for record in SeqIO.parse(f, "fasta"):
      if len(record.seq) <= max_length:
        out.write(record.format("fasta"))
      
if __name__=='__main__':
    parser = argparse.ArgumentParser(description='This script removes sequences longer than a specified length and creates a new file containing those not fulfilling the criteria')
    parser.add_argument('-i', dest = 'input_file', type = str, default= 'None',  help = 'Fasta file with wanted sequences to be removed')
    parser.add_argument('-o', dest= 'output_file', type = str, default= 'output.fasta', help ='Name of the output file (default= output.fasta')
    parser.add_argument('-s', dest= 'max_length', type = int, default= '200', help = 'The max length of the sequences you want to be removed (default=200)')
    args, unknown = parser.parse_known_args()

    remove_long_sequences(args.input_file, args.output_file, args.max_length)
