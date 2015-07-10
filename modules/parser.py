# parser.py: Parses various filetypes.
from classes import atom

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
		index     = opened_file.index(line)
		type      = this_line[2]
		residue   = this_line[3]
		x         = float(this_line[5])
		y         = float(this_line[6])
		z         = float(this_line[7])
		particle = atom.Atom(index, type, residue, x, y, z)
		atom_list.append(particle)
	print("Parsing complete.")
	return atom_list   
