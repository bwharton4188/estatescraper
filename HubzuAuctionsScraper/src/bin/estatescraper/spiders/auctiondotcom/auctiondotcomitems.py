
from scrapy.item import Item, Field
 
class AuctionDOTcomItems(Item):
    """"""
    # <div class="primaryAlertBanner listOnly yellow">Outbid period</div>
    alertBanner     = Field() 
    #<a class="searchTrackPDP" href="http://www.auction.com/North Carolina/residential-auction-asset/1590613-6965-8441-NEWFANE-ROAD-CHARLOTTE-NC-28269-E1433" row-index="1">8441 Newfane Road<br>Charlotte, NC, Mecklenburg 28269</a>
    fullAddress     = Field()  # Placeholder
    streetNumber    = Field()  # Placeholder 
    street          = Field()  # Placeholder
    state           = Field()  # Placeholder
    postcode        = Field()  # Placeholder 
    country         = Field()  # Placeholder
    #<li>
    #    <span class="searchResultLabel">Asset Type:</span>
    #    Residential
    #</li>    
    assetType       = Field() # 
    #<li>
    #    <span class="searchResultLabel">Foreclosure/Trustee No:</span>
    #    <span class="singleValue">113081 05187</span>
    #</li>
    ftNum           = Field() # 
    # <li class="highlight">
    #     <span class="searchResultLabel">Property ID:</span>
    #     1590613
    # </li>
    propertyID      = Field()  # <uniqueID>ABCD1234</uniqueID>
    # <li class="highlight">
    #     <span class="searchResultLabel">Item #:</span>
    #     E1433-1803
    # </li>
    itemNum         = Field() # 
    # <div class="dataItem">
    #      Est. Opening Bid:
    #      <span class="highlightedData dataValue">$57,600</span>
    #  </div>
    openingBid      = Field() #

    #   <span class="searchResultLabel">Auction Date:</span>
    #   <span>02/10/2014</span>
    auctionDate     = Field() # 
    # <li>
    #     <span class="searchResultLabel">Sale Location:</span>
    #     Durham County Courthouse - 1st Floor Break Room 510 South Dillard Street NC 27701
    # </li>
    saleLocation     = Field() #
    # <li>
    #     <span class="searchResultLabel">Time:</span>
    #     10:00 am
    # </li>    
    saleTime        = Field() #  
    # <li><span class="label">County</span><span class="value">Mecklenburg</span></li>
    county          = Field()
    # <li><span class="label">Property Type</span><span class="value">SFR</span></li>
    propertyType    = Field()
    # <li><span class="label">Bedrooms</span><span class="value">3.0</span></li>
    bedrooms        = Field()
    # <li><span class="label">Bathrooms</span><span class="value">3.0</span></li>
    bathrooms       = Field()
    # <li><span class="label">Occupancy Status</span><span class="value"></span></li>
    occupancyStatus = Field()
    # <li><span class="label">Lot Size (acres)</span><span class="value">0.14</span></li>
    lotSize         = Field()
    # <li><span class="label">Previously Valued To</span><span class="value">not available</span></li>    
    previousValue   = Field()
    # <a class="searchTrackPDP" href="http://www.auction.com/North Carolina/residential-auction-asset/1466738-6965-6931-SUNMAN-RD-CHARLOTTE-NC-28216-E1433" row-index="2">6931 Sunman Rd<br>Charlotte, NC, Mecklenburg 28216</a>
    datailLink      = Field()
    

################################################
#----- class="contentDetail searchResult" ------
# <div class="contentDetail searchResult" property-id="1466738">
#     <div class="layoutSingle left ultra-wide">
#         <div class="searchResultGalleryData">
#             <p>Item #:</p>
#             <p class="highlightedData">E1433-1102</p>
#             <p>CHARLOTTE, NC</p>
#         </div>
#         <div class="searchResultImageBox">
#             <div class="searchResultImage">
#                 <div class="secondaryAlertBanner hidden"></div>
#                 <a class="searchResultImageLink searchTrackPDP" href="http://www.auction.com/North Carolina/residential-auction-asset/1466738-6965-6931-SUNMAN-RD-CHARLOTTE-NC-28216-E1433" property-id="1466738" row-index="2"><img class="searchResultImage" src="http://cdn.mlhdocs.com/rcp_files/auctions/E-1433/photos/thumbnails/197897937-1_bigThumb.jpg" alt=""></a>
#             </div>
#             <div class="primaryAlertBanner listOnly yellow">Outbid period</div>
#         </div>
#         <ul class="searchResultInfo major"><li class="searchResultAddress"><a class="searchTrackPDP" href="http://www.auction.com/North Carolina/residential-auction-asset/1466738-6965-6931-SUNMAN-RD-CHARLOTTE-NC-28216-E1433" row-index="2">6931 Sunman Rd<br>Charlotte, NC, Mecklenburg 28216</a></li><li>
#         <span class="searchResultLabel">Asset Type:</span>
#         Residential
#     </li><li>
#         <span class="searchResultLabel">Foreclosure/Trustee No:</span>
#         <span class="singleValue">12-026622-FC01</span>
#     </li>
#             <li class="highlight">
#         <span class="searchResultLabel">Property ID:</span>
#         1466738
#     </li>
#             <li class="highlight">
#         <span class="searchResultLabel">Item #:</span>
#         E1433-1102
#     </li>
#         </ul>
#         <div class="clear"></div>
#         <div class="primaryAlertBanner galleryOnly yellow">Outbid period</div>
#     </div>
#     <div class="layoutSingle right">
#         <ul class="searchResultInfo minor">
#         </ul>
#         <ul class="searchResultInfo major"><li class="highlightLarge">
#         <span class="searchResultLabel">Est. Opening Bid:</span>
#         $57,600
#     </li>
#             <li class="highlight">
#         <span class="searchResultLabel">Auction Date:</span>
#         <span>02/10/2014</span>
#     </li><li>
#         <span class="searchResultLabel">Sale Location:</span>
#         Mecklenburg County Courthouse - Main Entrance 832 East Fourth Street NC 28202
#     </li><li>
#         <span class="searchResultLabel">Time:</span>
#         11:00 am
#     </li>
#         </ul>
#     </div>
#     <div class="clear"></div>
#     <div class="buttonRow right">
#         <a class="button small transparent searchPropertySaved" property-id="1466738">Property Saved</a>
#             <a class="button primary small searchSaveProperty" property-id="1466738">Save Now</a>
#             <a class="button blue small searchTrackPDP" href="http://www.auction.com/North Carolina/residential-auction-asset/1466738-6965-6931-SUNMAN-RD-CHARLOTTE-NC-28216-E1433" row-index="2">More Details</a>
#         
#     </div>
#     <div class="galleryDataSection">
#     <div class="dataItem">
#             Est. Opening Bid:
#             <span class="highlightedData dataValue">$57,600</span>
#         </div>
#     
#     </div>
#     <div class="clear"></div>
#     <script type="text/html" id="tooltip-1466738">
#         <div class="propertyHover">
#             <div class="header">
#                     Item #
#                 <span class="itemNo">
#                     E1433-1102
#                 </span>
#                 |
#                 <span class="address">
#                     6931 Sunman Rd Charlotte, NC 28216
#                 </span>
#             </div>
#             <ul class="propertyFields">
#                 <li><span class="label">County</span><span class="value">Mecklenburg</span></li>
#                 <li><span class="label">Property Type</span><span class="value">SFR</span></li>
#                 <li><span class="label">Bedrooms</span><span class="value">3.0</span></li>
#                 <li><span class="label">Bathrooms</span><span class="value">3.0</span></li>
#                 <li><span class="label">Occupancy Status</span><span class="value"></span></li>
#                 <li><span class="label">Lot Size (acres)</span><span class="value">0.14</span></li>
#                 <li><span class="label">Previously Valued To</span><span class="value">not available</span></li>
#             </ul>
#             <div class="clear"></div>
#             <div class="propertyImageBox">
#                 <img class="propertyImage" src="http://cdn.mlhdocs.com/rcp_files/auctions/E-1433/photos/thumbnails/197897937-1_bigThumb.jpg" />
#             </div>
#             
#         </div>
#     </script>
# </div>