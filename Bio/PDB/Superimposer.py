from Numeric import Float0

from Bio.SVDSuperimposer import SVDSuperimposer
from Bio.PDB.PDBExceptions import PDBException

class Superimposer:
    def __init__(self):
        self.rotran=None
        self.rms=None

    def set_atoms(self, fixed, moving):
        """
        fixed --- lost of atoms
        moving --- list of atoms

        Moving will be translated/rotated on fixed.
        """
        if not (len(fixed)==len(moving)):
            raise PDBError, "Fixed and moving atom lists differ in size"
        l=len(fixed)
        fixed_coord=zeros((l, 3), 'd')
        moving_coord=zeros((l, 3), 'd')
        for i in range(0, len(fixed)):
            fixed_coord[i]=fixed[i].get_coord()
            moving_coord[i]=moving[i].get_coord()
        sup=SVDSuperimposer()
        sup.set(fixed_coord, moving_coord)
        sup.run()
        self.rms=sup.get_rms()
        self.rotran=sup.get_rotran()

    def apply(self, atom_list):
        """
        Rotate/translate a list of atoms.
        """
        if self.rotran is None:
            raise DBNError, "No transformation has been calculated yet"
        rot, tran=self.rotran
        rot=rot.astype(Float0)
        tran=rot.astype(Float0)
        for atom in atom_list:
            atom.transform(rot, tran)


if __name__=="__main__":

    import sys
    from Numeric import *

    from Bio.PDB import *

    p=PDBParser()
    s1=p.get_structure("FIXED", sys.argv[1])
    fixed=Selection.unfold_entities(s1, "A")

    s2=p.get_structure("MOVING", sys.argv[1])
    moving=Selection.unfold_entities(s2, "A")

    rot=identity(3).astype(Float0)
    tran=array((1.0, 2.0, 3.0), Float0)

    for atom in moving:
        atom.transform(rot, tran)
    
    sup=Superimposer()

    sup.set_atoms(fixed, moving)

    print sup.rotran
    print sup.rms

    sup.apply(moving)




