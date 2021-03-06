# Pymrio_development
Contributions to the development of Pymrio

The purpose of this script is to use the Pymrio, Pandas, Numpy, Matplotlib libraries to: Parse the EXIOBASE3 data, loop through the data and collect relevent time series data on GHG emissions (as well as other enviornmental stressors) per country and store this information in a table and produce visualizations. 

The file "Main.py" includes the script for a program based on user input. Other files include the get_emissions functions using Pymrio and Numpy which intakes two arguments (region and stressor) and prints the relevant data. I use pandas and numpy within the function. Later on the get_emission_viz function takes the output of this function and visualises it in a bar graph using matplotlib. 

Curently the script works on a test dataset within the pymrio library. 

The script includes a "get_emission_viz" function which intakes a region and emission type and outputs the relevant invormation in the format of a bar chart. Similar to the chart bellow. Running: **get_emission_viz('reg2', 'air')** would produce the bellow vizualisation.  ![output](https://user-images.githubusercontent.com/62759252/134172231-d48066c5-1d4e-4511-9699-e4e4d4c6d5d6.png)

The visualisation can still be further developed. I Imagine the next step would be adjusting the script and visualisation to work on the bigger datasets. 

The latest contribution is the **get_ts_viz function** which produces a time series visualization of the gwg emissions of a given country from the year 2015-2017. It produces the bellow vislualization. ![output](https://user-images.githubusercontent.com/62759252/136377744-6ffc1724-92e0-46b3-b8ae-c8a8a327e1ee.png) 

The code for this visualization can be found in the pymrio_dev.py file along with the **get_time_series** function which simply outputs the gwg emissions of the given state in a pandas dataframe format. 
