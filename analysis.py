import pickle
import numpy as np
import matplotlib.pyplot as plt

with open('libros.pkl', 'rb') as f:
    libros = pickle.load(f)
    
with open('libraries.pkl', 'rb') as f:
    libraries = pickle.load(f)
    
    
tasas = np.array([l.rate for l in libraries])
tregs = np.array([l.treg for l in libraries])


formula = np.array([np.sqrt(l.rate/l.treg) for l in libraries])

plt.hist(formula, bins=100)

