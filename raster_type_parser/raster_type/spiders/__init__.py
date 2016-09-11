import scrapy
from raster_type.items import RasterTypeItem


class Raster_Type_Spyder(scrapy.Spider):
    name = "raster"
    allowed_domains = ["gdal.org"]
    start_urls = [
        "http://www.gdal.org/formats_list.html"
    ]

    def parse(self, response):
        for row in response.css("tr"):
            fileformat = RasterTypeItem()
            if (row.css("td:nth-child(1) a::text").extract() == None):
                fileformat['long_name'] = row.css("td:nth-child(1)::text").extract()
            else:
                fileformat['long_name'] = row.css("td:nth-child(1) a::text").extract()

            fileformat['short_name'] = row.css("td:nth-child(2)::text").extract()
            fileformat['flag'] = row.css("td:nth-child(3)::text").extract()
            yield fileformat
