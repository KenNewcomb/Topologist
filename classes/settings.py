# settings.py: A class to store settings.

class Settings:

	input_files = []
	bonds = []
	type1 = ""
	type2 = ""
	distance = 0.0
	bond_length = 0.0
	force_constant = 0.0
	output = ""
	
	def addInput(self, filename):
		self.input_files.append(filename)
	
	def addBond(self, type1, type2, distance, bond_length, force_constant):
		self.bonds.append([type1, type2, distance, bond_length, force_constant])
	
	def addOutput(self, output):
		self.output = output
	
	def getInputFiles(self):
		return self.input_files

	def getBonds(self):
		return self.bonds

	def getBondLength(self, atom1, atom2):
		for bond in self.bonds:
			if bond[0] == atom1.getAtomType() and bond[1] == atom2.getAtomType():
				return bond[3]
	def getForceConstant(self, atom1, atom2):
		for bond in self.bonds:
			if bond[0] == atom1.getAtomType() and bond[1] == atom2.getAtomType():
				return bond[4]
	
	def getInputType(self, filenumber):
		return self.input_files[filenumber].split('.')[1]

	def getOutputType(self):
		return self.output
