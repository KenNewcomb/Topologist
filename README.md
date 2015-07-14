Topologist (in development!)
==========

Atomistic simulation has allowed scientists and engineers to model a wide variety of chemical systems. While a plethora of techniques exist, they all rely on a <a href="http://en.wikipedia.org/wiki/Force_field_(chemistry)" target="_blank">model for the interactions between and within molecules</a>.  For chemical species with a complicated intramolecular structure, this task can become tedious and error-prone.

Topologist makes this task a breeze. You simply provide it the molecular coordinate files describing your system, as well as some basic information about the connectivity. Topologist then searches the coordinates for the bonds, and generates the topology file for your software of choice. Your life is about to get a whole lot simpler!

Supported Formats
----------------

Topologist can currently read .pdb and .gro files, and can output .top (GROMACS topology) files. 

Usage
------

	python3 topologist.py

Topologist will look for a file named "settings" in the program directory. The input file contains the filename of the molecular coordinate file and bonding information. A sample settings file is given below:

	input methanol.pdb

	bond C H 1.1
	bond C O 1.3-1.5
	bond O H 0.9

	output GROMACS

There are several keywords that Topologist accepts. The **input** keyword specifies the coordinate files to process, separated by a space. Each coordinate file should define a **molecule**, not an atom. The **bond** keyword is followed by the two groups to search for, and the bond length (in Angstroms). If a range is given, Topologist will search within that range; if not, it assumes a 0.1 Angstrom tolerance. Finally, the **output** keyword specifies the type of topology desired. In the simple example given above, a methanol data file is read, analyzed for the existence of three bonds (C-H, C-O, and O-H), and a GROMACS topology file is generated.

Note: Each coordinate file should represent one and only one molecule.
