# Mite-Detection-In-Grapevine-(Linux-based).
**MITEs detection in grapevine's reference genome**

**Entry _Under Cosntruction!_**

As a effort to ensure the alimentary soverinity to the future generations, blablabla...

Index:

1. Explanation of the procedure

2. Programs needed

3. Protocol used for the analysis in the V4 PN40024 reference genome of _Vitis vinifera_

4. Attached documents details

**Explanation**


**Programs used**
1. MiteFinder II:
2. MiteTracker:
3. Mitetracker/blast:
4. MiteTracker/vsearch:
5. R-cran:
6. RStudio:
7. 'TE' package for R:
8. Jbrowse:


**Protocol for MITEs detection, classification and study**


**Troubleshoting**

*Clustering problem:* In my case, I've a big problem with the Clustering analysis by MiteTracker/Vsearch, because when MITETracker.py script opens the vsearchcluster.py, it was impossible to find the library "vsearch" (it's shared library). The solution was to change the line "./vsearchVERSION/bin/vsearch" for the complete path to the library "/home/user/vsearchVERSION/bin/vsearch".
If you're not sure about the path to your vsearch, just run this:
`find /home -type f -name vsearch `
and copy the path that appears.

**Attached documents**



For any doubt don't hesitate to write an email to: _alvaro.vidal@fmach.it_ 
This work was supported by COST Action AC18111 "PlantEd" via Virtual Mobility Grant.
