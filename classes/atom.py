# atom.py: A class representing an atom.

class Atom:
	index   = 0
	type    = ""
	residue = ""
	x       = 0.0
	y       = 0.0
	z       = 0.0

	def __init__(self, index, type, residue, x, y, z):
		self.index    = index
		self.type     = type
		self.residue  = residue
		self.x        = float(x)
		self.y        = float(y)
		self.z        = float(z)
