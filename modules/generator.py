# Generator.py: Generates the [bonds] and [angles] section of a GROMACS topology file.
from math import ceil
output_file = []

def GROMACSDefaults():
	"""Generates the [ defaults ]"""
	defaults_section = []
	defaults.append(";\tnbfunc\tcomb-rule\tgen-pairs\tfudgeLJ\tfudgeQQ")
	defaults.append("\t{0}\t{1}\t{2}\t{3}\t{4}".format(1,2,'no',1,1))

def GROMACSAtoms(atom_list):
	atoms_section = []
	atoms_section.append("")
	pass

def GROMACSNonbonded():
	pass

def GROMACSBonds(bond_list):
	bonds_section = []
	bonds_section.append("[ bonds ]")
	bonds_section.append(";\ti\tj\tfunc\tlength\t\tforce.c")
	for bond in bond_list:
		bonds_section.append("\t{0}\t{1}\t{2}\t{3}\t\t{4}".format(bond.atom1.index, bond.atom2.index, 1, ceil(bond.distance*10000)/10000, "No force constant given."))
	
	output_file.append(bonds_section)

def GROMACSAngles():
	pass

def GROMACSSystem():
	pass

def GROMACSMolecules():
	pass

def writeTopology():
	topology = open('output', 'w')

	for line in output_file:
		topology.write(line + "\n")

	topology.close()
