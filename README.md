# RBB
Reciprocal Best Blast of GOS database
========

RBB is a program designed to perform a Reciprocal Best Blast against a given BLAST formatted database. This code has been optimized to work with the Global Ocean Sampling Expedition [GOS] (http://www.jcvi.org/cms/research/projects/gos/overview) and Tara (http://ocean-microbiome.embl.de/companion.html) datasets. 

INSTALLATION
------------  

RBB was written in Python 3. Python was installed using the Anaconda free distribution. Installation of Anaconda can be found at: https://docs.continuum.io/anaconda/install.

RBB also requires [BioPython] to be installed. Please visit (http://biopython.org/wiki/Documentation) for documentation regarding BioPython

RBB also requires the BLAST+ suite to be installed on your local PATH. Please visit (https://blast.ncbi.nlm.nih.gov/Blast.cgi?PAGE_TYPE=BlastDocs&DOC_TYPE=Download) for usage and help installing.

The RBB repository also includes a shell script for use on unix systems to create a database and conduct a BLAST. This author recommends not running a large BLAST on your local computer as the memory requirements can get quite large for these databases.

USAGE
-----

RBB has 4 main steps:

#1


