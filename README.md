# TAOW
TAOW - Turbidity Assessment Over Water - 2017 Summer

SETUP:

Dependencies
Software/Languages: Arcpy, ArcMap, Python
Assumptions: User has Net CDF files that were atmospherically corrected from ACOLITE software. 

__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

ABOUT THE CODE:

The Chesapeake Bay Automation Master Script provides automation for processing atmosperhically corrected satellite imagery.
This script specifically pre-processes Landsat 8 and Sentinel-2 datasets that were atmospherically corrected by ACOLITE. 

__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

CONVERTING NET CDF TO RASTER DESCRIPTION:

This section takes ACOLITE-produced atmospherically corrected satellite imagery products (output as netCDF files from ACOLITE software), and converts them back into geoTIFFs. 
The script utlizes ArcPy's "MakeNetCDFRasterLayer_md" "CopyRaster_management" functions to create rasters of the products within the NetCDFs for all scenes. 
def NetCDF2GeoTIFF(curDir, variableList) contains a list of all possible output products that ACOLITE offers for both Landsat 8 and Sentinel-2 that will be converted to rasters. 
__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

LINKS TO DOWNLOAD ARCGIS TOOLBOX FILES:

BatchCDF2Raster_Sentinel2.tbx
https://drive.google.com/file/d/0B4u-x_yRw1ebUEh2UFhFNnZjWXM/view?usp=sharing

BatchCDF2Raster_Landsat8.tbx
https://drive.google.com/file/d/0B4u-x_yRw1ebSkYtOHU5MFVpazQ/view?usp=sharing



POINT OF CONTACT:

Antonio Alvarado 
Email: antonioalvaradojr@gmail.com


