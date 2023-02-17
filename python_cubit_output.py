#!python

cubit.cmd('imprint all')
cubit.cmd('merge all')
cubit.cmd('compress all')

#mesh element
mesh_name = "mesh_elements_file"
meshfile = open(mesh_name, 'w')
hex_list = cubit.parse_cubit_list('hex','all')
num_elems = len(hex_list)
print('total number of elements:', str(num_elems))
meshfile.write(str(num_elems) + '\n')
for hexa in hex_list:
    nodes = cubit.get_connectivity('hex', hexa)
    txt = str(hexa) + ' ' + ' '.join(str(x) for x in nodes) + '\n'
    meshfile.write(txt)
meshfile.close()
print('Finish output element file to mesh_elements')

#mesh_node
node_name = "nodes_coords_file"
nodecoord = open(node_name, 'w')
node_list = cubit.parse_cubit_list('node', 'all')
num_nodes = len(node_list)
print('number of nodes:', str(num_nodes))
nodecoord.write(str(num_nodes) + '\n')
for node in node_list:
    x, y, z = cubit.get_nodal_coordinates(node)
    #txt = str(node) + ' ' + str(x) + ' ' + str(y) + ' ' + str(z) + '\n'
    #txt = ('%10i %20f %20f %20f\n') % (node, x, y, z)
    txt = ('%10i %20.4f %20.4f %20.4f\n') % (node, x, y, z)
    nodecoord.write(txt)
nodecoord.close()
print('Finish output node file to mesh_nodes')


#boundary surfaces (elements and x,y,z min &max)


#fault surfaces (elements and normal vector)


#PML layers (x,y,z min &max)
