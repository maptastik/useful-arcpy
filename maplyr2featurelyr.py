"""Create feature layers of layers in an ArcGIS Pro map

This function create feature layers from all the non-basemap layers in an ArcGIS Pro map.
"""

import arcpy

def maplyr2featurelyr(map_name, project='CURRENT', map_index = 0, feature_lyr_name_suffix = ''):
  aprx = arcpy.mp.ArcGISProject(project)
  m = aprx.listMaps(map_name)[map_index]
  for lyr in m.listLayers():
    if lyr.isBasemapLayer:
      pass
    else:
      arcpy.MakeFeatureLayer_management(lyr.name, "{stem}{suffix}".format(stem = lyr.name, suffix = feature_lyr_name_suffix))
