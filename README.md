# Pymrio_development
Contributions to the development of Pymrio

The purpose of this script is to use the Pymrio, Pandas, Numpy, Matplotlib libraries to: Parse the EXIOBASE3 data, loop through the data and collect relevent time series data on GHG emissions (as well as other enviornmental stressors) per country and store this information in a table and produce visualizations. 

The file "Main.py" includes the script for a program based on user input. Other files include the get_emissions functions using Pymrio and Numpy. 

Curently the script works on a test dataset within the pymrio library. 

The script also includes a "get_emission_viz" function whihc intakes a region and emission type and outputs the relevant invormation in the format of a bar chart. Similar to the chart bellow. Running: get_emission_viz('reg2', 'air') would produce the bellow vizualisation.  ![output](https://user-images.githubusercontent.com/62759252/134172231-d48066c5-1d4e-4511-9699-e4e4d4c6d5d6.png)

The visualisation can still be further developed. I Imagine the next step would be adjusting the script and visualisation to work on the bigger datasets. 
