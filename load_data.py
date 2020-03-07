
# %%
import numpy as np
import matplotlib.pyplot as plt
import pickle

batch1 = pickle.load(open(r'batch1.pkl', 'rb'))

numBat1 = len(batch1.keys())
numBat1

batch2 = pickle.load(open(r'batch2.pkl','rb'))

numBat2 = len(batch2.keys())
numBat2

batch3 = pickle.load(open(r'batch3.pkl','rb'))


numBat3 = len(batch3.keys())
numBat3

numBat = numBat1 + numBat2 + numBat3
numBat


bat_dict = {**batch1, **batch2, **batch3}


for i in bat_dict.keys():
    plt.plot(bat_dict[i]['summary']['cycle'], bat_dict[i]['summary']['QD'])
plt.xlabel('Cycle Number')
plt.ylabel('Discharge Capacity (Ah)')

# %%
