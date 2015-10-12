"""
/***************************************************************************
 RUSLECalculator_resurce
                                 A QGIS plugin
 Plugin
                             -------------------
        begin                : 2015-03-12
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Matteo Scarpa
        email                : matteoscarpa92@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

AEZ100 = 11.6171685
AEZ200 = 11.6171685
AEZ300 = 13.5533632

RASTER_FILE = {' AAIGrid': 'Arc/Info ASCII Grid',
               ' ACE2': 'ACE2',
               ' ADRG': 'ADRG/ARC Digitilized Raster Graphics (.gen/.thf)',
               ' AIG': 'Arc/Info Binary Grid (.adf)',
               ' AIRSAR': 'AIRSAR Polarimetric',
               ' ARG': 'Azavea Raster Grid',
               ' BLX': 'Magellan BLX Topo (.blx, .xlb)',
               ' BAG': 'Bathymetry Attributed Grid (.bag)',
               ' BMP': 'Microsoft Windows Device Independent Bitmap (.bmp)',
               ' BSB': 'BSB Nautical Chart Format (.kap)',
               ' BT': 'VTP Binary Terrain Format (.bt)',
               ' CALS': 'CALS Type I',
               ' CEOS': 'CEOS (Spot for instance)',
               ' COSAR': 'TerraSAR-X Complex SAR Data Product',
               ' CTG': 'USGS LULC Composite Theme Grid',
               ' DDS': 'DirectDraw Surface',
               ' DIMAP': 'Spot DIMAP (metadata.dim)',
               ' DODS': 'DODS / OPeNDAP',
               ' DOQ1': 'First Generation USGS DOQ (.doq)',
               ' DOQ2': 'New Labelled USGS DOQ (.doq)',
               ' DTED': 'Military Elevation Data (.dt0, .dt1, .dt2)',
               ' E00GRID': 'Arc/Info Export E00 GRID',
               ' ECRGTOC': 'ECRG Table Of Contents (TOC.xml)',
               ' ECW': 'ERDAS Compressed Wavelets (.ecw)',
               ' EHdr': 'ESRI .hdr Labelled',
               ' EIR': 'Erdas Imagine Raw',
               ' ELAS': 'NASA ELAS',
               ' ENVI': 'ENVI .hdr Labelled Raster',
               ' EPSILON': 'Epsilon - Wavelet compressed images',
               ' ERS': 'ERMapper (.ers)',
               ' ESAT': 'Envisat Image Product (.n1)',
               ' FAST': 'EOSAT FAST Format',
               ' FITS': 'FITS (.fits)',
               ' GENBIN': 'Generic Binary (.hdr Labelled)',
               ' GPKG': 'GeoPackage',
               ' GEORASTER': 'Oracle Spatial GeoRaster',
               'GFF': 'GSat File Format',
               ' GIF': 'Graphics Interchange Format (.gif)',
               ' GRIB': 'WMO GRIB1/GRIB2 (.grb)',
               ' GMT': 'GMT Compatible netCDF',
               ' GRASS': 'GRASS Raster Format',
               ' GRASSASCIIGrid': 'GRASS ASCII Grid',
               ' GSAG': 'Golden Software ASCII Grid',
               ' GSBG': 'Golden Software Binary Grid',
               ' GS7BG': 'Golden Software Surfer 7 Binary Grid',
               ' GTA': 'Generic Tagged Arrays (.gta)',
               ' GTiff': 'TIFF / BigTIFF / GeoTIFF (.tif)',
               ' GXF': 'GXF - Grid eXchange File',
               ' HDF4': 'Hierarchical Data Format Release 4 (HDF4)',
               ' HDF5': 'Hierarchical Data Format Release 5 (HDF5)',
               ' HF2': 'HF2/HFZ heightfield raster',
               ' HFA': 'Erdas Imagine (.img)',
               ' IDA': 'Image Display and Analysis (WinDisp)',
               ' ILWIS': 'ILWIS Raster Map (.mpr,.mpl)',
               ' INGR': 'Intergraph Raster',
               ' IRIS': 'IRIS',
               ' ISCE': 'ISCE raster',
               ' ISIS2': 'USGS Astrogeology ISIS cube (Version 2)',
               ' ISIS3': 'USGS Astrogeology ISIS cube (Version 3)',
               ' JAXAPALSAR': 'JAXA PALSAR Product Reader (Level 1.1/1.5)',
               ' JDEM': 'Japanese DEM (.mem)',
               ' JPEG': 'JPEG JFIF (.jpg)',
               ' JPEGLS': 'JPEG-LS',
               ' JP2OpenJPEG': 'JPEG2000 (.jp2, .j2k)',
               ' JPIPKAK': 'JPIP (based on Kakadu)',
               ' KEA': 'KEA',
               ' KRO': 'KRO',
               ' L1B': 'NOAA Polar Orbiter Level 1b Data Set (AVHRR)',
               ' LAN': 'Erdas 7.x .LAN and .GIS',
               ' LCP': 'FARSITE v.4 LCP Format',
               ' Leveller': 'Daylon Leveller Heightfield',
               ' MBTiles': 'MBTiles',
               ' MAP': 'OziExplorer .MAP',
               ' MEM': 'In Memory Raster',
               ' MFF': 'Vexcel MFF',
               ' MFF2 (HKV)': 'Vexcel MFF2',
               ' MG4Lidar': 'MG4 Encoded Lidar',
               ' MrSID': 'Multi-resolution Seamless Image Database',
               ' MSG': 'Meteosat Second Generation',
               ' MSGN': 'EUMETSAT Archive native (.nat)',
               ' NDF': 'NLAPS Data Format',
               ' NGSGEOID': 'NOAA NGS Geoid Height Grids',
               ' NITF': 'NITF (.ntf, .nsf, .gn?, .hr?, .ja?, .jg?, .jn?, .lf?, .on?, .tl?, .tp?, etc.)',
               ' netCDF': 'NetCDF',
               ' OGDI': 'OGDI Bridge',
               ' OZI': 'OZI OZF2/OZFX3',
               ' PAux': 'PCI .aux Labelled',
               ' PCIDSK': 'PCI Geomatics Database File',
               ' PCRaster': 'PCRaster',
               ' PDF': 'Geospatial PDF',
               ' PDS': 'NASA Planetary Data System',
               ' PLMosaic': 'Planet Labs Mosaics API',
               ' PNG': 'Portable Network Graphics (.png)',
               ' PostGISRaster': 'PostGIS Raster (previously WKTRaster)',
               ' PNM': 'Netpbm (.ppm,.pgm)',
               ' R': 'R Object Data Store',
               ' RASDAMAN': 'Rasdaman',
               ' Rasterlite': 'Rasterlite - Rasters in SQLite DB',
               ' RIK': 'Swedish Grid RIK (.rik)',
               ' RMF': 'Raster Matrix Format (*.rsw, .mtw)',
               ' ROI_PAC': 'ROI_PAC Raster',
               ' RPFTOC': 'Raster Product Format/RPF (CADRG, CIB)',
               ' RS2': 'RadarSat2 XML (product.xml)',
               ' RST': 'Idrisi Raster',
               ' SAFE': 'Sentinel SAFE (manifest.safe)',
               ' SAGA': 'SAGA GIS Binary format',
               ' SAR_CEOS': 'SAR CEOS',
               ' SDE': 'ArcSDE Raster',
               ' SDTS': 'USGS SDTS DEM (*CATD.DDF)',
               ' SGI': 'SGI Image Format',
               ' SNODAS': 'Snow Data Assimilation System',
               ' SRP': 'Standard Raster Product (ASRP/USRP)',
               ' SRTMHGT': 'SRTM HGT Format',
               ' TERRAGEN': 'Terragen Heightfield (.ter)',
               ' USGSDEM': 'USGS ASCII DEM / CDED (.dem)',
               ' VICAR': 'VICAR',
               ' VRT': 'GDAL Virtual (.vrt)',
               ' WCS': 'OGC Web Coverage Service',
               ' WEBP': 'WEBP',
               ' WMS': 'OGC Web Map Service',
               ' WMTS': 'OGC Web Map Tile Service',
               ' XPM': 'X11 Pixmap (.xpm)',
               ' XYZ': 'ASCII Gridded XYZ',
               ' ZMap': 'ZMap Plus Grid'}
RASTER_DRIVER = {'Arc/Info ASCII Grid': ' AAIGrid',
                 'ACE2': ' ACE2',
                 'ADRG/ARC Digitilized Raster Graphics (.gen/.thf)': ' ADRG',
                 'Arc/Info Binary Grid (.adf)': ' AIG',
                 'AIRSAR Polarimetric': ' AIRSAR',
                 'Azavea Raster Grid': ' ARG',
                 'Magellan BLX Topo (.blx, .xlb)': ' BLX',
                 'Bathymetry Attributed Grid (.bag)': ' BAG',
                 'Microsoft Windows Device Independent Bitmap (.bmp)': ' BMP',
                 'BSB Nautical Chart Format (.kap)': ' BSB',
                 'VTP Binary Terrain Format (.bt)': ' BT',
                 'CALS Type I': ' CALS',
                 'CEOS (Spot for instance)': ' CEOS',
                 'TerraSAR-X Complex SAR Data Product': ' COSAR',
                 'USGS LULC Composite Theme Grid': ' CTG',
                 'DirectDraw Surface': ' DDS',
                 'Spot DIMAP (metadata.dim)': ' DIMAP',
                 'DODS / OPeNDAP': ' DODS',
                 'First Generation USGS DOQ (.doq)': ' DOQ1',
                 'New Labelled USGS DOQ (.doq)': ' DOQ2',
                 'Military Elevation Data (.dt0, .dt1, .dt2)': ' DTED',
                 'Arc/Info Export E00 GRID': ' E00GRID',
                 'ECRG Table Of Contents (TOC.xml)': ' ECRGTOC',
                 'ERDAS Compressed Wavelets (.ecw)': ' ECW',
                 'ESRI .hdr Labelled': ' EHdr',
                 'Erdas Imagine Raw': ' EIR',
                 'NASA ELAS': ' ELAS',
                 'ENVI .hdr Labelled Raster': ' ENVI',
                 'Epsilon - Wavelet compressed images': ' EPSILON',
                 'ERMapper (.ers)': ' ERS',
                 'Envisat Image Product (.n1)': ' ESAT',
                 'EOSAT FAST Format': ' FAST',
                 'FITS (.fits)': ' FITS',
                 'Generic Binary (.hdr Labelled)': ' GENBIN',
                 'GeoPackage': ' GPKG',
                 'Oracle Spatial GeoRaster': ' GEORASTER',
                 'GSat File Format': 'GFF',
                 'Graphics Interchange Format (.gif)': ' GIF',
                 'WMO GRIB1/GRIB2 (.grb)': ' GRIB',
                 'GMT Compatible netCDF': ' GMT',
                 'GRASS Raster Format': ' GRASS',
                 'GRASS ASCII Grid': ' GRASSASCIIGrid',
                 'Golden Software ASCII Grid': ' GSAG',
                 'Golden Software Binary Grid': ' GSBG',
                 'Golden Software Surfer 7 Binary Grid': ' GS7BG',
                 'Generic Tagged Arrays (.gta)': ' GTA',
                 'TIFF / BigTIFF / GeoTIFF (.tif)': ' GTiff',
                 'GXF - Grid eXchange File': ' GXF',
                 'Hierarchical Data Format Release 4 (HDF4)': ' HDF4',
                 'Hierarchical Data Format Release 5 (HDF5)': ' HDF5',
                 'HF2/HFZ heightfield raster': ' HF2',
                 'Erdas Imagine (.img)': ' HFA',
                 'Image Display and Analysis (WinDisp)': ' IDA',
                 'ILWIS Raster Map (.mpr,.mpl)': ' ILWIS',
                 'Intergraph Raster': ' INGR',
                 'IRIS': ' IRIS',
                 'ISCE raster': ' ISCE',
                 'USGS Astrogeology ISIS cube (Version 2)': ' ISIS2',
                 'USGS Astrogeology ISIS cube (Version 3)': ' ISIS3',
                 'JAXA PALSAR Product Reader (Level 1.1/1.5)': ' JAXAPALSAR',
                 'Japanese DEM (.mem)': ' JDEM',
                 'JPEG JFIF (.jpg)': ' JPEG',
                 'JPEG-LS': ' JPEGLS',
                 'JPEG2000 (.jp2, .j2k)': ' JPEG2000',
                 'JPIP (based on Kakadu)': ' JPIPKAK',
                 'KEA': ' KEA',
                 'KRO': ' KRO',
                 'NOAA Polar Orbiter Level 1b Data Set (AVHRR)': ' L1B',
                 'Erdas 7.x .LAN and .GIS': ' LAN',
                 'FARSITE v.4 LCP Format': ' LCP',
                 'Daylon Leveller Heightfield': ' Leveller',
                 'MBTiles': ' MBTiles',
                 'OziExplorer .MAP': ' MAP',
                 'In Memory Raster': ' MEM',
                 'Vexcel MFF': ' MFF',
                 'Vexcel MFF2': ' MFF2 (HKV)',
                 'MG4 Encoded Lidar': ' MG4Lidar',
                 'Multi-resolution Seamless Image Database': ' MrSID',
                 'Meteosat Second Generation': ' MSG',
                 'EUMETSAT Archive native (.nat)': ' MSGN',
                 'NLAPS Data Format': ' NDF',
                 'NOAA NGS Geoid Height Grids': ' NGSGEOID',
                 'NITF (.ntf, .nsf, .gn?, .hr?, .ja?, .jg?, .jn?, .lf?, .on?, .tl?, .tp?, etc.)': ' NITF',
                 'NetCDF': ' netCDF',
                 'OGDI Bridge': ' OGDI',
                 'OZI OZF2/OZFX3': ' OZI',
                 'PCI .aux Labelled': ' PAux',
                 'PCI Geomatics Database File': ' PCIDSK',
                 'PCRaster': ' PCRaster',
                 'Geospatial PDF': ' PDF',
                 'NASA Planetary Data System': ' PDS',
                 'Planet Labs Mosaics API': ' PLMosaic',
                 'Portable Network Graphics (.png)': ' PNG',
                 'PostGIS Raster (previously WKTRaster)': ' PostGISRaster',
                 'Netpbm (.ppm,.pgm)': ' PNM',
                 'R Object Data Store': ' R',
                 'Rasdaman': ' RASDAMAN',
                 'Rasterlite - Rasters in SQLite DB': ' Rasterlite',
                 'Swedish Grid RIK (.rik)': ' RIK',
                 'Raster Matrix Format (*.rsw, .mtw)': ' RMF',
                 'ROI_PAC Raster': ' ROI_PAC',
                 'Raster Product Format/RPF (CADRG, CIB)': ' RPFTOC',
                 'RadarSat2 XML (product.xml)': ' RS2',
                 'Idrisi Raster': ' RST',
                 'Sentinel SAFE (manifest.safe)': ' SAFE',
                 'SAGA GIS Binary format': ' SAGA',
                 'SAR CEOS': ' SAR_CEOS',
                 'ArcSDE Raster': ' SDE',
                 'USGS SDTS DEM (*CATD.DDF)': ' SDTS',
                 'SGI Image Format': ' SGI',
                 'Snow Data Assimilation System': ' SNODAS',
                 'Standard Raster Product (ASRP/USRP)': ' SRP',
                 'SRTM HGT Format': ' SRTMHGT',
                 'Terragen Heightfield (.ter)': ' TERRAGEN',
                 'USGS ASCII DEM / CDED (.dem)': ' USGSDEM',
                 'VICAR': ' VICAR',
                 'GDAL Virtual (.vrt)': ' VRT',
                 'OGC Web Coverage Service': ' WCS',
                 'WEBP': ' WEBP',
                 'OGC Web Map Service': ' WMS',
                 'OGC Web Map Tile Service': ' WMTS',
                 'X11 Pixmap (.xpm)': ' XPM',
                 'ASCII Gridded XYZ': ' XYZ',
                 'ZMap Plus Grid': ' ZMap'}
