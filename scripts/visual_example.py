# ---------------------------------------------
#
# The file visual_example is part of the gbgb project.
# Copyright (c) 2014 Andrey Sobolev  
# License GNU GPL v.2
# See http://github.com/ansobolev/gbgb for details
#
# ---------------------------------------------

import numpy as np
from gbgb.helpers import pc, lcm
import gbgb.visual as vis

crd = pc(3, 3, 3)
av = vis.AtomsVisual('atoms', crd)
av.add_atoms("a1", pc(2, 2, 2) + np.array([0.5, 0.5, 0.5]), color=(1, 0, 0))

miller = np.array([2, 1, 2])
xyz = lcm(*miller) / miller
plane = np.diag(xyz)

plane_vis = vis.VectorVisual('plane', plane)

vis.show()
