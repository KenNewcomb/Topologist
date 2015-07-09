# Build.py: Build a GROMACS topology file (.top) from a coordinate file (.pdb)
# Your life is about to get a whole lot easier.
import sys

def usage():
	print("Usage: python3 build.py input.gro")

# Check for sane input
if len(sys.argv) != 2:
	usage()

# Check for file type/extension
full_file = sys.argv[1]
file_list = full_file.split('.')
filename = file_list[0]
extension = file_list[1]

if extension == 'pdb':
	print("Protein DataBank (.pdb) file detected.")
elif extension == 'gro':
	print("Gromos Coordinate File (.gro) file detected.")
else:
	print("File extension not found.")
