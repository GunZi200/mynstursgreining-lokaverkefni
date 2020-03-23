
# %%
import numpy as np
import matplotlib.pyplot as plt
import pickle

# %%

batch1 = pickle.load(open(r'batch1.pkl','rb'))
batch2 = pickle.load(open(r'batch2.pkl','rb'))
batch3 = pickle.load(open(r'batch3.pkl','rb'))

# %%
# Fjöldi battería
numBat1 = len(batch1.keys())
numBat2 = len(batch2.keys())
numBat3 = len(batch3.keys())
numBat = numBat1 + numBat2 + numBat3


# sameinum skrárnar í eitt dictionary
bat_dict = {**batch1, **batch2, **batch3}
#plt.plot(bat_dict['b1c43']['summary']['V'], bat_dict['b1c43']['summary']['QD'])
# %%
"""
for i in bat_dict.keys():
    cycleNR = np.array(bat_dict[i]['summary']['cycle'], dtype='int')
    for j in cycleNR:
        try:
            y = list(bat_dict[i]['cycles'][str(j)]['V'])
        except KeyError:
            continue
        firstIndex = 0;

        for k in range(1,len(y)-1):
            if np.around(y[k],decimals = 2) == 3.60 and np.around(y[k+1],decimals = 2) == 3.59 :
                print(k)
                firstIndex = k
        bat_dict[i]['cycles'][str(j)]['V'] = y[firstIndex:]
        
        for k in range(firstIndex,len(y)-1):
            if np.around(y[k],decimals = 2) == 2.01 and np.around(y[k+1],decimals = 2) == 2 :
                print(k)
                LastIndex = k
                break

        bat_dict[i]['cycles'][str(j)]['V'] = y[firstIndex:LastIndex]
        bat_dict[i]['cycles'][str(j)]['Qd'] = bat_dict[i]['cycles'][str(j)]['Qd'][firstIndex:LastIndex]
"""
# %%


plt.plot(bat_dict['b1c43']['cycles']['100']['Qd'], bat_dict['b1c43']['cycles']['100']['V'])

# %%
arrVoltage = np.around(list(bat_dict['b1c43']['cycles']['100']['V']),decimals=2)
arrCharge = np.around(list(bat_dict['b1c43']['cycles']['100']['Qd']),decimals=2)

# %%
#highestVoltage = arrVoltage[0] # fyrsta stak í listanum
#lowestVoltage = arrVoltage[-1] # síðasta stak í listanum

# %%
chargeInterpolated = dict(bat_dict)
# %%
from scipy.interpolate import interp1d
for i in chargeInterpolated.keys():
    cycleNR = np.array(chargeInterpolated[i]['summary']['cycle'], dtype='int')
    for j in cycleNR:
        try:
            Qd = np.around(chargeInterpolated[i]['cycles'][str(j)]['Qd'],decimals=2)
            V = np.around(chargeInterpolated[i]['cycles'][str(j)]['V'],decimals=2)
            chargeInterpolated[i]['cycles'][str(j)]['Qd'] = interp1d(V,Qd,kind='nearest')
        except KeyError:
            break

# %%
#import scipy
from scipy.signal import savgol_filter 
voltage = np.linspace(2.0, 3.6, 1000)
Y = chargeInterpolated['b1c43']['cycles']['100']['Qd'](voltage)
# %%
plt.plot(voltage, Y)

# %%
