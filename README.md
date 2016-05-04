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
Make a BLAST database using the makeblastdb command from the BLAST+ suite.

    makeblastdb -dbtype nucl -in *input_fasta* -parse_seqids -hash_index

