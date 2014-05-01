#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Tests for OpenPNM """

from __future__ import print_function, division, absolute_import
import pytest

import OpenPNM
import numpy as np

def test_template_generator():
    R = np.array([[[0,0],[0,1]]])
    pn = OpenPNM.Network.Template(name='template')
    pn.generate(R)
    pn.prune(R>0.5)
    assert len(pn.get_pore_data(prop='coords'))==3
    assert len(pn.get_throat_data(prop='connections'))==2

def test_linear_solver():
    # fix cube dimensions?
    pn = OpenPNM.Network.Cubic(name='net')
    pn.generate(add_boundaries=False)

    x,y,z = pn.get_pore_data(prop='coords').T
    left = x==x.min()
    right = x==x.max()
    ics = 2*left + 1*right

    sol = OpenPNM.Shortcuts.solve_linear(pn, ics)
    assert( np.allclose(sol, np.array([2,1.5,1]*9)) )

if __name__ == '__main__':
    pytest.main([__file__])