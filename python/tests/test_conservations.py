import pytest
import math

@pytest.mark.parametrize("part, momentum",[
<<<<<<< HEAD
("pi-", 2 .0),
=======
("pi-", 2.0),
>>>>>>> 6a9b0dd8083ac9463f90f74dca06441f0ba7ab2d
("pi+",2.0)])
def test_conservation(conservation, part, momentum, resolution):
    for attr in ['Pt','E','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
