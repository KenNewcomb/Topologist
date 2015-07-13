# parser.py: Parses various filetypes.
from classes import atom, settings

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
	print("Parsing file...")
	# Create a list to store atoms.
	atom_list = []

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
		if line.strip() == "END":
			print("Parsing complete.")
			return atom_list  
		this_line = line.split()
		index     = opened_file[firstatom-1:].index(line)
		type      = this_line[2]
		residue   = this_line[3]
		x         = float(this_line[5])
		y         = float(this_line[6])
		z         = float(this_line[7])
		particle = atom.Atom(index, type, residue, x, y, z)
		print("Created atom. Index={0}, Type={1}, Res={2}, x={3}, y={4}, z={5}".format(index, type, residue, x, y, z))
		atom_list.append(particle)
	print("Parsing complete.")
	return atom_list   
