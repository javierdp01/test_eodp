
# MAIN FUNCTION TO CALL THE ISM MODULE

from ism.src.ism import ism

# Directory - this is the common directory for the execution of the E2E, all modules
auxdir = r'C:\\Users\javie\Desktop\EODP\test_eodp\auxiliary'
indir = r"C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\input\gradient_alt100_act150" # small scene
outdir = r"C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\myoutputs"

# Initialise the ISM
myIsm = ism(auxdir, indir, outdir)
myIsm.processModule()
