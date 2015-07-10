# processor.py: Process a parsed file. Find bond lengths, angles, etc.
from math import sqrt
from classes import bond

def findAtomicDistances(atom_list):
	"""Finds the distance between all atoms in a list."""
	print("Detecting atomic distances...")
	connectivities = []
	for index1 in range(0, len(atom_list)-1):
		for index2 in range(index1+1, len(atom_list)):
			dx = atom_list[index1].x - atom_list[index2].x
			dy = atom_list[index1].y - atom_list[index2].y
			dz = atom_list[index1].z - atom_list[index2].z
			distance = sqrt(dx**2 + dy**2 + dz**2)
			atom1 = atom_list[index1]
			atom2 = atom_list[index2]
			connectivities.append([atom1, atom2, distance])
	return connectivities

def findBonds(atom_list, connectivities, bonds): 

	# Loop over bond distance list and search for each distance in the distances list
	found_bonds = []

	for pair in bonds:
		type1check = pair[0]
		type2check = pair[1]
		distancecheck = float(pair[2])
		for connect in connectivities:
			type1 = connect[0].type
			type2 = connect[1].type
			distance = float(connect[2])
			if type1check == type1 and type2check == type2:
				if abs(distancecheck - distance) < 0.1:
					atom1 = atom_list[connect[0].index]
					atom2 = atom_list[connect[1].index]
					dr    = connect[2]
					found_bond = bond.Bond(atom1, atom2, dr)
					found_bonds.append(found_bond)
	return found_bonds

def findAtomicAngles(atom_list):
	angles = []
	pass
