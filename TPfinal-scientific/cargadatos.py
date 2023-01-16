
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from io import StringIO

##leo el archivo desde mi computadora
online = True
if (online == True):
        url = requests.get('https://drive.google.com/file/d/1xS091zSODR9431r7GNJI4IYHoFRCCQCr/view?usp=sharing')
    csv_raw = StringIO(url.text)
    signals = pd.read_csv(csv_raw, delimiter=' ', names = ['timestamp','counter','eeg','attention','meditation','blinking'])
else:
    signals = pd.read_csv('C:\\Users\\natal\\OneDrive\\Nat2022\\Analisis datos\\datasets\\datos-cientificos\\eeg.dat', delimiter=' ', names = ['timestamp','counter','eeg','attention','meditation','blinking'])

##lo guarde en el proyecto
##base = pd.read_csv('TPfinal\\data\\eeg.dat', delimiter=' ', names = ['timestamp','counter','eeg','attention','meditation','blinking'])

print('Estructura de la informacion :')
print('signals')
print(signals.head())

