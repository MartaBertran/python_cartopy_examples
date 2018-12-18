# MAPS PROJECTIONS (using cartopy with matplotlib)
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

# Define projection
ax = plt.axes(projection=ccrs.Mollweide())
# Define a background
ax.stock_img()

# Display the plot
plt.show()
