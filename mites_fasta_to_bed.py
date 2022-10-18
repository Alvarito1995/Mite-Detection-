#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 11:07:31 2022

Script para pasar del output en fasta de mitefinderII a un fichero bed que se pueda
cargar como track en un jbrowse con el genoma de vid cargado.

@author: David Navarro
"""

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
        # Le estoy añadiendo al nombre qué tipo de cambios tiene el MITE, m1, m0 etc.
        name = "mite" + "_" + temp[8] + "_" + temp[7]
        out_text += ("chr" + chromosome + "\t" + start + "\t" + end + 
                    "\t" + name + "\t" + "1" + "\t" + "+" + "\n")
    
f.close()

f_out = "mitesvides.bed"

f = open(f_out, "w", encoding="utf-8")

f.write(out_text)

f.close()
