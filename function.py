#import libraries (test dataset)
import pymrio
test_mrio = pymrio.load_test()

test_mrio.emissions.D_cba

#Calculate missing tables
test_mrio.calc_all()

df = test_mrio.emissions.D_cba
df.head()

#create function 

def get_emission(region, emission_type):
    import numpy as np
    df1= df[np.in1d(df.index.get_level_values(1), [emission_type])]
    df2 = df1[region]
    print(df2)

get_emission('reg1', 'air')

