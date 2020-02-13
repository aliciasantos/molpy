@pytest.mark.parametrize(
    "molecule, com",
    [("water", [9.81833333, 7.60366667, 12.673]), ("benzene", [-1.4045, 0, 0])],
)
def test_read_xyz(molecule, com):

    mol = molpy.data.get_molecule(molecule)
    print(np.mean(mol["geometry"], axis=0))
    print(com)
    assert np.allclose(np.mean(mol["geometry"], axis=0), com)
