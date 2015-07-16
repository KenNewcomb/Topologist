Topologist
==========

Atomistic simulation has allowed scientists and engineers to model a wide variety of chemical systems. While a plethora of techniques exist, they all rely on a <a href="http://en.wikipedia.org/wiki/Force_field_(chemistry)" target="_blank">model for the interactions between and within molecules</a>.  For chemical species with a complicated intramolecular structure, this task can become tedious and error-prone.

Topologist makes this task a breeze. You simply provide it the molecular coordinate files describing your system, as well as some basic information about the connectivity. Topologist then searches the system for bonds, angles, and dihedrals, and generates the topology file for your software of choice.

Supported Formats
----------------

Topologist can currently read .pdb and .gro files, and can output .top (GROMACS topology) files. 

Usage
------

	python3 topologist.py

Topologist will look for a file named "settings" in the program directory. A sample settings file is given below:

	input water.pdb

	system Water
	bond  OW HW 0.9-1.0 0.96
	angle HW OW HW 109.5 10.4

	output top

There are several keywords that Topologist accepts:

1. **input**: This keyword specifies the path(s) of the coordinate file(s), separated by a space. Each coordinate file should define a single **molecule**, not an atom. 

2. **system**: Provide a name for the system.

3. **bond**: This keyword is followed by two bonded atom types, the bond length between them, and the force constant. You can either specify a bond length range (0.8-1.0) to search or a single value (1.5), in which case, topologist will search for any bond within 0.1 angstroms. 

4. **angle**: This keyword is followed by the three groups that particpate in a bend, the equilibrium angle, and the bending force constant.

5. **output**: This keyword specifies the type of topology to be output by the program. At present, Topologist only supports writing GROMACS (.top) files.

Development
-----------

Topologist is still in its early stages of development and is not quite ready for general use. Use at your own risk! The topologies generated at this point may contain errors. Always perform a sanity check on the generated file. 

Features to be implemented:
* Angles, dihedrals, and impropers
* Parsing atomic charges
* LAMMPS support
* Automatic bond, angle detection
* The ability to specify non-bonded parameters and system information so a "complete" topology can be generated without further user input.

Pull requests welcome!

Acknowledgements
----------------

Special thanks to <a href="https://github.com/mike5603" target="_blank">Michael Humbert</a> for his keen debugging eyes.
