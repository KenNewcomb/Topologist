### topologist.py: Build a molecular topology file from a coordinate file.
import sys
from modules import parser, processor, generator
from classes import topology as top

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
	      Developed by the Maginn Group at Notre Dame.\n""")

logo()

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
		new_molecule = parser.parsePDB(input_files[input_file])
		topology.addMolecule(new_molecule)
	elif input_extension == 'gro':
		parser.parseGRO(input_file)
	else:
		print("File extension not supported.")
		exit()

# Process topology
topology = processor.findAtomicDistances(topology)
topology = processor.findBonds(topology, settings)
topology = processor.findAngles(topology, settings)

# Call appropriate output generator
if output_extension == 'top':
	generator.GROMACSDefaults()
	generator.GROMACSAtomtypes(topology.getAtomTypes(), settings)
	generator.GROMACSNonbonded(topology.getAtomTypes())
	for molecule in topology.getMolecules():
		generator.GROMACSMoleculetype(molecule)
		generator.GROMACSAtoms(molecule)
		generator.GROMACSBonds(molecule.getBonds(), settings)
		generator.GROMACSAngles(molecule.getAngles(), settings)
	generator.GROMACSSystem(settings)
	generator.GROMACSMolecules(topology)
	generator.writeTopology()
