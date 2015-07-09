### topologist.py: Build a molecular topology file from a coordinate file.
## Your life is about to get a whole lot easier. ##
import sys
import parser
import processor
import generator

def usage():
	"""Instruct the user how to use Topologist"""
	print("Usage: python3 build.py input.gro topol.top")
	print("Currently supported molecular coordinate formats:")
	print("\t.gro: GROMOS file format")
	print("\t.pdb: Protein DataBank file format")
	print("Currently supported molecular topology formats:")
	print("\t.top: GROMACS topology file")

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
if len(sys.argv) != 3:
	usage()
	exit()

# Check for file type/extension
full_file = sys.argv[1]
file_list = full_file.split('.')
filename = file_list[0]
extension = file_list[1]

# Call appropriate parser
if extension == 'pdb':
	print("Protein DataBank (.pdb) file detected.")
	parsed_file = parser.parsePDB(full_file)
	distances = processor.findAtomicDistances(parsed_file[2:])
	processor.findBonds(parsed_file[2:], distances)
	
elif extension == 'gro':
	print("GROMOS Coordinate File (.gro) file detected.")
	parser.parseGRO(full_file)
else:
	print("File extension not supported.")
	usage()
