# topology.py: a class representing a chemical topology.

class Topology():

	molecules = []

	def __init__(self):
		pass

	def addAtoms(self, atom_list):
		for atom in atom_list:
			self.atoms.append(atom)
	
	def addBonds(self, bond_list):
		for bond in bond_list:
			self.bonds.append(bond)

	def getAtoms(self);
		return atoms

	def getAtomTypes(self):
		atomtypes = []
		for atom in atom_list:
			if atom.type not in atomtypes:
				atomtypes.append(atom.type)
