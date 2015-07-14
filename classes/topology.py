# topology.py: a class representing a chemical topology.

class Topology():

	molecules = []
	output_type = ""

	def addMolecule(self, molecule):
		self.molecules.append(molecule)
	
	def getMolecules(self):
		return self.molecules

	def getAtomTypes(self):
		atomtypes = []
		for molecule in molecules:
			for atom in molecule:
				if atom not in atomtypes:
					atomtypes.append(atom)
		return atomtypes

	def setOutputType(self, output_type):
		self.output_type = output_type
