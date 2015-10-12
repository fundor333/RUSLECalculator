from osgeo import ogr

cnt = ogr.GetDriverCount()

for i in range(cnt):
    driver = ogr.GetDriver(i)
    driverName = driver.GetName()
    print(driverName)
