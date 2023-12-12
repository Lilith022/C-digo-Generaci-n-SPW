'''Codigo realizado en grupo por
Ramon Sarmiento
Cristian Rugeles'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal

f = 2400  # Frecuencia senal triangular
t = np.arange(0, 0.0166667, 1 / (f * 50))  # Vector de tiempos
sinwave = np.sin(377 * t)*0.98  # Seno y -Seno a 60Hz
minsin = -sinwave

triangular_wave = 1 * signal.sawtooth(2 * np.pi * f * t, width=0.5)  # Creacion de senal triangular

Vq1 = (sinwave > triangular_wave) * 5  # Obtencion de pulsos Q1
Vq4 = (minsin < triangular_wave) * 5  # Obtencion de pulsos Q4
Vq2 = (minsin > triangular_wave) * 5  # Obtencion de pulsos Q2
Vq3 = (sinwave < triangular_wave) * 5  # Obtencion de pulsos Q3
plt.figure(1)

plt.subplot(4,1,1)
plt.plot(t, Vq1)
plt.title('Vq1')

plt.subplot(4,1,2)

plt.plot(t, Vq4)
plt.title('Vq4')

plt.subplot(4,1,3)

plt.plot(t, Vq2)
plt.title('Vq2')

plt.subplot(4,1,4)
plt.plot(t, Vq3)
plt.title('Vq3')

plt.subplots_adjust(left=0.125, bottom=0.1, right=0.9, top=1, wspace=0.2, hspace=1)
pq1 = Vq1.astype(int)
pq4 = Vq4.astype(int)
pq2 = Vq2.astype(int)
pq3 = Vq3.astype(int)

data = {'t': t, 'Vq1': pq1}
df = pd.DataFrame(data)
df.to_csv('5VPQ1.tsv', sep='\t', index=False, header=False)  # Elimina el encabezado y utiliza '\t' como separador

data = {'t': t, 'Vq4': pq4}
df = pd.DataFrame(data)
df.to_csv('5VPQ4.tsv', sep='\t', index=False, header=False)

data = {'t': t, 'Vq2': pq2}
df = pd.DataFrame(data)
df.to_csv('5VPQ2.tsv', sep='\t', index=False, header=False)

data = {'t': t, 'Vq3': pq3}
df = pd.DataFrame(data)
df.to_csv('5VPQ3.tsv', sep='\t', index=False, header=False)

plt.show()