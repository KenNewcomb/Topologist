# Processor.py: Process a parsed file. Find bond lengths, angles, etc.
from math import sqrt
from classes import bond

def findAtomicDistances(atom_list):
	"""Finds the distance between all atoms in a list."""
	print("Detecting atomic distances...")
	distances = []
	for atom1 in range(0, len(atom_list)-1):
		for atom2 in range(atom1+1, len(atom_list)):
			dx = atom_list[atom1].x - atom_list[atom2].x
			dy = atom_list[atom1].y - atom_list[atom2].y
			dz = atom_list[atom1].z - atom_list[atom2].z
			distance = sqrt(dx**2 + dy**2 + dz**2)
			distances.append([atom1, atom2, distance])
	return distances

def findBonds(atom_list, distances):
	bond_lengths = input("Enter the bond lengths to be detected (separated by spaces): ")
	bond_lengths = bond_lengths.split()

	# Loop over bond distance list and search for each distance in the distances list
	found_bonds = []
	for length in bond_lengths:
		for distance in distances:
			if abs(float(length) - float(distance[2])) < 0.15:
				atom1 = atom_list[distance[0]]
				atom2 = atom_list[distance[1]]
				dr    = distance[2]
				found_bond = bond.Bond(atom1, atom2, dr)
				found_bonds.append(found_bond)
	return found_bonds

def findAtomicAngles(atom_list):
	angles = []
	pass
