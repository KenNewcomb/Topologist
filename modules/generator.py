# Generator.py: Generates the [bonds] and [angles] section of a GROMACS topology file.
output_file = []

def GROMACSDefaults():
	"""Generates the [ defaults ]"""
	global output_file
	output_file.append("[ defaults ]")
	output_file.append(";\tnbfunc\tcomb-rule\tgen-pairs\tfudgeLJ\tfudgeQQ")
	output_file.append("\t{0}\t{1}\t{2}\t{3}\t{4}".format(1,2,'no',1,1))
	output_file.append("")

def GROMACSAtomtypes(atomtypes, settings):
	global output_file
	output_file.append("[ atomtypes ]")
	output_file.append(";\tname\tAt.Num.\tmass\tcharge\tptype\tsigma\tepsil")
	for atomtype in atomtypes:
		atom_info = settings.getAtomInfo(atomtype)
		output_file.append("\t{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}".format(atomtype, atom_info[1], atom_info[2], atom_info[3], "A", atom_info[4], atom_info[5]))
	output_file.append("")
	pass

def GROMACSAtoms(molecule, settings):
	global output_file
	output_file.append("[ atoms ]")
	output_file.append(";\tid\ttype\tresnr\tresidue\t\tatom\tcgnr\tcharge\tmass")
	for atom in molecule.getAtoms():
		output_file.append("\t{0}\t{1}\t{2}\t{3}\t\t{4}\t{5}\t{6}\t{7}".format(atom.getIndex(), atom.getAtomType(), 1, molecule.getResidue(), atom.getAtomType(),1, settings.getAtomInfo(atom.getAtomType())[3], settings.getAtomInfo(atom.getAtomType())[2] ))
	output_file.append("")

def GROMACSNonbonded(atomtypes, settings):
	global output_file
	output_file.append("[ nonbond_params ]")
	output_file.append(";\ti\tj\tfunc\tsigma\teps(c12)kJ/mol")
	for atomtype1 in range(0, len(atomtypes)-1):
		for atomtype2 in range(atomtype1, len(atomtypes)):
			if atomtype1 != atomtype2:
				if settings.mix == True:
					sigma = (settings.getSigma(atomtypes[atomtype1])+settings.getSigma(atomtypes[atomtype2]))/2
					epsilon = (settings.getEpsilon(atomtypes[atomtype1])*settings.getEpsilon(atomtypes[atomtype2]))**(1/2)
					output_file.append("\t{0}\t{1}\t{2}\t{3:.3f}\t{4:.3f}".format(atomtypes[atomtype1], atomtypes[atomtype2], 1, sigma, epsilon ))
				else:
					output_file.append("\t{0}\t{1}".format(atomtypes[atomtype1], atomtypes[atomtype2]))
	output_file.append("")

def GROMACSBonds(bonds, settings):
	global output_file
	if bonds == []:
		return
	output_file.append("[ bonds ]")
	output_file.append(";\ti\tj\tfunc\tlength\t\tforce.c")
	for bond in bonds:
		output_file.append("\t{0}\t{1}\t{2}\t{3}\t\t{4}".format(bond.atom1.index, bond.atom2.index, 1, settings.getBondLength(bond.atom1, bond.atom2), settings.getForceConstant(bond.atom1, bond.atom2)))
	output_file.append("")
	
def GROMACSAngles(angles, settings):
	global output_file
	if angles == []:
		return
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

def GROMACSMoleculetype(molecule, settings):
	global output_file
	output_file.append("[ moleculetype ]")
	output_file.append(";\tmolname\tnrexcl")
	output_file.append("\t{0}\t{1}".format(molecule.getResidue(), settings.getMoleculeInfo(molecule.getResidue())[2]))
	output_file.append("")

def GROMACSMolecules(topology, settings):
	output_file.append("[ molecules ]")
	output_file.append(";\tresidue\tnmol")
	for molecule in topology.getMolecules():
		output_file.append("\t{0}\t{1}".format(molecule.getResidue(), settings.getMoleculeInfo(molecule.getResidue())[1]))
	output_file.append("")

def writeVMDBonds(topology):
        vmd_bonds = open('bonds', 'w')
        vmds = []
        for molecule in topology.getMolecules():
                vmds.append("# MOLECULE {0}".format(molecule.getResidue()))
                for bond in molecule.getBonds():
                        vmds.append("topo addbond {0} {1}".format(bond.atom1.index-1, bond.atom2.index-1))

        for vmd in vmds:
                vmd_bonds.write(vmd + "\n")


def writeTopology():
	global output_file
	topology = open('output', 'w')

	for line in output_file:
		topology.write(line + "\n")

	print("Topology successfully written to ./output .\n")
	topology.close()
