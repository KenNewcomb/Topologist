# Generator.py: Generates the [bonds] and [angles] section of a GROMACS topology file.
output_file = []

def GROMACSDefaults():
	"""Generates the [ defaults ]"""
	global output_file
	output_file.append("[ defaults ]")
	output_file.append(";\tnbfunc\tcomb-rule\tgen-pairs\tfudgeLJ\tfudgeQQ")
	output_file.append("\t{0}\t{1}\t{2}\t{3}\t{4}".format(1,2,'no',1,1))
	output_file.append("")

def GROMACSAtomtypes(atomtypes):
	global output_file
	output_file.append("[ atomtypes ]")
	output_file.append(";\tname\tatomic_num\tmass\tcharge\tptype\tsigma\tepsil")
	for atomtype in atomtypes:
		output_file.append("\t{0}".format(atomtype))
	output_file.append("")
	pass

def GROMACSAtoms(molecule):
	global output_file
	output_file.append("[ atoms ]")
	output_file.append("\tid\ttype\tresnr\tresidue\t\tatom\tcgnr\tcharge\tmass")
	for atom in molecule.getAtoms():
		output_file.append("\t{0}\t{1}\t{2}\t{3}\t\t{4}\t{5}".format(atom.getIndex(), atom.getAtomType(), 1, molecule.getResidue(), atom.getAtomName(),1))
	output_file.append("")

def GROMACSNonbonded(atomtypes):
	global output_file
	output_file.append("[ nonbond_params ]")
	output_file.append(";\ti\tj\tfunc\tsigma\teps(c12)kJ/mol")
	for atomtype1 in range(0, len(atomtypes)-1):
		for atomtype2 in range(atomtype1, len(atomtypes)):
			if atomtype1 != atomtype2:
				output_file.append("\t{0}\t{1}".format(atomtypes[atomtype1], atomtypes[atomtype2]))
	output_file.append("")

def GROMACSBonds(bonds, settings):
	global output_file
	output_file.append("[ bonds ]")
	output_file.append(";\ti\tj\tfunc\tlength\t\tforce.c")
	for bond in bonds:
		output_file.append("\t{0}\t{1}\t{2}\t{3}\t\t{4}".format(bond.atom1.index, bond.atom2.index, 1, settings.getBondLength(bond.atom1, bond.atom2), settings.getForceConstant(bond.atom1, bond.atom2)))
	output_file.append("")
	
def GROMACSAngles(angles, settings):
	global output_file
	output_file.append("[ angles ]")
	output_file.append(";\ti\tj\tk\tfunc\tangle\tforce.c")
	for angle in angles:
		output_file.append("\t{0}\t{1}\t{2}\t{3}\t{4}\t{5}".format(angle.atom1.index, angle.atom2.index, angle.atom3.index, 1, settings.getAngle(angle.atom1, angle.atom2, angle.atom3), settings.getAngleConstant(angle.atom1, angle.atom2, angle.atom3)))
	output_file.append("")

def GROMACSSystem(settings):
	global output_file
	output_file.append("[ system ]")
	output_file.append(settings.getSystem())
	output_file.append("")

def GROMACSMoleculetype(molecule):
	global output_file
	output_file.append("[ moleculetype ]")
	output_file.append(";\tmolname\tnrexcl")
	output_file.append("\t{0}".format(molecule.getResidue()))
	output_file.append("")

def GROMACSMolecules(topology):
	output_file.append("[ molecules ]")
	for molecule in topology.getMolecules():
		output_file.append(molecule.getResidue())
	output_file.append("")

def writeTopology():
	global output_file
	topology = open('output', 'w')

	for line in output_file:
		topology.write(line + "\n")

	print("Topology successfully written to ./output .\n")
	topology.close()
