# processor.py: Process a parsed file. Find bond lengths, angles, etc.
from math import sqrt
from classes import bond

def findAtomicDistances(atom_list):
	"""Finds the distance between all atoms in a list."""
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
	found_bonds = []
	# Loop over bonds to check
	for pair in bonds:
		type1check = pair[0]
		type2check = pair[1]
		distancecheck = pair[2]

		# Loop over connectivities between atoms
		for connect in connectivities:
			type1 = connect[0].type
			type2 = connect[1].type
			distance = float(connect[2])
	
			# If both atom types are the same, check the distances
			if type1check == type1 and type2check == type2:

				# If range of distances to check is given
				if '-' in distancecheck:
					distance1 = float(distancecheck.split('-')[0])
					distance2 = float(distancecheck.split('-')[1])
					if distance >= distance1 and distance <= distance2:
						atom1 = atom_list[connect[0].index-1]
						atom2 = atom_list[connect[1].index-1]
						dr    = connect[2]
						found_bond = bond.Bond(atom1, atom2, dr)
						found_bonds.append(found_bond)

				# If one distance is given, search within 0.1 angstroms.
				else:
					if abs(float(distancecheck)- distance) < 0.1:
						atom1 = atom_list[connect[0].index]
						atom2 = atom_list[connect[1].index]
						dr    = connect[2]
						found_bond = bond.Bond(atom1, atom2, dr)
						found_bonds.append(found_bond)
	return found_bonds

def findAtomicAngles(atom_list):
	angles = []
	pass
