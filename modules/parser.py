# parser.py: Parses various filetypes.
from classes import atom, molecule, settings

def parseSettings(file_list):
	"""Parses the input file."""
	# Make a new settings object
	setting_object = settings.Settings()

	# Read the file line by line
	for line in file_list:
		this_line = line.split()

		# If the line is blank
		if this_line == []:
			pass
		elif this_line[0] == 'input':
			filename = this_line[1]
			setting_object.addInput(filename)
		elif this_line[0] == 'bond':
			atom1 = this_line[1]
			atom2 = this_line[2]
			distance = this_line[3]
			setting_object.addBond(atom1, atom2, distance)
		elif this_line[0] == 'output':
			output = this_line[1]
			setting_object.addOutput(output)
	return setting_object

def parsePDB(filename):
	"""Parses a .pdb file."""
	# Create a new molecule object.
	new_molecule = molecule.Molecule()

	# Read the file into memory.
	opened_file = open(filename, 'r').readlines()
	
	# Find first coordinate entry.
	for line in range(0, len(opened_file)):
		# Find first HETATM keyword
		if opened_file[line].split()[0] == 'HETATM':
			firstatom = line
			break

	# Extract the coordinates
	for line in opened_file[firstatom:]:
		# If you reach the end of a PDB file via an END statement
		if line.strip() == "END":
			print("Parsing complete.")
			return new_molecule
		# Split the line into its various data
		this_line = line.split()
		# Set the index, x, y, and z for atom; set the residue type for the molecule
		index     = opened_file[firstatom-1:].index(line)
		atomtype  = this_line[2]
		new_molecule.setResidue(this_line[3])
		x         = float(this_line[5])
		y         = float(this_line[6])
		z         = float(this_line[7])
		particle = atom.Atom(index, atomtype, x, y, z)
		new_molecule.addAtom(particle)
	print("Parsing complete.")
	return new_molecule

def parseGRO(filename):
	"""Parses a .gro file."""
	print("Cannot parse .gro files yet.")
	exit()
