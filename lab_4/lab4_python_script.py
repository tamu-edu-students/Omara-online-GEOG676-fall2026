import arcpy

arcpy.env.workspace = r'C:\DevSource\Omara-online-GEOG676-fall2026\lab_4\codes_env'
folder_path = r'C:\DevSource\Omara-online-GEOG676-fall2026\lab_4'
gdb_name = 'TheLab4.gdb'
gdb_path = folder_path + '\\' + gdb_name
arcpy.CreateFileGDB_management(folder_path, gdb_name)

csv_path = r'C:\Users\liamo\Downloads\garages.csv'
garage_layer_name = 'Garage_Points'
garages = arcpy.MakeXYEventLayer_management(csv_path, 'X', 'Y', garage_layer_name)

input_layer = garages
arcpy.FeatureClassToGeodatabase_conversion(input_layer, gdb_path)
garage_points = gdb_path + '\\' + garage_layer_name

campus = r'C:\Users\liamo\Downloads\Campus.gdb-20240114T205617Z-001\Campus.gdb'
buildings_campus = campus + '\\Structures'
buildings = gdb_path + '\\' + 'Buildings'

arcpy.Copy_management(buildings_campus, buildings)

#reproject the garage points to match the spatial reference of the buildings layer
spatial_ref = arcpy.Describe(buildings).spatialReference
arcpy.Project_management(garage_points, gdb_path + '\\Garage_Points_reprojected', spatial_ref)

#buffer the garages
garage_buffered = arcpy.Buffer_analysis(gdb_path + '\\Garage_Points_reprojected', gdb_path + '\\Garage_Points_buffered', 150)

#intersect buffer with buildings
arcpy.Intersect_analysis([garage_buffered, buildings], gdb_path + '\\Garage_Building_Intersection', 'ALL')

arcpy.TableToTable_conversion(gdb_path + '\\Garage_Building_Intersection.dbf', 'C:\\DevSource\\Omara-online-GEOG676-fall2026\\lab_4', 'nearbyBuildings.csv')
