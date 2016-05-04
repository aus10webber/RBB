# Example of how to execute with the files provided

This will provide a walkthrough with the given files.

Here are the files and their contents. All output files have been uploaded for ease, but only 3 files are required to run this.

WORKFLOW
** For ease, These are broken up into the steps that are listed in the RBB/README.md**



**Step 1** 

  * Make blast database using set of GOS metagenomic reads. For ease I have included the already created database as **GOS.GS044.fna** 

                makeblastdb -dbtype nucl -in GOS.GS044.fna -parse_seqids -hash_index


  * BLAST query sequence (*ecoli.fna*) against newly made db(*GOS.GS.044.fna*)
                blastn -query ecoli.fna -task blastn -db GOS.GS044.fna -out example_ecoli_BLAST -outfmt 6




