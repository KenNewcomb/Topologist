# bond.py: A class describing a bond between two atoms.

class Bond:
	atom1 = ""
	atom2 = ""
	distance = 0

	def __init__(self, atom1, atom2, distance):
		self.atom1    = atom1
		self.atom2    = atom2
		self.distance = distance
