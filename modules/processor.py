# processor.py: Process a parsed file. Find bond lengths, angles, etc.
from math import sqrt
from classes import bond as James
from classes import angle
from itertools import permutations

def findAtomicDistances(topology):
	"""Finds the distance between all atoms in each molecule."""
	molecules = topology.getMolecules()
	for molecule in molecules:
		atoms = molecule.getAtoms()
		for index1 in range(0, len(atoms)-1):
			for index2 in range(index1+1, len(atoms)):
				dx = atoms[index1].x - atoms[index2].x
				dy = atoms[index1].y - atoms[index2].y
				dz = atoms[index1].z - atoms[index2].z
				distance = sqrt(dx**2 + dy**2 + dz**2)
				atom1 = atoms[index1]
				atom2 = atoms[index2]
				molecule.addConnectivity([atom1, atom2, distance])
	return topology

def findBonds(topology, settings):
	"""Locates the bonds indicated in the settings file."""
	# Loop over bonds to check
	bonds_to_search = settings.getBonds()
	molecules = topology.getMolecules()
	for bond in bonds_to_search:
		type1check = bond[0]
		type2check = bond[1]
		distancecheck = bond[2]

		# Loop over connectivities between atoms
		for molecule in molecules:
			connectivities = molecule.getConnectivities()
			for connectivity in connectivities:
				type1 = connectivity[0].atomtype
				type2 = connectivity[1].atomtype
				distance = float(connectivity[2])
	
				# If both atom types are the same, check the distances
				if type1check == type1 and type2check == type2:

					# If range of distances to check is given
					if '-' in distancecheck:
						distance1 = float(distancecheck.split('-')[0])
						distance2 = float(distancecheck.split('-')[1])
						if distance >= distance1 and distance <= distance2:
							atom1 = connectivity[0]
							atom2 = connectivity[1]
							dr    = connectivity[2]
							found_bond = James.Bond(atom1, atom2, dr)
							molecule.addBond(found_bond)
							atom1.addNeighbor(atom2)
							atom2.addNeighbor(atom1)

					# If one distance is given, search within 0.1 angstroms.
					else:
						if abs(float(distancecheck)- distance) < 0.1:
							atom1 = connectivity[0]
							atom2 = connectivity[1]
							dr    = connectivity[2]
							found_bond = James.Bond(atom1, atom2, dr)
							molecule.addBond(found_bond)
							atom1.addNeighbor(atom2)
							atom2.addNeighbor(atom1)
	return topology

def findAngles(topology, settings):
	for molecule in topology.getMolecules():
		for atom in molecule.getAtoms():
			for neighbor1 in atom.getNeighborList():
				for neighbor2 in neighbor1.getNeighborList():
					if atom.getIndex() < neighbor2.getIndex() and settings.getAngle(atom, neighbor1, neighbor2) != None:
						search_angle = settings.getAngle(atom, neighbor1, neighbor2)
						possible_angle = angle.Angle(atom, neighbor1, neighbor2, search_angle)
						molecule.addAngle(possible_angle)
	return topology
