# Processor.py: Process a parsed file. Find bond lengths, angles, etc.
import math

def findAtomicDistances(atom_list):
	"""Finds the distance between all atoms in a list."""
	distances = []
	for atom1 in range(0, len(atom_list)-1):
		for atom2 in range(atom1+1, len(atom_list)):
			dx = atom_list[atom1][3] - atom_list[atom2][3]
			dy = atom_list[atom1][4] - atom_list[atom2][4]
			dz = atom_list[atom1][5] - atom_list[atom2][5]
			distance = math.sqrt(dx**2 + dy**2 + dz**2)
			distances.append([atom1, atom2, distance])
	return distances

def findBonds(atom_list, distances):
	bond_list = input("Enter the bond lengths to be detected (separated by spaces): ")
	bond_list = bond_list.split()

	# Loop over bond distance list and search for each distance in the distances list
	for bond in bond_list:
		for distance in distances:
			if abs(float(bond) - float(distance[2])) < 0.15:
				print("Bond detected: Atom 1 Type: {}, Atom 2 Type: {}".format(atom_list[distance[0]][1], atom_list[distance[1]][1]))
