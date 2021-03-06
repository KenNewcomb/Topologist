# atom.py: A class representing an atom.

class Atom:

	index    = 1
	atomtype = ""
	x        = 0.0
	y        = 0.0
	z        = 0.0
	neighborlist = []

	def __init__(self, index, atomtype, x, y, z):
		self.index    = index
		self.atomtype = atomtype
		self.x        = float(x)
		self.y        = float(y)
		self.z        = float(z)
		self.neighborlist = []	

	def getIndex(self):
		return self.index

	def getAtomType(self):
		return self.atomtype

	def addNeighbor(self, neighbor):
		self.neighborlist.append(neighbor)
	
	def getNeighborList(self):
		return self.neighborlist
