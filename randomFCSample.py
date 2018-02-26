import arcpy
import numpy as np

def randomFCSample(fc, fd='sample_fd', sample_field='OBJECTID', sample_pct=10):
    count_class = arcpy.GetCount_management(fc)
    count = int(count_class[0])
    random_vals = np.random.choice(count, int(count*(sample_pct/100)))
    arcpy.MakeFeatureLayer_management(fc,
                                      fd + "_" + str(sample_pct) + 'pct',
                                      sample_field + ' IN ' + str(tuple(random_vals)))
