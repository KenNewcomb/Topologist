# test_module.py: A testing class for Topologist
import unittest
from modules import parser, processor, generator
from classes import atom

## Test Molecule: Water
atom_list = []
# Build atom list
oxygen = atom.Atom(0, "OW", "HOH", 0.000, 0.000, 0.000)
hydrogen1 = atom.Atom(1, "H1", "HOH", 0.577, 0.816, 0.000)
hydrogen2 = atom.Atom(2, "H2", "HOH", 0.577, -0.816, 0.000)
atom_list.append(oxygen)
atom_list.append(hydrogen1)
atom_list.append(hydrogen2)
# Make distance object
distances = []
distances.append(0, 1, 1.277)
distances.append(0, 2, 1.277)

class TestModule(unittest.TestCase):
	def test_parsePDB(self):	
		self.assertEqual(parser.parsePDB(water.pdb), atom_list) 
	
	def test_findAtomicDistances(self):
		self.assertAlmostEqual(processor.findAtomicDistances(atom_list), distances)

if __name__ == '__main__':
	unittest.main()
