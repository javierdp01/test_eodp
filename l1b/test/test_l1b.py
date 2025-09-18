from common.io.writeToa import writeToa, readToa
from matplotlib import pyplot as plt

# plot the isrf vs l1b

# We load the isrf files
toa_isrf_0 = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\output", "ism_toa_isrf_VNIR-0.nc")
toa_isrf_1 = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\output", "ism_toa_isrf_VNIR-1.nc")
toa_isrf_2 = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\output", "ism_toa_isrf_VNIR-2.nc")
toa_isrf_3 = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\output", "ism_toa_isrf_VNIR-3.nc")

# We load the l1b files from myoutputs
toa_l1b_0_myoutputs = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-L1B\myoutputs", "l1b_toa_VNIR-0.nc")
toa_l1b_1_myoutputs = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-L1B\myoutputs", "l1b_toa_VNIR-1.nc")
toa_l1b_2_myoutputs = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-L1B\myoutputs", "l1b_toa_VNIR-2.nc")
toa_l1b_3_myoutputs = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-L1B\myoutputs",  "l1b_toa_VNIR-3.nc")

# We load the l1b files from outputs
toa_l1b_0_output = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-L1B\output", "l1b_toa_VNIR-0.nc")
toa_l1b_1_output = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-L1B\output", "l1b_toa_VNIR-1.nc")
toa_l1b_2_output = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-L1B\output", "l1b_toa_VNIR-2.nc")
toa_l1b_3_output = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-L1B\output",  "l1b_toa_VNIR-3.nc")

# We load the l1b files from myoutputs_noeq
toa_l1b_0_myoutputsnoeq = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-L1B\myoutputs_noeq", "l1b_toa_VNIR-0.nc")
toa_l1b_1_myoutputsnoeq = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-L1B\myoutputs_noeq", "l1b_toa_VNIR-1.nc")
toa_l1b_2_myoutputsnoeq = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-L1B\myoutputs_noeq", "l1b_toa_VNIR-2.nc")
toa_l1b_3_myoutputsnoeq = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-L1B\myoutputs_noeq",  "l1b_toa_VNIR-3.nc")

# We create the different plots


