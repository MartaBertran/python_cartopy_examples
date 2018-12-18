# MAPS PROJECTIONS (using cartopy with matplotlib)
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

# Define projection
ax = plt.axes(projection=ccrs.Mollweide())
# The stock_img() method adds an underlay image to the map. 
# For the cartopy library, the default option is a downsampled version of the Natural Earth shaded relief raster. 
# The source code can be found at https://scitools.org.uk/cartopy/docs/latest/_modules/cartopy/mpl/geoaxes.html#GeoAxes.stock_img
ax.stock_img()

# Display the plot
plt.show()
