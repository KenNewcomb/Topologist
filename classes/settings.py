# settings.py: A class to store settings.

class Settings:

	input_files = []
	bonds = []
	output = ""

	def addInput(self, filename):
		self.input_files.append(filename)
	
	def addBond(self, type1, type2, distance):
		self.bonds.append([type1, type2, distance])
	
	def addOutput(self, output):
		self.output = output
	
	def getInputFiles(self):
		return self.input_files

	def getBonds(self):
		return self.bonds

	def getInputType(self, filenumber):
		return self.input_files[filenumber].split('.')[1]

	def getOutputType(self):
		return self.output
