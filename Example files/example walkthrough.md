# Example of how to execute with the files provided

This will provide a walkthrough with the given files.

Here are the files and their contents. All output files have been uploaded for peace of mind, but only 3 files are required to run this.

  * *GOS.GS044.fna* -- BLAST formatted database from one GOS sampling site

  * *ecoli.fna* -- fasta file containing sequence of *Escherichia coli* O157:H7 str. Sakai chromosome, complete genome

  * *example_ecoli_BLAST* -- conatains BLASTn results of ecoli.fna against GOS.GS044.fna

  * **Results** -- directory containing expected result files


WORKFLOW

**For ease, These are broken up into the steps that are listed in the RBB/README.md**


**Step 1** 

  * Make blast database using set of GOS metagenomic reads. For ease I have included the already created database as **GOS.GS044.fna** 

                makeblastdb -dbtype nucl -in GOS.GS044.fna -parse_seqids -hash_index


  * BLAST query sequence (*ecoli.fna*) against newly made db(*GOS.GS.044.fna*)

                blastn -query ecoli.fna -task blastn -db GOS.GS044.fna -out example_ecoli_BLAST -outfmt 6


**Step 2**

  * Get fasta sequences back from BLAST output

                get_fastas.py --F \..\example_ecoli_BLAST --directory \..\test --db \..\GOS.GS044.fna


**Step 3**

  * This can be done using a repeat of **Step 1**, but I have uploaded a test second BLAST file with 5 sequences (1 unique, 2 duplicate, and 2 that don't match)


  * These can be found in secondblast_example.txt


**Step 4**

  * Use RBH to compare 2 outputs

                 rbh_35.py \..\secondblast_example.txt \..\RBB\tophits.txt -a nucl -t blastn -i 70 -c 50 -o \..\RBB\Ecoli_RBBtest.tsv

