# parser.py: Parses various filetypes.
from classes import atom, molecule, settings

def parseSettings(settings_file):
	"""Parses the input file."""
	# Make a new settings object
	setting_object = settings.Settings()

	# Read the file line by line
	for line in settings_file:
		this_line = line.split()
		if this_line == []:
			pass
		elif this_line[0] == 'input':
			for filename in this_line[1:]:
				setting_object.addInput(filename)
		elif this_line[0] == 'bond':
			atom1 = this_line[1]
			atom2 = this_line[2]
			distance = this_line[3]
			bond_length = this_line[4]
			force_constant = this_line[5]
			setting_object.addBond(atom1, atom2, distance, bond_length, force_constant)
		elif this_line[0] == 'output':
			output = this_line[1]
			setting_object.addOutput(output)
		elif this_line[0] == '#':
			pass
	return setting_object

def parsePDB(filename):
	"""Parses a .pdb file."""
	# Create a new molecule object.
	new_molecule = []
	new_molecule = molecule.Molecule(filename)

	# Read the file into memory.
	opened_file = open(filename, 'r').readlines()
	
	# Find first coordinate entry.
	for line in range(0, len(opened_file)):
		# Find first HETATM keyword
		if opened_file[line].split()[0] == 'HETATM' or opened_file[line].split()[0] == 'ATOM':
			firstatom = line
			break

	# Extract the coordinates
	for line in opened_file[firstatom:]:
		# If you reach the end of a PDB file via an END statement
		if line.strip() == "END":
			return new_molecule
		# Split the line into its various data
		this_line = line.split()
		# Set the index, x, y, and z for atom; set the residue type for the molecule
		index     = opened_file[firstatom:].index(line)+1
		atomtype  = this_line[2]
		x         = float(this_line[5])
		y         = float(this_line[6])
		z         = float(this_line[7])
		particle = atom.Atom(index, atomtype, x, y, z)
		new_molecule.addAtom(particle)
	return new_molecule

def parseGRO(filename):
	"""Parses a .gro file."""
	print("Cannot parse .gro files yet.")
	exit()
