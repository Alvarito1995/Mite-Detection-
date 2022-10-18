# (LINUX-BASED)-Mite-Detection-In-Grapevine-Genome.
**MITEs detection in grapevine's reference genome focused in the Drought tolerance related-MITEs, as an example that can be extrapolated to other plants species**

**This Entry is  _¡Under Construction!_**

As a effort to ensure the alimentary sovereignty to the future generations, blablabla...

Index:

1. Explanation of the procedure.

2. Programs needed.

3. Protocol used for the analysis in the V4 PN40024 reference genome of _Vitis vinifera_.

4. Details regarding the Attached Documents.

6. Final remarks.


**Explanation**


**Programs used**
1. [MiteFinderII](https://github.com/jhu99/miteFinder)[^4].
2. [MiteTracker](https://github.com/INTABiotechMJ/MITE-Tracker)[^3]
3. [Mitetracker/blast](https://blast.ncbi.nlm.nih.gov/doc/elastic-blast/tutorials/pypi-install.html)[^2]
4. [MiteTracker/vsearch](https://github.com/torognes/vsearch)[^1]
5. [R](www.r-project.org)
6. [RStudio](www.rstudio.com)
7. ['TE' package for R](https://cran.r-project.org/web/packages/TE/index.html)
8. [Jbrowse](https://jbrowse.org/jb2/)


**Protocol for MITEs detection, classification and study**

As Jbrowse doesn't detect that type of file, should be transformed to [.BED format](https://genome.ucsc.edu/FAQ/FAQformat.html#format1), 

**Troubleshooting**

*Clustering problem:* In my case, I've a big problem with the Clustering analysis by MiteTracker/Vsearch, because when MITETracker.py script opens the vsearchcluster.py, it was impossible to find the library "vsearch" (it's shared library). The solution was to change the line `./vsearchVERSION/bin/vsearch`  for the complete path to the library `/home/user/vsearchVERSION/bin/vsearch`.
If you're not sure about the path to your vsearch, just run this:
`find /home -type f -name vsearch `
and copy-paste the path that appears in the vsearchcluster.py script.

**Attached documents**

In the attached documents you can find:

1. [PN40024.zip](https://integrape.eu/wp-content/uploads/2021/11/PN40024.v4_11_05_21.zip): click to download the reference genome of _Vitis vinifera_ in the V4 version of PN40024, the fasta document contain the last sequencing data available at this moment (October/2022). 

2. Mitesvides.fasta: Output file obtained from the MiteFinderII analysis, in the format, for all the 19.819 MITEs identified in the grapevine genome:

`mite|6|4131|4140|4194|4203|t3|4138|m1|ave_score:0.649614 
GTTGCTCACCCCTGCTCTTGAGCCTTTGAAACATCTACACCAATTTTTTATTGTTTTCAT 
CTATCCGTTTAAGTGGATTAAAATGATGTTTTTTAATTTTTTTTTATATTTTTTGGGCCG...`

Where the 6 means the serial number of chromosome and 4131|4140|4194|4203 are the position of TIRs. t3 means the length of TSD is 3. m1 means the TIR is the imperfect inverted repeats and 4138 is the mismatch base. The ave_score:0.649614 is the score of MITE sequence(More details can be seen in [MiteFinderII](https://github.com/jhu99/miteFinder)).

3. Mites_fasta_to_bed.py: Python3 script to change the file type from the output *Mitesvides.fasta* to *Mitesvides.Bed*.

4. Mitesvides.bed: Document created to use as a Jbrowse Track, that let us analize the genomic location of each specific MITE regarding the genes. This gives us the possibility to study the Cis-Regulatory MITEs, the orientation and sequences involved. 

6. 

**Final remarks**

This work was supported by COST Action CA18111 [PlantEd](https://plantgenomeediting.eu/) by the Virtual Mobility Grant "MITEs identification in grapevine genome as a tool for future genome editing target to improve drought resistance".

This work was carried out in a colaborative way between the Biotechnology vegetal unit from the Fondazione Edmund Mach (TN, Italy), and the TOMS Biolab from I2SysBio (Valencia, Spain). By Álvaro Vidal Valenzuela, David Navarro, Tomás Matus and Mickael Malnoy.

For any doubt don't hesitate to [email me](alvaro.vidal@fmach.it).



[^1]: Rognes T, Flouri T, Nichols B, Quince C, Mahé F. (2016) VSEARCH: a versatile open source tool for metagenomics. PeerJ 4:e2584. doi: 10.7717/peerj.2584
[^2]: Crescente, J., Zavallo, D., Helguera, M. et al. MITE Tracker: an accurate approach to identify miniature inverted-repeat transposable elements in large genomes. BMC Bioinformatics 19, 348 (2018). https://doi.org/10.1186/s12859-018-2376-y
[^3]: Crescente, Juan Manuel, et al. "MITE Tracker: an accurate approach to identify miniature inverted-repeat transposable elements in large genomes." BMC Bioinformatics 19.1 (2018): 348. 
[^4]: Hu, J., Zheng, Y. & Shang, X. MiteFinderII: a novel tool to identify miniature inverted-repeat transposable elements hidden in eukaryotic genomes. BMC Med Genomics 11 (Suppl 5), 101 (2018). https://doi.org/10.1186/s12920-018-0418-y

 
