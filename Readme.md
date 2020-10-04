vaspsub Dope_GaN_32/minimization -n 16 -t 24
cp Dope_GaN_32/minimization/CONTCAR Dope_GaN_32/bandgap/POSCAR 
vaspsub Dope_GaN_32/bandgap -n 16 -t 24
I think then we copied the CHGCAR into the non-self consistent bandgap2/3
vaspsub Dope_GaN_32/bandgap3 -n 16 -t 24
Basically the DOSCAR is the DOS calculation (overlapped)
