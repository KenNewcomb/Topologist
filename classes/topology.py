# topology.py: a class representing a chemical topology.
from classes import molecule

class Topology():

	molecules = []
	output_type = ""

	def __init__(self):
		self.molecules = []
		self.output_type = ""

	def addMolecule(self, molecule):
		self.molecules.append(molecule)

	def getMolecules(self):
		return self.molecules

	def getAtomTypes(self):
		atomtypes = []
		for molecule in self.molecules:
			for atom in molecule.getAtoms():
				if atom.getAtomType() not in atomtypes:
					atomtypes.append(atom.getAtomType())
		return atomtypes

	def setOutputType(self, output_type):
		self.output_type = output_type
