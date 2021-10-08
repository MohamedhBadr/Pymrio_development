# %%
#import libraries
import pymrio
import pandas as pd
import numpy as np 
from pathlib import Path
import matplotlib as plt


# %%
#import Exiobase 2017

io_path_2017 = Path("./IOT_2017_pxp.zip")
io_2017 = pymrio.parse_exiobase3(io_path_2017)
# %%
#calculate all and get d_cba

gwp = "GHG emissions (GWP100) | Problem oriented approach: baseline (CML, 2001) | GWP100 (IPCC, 2007)"
io_2017.calc_all()
d_cba_2017 = io_2017.impacts.D_cba_reg.loc[gwp, :]



#Import and Proccess EXIO 2015
io_path_2015 = Path("./IOT_2015_ixi.zip")
io_2015 = pymrio.parse_exiobase3(io_path_2015)
io_2015.calc_all()
d_cba_2015 = io_2015.impacts.D_cba_reg.loc[gwp, :]

# %%
#Import and Proccess EXIO 2016
io_path_2016 = Path("./IOT_2016_ixi.zip")
io_2016 = pymrio.parse_exiobase3(io_path_2016)
io_2016.calc_all()
d_cba_2016 = io_2016.impacts.D_cba_reg.loc[gwp, :]

# %%
#merge into one dataframe 

io_2015_2016 = pd.merge(d_cba_2015, d_cba_2016, left_index=True, right_index=True)
io_2015__2017 = pd.merge(io_2015_2016, d_cba_2017, left_index=True, right_index=True)
io_2015__2017

# %%
#Rename columns 
df = io_2015__2017
df = df.rename(columns={'GHG emissions (GWP100) | Problem oriented approach: baseline (CML, 2001) | GWP100 (IPCC, 2007)_x': '2015'})
df = df.rename(columns={'GHG emissions (GWP100) | Problem oriented approach: baseline (CML, 2001) | GWP100 (IPCC, 2007)_y': '2016'})
df = df.rename(columns={'GHG emissions (GWP100) | Problem oriented approach: baseline (CML, 2001) | GWP100 (IPCC, 2007)': '2017'})
df
# %%
#define function that gets country and emissions 
def get_time_series(country_code):
    df2 = df[country_code]
    ax = df2.unstack(level=1).plot(kind='bar', subplots=False, rot=0, figsize=(10, 5), layout=(4, 6))
    plt.title(emission_type + '_pollution_in_' +region)
    plt.tight_layout()


# %%
#Write function to return values 
def get_time_series(country):
    df2 = df.loc[ country , : ]
    df2
    return df2
# %%
#test function (appears to work fine)
df_russia = get_time_series('RU')
df_russia
# %%
#Write a visualization function
def get_ts_viz (country_code):
    new_df = get_time_series(country_code)
    new_df = new_df.reset_index()
    plt.pyplot.title('GWP in ' + country_code)
    plt.pyplot.bar('index', country_code, width=0.75, bottom=None, align='center', data=new_df)

# %%
#Test visualization function 
get_ts_viz('IN')
# %%
