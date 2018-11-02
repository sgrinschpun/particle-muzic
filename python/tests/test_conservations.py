import pytest
import math

@pytest.mark.parametrize("part, momentum",[
("pi-", 3.0)])
def test_conservation(conservation, part, momentum, resolution):
    for attr in ['E','Pt','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
