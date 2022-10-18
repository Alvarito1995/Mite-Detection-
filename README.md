# (LINUX-BASED)-Mite-Detection-In-Grapevine-Genome.
**MITEs detection in grapevine's reference genome as an example that can be extrapolated to other plants species**

**Entry _Under Construction!_**

As a effort to ensure the alimentary sovereignty to the future generations, blablabla...

Index:

1. Explanation of the procedure

2. Programs needed

3. Protocol used for the analysis in the V4 PN40024 reference genome of _Vitis vinifera_

4. Attached documents details

5. Bibliography

**Explanation**


**Programs used**
1. MiteFinderII:
2. MiteTracker:
3. Mitetracker/blast:
4. MiteTracker/vsearch:
5. R: www.r-project.org
6. RStudio: www.rstudio.com
7. 'TE' package for R: https://cran.r-project.org/web/packages/TE/index.html
8. Jbrowse: https://jbrowse.org/jb2/


**Protocol for MITEs detection, classification and study**


**Troubleshooting**

*Clustering problem:* In my case, I've a big problem with the Clustering analysis by MiteTracker/Vsearch, because when MITETracker.py script opens the vsearchcluster.py, it was impossible to find the library "vsearch" (it's shared library). The solution was to change the line `./vsearchVERSION/bin/vsearch`  for the complete path to the library `/home/user/vsearchVERSION/bin/vsearch`.
If you're not sure about the path to your vsearch, just run this:
`find /home -type f -name vsearch `
and copy-paste the path that appears in the vsearchcluster.py script.

**Attached documents**

In the attached documents you can find:
1. The reference genome of _Vitis vinifera_ in the V4 version of PN40024: Fasta document containing the last sequencing data available at this time (18/10/2022). 

2. Mitesvides: Output file obtained from the MiteFinderII analysis, in the format, for all the 19.819 MITEs identified in the grapevine genome:
`mite|6|4131|4140|4194|4203|t3|4138|m1|ave_score:0.649614 
GTTGCTCACCCCTGCTCTTGAGCCTTTGAAACATCTACACCAATTTTTTATTGTTTTCAT 
CTATCCGTTTAAGTGGATTAAAATGATGTTTTTTAATTTTTTTTTATATTTTTTGGGCCG...`
Where the 6 means the serial number of chromosome and 4131|4140|4194|4203 are the position of TIRs. t3 means the length of TSD is 3. m1 means the TIR is the imperfect inverted repeats and 4138 is the mismatch base. The ave_score:0.649614 is the score of MITE sequence(More details can be seen in the **Programs used/MiteFinderII** citation).

3. 

For any doubt don't hesitate to write an email to: _alvaro.vidal@fmach.it_ 
This work was supported by COST Action AC18111 "PlantEd" via Virtual Mobility Grant.
