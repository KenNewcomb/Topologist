# settings.py: A class to store settings.

class Settings:

	input_files = []
	bonds = []
	bondatom1 = ""
	bondatom2 = ""
	distance = 0.0
	bond_length = 0.0
	force_constant = 0.0
	output = ""
	angleatom1 = ""
	angleatom2 = ""
	angleatom3 = ""
	angle = 0.0
	angle_constant = 0.0
	angles = []
	atoms = []
	mix = False
	system = ""

	def addInput(self, filename):
		self.input_files.append(filename)
	
	def addBond(self, bondatom1, bondatom2, distance, bond_length, force_constant):
		self.bonds.append([bondatom1, bondatom2, distance, bond_length, force_constant])
	
	def addAngle(self, angleatom1, angleatom2, angleatom3, angle, angle_constant):
		self.angles.append([angleatom1, angleatom2, angleatom3, angle, angle_constant])

	def addOutput(self, output):
		self.output = output
	
	def addSystem(self, system):
		self.system = system
	
	def addAtom(self, symbol, number, mass, charge, sigma, epsilon):
		atom = [symbol, number, mass, charge, sigma, epsilon]
		self.atoms.append(atom)
	
	def getSystem(self):
		return self.system

	def getInputFiles(self):
		return self.input_files

	def getBonds(self):
		return self.bonds

	def getAngles(self):
		return self.angles

	def getBondLength(self, atom1, atom2):
		for bond in self.bonds:
			if bond[0] == atom1.getAtomType() and bond[1] == atom2.getAtomType():
				return bond[3]
	def getForceConstant(self, atom1, atom2):
		for bond in self.bonds:
			if bond[0] == atom1.getAtomType() and bond[1] == atom2.getAtomType():
				return bond[4]
	def getAngle(self, atom1, atom2, atom3):
		for angle in self.angles:
			if angle[0] == atom1.getAtomType() and angle[1] == atom2.getAtomType() and angle[2] == atom3.getAtomType():
				return angle[3]

	def getAngleConstant(self, atom1, atom2, atom3):
		for angle in self.angles:
			if angle[0] == atom1.getAtomType() and angle[1] == atom2.getAtomType() and angle[2] == atom3.getAtomType():
				return angle[4]
	def getInputType(self, filenumber):
		return self.input_files[filenumber].split('.')[1]

	def getOutputType(self):
		return self.output

	def getSigma(self, atomtype):
		for atom in self.atoms:
			if atom[0] == atomtype:
				return float(atom[4])
	def getEpsilon(self, atomtype):
		for atom in self.atoms:
			if atom[0] == atomtype:
				return float(atom[5])

	def getAtomInfo(self, atomtype):
		for atom in self.atoms:
			if atom[0] == atomtype:
				return atom
	
	def mix(self):
		self.mix = True
