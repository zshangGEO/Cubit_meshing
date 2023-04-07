#boundary surfaces (elements and x,y,z min &max)
surfaces_xmin = [26, 35, 41, 45]
surfaces_xmax = [32, 37, 42, 47]
surfaces_ymin = [40, 44]
surfaces_ymax = [36, 46]
surfaces_zmin = [43]
surfaces_zmax = [4, 10, 14, 23, 28, 33, 38]
#xmin boundary surfaces (left)
surface_nodes = cubit.get_surface_nodes(surfaces_xmin[0])
x, y, z = cubit.get_nodal_coordinates(surface_nodes[0])
xmin = x
#xmax boundary surfaces (right)
xmax = xmin + cubit.get_distance_between_entities("surface",surfaces_xmin[0],"surface",surfaces_xmax[0])
#ymin boundary surfaces (front)
surface_nodes = cubit.get_surface_nodes(surfaces_ymin[0])
x, y, z = cubit.get_nodal_coordinates(surface_nodes[0])
ymin = y
#ymax boundary surfaces (back)
ymax = ymin + cubit.get_distance_between_entities("surface",surfaces_ymin[0],"surface",surfaces_ymax[0])
#zmin boundary surfaces (bottom)
surface_nodes = cubit.get_surface_nodes(surfaces_zmin[0])
x, y, z = cubit.get_nodal_coordinates(surface_nodes[0])
zmin = z
#zmax boundary surfaces (top)
zmax = zmin + cubit.get_distance_between_entities("surface",surfaces_zmin[0],"surface",surfaces_zmax[0])      
#Output the boundary surface minimum and maximum valuse   
boundary_file = "boundary" + ".dat"
fboundary_file = open(boundary_file, 'w') 
fboundary_file.write('x boundary coordinates at minmum and maximum' + '\n') 
fboundary_file.write(str(xmin) + ' ' + str(xmax) + '\n') 
fboundary_file.write('y boundary coordinates at minmum and maximum' + '\n') 
fboundary_file.write(str(ymin) + ' ' + str(ymax) + '\n') 
fboundary_file.write('z boundary coordinates at minmum and maximum' + '\n') 
fboundary_file.write(str(zmin) + ' ' + str(zmax) + '\n')
fboundary_file.close()
print('Finish output boundary files')

#PML layers (x,y,z min &max)
#x left PML
xlm_surface = [26, 1]
#x left min and max
xlmin = xmin
xlmax = xlmin + cubit.get_distance_between_entities("surface",xlm_surface[0],"surface",xlm_surface[1])
#x right PML
xrm_surface = [2, 32]
#x right min and max
xrmax = xmax
xrmin = xrmax - cubit.get_distance_between_entities("surface",xrm_surface[0],"surface",xrm_surface[1])
#y fron PML
yfm_surface = [40, 7, 11, 13, 19, 25, 30]
#y fron min and max
yfmin = ymin
yfmax = yfmin + cubit.get_distance_between_entities("surface",yfm_surface[0],"surface",yfm_surface[1])
#y back PML
ykm_surface = [36, 5, 9, 15, 21, 27, 31]
#y back min and max
ykmax = ymax 
ykmin = ymax - cubit.get_distance_between_entities("surface",ykm_surface[0],"surface",ykm_surface[1])
#z top PML
#z top min and max
#z bottom PML
zbm_surface = [43, 18, 24, 29, 34, 39]
#z bottom min and max
zbmin = zmin
zbmax = zmin + cubit.get_distance_between_entities("surface",zbm_surface[0],"surface",zbm_surface[1])
#Output the PML surface minimum and maximum valuse   
pml_file = "pml" + ".dat"
fpml_file = open(pml_file, 'w') 
fpml_file.write('x PML coordinates at minmum and maximum of left and right sides' + '\n') 
fpml_file.write(str(xlmin) + ' ' + str(xlmax) + '\n') 
fpml_file.write(str(xrmin) + ' ' + str(xrmax) + '\n') 
fpml_file.write('y PML coordinates at minmum and maximum of front and back sides' + '\n') 
fpml_file.write(str(yfmin) + ' ' + str(yfmax) + '\n') 
fpml_file.write(str(ykmin) + ' ' + str(ykmax) + '\n') 
fpml_file.write('z PML coordinates at minmum and maximum of bottom side' + '\n') 
fpml_file.write(str(zbmin) + ' ' + str(zbmax) + '\n')
fpml_file.close()
print('Finish output PML files')
