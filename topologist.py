### topologist.py: Build a molecular topology file from a coordinate file.
## Your life is about to get a whole lot easier. ##
import sys
from modules import parser, processor, generator

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

# Check input/output file type
input_file = sys.argv[1]
inputs = input_file.split('.')
input_filename = inputs[0]
input_extension = inputs[1]

output_file = sys.argv[2]
outputs = output_file.split('.')
output_filename = outputs[0]
output_extension = outputs[1]

# Call appropriate parser
if input_extension == 'pdb':
	print("Protein DataBank (.pdb) file detected.")
	atom_list = parser.parsePDB(input_file)
	distances = processor.findAtomicDistances(atom_list)
	bonds = processor.findBonds(atom_list, distances)
	
elif input_extension == 'gro':
	print("GROMOS Coordinate File (.gro) file detected.")
	parser.parseGRO(input_file)
else:
	print("File extension not supported.")
	usage()

# Call appropriate generator
if output_extension == 'top':
	print("Generating GROMACS topology file (.top).")
	generator.GROMACSBonds(bonds)
	generator.GROMACSAngles()
