### topologist.py: Build a molecular topology file from a coordinate file.
import sys
from modules import parser, processor, generator
from classes import topology as top
import time

def logo():
	print("""
            -------------------------------------------------
             ______                  __            _      __ 
	    /_  __/___  ____  ____  / /___  ____ _(_)____/ /_
	     / / / __ \/ __ \/ __ \/ / __ \/ __ `/ / ___/ __/
	    / / / /_/ / /_/ / /_/ / / /_/ / /_/ / (__  ) /_  
	   /_/  \____/ .___/\____/_/\____/\__, /_/____/\__/  
	             /_/                  /____/              
	   --------------------------------------------------
	   Generating complex chemical topologies since 2015.\n""")

# Users gotta see the logo :)
logo()
time.sleep(2)

# Check for settings file
try:
	settings_file = open('settings', 'r').readlines()
	settings = parser.parseSettings(settings_file)
except FileNotFoundError:
	print("No input file found! See program documentation.")
	exit()

input_files = settings.getInputFiles()
topology = top.Topology()

# Loop over molecules to process
for input_file in range(0, len(input_files)):
	input_extension = settings.getInputType(input_file)
	output_extension = settings.getOutputType()

	# Call appropriate input parser
	if input_extension == 'pdb':
		print("Protein DataBank (.pdb) file detected.")
		new_molecule = parser.parsePDB(input_files[input_file])
		topology.addMolecule(new_molecule)

	elif input_extension == 'gro':
		print("GROMACS Coordinate File (.gro) file detected.")
		parser.parseGRO(input_file)
	else:
		print("File extension not supported.")
		exit()

# Process topology
processor.findAtomicDistances(topology)
processor.findBonds(topology)

# Call appropriate output generator
if output_extension == 'top':
	print("Generating GROMACS topology file (.top).")
	defaults = generator.GROMACSDefaults()
	atoms = generator.GROMACSAtoms(topology.getAtoms())
	generator.GROMACSBonds(topology.getBonds())
	generator.GROMACSAngles()
	generator.writeTopology()
