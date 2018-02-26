import acrpy
import csv

fc_fields = ['PARKID', 'NAME']
csv_heads = ['Park ID Number', 'Park Name', 'Master Plan Date']
outCSV = 'ParkMasterPlanDates.csv'
with open(outCSV, 'w') as output:
    writer = csv.writer(output)
    writer.writerow(csv_heads)
    with arcpy.da.SearchCursor('RALEIGH.PARKS', field_names = fc_fields) as cursor:
        for row in cursor:
            writer.writerow(row)
        del cursor
