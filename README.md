Topologist
==========

Computer simulation has allowed scientists and engineers to model a wide variety of chemical and physical systems. A plethora of techniques exist, ranging from highly accurate, but computationally expensive quantum mechanical methods to cheaper methods. Regardless of the technique/software used, the <a href="http://en.wikipedia.org/wiki/Topology_(chemistry)" target="_blank">chemical topology</a>
 of the system must be completely described.  For species with a complicated chemical structure, this task can be tedious and error-prone.

Topologist makes this task a breeze. You simply provide it the molecular coordinate files describing your system, as well as some basic information about the bonding. Then, Topologist generates the topology for your software of choice. Your life is about to get a whole lot simpler.

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

There are several keywords that Topologist accepts. The **input** keyword specifies the coordinate files to process. The **bond** keyword is followed by the two groups to search for, and the bond length (in Angstroms). If a range is given, Topologist will search within that range; if not, it assumes a 0.1 Angstrom tolerance. Finally, the **output** keyword specifies the type of topology desired. 
