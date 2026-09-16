import arcpy

print("Python works!")
print("ArcPy works!")

print("ArcGIS Pro version:", arcpy.GetInstallInfo()["Version"])
print("Product:", arcpy.GetInstallInfo()["ProductName"])
print("Current workspace:", arcpy.env.workspace)