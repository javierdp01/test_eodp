import numpy as np

from common.io.writeToa import writeToa, readToa
from matplotlib import pyplot as plt

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

# We check the absolute error
def check_band(toa_my, toa_ref, tol=0.01):
    diff = np.abs(toa_ref - toa_my) / np.maximum(toa_ref, 1e-12) * 100
    mu = np.mean(diff)
    sigma = np.std(diff)

    threshold = mu + 3*sigma

    ok = threshold < tol
    return mu, sigma, threshold, ok

mu0, sigma0, threshold0, ok0 = check_band(toa_l1b_0_output, toa_l1b_0_myoutputs, tol=0.01)
mu1, sigma1, threshold1, ok1 = check_band(toa_l1b_1_output, toa_l1b_1_myoutputs, tol=0.01)
mu2, sigma2, threshold2, ok2 = check_band(toa_l1b_2_output, toa_l1b_2_myoutputs, tol=0.01)
mu3, sigma3, threshold3, ok3 = check_band(toa_l1b_3_output, toa_l1b_3_myoutputs, tol=0.01)

print("Band 0: mean=", mu0, " std=", sigma0, " threshold=", threshold0, " ok=", ok0)
print("Band 1: mean=", mu1, " std=", sigma1, " threshold=", threshold1, " ok=", ok1)
print("Band 2: mean=", mu2, " std=", sigma2, " threshold=", threshold2, "ok=", ok2)
print("Band 3: mean=", mu3, " std=", sigma3, " threshold=", threshold3, "ok=", ok3)


# We create the different plots
# ISRF VS MYOUTPUTS
plt.plot(  toa_isrf_0[0,:], label='isrf')
plt.plot( toa_l1b_0_myoutputs[0,:], label='myoutputs')
plt.title("isrf vs myoutputs 0")
plt.legend()
plt.show()
plt.plot(  toa_isrf_1[0,:], label='isrf')
plt.plot( toa_l1b_1_myoutputs[0,:], label='myoutputs')
plt.title("isrf vs myoutputs 1")
plt.legend()
plt.show()
plt.plot(  toa_isrf_2[0,:], label='myoutputs')
plt.plot( toa_l1b_2_myoutputs[0,:], label='myoutputs')
plt.title("isrf vs myoutputs 2")
plt.legend()
plt.show()
plt.plot(  toa_isrf_3[0,:], label='isrf')
plt.plot( toa_l1b_3_myoutputs[0,:], label='myoutputs')
plt.title("isrf vs myoutputs 3")
plt.legend()
plt.show()

#MYOUTPUTS VS NO EQUALIZATION
plt.plot(  toa_l1b_0_myoutputsnoeq[0,:], label='myoutputsnoeq')
plt.plot( toa_l1b_0_myoutputs[0,:], label='myoutputs')
plt.title("myoutputs vs myoutputs_noeq 0")
plt.legend()
plt.show()
plt.plot(  toa_l1b_1_myoutputsnoeq[0,:], label='myoutputsnoeq')
plt.plot( toa_l1b_1_myoutputs[0,:], label='myoutputs')
plt.title("myoutputs vs myoutputs_noeq 1")
plt.legend()
plt.show()
plt.plot(  toa_l1b_2_myoutputsnoeq[0,:], label='myoutputsnoeq')
plt.plot( toa_l1b_2_myoutputs[0,:], label='myoutputs')
plt.title("myoutputs vs myoutputs_noeq 2")
plt.legend()
plt.show()
plt.plot(  toa_l1b_3_myoutputsnoeq[0,:], label='myoutputsnoeq')
plt.plot( toa_l1b_3_myoutputs[0,:], label='myoutputs')
plt.title("myoutputs vs myoutputs_noeq 3")
plt.legend()
plt.show()
