import molpy
import pytest

@pytest.mark.parametrize("point1,point2,bench", [
    ([0,1],[0,0],1),
    ([0,2],[0,0],2),
    ([0,2.49999],[0,-2.49999],5),
])

def test_distance1(point1, point2, bench):
    assert molpy.util.distance(point1, point2)==pytest.approx(bench, abs=1.e-3)


def test_distance_failure():
    assert molpy.util.distance([0],[3] !=5)
