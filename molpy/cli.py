import argparse
import molpy

if __name__ = '__main__':
    parser = argparse.ArgumentParser(description='''A Molecule utility that reads xyz
    files and calculates distances between atoms at index1 and index2''')
    parser.add_argument('filename', type=str, help='The xyz file to read.')
    parser.add_argument('index1', type=int, help='Index of the first atom.')
    parser.add_argument('index2', type=int, help='Index of the second atom.')
    args = parser.parse_args()

print(args)


mol = molpy.util.read_xyz(args.filename)
print(mol)