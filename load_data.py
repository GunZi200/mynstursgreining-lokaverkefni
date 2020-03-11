
# %%
import numpy as np
import matplotlib.pyplot as plt
import pickle

# %%

batch1 = pickle.load(open(r'batch1.pkl', 'rb'))
batch2 = pickle.load(open(r'batch2.pkl','rb'))
batch3 = pickle.load(open(r'batch3.pkl','rb'))

# %%
# Fjöldi battería
numBat1 = len(batch1.keys())
numBat2 = len(batch2.keys())
numBat3 = len(batch3.keys())
numBat = numBat1 + numBat2 + numBat3


# sameinum skrárnar í einn dictionary
bat_dict = {**batch1, **batch2, **batch3}
# %%
#plt.plot(bat_dict['b1c43']['cycles']['100']['Qd'], bat_dict['b1c43']['cycles']['100']['V'])
#print(len(bat_dict['b1c43']['cycles']['100']['V']))
y = bat_dict['b1c43']['cycles']['100']['V']
print(y)

firstIndex = 0;
for i in range(1,1000) :
    #print(i, np.around(bat_dict['b1c43']['cycles']['100']['V'][i], decimals=2))
    if np.around(y[i],decimals = 2) == 3.60 and np.around(y[i+1],decimals = 2) == 3.59 :
        print(i, y[i])
        firstIndex = i

bat_dict['b1c43']['cycles']['100']['V'] = y[firstIndex:]

# %%
#print(np.around(y[651:],decimals=2))
for i in range(firstIndex,len(y)) :
    
    #print(i, np.around(bat_dict['b1c43']['cycles']['100']['V'][i], decimals=2))
    if np.around(y[i],decimals = 2) == 2.01 and np.around(y[i+1],decimals = 2) == 2 :
        print(i, y[i])
        LastIndex = i
        break
# %%

bat_dict['b1c43']['cycles']['100']['V'] = y[firstIndex:LastIndex]
bat_dict['b1c43']['cycles']['100']['Qd'] = bat_dict['b1c43']['cycles']['100']['Qd'][firstIndex:LastIndex]
plt.plot(bat_dict['b1c43']['cycles']['100']['Qd'], bat_dict['b1c43']['cycles']['100']['V'])


# %%
samples = 1000
step = (3.6-2.0)/(samples-1)
# Start = 5, Stop = 30, Step Size = 2
#x = np.arange(2.0, 3.6+step, step, dtype=float)
x = np.linspace(2,3.6,1000)
# %%
from scipy.interpolate import interp1d
for i in bat_dict.keys():
    cycleNR = np.array(bat_dict[i]['summary']['cycle'], dtype='int')
    for j in cycleNR:
        try:
            #print(bat_dict[i]['cycles'][str(j)]['V'].size)
            #print(bat_dict[i]['cycles'][str(j)]['Qd'].size)
            #bat_dict[i]['cycles'][str(j)]['T'] = interp1d(bat_dict[i]['cycles'][str(j)]['V'], bat_dict[i]['cycles'][str(j)]['T'])
            bat_dict[i]['cycles'][str(j)]['Qd'] = interp1d(np.around(bat_dict[i]['cycles'][str(j)]['V'],decimals=2), np.around(bat_dict[i]['cycles'][str(j)]['Qd'],decimals=2))
        except KeyError:
            break

# %%
import scipy
from scipy.signal import savgol_filter

def resample_by_interpolation(signal, input_fs, output_fs):
    
    scale = output_fs / input_fs
    # calculate new length of sample
    n = round(len(signal) * scale)
    print(n)

    # use linear interpolation
    # endpoint keyword means than linspace doesn't go all the way to 1.0
    # If it did, there are some off-by-one errors
    # e.g. scale=2.0, [1,2,3] should go to [1,1.5,2,2.5,3,3]
    # but with endpoint=True, we get [1,1.4,1.8,2.2,2.6,3]
    # Both are OK, but since resampling will often involve
    # exact ratios (i.e. for 44100 to 22050 or vice versa)
    # using endpoint=False gets less noise in the resampled sound
    resampled_signal = np.interp(
        np.linspace(2.0, 3.6, 1000, endpoint=False),  # where to interpret
        np.linspace(2.0, 3.6, len(signal), endpoint=False),  # known positions
        signal,  # known data points
    )
    return resampled_signal
yre_interpolation = resample_by_interpolation(bat_dict['b1c43']['cycles']['100']['Qd'](x), 1090, 1000)
#y1,x1 = scipy.signal.resample(bat_dict['b1c43']['cycles']['100']['Qd'],1000,bat_dict['b1c43']['cycles']['100']['V'])
plt.plot(x, savgol_filter(yre_interpolation, 5, 0))

# %%
