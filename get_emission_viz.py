#%%
import pandas as pd

#import libraries needed for function 
import numpy as np
import pymrio
import matplotlib.pyplot as plt

#create function (a more efficient way of writing the function?)

def get_emission_viz(region, emission_type):
    test_mrio = pymrio.load_test()
    test_mrio.calc_all()
    df = test_mrio.emissions.D_cba
    df1 = df[np.in1d(df.index.get_level_values(1), [emission_type])]
    df2 = df1[region]
    ax = df2.unstack(level=1).plot(kind='bar', subplots=False, rot=0, figsize=(10, 5), layout=(4, 6))
    plt.title(emission_type + '_pollution_in_' +region)
    plt.tight_layout()

#test
get_emission_viz('reg2', 'air')

#output_file = input("Save file as \n")
#df3.to_csv(output_file + '.tsv', sep ='\t')

#visualize the output of the function 

# %%
