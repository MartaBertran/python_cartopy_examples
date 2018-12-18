# ADDING DATA TO THE MAP (Using Cartopy with Matplotlib)
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

# Plot basic map with PlateCarree() projection and default background
ax = plt.axes(projection=ccrs.PlateCarree())
ax.stock_img()

# Define longitudes and latitudes for New York
ny_lon, ny_lat = -75, 43
# Define longitudes and latitudes for Delhi
delhi_lon, delhi_lat = 77.23, 28.61

# Plot a blue line between the two cities following the shape of the Earth (Geodetic)
plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat], color='blue', linewidth=2, marker='o', transform=ccrs.Geodetic(),)

# Plot a straight grey line between the two cities 
plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat], color='gray', linestyle='--', transform=ccrs.PlateCarree(),)

# Plot a the name of the cities, adding some integers to longitudes and latitudes so that the text is not overlapped with the lines

plt.text(ny_lon - 3, ny_lat - 12, 'New York',
         horizontalalignment='right',
         transform=ccrs.Geodetic())

plt.text(delhi_lon + 3, delhi_lat - 12, 'Delhi',
         horizontalalignment='left',
         transform=ccrs.Geodetic())

# Display the final plot
plt.show()
