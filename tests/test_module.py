# test_module.py: A testing class for Topologist
import unittest
from modules import parser, processor, generator
from classes import atom

## Test Molecule: Water ##
# Build atom list
atom_list = []
oxygen = atom.Atom(0, "OW", "HOH", 0.000, 0.000, 0.000)
hydrogen1 = atom.Atom(1, "H1", "HOH", 0.577, 0.816, 0.000)
hydrogen2 = atom.Atom(2, "H2", "HOH", 0.577, -0.816, 0.000)
atom_list.append(oxygen)
atom_list.append(hydrogen1)
atom_list.append(hydrogen2)

# Make distance object
distances = []
distances.append([0, 1, 0.998])
distances.append([0, 2, 0.998])
distances.append([1, 2, 1.632])

class TestModule(unittest.TestCase):
	def test_parsePDB(self):	
		parsed_pdb = parser.parsePDB('water.pdb')
		for atom in range(0, len(parsed_pdb)):
			self.assertEqual(parsed_pdb[atom].x, atom_list[atom].x) 
	
	def test_findAtomicDistances(self):
		atomic_distances = processor.findAtomicDistances(atom_list)
		for dist in range(0, len(atomic_distances)):	
			self.assertAlmostEqual(atomic_distances[dist][0], distances[dist][0], 2)
			self.assertAlmostEqual(atomic_distances[dist][1], distances[dist][1], 2)
			self.assertAlmostEqual(atomic_distances[dist][2], distances[dist][2], 2)

if __name__ == '__main__':
	unittest.main()
