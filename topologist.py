### topologist.py: Build a GROMACS topology file (.top) from a coordinate file (.pdb)
## Your life is about to get a whole lot easier. ##
import sys
import parser
import processor
import generator

def usage():
	print("Usage: python3 build.py input.gro")

def logo():
	print("""
            --------------------------------------------------
             ______                  __            _      __ 
	    /_  __/___  ____  ____  / /___  ____ _(_)____/ /_
	     / / / __ \/ __ \/ __ \/ / __ \/ __ `/ / ___/ __/
	    / / / /_/ / /_/ / /_/ / / /_/ / /_/ / (__  ) /_  
	   /_/  \____/ .___/\____/_/\____/\__, /_/____/\__/  
	             /_/                  /____/              
	   ---------------------------------------------------\n""")
logo()

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
	parsed_file = parser.parsePDB(full_file)
	distances = processor.findAtomicDistances(parsed_file[2:])
	processor.findBonds(parsed_file[2:], distances)
	
elif extension == 'gro':
	print("Gromos Coordinate File (.gro) file detected.")
	parser.parseGRO(full_file)
else:
	print("File extension not found.")
