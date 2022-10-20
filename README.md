# (LINUX-BASED) MITE Detection In Grapevine Genome.
**_Miniature Inverted-repeat Transposable Elements_ (MITEs) detection in grapevine's reference genome focused in the Drought tolerance related-MITEs, as an example that can be extrapolated to other plants species**

**This Entry is  _¡Under Construction!_**

As a effort to ensure the alimentary sovereignty to the future generations, we must, as scientists, try to maintain technological advances at the level that the future requires, which is why this work of compilation and analysis of Miniature Inverted-repeat Transposable Elements is carried out, in search of new clues to understand and improve tolerance to water stress by fruit trees such as vines and apple trees, but that can be used for other plant species, as a tool for future genetic improvements that allow us to feed the future world. For us as a team, the goal is that wine can continue to exist as long as humanity does, cheers!

**Index:**

1. Explanation of the procedure.

2. Programs used.

3. Protocol used for the analysis in the V4 PN40024 reference genome of _Vitis vinifera_.

4. Troubleshooting.

5. Details regarding the Attached Documents.

6. Final remarks.


**Explanation**

This month (October 2022) it was published a research article from the Qingmei Guan group[^5], that shows a relationship between an specific MITE present in the promoter of the apple tree gene "MdRFNR1" that make it drought-activated. Therefore, it became necessary to study this specific MITE in the grapevine plant genome, to analyze the possibilities of a conserved function in fruit trees, and thus explore the possibilities that non-coding DNA gives us in the gene improvement of plants, and let us elucidate a little better how cis-elements controls the gene expression under stress conditions. This work of search and analysis of MIT elements related to the response to water stress, is framed within Álvaro Vidal's doctoral thesis, and is complemented by [VitViz/HydricAtlas](http://www.vitviz.tk/HydricStressAtlas/), an application for generating heatmaps to see gene expression in response to drought, developed at the beginning of this year, thats takes all the RNA-seq data available for grapevine and drought, which allows separating expression levels by tissues, stress levels, cultivars and bioprojects. This application was used in a complementary way with this analysis, to improve the results. 

**Programs used**
1. [MiteFinderII](https://github.com/jhu99/miteFinder)[^1].
2. [MiteTracker](https://github.com/INTABiotechMJ/MITE-Tracker)[^2]
3. [Mitetracker/blast](https://blast.ncbi.nlm.nih.gov/doc/elastic-blast/tutorials/pypi-install.html)[^3]
4. [MiteTracker/vsearch](https://github.com/torognes/vsearch)[^4]
5. [R](www.r-project.org)
6. [RStudio](www.rstudio.com)
7. ['TE' package for R](https://cran.r-project.org/web/packages/TE/index.html)
8. [Jbrowse](https://jbrowse.org/jb2/)
9. [Mafft](https://mafft.cbrc.jp/alignment/software/linux.html)
10. [Iqtree](http://www.iqtree.org/doc/Quickstart)


**Protocol for MITEs detection, classification and study**
Once all the programs and packages listed before were installed and tested (Each one has an explanation for the instalation in the official page), the procedure starts with the MITE search upon the Reference genome, taking at least 80% of identity for each MITE, if you want to extrapolate it to other cultivars (this is the case).
The first and more usefull approach used was the Jbrowse's track construction for MITE search:
1. First you should download the sequence of your genome of reference
2. The next step is to analyse all the genome looking for the basic domain of MITE by using MiteFinderII opening the terminal from the its folder and typing `python3 MITETracker.py  -g /home/user/PATHWAY/genome.fasta -j OUTPUTNAME`
3. As Jbrowse doesn't detect .FASTA files, this should be transformed to [.BED format](https://genome.ucsc.edu/FAQ/FAQformat.html#format1), so the output of this analysis (described bellow in the _attached documents_ part), should be transformed to a Jbrowse-track file, by changinf it to .BED format by using the **Mites_fasta_to_bed.py** script that's contains:


```
f_in = "datos/mitesvides.fasta"
f = open(f_in, "r", encoding="utf-8")
out_text = ""
for line in f:
    if line[0] == ">":
        temp = line.split("|")
        chromosome = temp[1]
        TSD = int(temp[6][1:])
        start = str(int(temp[2]) - TSD)
        end = str(int(temp[5]) + TSD)
        name = "mite" + "_" + temp[8] + "_" + temp[7]
        out_text += ("chr" + chromosome + "\t" + start + "\t" + end +
                    "\t" + name + "\t" + "1" + "\t" + "+" + "\n")
f.close()
f_out = "mitesvides.bed"
f = open(f_out, "w", encoding="utf-8")
f.write(out_text)
f.close()
```

4. Once you obtain the .BED file, you can open the JBrowse of your genome with the tracks that makes easier the analysis for you, in this case the V3 ID code ("genenames-track") was used, in order to estimate the promoter location in each case.
5. Select the genes that interest you the most, and look the UTR region up to 2500 pb if thereŕe some MITEs identified, and take the specific sequence of all of them in .fasta format. 
In this case, we used 42 genes related to drought-stress response in grapevine, looking on their UTR region and found 11 MITEs to study.
6. As the main objective of this analysis is to identify the drought-stress related MITEs, the next step is to look wich of the detected MITEs are the mPIF-like type, using multiple sequence alignment and phylogenetic tree construction. So we identify some consensus sequences of MITE (in document _consenso.fasta_), and make a .FASTA file containing all of the consensus sequence plus the MITEs identifyed in the normal format:

```
>NAME
(SEQ)ATTATATTATTAT
```

7. In order to carry out the multiple sequence alignment the `mafft` code was used to obtain the **.phy** file.
8. Then IQtree was used by typing `iqtree -b 1000 -s DOC.phy -nt 4` in the terminal, for a 1000 bootstrap analysis (if you want less-fiable but quick result, just use less bootstraps), and you will obtain a **.treefile** file that can be analysed online in [IcyTree](Icytree.org) looking for nodes between your sequence of interest (mPIF1 in this case), with your input sequences with at least 70 as a value (70%).
9. Finally, to carry out the drought-related MITEs identification in promoters, we select the more similar sequences with mPIF1.[^5]

Other analysis that you can carry out in this field, is the estatistical analysis of MITEs in your genome by using MiteTracker and RStudio with the TE package. 

***SETTING THIS UP (YET)***


 

**Troubleshooting**

*Clustering problem:* In my case, I've a big problem with the Clustering analysis by MiteTracker/Vsearch, because when MITETracker.py script opens the vsearchcluster.py, it was impossible to find the library "vsearch" (it's shared library). The solution was to change the line `./vsearchVERSION/bin/vsearch`  for the complete path to the library `/home/user/vsearchVERSION/bin/vsearch`.
If you're not sure about the path to your vsearch, just run this:
`find /home -type f -name vsearch `
and copy-paste the path that appears in the vsearchcluster.py script.
For other specific Toubles, please check in each tool's webpage.

**Attached documents**

In the attached documents you can find:

1. [PN40024.zip](https://integrape.eu/wp-content/uploads/2021/11/PN40024.v4_11_05_21.zip): click to download the reference genome of _Vitis vinifera_ in the V4 version of PN40024, the fasta document contain the last sequencing data available at this moment (October/2022). 

2. Mitesvides.fasta: Output file obtained from the MiteFinderII analysis, in the format, for all the 19.819 MITEs identified in the grapevine genome:

```
mite|6|4131|4140|4194|4203|t3|4138|m1|ave_score:0.649614 
GTTGCTCACCCCTGCTCTTGAGCCTTTGAAACATCTACACCAATTTTTTATTGTTTTCAT 
CTATCCGTTTAAGTGGATTAAAATGATGTTTTTTAATTTTTTTTTATATTTTTTGGGCCG...
```

Where the 6 means the serial number of chromosome and 4131|4140|4194|4203 are the position of TIRs. t3 means the length of TSD is 3. m1 means the TIR is the imperfect inverted repeats and 4138 is the mismatch base. The ave_score:0.649614 is the score of MITE sequence(More details can be seen in [MiteFinderII](https://github.com/jhu99/miteFinder)).

3. Mites_fasta_to_bed.py: Python3 script to change the file type from the output *Mitesvides.fasta* to *Mitesvides.Bed*.

4. Mitesvides.bed: Document created to use as a Jbrowse Track, that let us analize the genomic location of each specific MITE regarding the genes. This gives us the possibility to study the Cis-Regulatory MITEs, the orientation and sequences involved. 

6. secuenciasblanco.fasta: Document with the identified MITEs in the promotos of the drought-related genes identified in 

7. Consenso.fasta: Document used for the sequence alignment as a query to identify families of MITEs.

8. DOC.phy.treefile: Phylogenetic tree with 1000 boostraps between the identified MITEs and consensus ones.

**Final remarks**

This work was supported by COST Action CA18111 [PlantEd](https://plantgenomeediting.eu/) by the Virtual Mobility Grant "MITEs identification in grapevine genome as a tool for future genome editing target to improve drought resistance".

This work was carried out in a colaborative way between the Fondazione Edmund Mach (TN, Italy), and the I2SysBio (Valencia, Spain). By Álvaro Vidal Valenzuela, David Navarro, Tomás Matus and Mickael Malnoy.

For any doubt don't hesitate to [email me](alvaro.vidal@fmach.it).



[^4]: Rognes T, Flouri T, Nichols B, Quince C, Mahé F. (2016) VSEARCH: a versatile open source tool for metagenomics. PeerJ 4:e2584. doi: 10.7717/peerj.2584
[^3]: Crescente, J., Zavallo, D., Helguera, M. et al. MITE Tracker: an accurate approach to identify miniature inverted-repeat transposable elements in large genomes. BMC Bioinformatics 19, 348 (2018). https://doi.org/10.1186/s12859-018-2376-y
[^2]: Crescente, Juan Manuel, et al. "MITE Tracker: an accurate approach to identify miniature inverted-repeat transposable elements in large genomes." BMC Bioinformatics 19.1 (2018): 348. 
[^1]: Hu, J., Zheng, Y. & Shang, X. MiteFinderII: a novel tool to identify miniature inverted-repeat transposable elements hidden in eukaryotic genomes. BMC Med Genomics 11 (Suppl 5), 101 (2018). https://doi.org/10.1186/s12920-018-0418-y
[^5]: Chundong Niu, Lijuan Jiang, Fuguo Cao, Chen Liu, Junxing Guo, Zitong Zhang, Qianyu Yue, Nan Hou, Zeyuan Liu, Xuewei Li, Muhammad Mobeen Tahir, Jieqiang He, Zhongxing Li, Chao Li, Fengwang Ma, Qingmei Guan, Methylation of a MITE insertion in the MdRFNR1-1 promoter is positively associated with its allelic expression in apple in response to drought stress, The Plant Cell, Volume 34, Issue 10, October 2022, Pages 3983–4006, https://doi.org/10.1093/plcell/koac220


 
