# parser.py: Parses various filetypes.
def parsePDB(filename):
	"""Parses a .pdb file."""
	print("Parsing file...")
	# Instantiate a list to store parsed information.
	parsed_file = []

	# Read the file into memory.
	opened_file = open(filename, 'r').readlines()
	
	# Extract name and author
	name = opened_file[0]
	author = opened_file[1]
	parsed_file.append(name)
	parsed_file.append(author)

	# Extract the coordinates
	for line in opened_file[2:]:
		if line.strip() == "END":
			print("Parsing complete.")
			break
		this_line = line.split()
		atom_index= opened_file[2:].index(line)
		atom_type = this_line[2]
		residue   = this_line[3]
		x         = float(this_line[5])
		y         = float(this_line[6])
		z         = float(this_line[7])
		particle = [atom_index, atom_type, residue, x, y, z]
		parsed_file.append(particle)
	return parsed_file
