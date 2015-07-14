# molecule.py: An object that represents a molecule.

class Molecule():

	residue = ""
	atoms = []
	bonds = []
	connectivities = []
	angles = []

	def __init__(self):
		pass
	
	def addAtom(self, atom):
		self.atoms.append(atom)
	
	def addBond(self, bond):
		self.bonds.append(bond)
	
	def addConnectivity(self, connectivity):
		self.connectivity.append(connectivity)

	def addAngle(self, angle):
		self.angles.append(bond)
	
	def setResidue(self, residue):
		self.residue = residue
		
	def getAtoms(self):
		return self.atoms

	def getBonds(self):
		return self.bonds
	
	def getAngles(self):
		return self.angles
	
	def getResidue(self, residue):
		return self.residue

	def getConnectivities(self):
		return self.connectivites
