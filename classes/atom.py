# atom.py: A class representing an atom.

class Atom:
	index   = 0
	atomtype    = ""
	x       = 0.0
	y       = 0.0
	z       = 0.0

	def __init__(self, index, atomtype, x, y, z):
		self.index    = index
		self.atomtype = atomtype
		self.x        = float(x)
		self.y        = float(y)
		self.z        = float(z)
