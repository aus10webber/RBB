# RBB
Reciprocal Best Blast of GOS database
========

RBB is a program designed to perform a Reciprocal Best Blast against a given BLAST formatted database. This code has been optimized to work with the Global Ocean Sampling Expedition [GOS] (http://www.jcvi.org/cms/research/projects/gos/overview) and [Tara] (http://ocean-microbiome.embl.de/companion.html) datasets. 

INSTALLATION
------------  

RBB was written in Python 3. Python was installed using the [Anaconda] (https://docs.continuum.io/anaconda/install) free distribution.

RBB also requires [BioPython] (http://biopython.org/wiki/Documentation) to be installed.

RBB also requires the [BLAST+ suite] (https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download) to be installed and on your local PATH.

The RBB repository also includes a shell script for use on unix systems to create a database and conduct a BLAST. This author recommends not running a large BLAST on your local computer as the memory requirements can get quite large for these databases.

USAGE
-----

RBB has 4 main steps:

#1
Make a BLAST database from a file containing fasta sequences using the makeblastdb command from the BLAST+ suite.

This requires **one input file**:
    *input fasta file* -- This is a file containing all fasta sequences to be used to make the database to be queried against.

        makeblastdb -dbtype nucl -in *input_fasta_file* -parse_seqids -hash_index

Use BLASTn to search a query sequence against the newly created database.

This requires **2 input files**:
   *query sequence* -- This is the fasta formatted sequence you wish to blast against the database 
   *new_db* -- This is the newly created BLAST formatted database created above.

        blastn -query *query sequence* -task blastn -db *new_db* - out *result_file* -outfmt 6
