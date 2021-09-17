#%%
import pandas as pd

#import libraries needed for function 
import numpy as np
import pymrio
import matplotlib as plt

#create function (a more efficient way of writing the function?)

def get_emission(region, emission_type):
    test_mrio = pymrio.load_test()
    test_mrio.calc_all()
    df = test_mrio.emissions.D_cba
    df1= df[np.in1d(df.index.get_level_values(1), [emission_type])]
    df2 = df1[region]
    return(df2)

#test
df3 = get_emission('reg2', 'water')

#output_file = input("Save file as \n")
#df3.to_csv(output_file + '.tsv', sep ='\t')

#visualize the output of the function 
ax = df3.unstack(level=0).plot(kind='bar', subplots=True, rot=0, figsize=(36, 24), layout=(4, 6))
plt.tight_layout()
# %%
