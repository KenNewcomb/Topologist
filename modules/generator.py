# Generator.py: Generates the [bonds] and [angles] section of a GROMACS topology file.
from math import ceil

def GROMACSAtoms(atom_list):
	pass

def GROMACSBonds(bond_list):
	bonds_section = []
	bonds_section.append("[ bonds ]")
	bonds_section.append(";\ti\tj\tfunc\tlength\t\tforce.c")
	for bond in bond_list:
		bonds_section.append("\t{0}\t{1}\t{2}\t{3}\t\t{4}".format(bond.atom1.index, bond.atom2.index, 1, ceil(bond.distance*10000)/10000, "No force constant given."))
	
	for line in bonds_section:
		print(line)
def GROMACSAngles():
	pass
