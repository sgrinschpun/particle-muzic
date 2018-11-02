import pytest
import math

@pytest.mark.parametrize("part, momentum",[
("pi+", 1.0),
("pi0", 0.5),
("pi-", 3.0)])
def test_conservation(conservation, part, momentum, resolution):
    for attr in ['E', 'charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
