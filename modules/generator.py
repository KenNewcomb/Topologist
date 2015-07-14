# Generator.py: Generates the [bonds] and [angles] section of a GROMACS topology file.
from math import ceil
output_file = []

def GROMACSDefaults():
	"""Generates the [ defaults ]"""
	global output_file
	output_file.append(";\tnbfunc\tcomb-rule\tgen-pairs\tfudgeLJ\tfudgeQQ")
	output_file.append("\t{0}\t{1}\t{2}\t{3}\t{4}".format(1,2,'no',1,1))
	output_file.append("")

def GROMACSAtoms(atomtypes):
	global output_file
	output_file.append(";\tname\tatomic_num\tmass\tcharge\tptype\tsigma\tepsil")
	for atomtype in atomtypes:
		output_file.append("\t{0}".format(atomtype))
	output_file.append("")
	pass

def GROMACSNonbonded():
	global output_file
	pass

def GROMACSBonds(bonds):
	global output_file
	output_file.append("[ bonds ]")
	output_file.append(";\ti\tj\tfunc\tlength\t\tforce.c")
	for bond in bonds:
		output_file.append("\t{0}\t{1}\t{2}\t{3}\t\t{4}".format(bond.atom1.index, bond.atom2.index, 1, ceil(bond.distance*10000)/10000, "No force constant given."))
	
def GROMACSAngles(angles):
	global output_file
	pass

def GROMACSSystem():
	global output_file
	pass

def GROMACSMolecules():
	global output_file
	pass

def writeTopology():
	global output_file
	topology = open('output', 'w')

	for line in output_file:
		topology.write(line + "\n")

	topology.close()
