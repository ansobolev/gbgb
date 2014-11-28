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

try:
    from enthought.mayavi import mlab
except ImportError:
    from mayavi import mlab


class Visual(object):
    """
    Generic class for visualizers
    """
    def __init__(self):
        pass

    @staticmethod
    def show():
        mlab.show()


class AtomsVisual(Visual):
    """ Visualization of atoms by their Cartesian coordinates
    """

    def __init__(self, crd):
        super(AtomsVisual, self).__init__()
        mlab.points3d(crd[:, 0], crd[:, 1], crd[:, 2])

    @staticmethod
    def add_atoms(crd, color):
        mlab.points3d(crd[:, 0], crd[:, 1], crd[:, 2], color=color)
