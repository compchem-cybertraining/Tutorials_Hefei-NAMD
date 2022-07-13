#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ase.io import read, write
from ase.build.supercells import make_supercell

M = [[3, 0, 0], [3, 6, 0], [0, 0, 1]]
pri_cell = read('unit_cell.vasp')
sup_cell = make_supercell(pri_cell, M)
sup_cell.center(vacuum=10, axis=2)

write('supercell.vasp', sup_cell, vasp5=True, sort=True, direct=True)

