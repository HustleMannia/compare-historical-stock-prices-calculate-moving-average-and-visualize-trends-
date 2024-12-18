# compare-historical-stock-prices-calculate-moving-average-and-visualize-trends-
This project aims to analyze historical stock prices, compute moving averages for trend detection, and visualize the trends. The analysis will help identify price patterns and trends, which are vital for informed decision-making in financial markets. 

               Team member 
1. Bansari timbadiya 
2. Archi vyas 
3. Janvi Patel
4. Jay Barrot
5. Jaimin Vedant 


       Libraries are used in this project 
       1. pandas 
       2. Nampy 
       3. seashore 

       Inian stock Market  

## Contributors
1.  Bansari timbadiya (KU2407U263)_ Python coding 
2.  Archi Vyas (KU2407U254)_ Manage all the files 
3.  Janvi Patel(KU2407U299)_ manage all the dataset 
4.  Jay Barrot (KU2407U264)_ code exection and code screenshot 
5.  Jaimin Vedant (KU2407U296)_ Support in all the department, manages all pyton coding 

  

## Table of Contents
1. [Introduction]
2. [Objective]
3. [Tools and Libraries Used]
4. [Data Sources]
5. [Installation]
6. [Usage]
7. [Analysis and Insights]
8. [Visualizations]
9. [Challenges Faced]
10. [Contributors]
11. [License]

---

## Introduction
Stock market analysis is essential for investors, analysts, and enthusiasts to make informed decisions about their investments. By comparing historical stock prices and analyzing trends using moving averages, one can identify patterns, predict market behavior, and reduce risks.

This project focuses on visualizing stock price trends and incorporating moving averages to smoothen price fluctuations, making trends more apparent. With an interactive and user-friendly web interface,

## Objective
The objective is to identify Indian stock price  , uncover key insights, and present a clear understanding of patterns in population movement over time. 


# Data Sources
- (Include the datasets or public data repositories used for the project)
- Mention sources such as census data, Forest cover loss  reports, or any open datasets.

## Installation
1. Clone the repository:

   git clone https://github.com/[unity_]/Compare_stock_price_calculate.git 

2. Navigate to the project directory:

   cd Compare_stock_price_calculate
   

3. Install the required libraries:

   pip install -r requirements.txt


## Usage
1. Load the Jupyter notebooks or Python scripts from the `src/` folder.
2. Execute the analysis scripts as described in the documentation.
3. View generated visualizations in the `visuals/` folder.

## Analysis and Insights
- Provide a summary of key findings, such as:
  - To analysis Compare_stock_price_calculate analysis 
  
  

## Visualizations
- Include sample visualizations like:
  - Heatmaps Seasonal forest cover analysis 
  - Comparative bar charts for Compare_stock_price_calculate   

## Challenges Faced
- Data cleaning issues (e.g., missing or incomplete data) 
- Handling large datasets
- Visualizing complex Forest cover  loss analysis 


# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
import rasterio
from rasterio.plot import show

# List of years with corresponding GeoTIFF file paths
years = [2020, 2021, 2022]  # Example years
file_paths = ["Compare_stock_price_calculate_{year}.tif" for year in years]  # Replace with actual file paths

# Initialize storage for deforested areas
deforested_areas = []

# Function to load GeoTIFF data
def load_raster(file_path):
    with rasterio.open(file_path) as src:
        data = src.read(1)  # Read the first band
        meta = src.meta  # Metadata for resolution
    return data, meta

# Process data for each pair of consecutive years
for i in range(len(file_paths) - 1):
    # Load raster data for the current year and next year
    current_data, meta = load_raster(file_paths[i])
    next_data, _ = load_raster(file_paths[i + 1])

    # Calculate forest change (deforestation)
    forest_change = next_data - current_data

    # Calculate deforested area (pixels with negative change)
    pixel_resolution = meta['transform'][0]  # Pixel size in meters
    deforested_area = np.sum(forest_change < 0) * pixel_resolution**2  # Area in square meters
    deforested_areas.append(deforested_area)

    # Visualize the forest change
    plt.figure(figsize=(10, 6))
    show(forest_change, cmap='RdYlGn', title=f"Forest Change ({years[i]}-{years[i+1]})")
    plt.colorbar(label="Change in Forest Cover")
    plt.show()

    # Print the calculated deforested area
    print(f"Deforested Area from {years[i]} to {years[i+1]}: {deforested_area} square meters")

# Plot deforestation trend over years
plt.figure(figsize=(8, 5))
plt.plot(years[:-1], deforested_areas, marker='o', linestyle='-', color='red')
plt.title("Yearly Deforestation Trends")
plt.xlabel("Year")
plt.grid(True)
plt.show()

print("Analysis Complete!")

         Usage

        1.  Load the Jupyter notebooks or Python scripts from the src/ folder.
        2.    Execute the analysis scripts as described in the documentation.
        3.   View generated visualizations in the visuals/ folder. 

         
