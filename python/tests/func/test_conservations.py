import pytest
import math

test_particles = [
("mu-", 2.0),
("pi+",2.0),
("K-", 2.0),
("K+",2.0),
("e-",2.0),
("e+",2.0),
("gamma",2.0)]

@pytest.mark.parametrize("part, momentum",test_particles)
def test_conservation(conservation, print_particle, particle, part, momentum, resolution):
    print_particle
    for attr in ['Pt', 'E','charge', 'baryonnumber', 'leptonnumber']:
        assert round(getattr(conservation.In,attr),resolution) == round(getattr(conservation.Out,attr), resolution)
