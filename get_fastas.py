#!/usr/bin/env python
# utf-8

"""
Reciprocal Best Blast
Austen T. Webber
2016_4_15
All Rights Reserved. Copyright 2016.

This script is meant to take any input database and run a RBB using any query
sequence or sequences. Output files will include fragment recruitment plots and
BLAST results of most closely related species. This program is optimized to
work with the GOS/Tara Oceans databases.
"""

import numpy as np
import argparse
import os
import sys
import pandas as pd
from Bio import SeqIO
import string
import pickle
import csv


def askingforfiles():
    parser = argparse.ArgumentParser(
        description="get name and output directory")
    parser.add_argument(
        "--F",
        required=True,
        help="BLAST results in tab delimited (outfmt=6) file",
        type=str
    )
    parser.add_argument(
        "--directory",
        required=True,
        help="Directory path for output .txtfile",
        type=str
    )
    parser.add_argument(
        "--db",
        required=True,
        help="Directory path for output .txtfile",
        type=str
    )
    return parser.parse_args()


def makedirectory(directory_file):  # Creates a new directory for output files
    newdir = os.path.join(directory_file, 'RBB')
    print(newdir)
    if not os.path.exists(newdir):
        os.makedirs(newdir)
    return newdir


def outputtabber(tab):  # This will parse the top blast hits
    df = pd.read_csv(tab, sep='\t', header=None)
    df.columns = ['query id', 'subject id', '% identity', 'alignment length',
                  'mismatches', 'gap opens', 'q. start', 'q. end', 's. start',
                  's. end', 'evalue', 'bit score']  # Gives the df header names
    '''adds lcl| to result names because that is how our db is formatted
       This also outputs our df as a list with each hit on a new line
       '''
    apple = df['subject id'] = 'lcl|' + df['subject id'].astype(str)
    my_list = apple.tolist()
    with open('topnames.txt', 'w') as file:
        for item in my_list:
            file.write("{}\n".format(item))


def dbtabber(tab2):
    ''' dbtabber creates a seq record or an index as a dictionary.
If the seq object is too large, it is necessary to use the indexed dictionary.
The parsed records object requires a lot of memory. Safer to go with index.
    '''
    with open(tab2, 'r') as infile:
        records = list(SeqIO.parse(tab2, 'fasta'))
        print(len(records))
    record_dict = SeqIO.index(tab2, "fasta")
    print(len(record_dict))


def getit(tab2):
    ''' getit captures all fasta files whose ID's were in the top BLAST hits
    '''
    df = open('topnames.txt', 'r')
    top_hits = [line.strip() for line in df]
    fasta_sequences = SeqIO.parse(open(tab2), 'fasta')
    SeqIO.write((seq for seq in fasta_sequences if seq.id in top_hits),
                'tophits.txt', "fasta")


def main():
    path = askingforfiles()
    X = makedirectory(path.directory)
    os.chdir(X)
    ttt = path.directory
    tab = path.F
    outputtabber(tab)
    tab2 = path.db
    dbtabber(tab2)
    getit(tab2)

if __name__ == '__main__':
    main()
