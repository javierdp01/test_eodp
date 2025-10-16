import numpy as np

from common.io.writeToa import writeToa, readToa
from config.ismConfig import ismConfig

# We load the isrf files
toa_isrf_0 = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\output", "ism_toa_isrf_VNIR-0.nc")
toa_isrf_1 = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\output", "ism_toa_isrf_VNIR-1.nc")
toa_isrf_2 = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\output", "ism_toa_isrf_VNIR-2.nc")
toa_isrf_3 = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\output", "ism_toa_isrf_VNIR-3.nc")

# We load the isrf files from myoutputs
toa_isrf_0_myoutputs = readToa("C:\\Users\\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\myoutputs", "ism_toa_isrf_VNIR-0.nc")
toa_isrf_1_myoutputs = readToa("C:\\Users\\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\myoutputs", "ism_toa_isrf_VNIR-1.nc")
toa_isrf_2_myoutputs = readToa("C:\\Users\\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\myoutputs", "ism_toa_isrf_VNIR-2.nc")
toa_isrf_3_myoutputs = readToa("C:\\Users\\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\myoutputs",  "ism_toa_isrf_VNIR-3.nc")

# We load the ism optical files from myoutputs
toa_ism_optical_0_myoutputs = readToa("C:\\Users\\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\myoutputs", "ism_toa_optical_VNIR-0.nc")
toa_ism_optical_1_myoutputs = readToa("C:\\Users\\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\myoutputs", "ism_toa_optical_VNIR-1.nc")
toa_ism_optical_2_myoutputs = readToa("C:\\Users\\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\myoutputs", "ism_toa_optical_VNIR-2.nc")
toa_ism_optical_3_myoutputs = readToa("C:\\Users\\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\myoutputs", "ism_toa_optical_VNIR-3.nc")

# We load the ism optical files from outputs
toa_ism_optical_0 = readToa("C:\\Users\\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\output", "ism_toa_optical_VNIR-0.nc")
toa_ism_optical_1 = readToa("C:\\Users\\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\output", "ism_toa_optical_VNIR-1.nc")
toa_ism_optical_2 = readToa("C:\\Users\\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\output", "ism_toa_optical_VNIR-2.nc")
toa_ism_optical_3 = readToa("C:\\Users\\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\output", "ism_toa_optical_VNIR-3.nc")


# We load the ism files from myoutputs
toa_ism_0_myoutputs = readToa("C:\\Users\\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\myoutputs", "ism_toa_VNIR-0.nc")
toa_ism_1_myoutputs = readToa("C:\\Users\\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\myoutputs", "ism_toa_VNIR-1.nc")
toa_ism_2_myoutputs = readToa("C:\\Users\\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\myoutputs", "ism_toa_VNIR-2.nc")
toa_ism_3_myoutputs = readToa("C:\\Users\\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\myoutputs", "ism_toa_VNIR-3.nc")

# We load the ism files
toa_ism_0 = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\output", "ism_toa_VNIR-0.nc")
toa_ism_1 = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\output", "ism_toa_VNIR-1.nc")
toa_ism_2 = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\output", "ism_toa_VNIR-2.nc")
toa_ism_3 = readToa("C:\\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-ISM\output", "ism_toa_VNIR-3.nc")

# We check the absolute error of the isrf files
def check_band(toa_my, toa_ref, tol=0.01):
    diff = np.abs(toa_ref - toa_my) / np.maximum(toa_ref, 1e-12) * 100
    mu = np.mean(diff)
    sigma = np.std(diff)

    threshold = mu + 3*sigma

    ok = threshold < tol
    return mu, sigma, threshold, ok

mu0, sigma0, threshold0, ok0 = check_band(toa_isrf_0, toa_isrf_0_myoutputs, tol=0.01)
mu1, sigma1, threshold1, ok1 = check_band(toa_isrf_1, toa_isrf_1_myoutputs, tol=0.01)
mu2, sigma2, threshold2, ok2 = check_band(toa_isrf_2, toa_isrf_2_myoutputs, tol=0.01)
mu3, sigma3, threshold3, ok3 = check_band(toa_isrf_3, toa_isrf_3_myoutputs, tol=0.01)

print("We check the isrf files:")
print("Band 0: mean =", mu0, " std =", sigma0, " threshold =", threshold0, " ok =", ok0)
print("Band 1: mean =", mu1, " std =", sigma1, " threshold =", threshold1, " ok =", ok1)
print("Band 2: mean =", mu2, " std =", sigma2, " threshold =", threshold2, "ok =", ok2)
print("Band 3: mean =", mu3, " std =", sigma3, " threshold =", threshold3, "ok =", ok3)

# We check the absolute error of the ism optical files
mu0, sigma0, threshold0, ok0 = check_band(toa_ism_optical_0, toa_ism_optical_0_myoutputs, tol=0.01)
mu1, sigma1, threshold1, ok1 = check_band(toa_ism_optical_1, toa_ism_optical_1_myoutputs, tol=0.01)
mu2, sigma2, threshold2, ok2 = check_band(toa_ism_optical_2, toa_ism_optical_2_myoutputs, tol=0.01)
mu3, sigma3, threshold3, ok3 = check_band(toa_ism_optical_3, toa_ism_optical_3_myoutputs, tol=0.01)

print("We check the ism optical files")
print("Band 0: mean =", mu0, " std =", sigma0, " threshold =", threshold0, " ok =", ok0)
print("Band 1: mean =", mu1, " std =", sigma1, " threshold =", threshold1, " ok =", ok1)
print("Band 2: mean =", mu2, " std =", sigma2, " threshold =", threshold2, "ok =", ok2)
print("Band 3: mean =", mu3, " std =", sigma3, " threshold =", threshold3, "ok =", ok3)

# Plot System MTF. Report the MTF at Nyquist frequency


# We check the absolute error of the ism files
mu0, sigma0, threshold0, ok0 = check_band(toa_ism_0, toa_ism_0_myoutputs, tol=0.01)
mu1, sigma1, threshold1, ok1 = check_band(toa_ism_1, toa_ism_1_myoutputs, tol=0.01)
mu2, sigma2, threshold2, ok2 = check_band(toa_ism_2, toa_ism_2_myoutputs, tol=0.01)
mu3, sigma3, threshold3, ok3 = check_band(toa_ism_3, toa_ism_3_myoutputs, tol=0.01)

print("We check the ism files:")
print("Band 0: mean =", mu0, " std =", sigma0, " threshold =", threshold0, " ok =", ok0)
print("Band 1: mean =", mu1, " std =", sigma1, " threshold =", threshold1, " ok =", ok1)
print("Band 2: mean =", mu2, " std =", sigma2, " threshold =", threshold2, "ok =", ok2)
print("Band 3: mean =", mu3, " std =", sigma3, " threshold =", threshold3, "ok =", ok3)

# Saturated pixels
def saturated_pixels(toa):
    number_pixels = 0
    config = ismConfig()
    max_value = 2 ** config.bit_depth - 1
    for i in range(toa.shape[0]):
        for j in range(toa.shape[1]):
            if (toa[i, j] == max_value):
                number_pixels += 1

    percentage = number_pixels / toa.size * 100
    return number_pixels,  percentage

number_pixels0, percentage_pixels0 = saturated_pixels(toa_ism_0_myoutputs)
number_pixels1, percentage_pixels1 = saturated_pixels(toa_ism_1_myoutputs)
number_pixels2, percentage_pixels2 = saturated_pixels(toa_ism_2_myoutputs)
number_pixels3, percentage_pixels3 = saturated_pixels(toa_ism_3_myoutputs)

print("We check the saturated pixels:")
print("Band 0: saturated pixels =", number_pixels0, " percentage = ", percentage_pixels0)
print("Band 1: saturated pixels =", number_pixels1, " percentage = ", percentage_pixels1)
print("Band 2: saturated pixels =", number_pixels2, " percentage = ", percentage_pixels2)
print("Band 3: saturated pixels =", number_pixels3, " percentage = ", percentage_pixels3)

indir = r'C:\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-L1C\input\gm_alt100_act_150C,C:\Users\javie\Desktop\EODP\SHARED-20250911T151756Z-1-001\SHARED\EODP_TER_2021\EODP-TS-L1C\input\l1b_output'
indir = indir.split(',')
print(indir)