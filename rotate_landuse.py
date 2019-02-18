#!/usr/bin/python
# -*- coding: utf8 -*-

import iris
import cartopy.crs as ccrs
import iris.quickplot as qplt
import matplotlib.pyplot as plt
import sys


def get_landuse_fraction(site,landuse,lat_site,lon_site,show_plot='yes',frac_file_location = '/storage/shared/research/met/micromet/JULES/Marine/Landuse/qrparm.veg.frac.LONDON.nc.cf'):
    """
    Produces a fraction of land use from 9 tiles: Can give all tiles or a specified tile.
    :param site: site choice as a string.
    :param landuse: Name of the tile which you want the land use for, as a string. Can be:
    broadleaf, needleleaf, C3, C4, shrubs, urban, lake, soil, ice or all for a list of all in <- that order.
    :return: fraction of land use requested. int if 1 type, list if all types.
    """

    # index of land use choices:
    if landuse == 'broadleaf':
        landuse_index = 0
    elif landuse == 'needleleaf':
        landuse_index = 1
    elif landuse == 'C3':
        landuse_index = 2
    elif landuse == 'C4':
        landuse_index = 3
    elif landuse == 'shrubs':
        landuse_index = 4
    elif landuse == 'urban':
        landuse_index = 5
    elif landuse == 'lake':
        landuse_index = 6
    elif landuse == 'soil':
        landuse_index = 7
    elif landuse == 'ice':
        landuse_index = 8
    elif landuse == 'all':
        pass
    else:
#        print 'The landuse option chosen does not exist. Choose again from: '
#        print 'broadleaf, needleleaf, C3, C4, shrubs, urban, lake, soil, ice or all'
        sys.exit()

    # imports the lon and lat in WGS84 from the variables.py dictionary. format [lon, lat].
    #loc = site_location[site]
    # X = LON, Y = LAT
    #x_old = loc[0]  # lon
    #y_old = loc[1]  # lat
    x_old = lon_site  # lon
    y_old = lat_site  # lat

    # PATH TO .FRAC FILE
    #frac_file_location = '/storage/shared/research/met/micromet/JULES/Marine/Landuse/qrparm.veg.frac.LONDON.nc.cf'

    # LOAD AS A CUBE
    cube = iris.load_cube(frac_file_location)
#    print ' '
#    print cube
#    print ' '

    # PLOTS TOTAL UK CUBE
    if landuse == 'all':
        landuse_list = ['broadleaf', 'needleleaf', 'C3', 'C4', 'shrubs', 'urban', 'lake', 'soil', 'ice']
        count = 0
        for item in landuse_list:
	    if show_plot=='yes':
            	plt.figure(figsize=(10, 20))
            	qplt.pcolormesh(cube[count, :, :], vmin=0, vmax=1, cmap='jet')
            	plt.gca().coastlines()
            	plt.title(item)
            	#plt.savefig('../plots/landuse_plots/' + 'whole_uk_' + item + '.png')
            	count += 1
    else:
	if show_plot=='yes':
            plt.figure(figsize=(10, 20))
            qplt.pcolormesh(cube[landuse_index, :, :], vmin=0, vmax=1, cmap='jet')
            plt.gca().coastlines()
            plt.title(landuse)
            #plt.savefig('../../plots/landuse_plots/' + 'whole_uk_' + landuse + '.png')


    # FINDS THE CLOSEST COORDINATES TO THE NEW X & Y IN THE MO FILE
    latitudes = cube.coord('latitude')
    longitudes = cube.coord('longitude')
 #   print latitudes
  #  print longitudes
    nearest_lat = latitudes.nearest_neighbour_index(y_old)
    nearest_lon = longitudes.nearest_neighbour_index(x_old)
#    print ' '
#    print 'index of nearest lat: ', nearest_lat
#    print 'index of nearest lon: ', nearest_lon

#    print ' '
#    print 'comparing closest coordinates to site:'
#    print 'LON:'
#    print 'site lon: ', x_old
#    print 'one less, closest, one more:'
#    print longitudes[nearest_lon - 1]
#    print longitudes[nearest_lon]
#    print longitudes[nearest_lon + 1]
#    print ' '
#    print 'LAT'
#    print 'site lat: ', y_old
#    print 'one less, closest, one more:'
#    print latitudes[nearest_lat - 1]
#    print latitudes[nearest_lat]
#    print latitudes[nearest_lat + 1]

    # CONSTRAINT
    # EXTRACTS INTEGERS FROM THE NEAREST VALUES FOR THE CONSTRAINT:
    lat_value = latitudes.cell(nearest_lat)
    lon_value = longitudes.cell(nearest_lon)
    #print 'lat_value',lat_value
    #print 'lon_value',lon_value
    gcon = iris.Constraint(coord_values={'latitude': lat_value,
                                         'longitude': lon_value})
    extracted = cube.extract(gcon)
    #print ' '
    #print extracted
    #print ' '

    #print 'sum of all fractions (should be 1): ', sum(extracted.data)

    if landuse == 'all':
     #   print 'All landuse: ', extracted.data
        return extracted.data
    else:
      #  print landuse, 'fraction: ', extracted.data[landuse_index]
        return extracted.data[landuse_index]






#toto=get_landuse_fraction('London','all',51.609375,-0.073125)

#print toto
#print ['broadleaf', 'needleleaf', 'C3', 'C4', 'shrubs', 'urban', 'lake', 'soil', 'ice']
#print sum(toto)

#plt.show()


# use if wanting to extract an area:
# ----------------------------------------------------------------------------------------------------------------------
# xu_3 = loc[0]            # lon
# yu_1 = loc[1]            # lat
# xu_4 = loc[0]+0.04       # lon
# yu_2 = loc[1]+0.04       # lat

# rot_pole1 = cube.coord('grid_latitude').coord_system.as_cartopy_crs()
# ll = ccrs.Geodetic()
#
# target_xy1 = rot_pole1.transform_point(xu_3, yu_1, ll) # lower left corner
# x_3 = target_xy1[0] + 360.
# y_1 = target_xy1[1]
# target_xy1 = rot_pole1.transform_point(xu_4, yu_2, ll) # upper right corner
# x_4 = target_xy1[0] + 360.
# y_2 = target_xy1[1]
#
# print x_3
# print y_1
#
# # variables to constraint the loaded variable. Attributes need to be contraint in a different way.
# gcon = iris.Constraint(coord_values={'grid_latitude':lambda cell: y_1 < cell < y_2,
#                                      'grid_longitude':lambda cell: x_3 < cell < x_4})
#
#
# extracted = cube.extract(gcon)
#
# print ' '
# print extracted
# print ' '
#
#
# print extracted.data

# plt.figure(figsize=(10, 20))
# qplt.pcolormesh(extracted[5, 0, 0], vmin=0, vmax=1)
# plt.savefig('ree2.png')

# ----------------------------------------------------------------------------------------------------------------------

# SYLVIA:
# # variables to constraint the loaded variable. Attributes need to be contraint in a different way.
# # See below for stash QH example.
# gcon = iris.Constraint(coord_values={'grid_latitude':lambda cell: y_1 < cell < y_2,
#                                      'grid_longitude':lambda cell: x_3 < cell < x_4})
#
#
#
# if variable == 'QH':
#     hcon = iris.Constraint(coord_values={'grid_latitude':lambda cell: y_1 < cell < y_2,
#                                          'grid_longitude':lambda cell: x_3 < cell < x_4})
# elif variable == 'Tair':
#     hcon = iris.Constraint(coord_values={'grid_latitude':lambda cell: y_1 < cell < y_2,
#                                          'grid_longitude':lambda cell: x_3 < cell < x_4})
#     levcon = iris.Constraint(model_level_number = 1)
