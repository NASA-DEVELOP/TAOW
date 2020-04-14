import shutil
import os
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")


arcpy.env.workspace = GetParameterAsText(0) #"Z:/LaRC_ChesapeakeBayWaterResourcesII/Sentinel2_AllScenes/NIRcorrected/T18SVG/done"    #change to the path where all files with .nc files are 
overwriteOutput = True

#Make NetCDF Raster Layer Input Variables
variableList = [arcpy.GetParameterAsText(1), arcpy.GetParameterAsText(2), arcpy.GetParameterAsText(3), arcpy.GetParameterAsText(4), arcpy.GetParameterAsText(5), arcpy.GetParameterAsText(6), arcpy.GetParameterAsText(7), arcpy.GetParameterAsText(8), arcpy.GetParameterAsText(9), arcpy.GetParameterAsText(10), arcpy.GetParameterAsText(11), arcpy.GetParameterAsText(12), arcpy.GetParameterAsText(13), arcpy.GetParameterAsText(14), arcpy.GetParameterAsText(15), arcpy.GetParameterAsText(16)] #["RRS_444", "RRS_497", "RRS_560", "RRS_664", "RRS_704", "RRS_740", "RRS_782", "RRS_835", "RRS_865", "RRS_1614", "RRS_2202", "T_DOGLIOTTI", "T_DOGLIOTTI_RED", "T_DOGLIOTTI_NIR", "T_GARABA_645_LIN", "T_NECHAD_645"]
XDimension = "x" 
YDimension = "y" 
bandDimmension = ""
dimensionValues = ""
valueSelectionMethod = ""
i = 1

SatelliteSceneFolder = arcpy.ListWorkspaces()
for folder in SatelliteSceneFolder:
	print folder 
	arcpy.env.workspace = folder
	ncFiles = arcpy.ListFiles("*.nc")
	for ncFile in ncFiles: 
		netCDFInput = os.path.abspath(folder) + '/' + ncFile
		netCDFInput_fixed = netCDFInput.replace('\\','/')
		for variable in variableList:
			print variable
			tempOutputRaster = "TemporaryRaster" + str(i)
			i = i + 1
			copyRasterOutput = os.path.abspath(folder) + '/' + ncFile.split(".")[0] + "_" + str(variable) + "_acolite_nirAtmosCorr" + ".tif"
			copyRasterOutput_fixed = copyRasterOutput.replace('\\','/')
			arcpy.MakeNetCDFRasterLayer_md(netCDFInput_fixed, variable, XDimension, YDimension, tempOutputRaster, bandDimmension, dimensionValues, valueSelectionMethod)
			arcpy.CopyRaster_management(tempOutputRaster, copyRasterOutput_fixed, "", "", "", "NONE", "NONE", "", "NONE", "NONE", "TIFF",  "NONE")
