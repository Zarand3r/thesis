import pyprocar
import os, argparse, glob, random
import git
import sys

repo = git.Repo("./", search_parent_directories=True)
homedir = repo.working_dir

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='EDR')
    parser.add_argument('--directory', default="bandgap2", help='VASP output files directory')
    parser.add_argument('--BAND', dest='BAND', action='store_true')
    parser.add_argument('--DOS', dest='DOS', action='store_true')

    hparams = parser.parse_args()
    hparams.directory = f"{homedir}/Dope_GaN_32/{hparams.directory}"

    if hparams.BAND:
    	# pyprocar.bandsplot('/Users/richardbao/Research/msc/thesis/Dope_GaN_32/bandgap2/PROCAR',
		# 	outcar='/Users/richardbao/Research/msc/thesis/Dope_GaN_32/bandgap2/OUTCAR',
		# 	elimit=[-7,10],mode='plain',color='blue',
		# 	savefig="/Users/richardbao/Research/msc/thesis/Dope_GaN_32/bandgap2/visualize/bandgap_plot.png")

		# pyprocar.bandsplot('/Users/richardbao/Research/msc/thesis/Dope_GaN_32/bandgap2/PROCAR',
		# 	outcar='/Users/richardbao/Research/msc/thesis/Dope_GaN_32/bandgap2/OUTCAR', mode='parametric',
		# 	elimit=[-7,10], savefig="/Users/richardbao/Research/msc/thesis/Dope_GaN_32/bandgap2/visualize/bandgap_plot.png")

		pyprocar.bandsplot(f'{hparams.directory}/PROCAR',
			outcar=f'{hparams.directory}/OUTCAR', mode='parametric',
			elimit=[-7,10], savefig=f'{hparams.directory}/visualize/bandgap_plot.png')
    	
    if hparams.DOS:
    	pyprocar.dosplot(f'{hparams.directory}/vasprun.xml',
          mode='plain',
          elimit=[-4, 4],
          orientation='horizontal',
          labels=[r'$\uparrow$', r'$\downarrow$'],
          title=r'Total Density of States SrVO$_3$',
          savefig=f'{hparams.directory}/visualize/dos_plot.png")