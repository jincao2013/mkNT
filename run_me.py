#!/usr/bin/env python

__author__ = "Jin Cao"
__copyright__ = "Copyright 2016, qfmda.com"
__version__ = "0.1"
__maintainer__ = "Jin Cao"
__email__ = "jincao2013@outlook.com"
__date__ = "Dec 2, 2016"

from mkNT import POSCAR_to_crystal_data,build_supercell,make_NT,crystal_data_to_POSCAR

############## input ##############
input_filename = 'POSCAR_unit'
A = 1
C = 1
vacuum_list = [10,15,20]
B_list = [8,9,10,11,12,13,14,15,16,17,18,19,20]
############## input ##############


for vacuum in vacuum_list:
	for B in B_list:
		crystal_data = POSCAR_to_crystal_data(input_filename)
		output_filename = 'POSCAR'+'_vacuum='+str(vacuum)+'_B='+str(B)
		crystal_data_supercell =build_supercell(A,B,C,crystal_data)
		crystal_data_NT = make_NT(crystal_data_supercell,vacuum)
		crystal_data_to_POSCAR(crystal_data_NT,output_filename)