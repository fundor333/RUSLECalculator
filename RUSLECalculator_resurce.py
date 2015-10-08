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

RASTER_FILE = {'HDF4': 'Hierarchical Data Format Release 4 (HDF4)', 'HDF5': 'Hierarchical Data Format Release 5 (HDF5)',
               'SAGA': 'SAGA GIS Binary format', 'BT': 'VTP Binary Terrain Format (.bt)',
               'SNODAS': 'Snow Data Assimilation System', 'MBTiles': 'MBTiles', 'OGDI': 'OGDI Bridge',
               'JDEM': 'Japanese DEM (.mem)', 'DODS': 'DODS / OPeNDAP', 'RIK': 'Swedish Grid RIK (.rik)',
               'SDTS': 'USGS SDTS DEM (*CATD.DDF)', 'GRASSASCIIGrid': 'GRASS ASCII Grid', 'XPM': 'X11 Pixmap (.xpm)',
               'WMS': 'OGC Web Map Service', 'SAFE': 'Sentinel SAFE (manifest.safe)', 'ZMap': 'ZMap Plus Grid',
               'LAN': 'Erdas 7.x .LAN and .GIS', 'ISCE': 'ISCE raster', 'GIF': 'Graphics Interchange Format (.gif)',
               'ROI_PAC': 'ROI_PAC Raster', 'SAR_CEOS': 'SAR CEOS', 'FITS': 'FITS (.fits)', 'MAP': 'OziExplorer .MAP',
               'GXF': 'GXF - Grid eXchange File', 'XYZ': 'ASCII Gridded XYZ', 'GSBG': 'Golden Software Binary Grid',
               'Rasterlite': 'Rasterlite - Rasters in SQLite DB', 'ECRGTOC': 'ECRG Table Of Contents (TOC.xml)',
               'RPFTOC': 'Raster Product Format/RPF (CADRG, CIB)', 'HF2': 'HF2/HFZ heightfield raster',
               'CEOS': 'CEOS (Spot for instance)', 'JPIPKAK': 'JPIP (based on Kakadu)', 'CALS': 'CALS Type I',
               'MFF': 'Vexcel MFF', 'DTED': 'Military Elevation Data (.dt0, .dt1, .dt2)',
               'BMP': 'Microsoft Windows Device Independent Bitmap (.bmp)', 'GSAG': 'Golden Software ASCII Grid',
               'INGR': 'Intergraph Raster', 'SRTMHGT': 'SRTM HGT Format', 'BLX': 'Magellan BLX Topo (.blx, .xlb)',
               'DDS': 'DirectDraw Surface', 'ACE2': 'ACE2', 'NGSGEOID': 'NOAA NGS Geoid Height Grids',
               'LCP': 'FARSITE v.4 LCP Format', 'GTiff': 'TIFF / BigTIFF / GeoTIFF (.tif)',
               'ESAT': 'Envisat Image Product (.n1)',
               'NITF': 'NITF (.ntf, .nsf, .gn?, .hr?, .ja?, .jg?, .jn?, .lf?, .on?, .tl?, .tp?, etc.)',
               'AIRSAR': 'AIRSAR Polarimetric', 'JPEG2000': 'JPEG2000 (.jp2, .j2k)',
               'L1B': 'NOAA Polar Orbiter Level 1b Data Set (AVHRR)',
               'JAXAPALSAR': 'JAXA PALSAR Product Reader (Level 1.1/1.5)', 'EIR': 'Erdas Imagine Raw', 'WEBP': 'WEBP',
               'CTG': 'USGS LULC Composite Theme Grid', 'HFA': 'Erdas Imagine (.img)', 'GRASS': 'GRASS Raster Format',
               'IDA': 'Image Display and Analysis (WinDisp)', 'PCIDSK': 'PCI Geomatics Database File', 'VICAR': 'VICAR',
               'VRT': 'GDAL Virtual (.vrt)', 'FAST': 'EOSAT FAST Format', 'ECW': 'ERDAS Compressed Wavelets (.ecw)',
               'RMF': 'Raster Matrix Format (*.rsw, .mtw)', 'BSB': 'BSB Nautical Chart Format (.kap)',
               'GTA': 'Generic Tagged Arrays (.gta)', 'TERRAGEN': 'Terragen Heightfield (.ter)',
               'NDF': 'NLAPS Data Format', 'SRP': 'Standard Raster Product (ASRP/USRP)', 'R': 'R Object Data Store',
               'KRO': 'KRO', 'ISIS3': 'USGS Astrogeology ISIS cube (Version 3)',
               'ISIS2': 'USGS Astrogeology ISIS cube (Version 2)', 'PDF': 'Geospatial PDF', 'GPKG': 'GeoPackage',
               'PCRaster': 'PCRaster', 'E00GRID': 'Arc/Info Export E00 GRID', 'GMT': 'GMT Compatible netCDF',
               'JPEGLS': 'JPEG-LS', 'MEM': 'In Memory Raster', 'GENBIN': 'Generic Binary (.hdr Labelled)', 'KEA': 'KEA',
               'OZI': 'OZI OZF2/OZFX3', 'DOQ1': 'First Generation USGS DOQ (.doq)',
               'DOQ2': 'New Labelled USGS DOQ (.doq)', 'Leveller': 'Daylon Leveller Heightfield',
               'GS7BG': 'Golden Software Surfer 7 Binary Grid', 'ERS': 'ERMapper (.ers)',
               'MrSID': 'Multi-resolution Seamless Image Database', 'PAux': 'PCI .aux Labelled', 'ELAS': 'NASA ELAS',
               'BAG': 'Bathymetry Attributed Grid (.bag)', 'MSG': 'Meteosat Second Generation',
               'AIG': 'Arc/Info Binary Grid (.adf)', 'PLMosaic': 'Planet Labs Mosaics API',
               'RS2': 'RadarSat2 XML (product.xml)', 'IRIS': 'IRIS', 'USGSDEM': 'USGS ASCII DEM / CDED (.dem)',
               'MFF2 (HKV)': 'Vexcel MFF2', 'SGI': 'SGI Image Format', 'RASDAMAN': 'Rasdaman',
               'WMTS': 'OGC Web Map Tile Service', 'PNM': 'Netpbm (.ppm,.pgm)', 'DIMAP': 'Spot DIMAP (metadata.dim)',
               'WCS': 'OGC Web Coverage Service', 'AAIGrid': 'Arc/Info ASCII Grid', 'PDS': 'NASA Planetary Data System',
               'JPEG': 'JPEG JFIF (.jpg)', 'COSAR': 'TerraSAR-X Complex SAR Data Product',
               'GRIB': 'WMO GRIB1/GRIB2 (.grb)', 'ADRG': 'ADRG/ARC Digitilized Raster Graphics (.gen/.thf)',
               'GEORASTER': 'Oracle Spatial GeoRaster', 'MSGN': 'EUMETSAT Archive native (.nat)',
               'MG4Lidar': 'MG4 Encoded Lidar', 'EHdr': 'ESRI .hdr Labelled',
               'EPSILON': 'Epsilon - Wavelet compressed images', 'ILWIS': 'ILWIS Raster Map (.mpr,.mpl)',
               'SDE': 'ArcSDE Raster', 'ENVI': 'ENVI .hdr Labelled Raster', 'netCDF': 'NetCDF',
               'ARG': 'Azavea Raster Grid', 'RST': 'Idrisi Raster',
               'PostGISRaster': 'PostGIS Raster (previously WKTRaster)', 'GFF': 'GSat File Format',
               'PNG': 'Portable Network Graphics (.png)'}
RASTER_DRIVER = {'Azavea Raster Grid': 'ARG', 'Spot DIMAP (metadata.dim)': 'DIMAP',
                 'ILWIS Raster Map (.mpr,.mpl)': 'ILWIS', 'MG4 Encoded Lidar': 'MG4Lidar', 'MBTiles': 'MBTiles',
                 'GMT Compatible netCDF': 'GMT', 'ArcSDE Raster': 'SDE', 'ZMap Plus Grid': 'ZMap',
                 'Generic Binary (.hdr Labelled)': 'GENBIN', 'Bathymetry Attributed Grid (.bag)': 'BAG',
                 'Golden Software ASCII Grid': 'GSAG', 'ERMapper (.ers)': 'ERS', 'JPEG2000 (.jp2, .j2k)': 'JPEG2000',
                 'Hierarchical Data Format Release 4 (HDF4)': 'HDF4', 'Epsilon - Wavelet compressed images': 'EPSILON',
                 'GRASS Raster Format': 'GRASS', 'Meteosat Second Generation': 'MSG', 'ISCE raster': 'ISCE',
                 'USGS SDTS DEM (*CATD.DDF)': 'SDTS', 'Oracle Spatial GeoRaster': 'GEORASTER',
                 'Generic Tagged Arrays (.gta)': 'GTA', 'Sentinel SAFE (manifest.safe)': 'SAFE', 'ACE2': 'ACE2',
                 'Arc/Info ASCII Grid': 'AAIGrid', 'BSB Nautical Chart Format (.kap)': 'BSB',
                 'Arc/Info Binary Grid (.adf)': 'AIG', 'SRTM HGT Format': 'SRTMHGT', 'Rasdaman': 'RASDAMAN',
                 'EUMETSAT Archive native (.nat)': 'MSGN', 'Microsoft Windows Device Independent Bitmap (.bmp)': 'BMP',
                 'Daylon Leveller Heightfield': 'Leveller', 'ECRG Table Of Contents (TOC.xml)': 'ECRGTOC',
                 'New Labelled USGS DOQ (.doq)': 'DOQ2', 'ADRG/ARC Digitilized Raster Graphics (.gen/.thf)': 'ADRG',
                 'ASCII Gridded XYZ': 'XYZ', 'Raster Matrix Format (*.rsw, .mtw)': 'RMF',
                 'ERDAS Compressed Wavelets (.ecw)': 'ECW', 'OziExplorer .MAP': 'MAP', 'OZI OZF2/OZFX3': 'OZI',
                 'GSat File Format': 'GFF', 'PCI Geomatics Database File': 'PCIDSK', 'Idrisi Raster': 'RST',
                 'JAXA PALSAR Product Reader (Level 1.1/1.5)': 'JAXAPALSAR', 'GRASS ASCII Grid': 'GRASSASCIIGrid',
                 'Image Display and Analysis (WinDisp)': 'IDA', 'Arc/Info Export E00 GRID': 'E00GRID',
                 'ENVI .hdr Labelled Raster': 'ENVI', 'Envisat Image Product (.n1)': 'ESAT',
                 'Snow Data Assimilation System': 'SNODAS', 'X11 Pixmap (.xpm)': 'XPM', 'GeoPackage': 'GPKG',
                 'Planet Labs Mosaics API': 'PLMosaic', 'NLAPS Data Format': 'NDF',
                 'NOAA NGS Geoid Height Grids': 'NGSGEOID', 'Graphics Interchange Format (.gif)': 'GIF',
                 'CEOS (Spot for instance)': 'CEOS', 'RadarSat2 XML (product.xml)': 'RS2',
                 'Hierarchical Data Format Release 5 (HDF5)': 'HDF5', 'WEBP': 'WEBP', 'Japanese DEM (.mem)': 'JDEM',
                 'VICAR': 'VICAR', 'Swedish Grid RIK (.rik)': 'RIK', 'JPEG JFIF (.jpg)': 'JPEG',
                 'ROI_PAC Raster': 'ROI_PAC', 'ESRI .hdr Labelled': 'EHdr',
                 'NOAA Polar Orbiter Level 1b Data Set (AVHRR)': 'L1B',
                 'NITF (.ntf, .nsf, .gn?, .hr?, .ja?, .jg?, .jn?, .lf?, .on?, .tl?, .tp?, etc.)': 'NITF',
                 'Magellan BLX Topo (.blx, .xlb)': 'BLX', 'OGC Web Map Service': 'WMS', 'FARSITE v.4 LCP Format': 'LCP',
                 'NASA ELAS': 'ELAS', 'USGS LULC Composite Theme Grid': 'CTG', 'OGDI Bridge': 'OGDI',
                 'SAR CEOS': 'SAR_CEOS', 'R Object Data Store': 'R', 'Standard Raster Product (ASRP/USRP)': 'SRP',
                 'WMO GRIB1/GRIB2 (.grb)': 'GRIB', 'KRO': 'KRO', 'PCRaster': 'PCRaster',
                 'First Generation USGS DOQ (.doq)': 'DOQ1', 'Terragen Heightfield (.ter)': 'TERRAGEN',
                 'Rasterlite - Rasters in SQLite DB': 'Rasterlite', 'PCI .aux Labelled': 'PAux',
                 'JPIP (based on Kakadu)': 'JPIPKAK', 'Vexcel MFF': 'MFF', 'KEA': 'KEA', 'FITS (.fits)': 'FITS',
                 'Intergraph Raster': 'INGR', 'NetCDF': 'netCDF', 'Raster Product Format/RPF (CADRG, CIB)': 'RPFTOC',
                 'CALS Type I': 'CALS', 'Vexcel MFF2': 'MFF2 (HKV)', 'OGC Web Coverage Service': 'WCS',
                 'GDAL Virtual (.vrt)': 'VRT', 'OGC Web Map Tile Service': 'WMTS', 'Erdas Imagine (.img)': 'HFA',
                 'IRIS': 'IRIS', 'Golden Software Binary Grid': 'GSBG', 'TIFF / BigTIFF / GeoTIFF (.tif)': 'GTiff',
                 'Erdas 7.x .LAN and .GIS': 'LAN', 'USGS ASCII DEM / CDED (.dem)': 'USGSDEM',
                 'Portable Network Graphics (.png)': 'PNG', 'DODS / OPeNDAP': 'DODS', 'GXF - Grid eXchange File': 'GXF',
                 'Golden Software Surfer 7 Binary Grid': 'GS7BG', 'USGS Astrogeology ISIS cube (Version 2)': 'ISIS2',
                 'Erdas Imagine Raw': 'EIR', 'EOSAT FAST Format': 'FAST',
                 'Multi-resolution Seamless Image Database': 'MrSID',
                 'Military Elevation Data (.dt0, .dt1, .dt2)': 'DTED', 'TerraSAR-X Complex SAR Data Product': 'COSAR',
                 'AIRSAR Polarimetric': 'AIRSAR', 'NASA Planetary Data System': 'PDS',
                 'PostGIS Raster (previously WKTRaster)': 'PostGISRaster', 'DirectDraw Surface': 'DDS',
                 'HF2/HFZ heightfield raster': 'HF2', 'SGI Image Format': 'SGI', 'In Memory Raster': 'MEM',
                 'JPEG-LS': 'JPEGLS', 'Geospatial PDF': 'PDF', 'Netpbm (.ppm,.pgm)': 'PNM',
                 'VTP Binary Terrain Format (.bt)': 'BT', 'USGS Astrogeology ISIS cube (Version 3)': 'ISIS3',
                 'SAGA GIS Binary format': 'SAGA'}
