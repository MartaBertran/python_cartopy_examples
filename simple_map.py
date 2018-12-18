# SIMPLE MAP (using cartopy with matplotlib)
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

# Define projection
ax = plt.axes(projection=ccrs.PlateCarree())

# Draw coastlines
ax.coastlines()

# Save the plot by calling plt.savefig() BEFORE  plt.show()
# Save the plot as a pdf file
plt.savefig('coastlines.pdf')
# Save the plot as a png file
plt.savefig('coastlines.png')

# Display the plot
plt.show()
