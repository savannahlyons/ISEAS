import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la
from scipy.integrate import odeint
from scipy.optimize import curve_fit
import math as math 
import pandas

#Reading Vega sheet from the Excel file 
LED_df = pandas.read_excel('LED_INFO.xlsx', sheet_name='Roth_Test')

#setting up array
x=np.arange(300,1000,1)
intensity = np.zeros(len(x))
intensity_profile = np.zeros((len(x),len(LED_df.index)))
#intensity_profile = [0 for x in range(len(LED_df.index))] #####need to have size of the number of wavelengths
#### want to fill with numpy arrays

#setting up values
wavelength = np.array(LED_df['Lambda'].tolist())
FWHM = np.array(LED_df['FWHM'].tolist()) 
power = np.array(LED_df['Power'].tolist())
sigma = (FWHM)/(2.355)

#Iteration for each LED
for i in range (0, len(LED_df.index)):
    intensity = ((1/(sigma[i]*np.sqrt(2*np.pi))) * (np.exp(-(((x-wavelength[i])**2)/(2*(sigma[i]**2))))))*power[i] 
    intensity_profile[:,i] = intensity

#creating the summation
summation = np.sum(intensity_profile, axis=1)

#plot intensity of first list array
fig1=plt.figure()
ax=plt.axes()
ax.plot(x,summation,'b')
ax.set_xlabel('wavelength (nm)')
ax.set_ylabel('intensity')
plt.grid()
plt.xticks(np.arange(min(x), max(x)+1, 50))
plt.yticks(np.arange(min(summation), max(summation)+50, 20))




