### topologist.py: Build a molecular topology file from a coordinate file.
import sys
from modules import parser, processor, generator

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

# Check for input file
try:
	settings_file = open('settings', 'r').readlines()
	settings = parser.parseSettings(settings_file)
except FileNotFoundError:
	print("No input file found! See program documentation.")
	exit()

# Loop over coordinate files.
input_files = settings.getInputFiles()
for input_file in input_files:
	file_number = input_files.index(input_file)
	input_extension = settings.getInputType(file_number)
	output_extension = settings.getOutputType()

	# Call appropriate input parser and processor
	if input_extension == 'pdb':
		print("Protein DataBank (.pdb) file detected.")
		atom_list = parser.parsePDB(input_file)
		distances = processor.findAtomicDistances(atom_list)
		bonds = processor.findBonds(atom_list, distances, settings.getBonds())

	elif input_extension == 'gro':
		print("GROMACS Coordinate File (.gro) file detected.")
		parser.parseGRO(input_file)
	else:
		print("File extension not supported.")
		exit()

	# Call appropriate output generator
	if output_extension == 'top':
		print("Generating GROMACS topology file (.top).")
		generator.GROMACSBonds(bonds)
		generator.GROMACSAngles()
