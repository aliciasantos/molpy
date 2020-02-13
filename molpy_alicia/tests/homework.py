import molpy
import pytest

@pytest.mark.parametrize("molecule, com", [("water", [0,0,0]), ("benzene", [0,0,0])])
def test_readers(molecule, com):
  mol = molpy.data.get_molecule(molecule)
  assert np.mean(mol["geometry"],axis=1)==com
