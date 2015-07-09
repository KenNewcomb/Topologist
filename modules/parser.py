# parser.py: Parses various filetypes.
def parsePDB(filename):
	"""Parses a .pdb file."""
	print("Parsing file...")
	# Instantiate a list to store parsed information.
	parsed_file = []

	# Read the file into memory.
	opened_file = open(filename, 'r').readlines()
	
	# Find first coordinate
	for line in range(0, len(opened_file)):
		if opened_file[line].split()[0] == 'HETATM':
			firstatom = line
			break

	# Extract the coordinates
	for line in opened_file[firstatom:]:
		if line.strip() == "END":
			print("Parsing complete.")
			return parsed_file
		this_line = line.split()
		atom_index= opened_file.index(line)
		atom_type = this_line[2]
		residue   = this_line[3]
		x         = float(this_line[5])
		y         = float(this_line[6])
		z         = float(this_line[7])
		particle = [atom_index, atom_type, residue, x, y, z]
		parsed_file.append(particle)
	print("Parsing complete.")
	return parsed_file
