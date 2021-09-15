#import libraries needed for function 
import numpy as np
import pymrio


#create function (a more efficient way of writing the function?)

def get_emission(region, emission_type):
    test_mrio = pymrio.load_test()
    test_mrio.calc_all()
    df = test_mrio.emissions.D_cba
    df1= df[np.in1d(df.index.get_level_values(1), [emission_type])]
    df2 = df1[region]
    print(df2)

#test
get_emission('reg2', 'water')


#more detail can be added by including a sector sub category/ filter
