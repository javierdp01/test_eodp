import numpy as np

from common.io.writeToa import writeToa, readToa
from config.ismConfig import ismConfig
from auxiliary.constants import constants
from math import pi

config = ismConfig()
constants = constants()

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

# Radiance to irradiance
print("Values for the factors: Focal lenth [m] -> f = ", config.f ," Telescope pupil diameter [m] -> D ", config.D ," Optical transmittance [-] -> Tr = ", config.Tr)
factor =  config.Tr * (pi / 4) * (config.D / config.f)**2
print("Value of the conversion factor = ", factor)


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

# Conversion factors
print("Values for the factors: Ligth speed [m/s] -> c =", constants.speed_light ,", Planck constant [m2 kg / s] -> h =", constants.h_planck ,", Pixel area [m2] -> A =", config.pix_size**2, ", Integration time [s] -> T =", config.t_int)
wv = config.wv
def irradiance2photons(c, h, A, T, band):
    E_in = A * T / 1000
    E_photon = (h*c)/ wv[band]
    factor = E_in / E_photon
    return factor

irradiance2photons0 = irradiance2photons(constants.speed_light, constants.h_planck, config.pix_size**2, config.t_int, 0)
irradiance2photons1 = irradiance2photons(constants.speed_light, constants.h_planck, config.pix_size**2, config.t_int, 1)
irradiance2photons2 = irradiance2photons(constants.speed_light, constants.h_planck, config.pix_size**2, config.t_int, 2)
irradiance2photons3 = irradiance2photons(constants.speed_light, constants.h_planck, config.pix_size**2, config.t_int, 3)

print("We check the factors:")
print("Band 0: irradiance to photons =", irradiance2photons0)
print("Band 1: irradiance to photons =", irradiance2photons1)
print("Band 2: irradiance to photons =", irradiance2photons2)
print("Band 3: irradiance to photons =", irradiance2photons3)

print("Quantum efficiency [e-/ph] -> QE =", config.QE)
print("Conversion factor Photons to Electrons =", config.QE)

print("Values for the factors: Output Conversion factor [V/e-] -> OCF =", config.OCF, ", Gain of the Analog-to-digital conversion [-] -> G =" , config.ADC_gain)
E2V = config.OCF * config.ADC_gain
print("Conversion factor Electrons to Volts =", E2V)

print("Values for the factors: Minimum Voltage [V] -> Min =", config.min_voltage, ", Maximum Voltage [V] -> Max =", config.max_voltage, ", bit depth [-] -> Depth =", config.bit_depth)
V2D = (2**config.bit_depth - 1) / (config.max_voltage - config.min_voltage)
print("Conversion factor Volts to Digital =", V2D)

# Saturated pixels
def saturated_pixels(toa):
    number_pixels = 0
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
