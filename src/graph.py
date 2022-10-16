import igraph as ig
import cv2
from PIL import Image, ImageOps


def create_graph(img_name, num_vert, edges, types, names):
    '''Generates an image containing the graph representation'''

    graph = ig.Graph(num_vert, edges)
    graph.vs["type"] = types
    graph.vs["name"] = names

    lay = graph.layout(layout='grid')

    ig.plot(
        graph,
        target = img_name,
        layout = lay,
        vertex_size = 42,
        vertex_color = "lightblue",
        vertex_frame_width = 4.0,
        vertex_frame_color = "white",
        vertex_label = graph.vs["name"],
        vertex_label_size = 1.0,
        edge_width = 4,
        edge_color = "black",
    )

    node_coords = {}

    for vert in range(num_vert):
        node_coords.update({graph.vs["name"][vert]:lay.coords[vert]})

    return img_name, node_coords


def pad_img(img_name):
    '''Adds margins to a given image'''

    img = Image.open(img_name)
    img_with_border = ImageOps.expand(img, border = 50, fill = 'white')
    img_with_border.save(img_name)
