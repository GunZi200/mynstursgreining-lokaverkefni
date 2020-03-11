# %%
import h5py
import matplotlib.pyplot as plt
import numpy as np
import pickle

# %%

matFilename2 = './Data/2017-06-30_batchdata_updated_struct_errorcorrect.mat'
f2 = h5py.File(matFilename2)

batch2 = f2['batch']

num_cells = batch2['summary'].shape[0]
bat_dict2 = {}
for i in range(num_cells):
    cl = f2[batch2['cycle_life'][i,0]].value
    policy = f2[batch2['policy_readable'][i,0]].value.tobytes()[::2].decode()
    summary_IR = np.hstack(f2[batch2['summary'][i,0]]['IR'][0,:].tolist())
    #summary_QC = np.hstack(f2[batch2['summary'][i,0]]['QCharge'][0,:].tolist())
    summary_QD = np.hstack(f2[batch2['summary'][i,0]]['QDischarge'][0,:].tolist())
    #summary_TA = np.hstack(f2[batch2['summary'][i,0]]['Tavg'][0,:].tolist())
    #summary_TM = np.hstack(f2[batch2['summary'][i,0]]['Tmin'][0,:].tolist())
    #summary_TX = np.hstack(f2[batch2['summary'][i,0]]['Tmax'][0,:].tolist())
    #summary_CT = np.hstack(f2[batch2['summary'][i,0]]['chargetime'][0,:].tolist())
    summary_CY = np.hstack(f2[batch2['summary'][i,0]]['cycle'][0,:].tolist())
    #summary = {'IR': summary_IR, 'QC': summary_QC, 'QD': summary_QD, 'Tavg':
    #            summary_TA, 'Tmin': summary_TM, 'Tmax': summary_TX, 'chargetime': summary_CT,
    #            'cycle': summary_CY}
    summary = {'IR': summary_IR, 'QD': summary_QD, 'cycle': summary_CY}
    cycles = f2[batch2['cycles'][i,0]]
    cycle_dict = {}
    for j in range(cycles['I'].shape[0]):
        #I = np.hstack((f2[cycles['I'][j,0]].value))
        #Qc = np.hstack((f2[cycles['Qc'][j,0]].value))
        Qd = np.hstack((f2[cycles['Qd'][j,0]].value))
        #Qdlin = np.hstack((f2[cycles['Qdlin'][j,0]].value))
        T = np.hstack((f2[cycles['T'][j,0]].value))
        #Tdlin = np.hstack((f2[cycles['Tdlin'][j,0]].value))
        V = np.hstack((f2[cycles['V'][j,0]].value))
        #dQdV = np.hstack((f2[cycles['discharge_dQdV'][j,0]].value))
        #t = np.hstack((f2[cycles['t'][j,0]].value))
        #cd = {'I': I, 'Qc': Qc, 'Qd': Qd, 'Qdlin': Qdlin, 'T': T, 'Tdlin': Tdlin, 'V':V, 'dQdV': dQdV, 't':t}
        cd = {'Qd': Qd, 'T': T, 'V':V}
        cycle_dict[str(j)] = cd
        
    cell_dict = {'cycle_life': cl, 'charge_policy':policy, 'summary': summary, 'cycles': cycle_dict}
    key = 'b2c' + str(i)
    bat_dict2[key]=   cell_dict
bat_dict2.keys()

matFilename1 = './Data/2017-05-12_batchdata_updated_struct_errorcorrect.mat'
f1 = h5py.File(matFilename1)

batch1 = f1['batch']

num_cells = batch1['summary'].shape[0]
bat_dict1 = {}
for i in range(num_cells):
    cl = f1[batch1['cycle_life'][i,0]].value
    policy = f1[batch1['policy_readable'][i,0]].value.tobytes()[::2].decode()
    summary_IR = np.hstack(f1[batch1['summary'][i,0]]['IR'][0,:].tolist())
    #summary_QC = np.hstack(f1[batch1['summary'][i,0]]['QCharge'][0,:].tolist())
    summary_QD = np.hstack(f1[batch1['summary'][i,0]]['QDischarge'][0,:].tolist())
    #summary_TA = np.hstack(f1[batch1['summary'][i,0]]['Tavg'][0,:].tolist())
    #summary_TM = np.hstack(f1[batch1['summary'][i,0]]['Tmin'][0,:].tolist())
    #summary_TX = np.hstack(f1[batch1['summary'][i,0]]['Tmax'][0,:].tolist())
    #summary_CT = np.hstack(f1[batch1['summary'][i,0]]['chargetime'][0,:].tolist())
    summary_CY = np.hstack(f1[batch1['summary'][i,0]]['cycle'][0,:].tolist())
    #summary = {'IR': summary_IR, 'QC': summary_QC, 'QD': summary_QD, 'Tavg':
    #            summary_TA, 'Tmin': summary_TM, 'Tmax': summary_TX, 'chargetime': summary_CT,
    #            'cycle': summary_CY}
    summary = {'IR': summary_IR, 'QD': summary_QD, 'cycle': summary_CY}
    cycles = f1[batch1['cycles'][i,0]]
    cycle_dict = {}
    for j in range(cycles['I'].shape[0]):
        #I = np.hstack((f1[cycles['I'][j,0]].value))
        #Qc = np.hstack((f1[cycles['Qc'][j,0]].value))
        Qd = np.hstack((f1[cycles['Qd'][j,0]][()]))
        #Qdlin = np.hstack((f1[cycles['Qdlin'][j,0]].value))
        T = np.hstack((f1[cycles['T'][j,0]][()]))
        #Tdlin = np.hstack((f1[cycles['Tdlin'][j,0]].value))
        V = np.hstack((f1[cycles['V'][j,0]][()]))
        #dQdV = np.hstack((f1[cycles['discharge_dQdV'][j,0]].value))
        #t = np.hstack((f1[cycles['t'][j,0]].value))
        #cd = {'I': I, 'Qc': Qc, 'Qd': Qd, 'Qdlin': Qdlin, 'T': T, 'Tdlin': Tdlin, 'V':V, 'dQdV': dQdV, 't':t}
        cd = {'Qd': Qd, 'T': T, 'V':V}
        cycle_dict[str(j)] = cd
        
    cell_dict = {'cycle_life': cl, 'charge_policy':policy, 'summary': summary, 'cycles': cycle_dict}
    key = 'b1c' + str(i)
    bat_dict1[key]=   cell_dict
print(bat_dict1.keys())

# %%

#remove batteries that do not reach 80% capacity
del bat_dict1['b1c8']
del bat_dict1['b1c10']
del bat_dict1['b1c12']
del bat_dict1['b1c13']
del bat_dict1['b1c22']

# %%

# There are four cells from batch1 that carried into batch2, we'll remove the data from batch2
# and put it with the correct cell from batch1
batch2_keys = ['b2c7', 'b2c8', 'b2c9', 'b2c15', 'b2c16']
batch1_keys = ['b1c0', 'b1c1', 'b1c2', 'b1c3', 'b1c4']
add_len = [662, 981, 1060, 208, 482];

for i, bk in enumerate(batch1_keys):
    bat_dict1[bk]['cycle_life'] = bat_dict1[bk]['cycle_life'] + add_len[i]
    for j in bat_dict1[bk]['summary'].keys():
        if j == 'cycle':
            bat_dict1[bk]['summary'][j] = np.hstack((bat_dict1[bk]['summary'][j], bat_dict2[batch2_keys[i]]['summary'][j] + len(bat_dict1[bk]['summary'][j])))
        else:
            bat_dict1[bk]['summary'][j] = np.hstack((bat_dict1[bk]['summary'][j], bat_dict2[batch2_keys[i]]['summary'][j]))
    last_cycle = len(bat_dict1[bk]['cycles'].keys())
    for j, jk in enumerate(bat_dict2[batch2_keys[i]]['cycles'].keys()):
        bat_dict1[bk]['cycles'][str(last_cycle + j)] = bat_dict2[batch2_keys[i]]['cycles'][jk]

del bat_dict2['b2c7']
del bat_dict2['b2c8']
del bat_dict2['b2c9']
del bat_dict2['b2c15']
del bat_dict2['b2c16']

with open('batch1.pkl','wb') as fp:
        pickle.dump(bat_dict1,fp)

with open('batch2.pkl','wb') as fp:
        pickle.dump(bat_dict2,fp)

# %%

matFilename = './Data/2018-04-12_batchdata_updated_struct_errorcorrect.mat'
f3 = h5py.File(matFilename)

batch3 = f3['batch']

num_cells = batch3['summary'].shape[0]
bat_dict3 = {}
for i in range(num_cells):
    cl = f3[batch3['cycle_life'][i,0]].value
    policy = f3[batch3['policy_readable'][i,0]].value.tobytes()[::2].decode()
    summary_IR = np.hstack(f3[batch3['summary'][i,0]]['IR'][0,:].tolist())
    #summary_QC = np.hstack(f3[batch3['summary'][i,0]]['QCharge'][0,:].tolist())
    summary_QD = np.hstack(f3[batch3['summary'][i,0]]['QDischarge'][0,:].tolist())
    #summary_TA = np.hstack(f3[batch3['summary'][i,0]]['Tavg'][0,:].tolist())
    #summary_TM = np.hstack(f3[batch3['summary'][i,0]]['Tmin'][0,:].tolist())
    #summary_TX = np.hstack(f3[batch3['summary'][i,0]]['Tmax'][0,:].tolist())
    #summary_CT = np.hstack(f3[batch3['summary'][i,0]]['chargetime'][0,:].tolist())
    summary_CY = np.hstack(f3[batch3['summary'][i,0]]['cycle'][0,:].tolist())
    #summary = {'IR': summary_IR, 'QC': summary_QC, 'QD': summary_QD, 'Tavg':
    #            summary_TA, 'Tmin': summary_TM, 'Tmax': summary_TX, 'chargetime': summary_CT,
    #            'cycle': summary_CY}
    summary = {'IR': summary_IR, 'QD': summary_QD, 'cycle': summary_CY}
    cycles = f3[batch3['cycles'][i,0]]
    cycle_dict = {}
    for j in range(cycles['I'].shape[0]):
        #I = np.hstack((f3[cycles['I'][j,0]].value))
        #Qc = np.hstack((f3[cycles['Qc'][j,0]].value))
        Qd = np.hstack((f3[cycles['Qd'][j,0]][()]))
        #Qdlin = np.hstack((f3[cycles['Qdlin'][j,0]].value))
        T = np.hstack((f3[cycles['T'][j,0]][()]))
        #Tdlin = np.hstack((f3[cycles['Tdlin'][j,0]].value))
        V = np.hstack((f3[cycles['V'][j,0]][()]))
        #dQdV = np.hstack((f3[cycles['discharge_dQdV'][j,0]].value))
        #t = np.hstack((f3f[cycles['t'][j,0]].value))
        #cd = {'I': I, 'Qc': Qc, 'Qd': Qd, 'Qdlin': Qdlin, 'T': T, 'Tdlin': Tdlin, 'V':V, 'dQdV': dQdV, 't':t}
        cd = {'Qd': Qd, 'T': T, 'V':V}
        cycle_dict[str(j)] = cd
        
    cell_dict = {'cycle_life': cl, 'charge_policy':policy, 'summary': summary, 'cycles': cycle_dict}
    key = 'b3c' + str(i)
    bat_dict3[key]=   cell_dict
bat_dict3.keys()

# remove noisy channels from batch3
del bat_dict3['b3c37']
del bat_dict3['b3c2']
del bat_dict3['b3c23']
del bat_dict3['b3c32']
del bat_dict3['b3c38']
del bat_dict3['b3c39']

with open('batch3.pkl','wb') as fp:
        pickle.dump(bat_dict3,fp)


# %%
