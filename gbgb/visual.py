# ---------------------------------------------
#
# The file visual is part of the gbgb project.  
# Copyright (c) 2014 Andrey Sobolev  
# License GNU GPL v.2
# See http://github.com/ansobolev/gbgb for details
#
# ---------------------------------------------
__author__ = 'andrey'

""" Visualization with Enthought Mayavi package
"""

import numpy as np
try:
    from enthought.mayavi import mlab
except ImportError:
    from mayavi import mlab


class Visual(object):
    """
    Generic class for visualizers
    """
    _sources = {}

    def __init__(self):
        pass

    def get_names(self):
        return self._sources.keys()

    def get_sources(self):
        return self._sources.iteritems()

    @staticmethod
    def show():
        mlab.show()


class AtomsVisual(Visual):
    """ Visualization of atoms by their Cartesian coordinates
    """

    def __init__(self, name, crd):
        super(AtomsVisual, self).__init__()
        self._sources["at_" + name] = mlab.points3d(crd[:, 0], crd[:, 1], crd[:, 2])

    def add_atoms(self, name, crd, color):
        self._sources["at_" + name] = mlab.points3d(crd[:, 0], crd[:, 1], crd[:, 2], color=color)


class VectorVisual(Visual):
    """ Vector visualization
    """

    def __init__(self, name, crd):
        super(VectorVisual, self).__init__()
        vectors = np.hstack((np.zeros_like(crd), crd))
        self._sources["v_" + name] = mlab.quiver3d(*vectors.T)

