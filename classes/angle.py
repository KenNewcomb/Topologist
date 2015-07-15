# angle.py: A class describing an angle between three atoms.

class Angle:
	atom1 = ""
	atom2 = ""
	atom3 = ""
	angle = 0.0

	def __init__(self, atom1, atom2, atom3, angle):
		self.atom1    = atom1
		self.atom2    = atom2
		self.atom3    = atom3
		self.angle    = angle
