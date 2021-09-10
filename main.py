# Write script that Loops through data and choose rows with GHG emissions 
#and store in tables with countries and years and their emissions. 

#import libraries (test dataset)
import pymrio
test_mrio = pymrio.load_test()

test_mrio.emissions.D_cba

#Calculate missing tables
test_mrio.calc_all()

df = test_mrio.emissions.D_cba
df.head()

#generate input message
region = input("Insert region name: \n")
emission_type = input("Insert compartment type (water/air): \n")

#return the emission type and region specified earlier
import numpy as np
df1= df[np.in1d(df.index.get_level_values(1), [emission_type])]
df1

#get relevant region
df2 = df1[region]

#for more detail sector specific values can be found
#sector = input("Insert sector: \n")
#df3 = df2[sector]
#df3

### This would give for example the value of: water stressors caused by trade in region one 