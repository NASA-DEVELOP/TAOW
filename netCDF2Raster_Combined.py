import shutil
import os
from arcpy.sa import *
arcpy.CheckOutExtension("Spatial")


#Functions for Moving Files To Their Newly Created Folders Based on File Name:
def extractSatelliteName(filename):
	return filename[:3]

def extractDate(filename):
	return filename[3:19]

def createFolderFromFilename(workspace, filename):
	satelliteString = extractSatelliteName(filename)
	dateString = extractDate(filename)
	currentDir = workspace
	newFolderName = os.path.join(currentDir,satelliteString + dateString)
	if not os.path.exists(newFolderName):
		os.makedirs(newFolderName)
	return newFolderName

def movedACOLITEfiles(destinationpath):
	currentFolder = destinationpath 
	for files in os.listdir(currentFolder):
		if not files.endswith("acolite.tif"):
			continue
		newFolderName = createFolderFromFilename(currentFolder,files)
		satelliteString = extractSatelliteName(files)
		dateString = extractDate(files)
		matchingName = satelliteString + dateString
		for file in os.listdir(currentFolder):
			if not file.endswith("acolite.tif"):
				continue
			satelliteString2 = extractSatelliteName(file)
			dateString2 = extractDate(file)
			if satelliteString == satelliteString2 and dateString == dateString2:
				originalFile = os.path.join(currentFolder,file)
				newFile = os.path.join(newFolderName,file)
				shutil.move(originalFile,newFile)


arcpy.env.workspace = "D:/2017Summer_LaRC_ChesapeakeBayWaterResourcesII/Landsat8_AllScenes"
destinationpath = "D:/2017Summer_LaRC_ChesapeakeBayWaterResourcesII/Landsat8_AllScenes/L8_Outputs"
overwriteOutput = True

#Make NetCDF Raster Layer Input Variables
variableList_L8 = ["RRS_443", "RRS_483", "RRS_561", "RRS_655", "RRS_865", "RRS_1609", "RRS_2201", "T_DOGLIOTTI", "T_DOGLIOTTI_RED", "T_DOGLIOTTI_NIR", "T_GARABA_645_LIN", "T_NECHAD_645"]
variableList_S2 = ["RRS_444", "RRS_497", "RRS_560", "RRS_664", "RRS_704", "RRS_740", "RRS_782", "RRS_835", "RRS_865", "RRS_1614", "RRS_2202", "T_DOGLIOTTI", "T_DOGLIOTTI_RED", "T_DOGLIOTTI_NIR", "T_GARABA_645_LIN", "T_NECHAD_645"]
XDimension = "x" 
YDimension = "y" 
bandDimmension = ""
dimensionValues = ""
valueSelectionMethod = ""
i = 1

Landsat8Folder = arcpy.ListWorkspaces()
for folder in Landsat8Folder:
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
			copyRasterOutput = os.path.abspath(folder) + '/' + ncFile.split(".")[0] + "_" + str(variable) + "_acolite" + ".tif"
			copyRasterOutput_fixed = copyRasterOutput.replace('\\','/')
			arcpy.MakeNetCDFRasterLayer_md(netCDFInput_fixed, variable, XDimension, YDimension, tempOutputRaster, bandDimmension, dimensionValues, valueSelectionMethod)
			arcpy.CopyRaster_management(tempOutputRaster, copyRasterOutput_fixed, "", "", "", "NONE", "NONE", "", "NONE", "NONE", "TIFF",  "NONE")
			source = os.listdir(folder)
			for geoTiff in source:
				if geoTiff.endswith("acolite.tif"):
					shutil.move(os.path.join(folder,geoTiff), os.path.join(destinationpath,geoTiff))

movedACOLITEfiles(destinationpath)