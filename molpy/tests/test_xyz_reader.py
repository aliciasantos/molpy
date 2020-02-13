import numpy as np
import pytest
import molpy


@pytest.mark.parametrize(
    "point1, point2, bench",
    [([0, 1], [0,0], 1), ([0, 2], [0,0], 2), ([2.236, 2.236], [0, 0], 3.162)],
)
def test_distance(point1, point2, bench):
    assert molpy.util.distance(point1, point2) == pytest.approx(bench, abs=1.0e-3)

def test_distance_failure():
    assert molpy.util.distance([0], [3]) != 5



@pytest.mark.parametrize(
    "molecule, com",
    [("water", [9.81833333, 7.60366667, 12.673]), ("benzene", [-1.4045, 0, 0])],
)
def test_read_xyz(molecule, com):

    mol = molpy.data.get_molecule(molecule)
    print(np.mean(mol["geometry"], axis=0))
    print(com)
    assert np.allclose(np.mean(mol["geometry"], axis=0), com)



#@pytest.mark.parametrize(
#    "molecule, cog, natoms",
#    [("water", [9.81833333, 7.60366667, 12.673]), ("benzene", [-1.4045, 0, 0])],
#)
#def test_read_xyz(molecule, cog, natoms):

#    mol = molpy.data.get_molecule(molecule)
#    print(np.mean(mol["geometry"], axis=0))
#    print(com)
#    assert np.allclose(np.mean(mol["geometry"], axis=0), cog)
#    assert len(mol["geometry"]) == natoms
#    assert len(mol['symbols']) == natoms


def test_get_molecule_missing():
    with pytest.raises(FileNotFoundError): #makes sure the file is closed when with ends
        mol = molpy.data.get_molecule("non-existant")
