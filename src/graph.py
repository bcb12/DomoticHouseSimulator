import igraph as ig
from PIL import Image, ImageOps
from constants import RESIZE_VALUE, VERTEX_SIZE, VERTEX_FRAME_WIDTH, VERTEX_LABEL_SIZE,\
    EDGE_WIDTH, MARGIN, IMG_NAME


def create_graph(num_vert, edges, types, names):
    '''Generates an image containing the graph representation'''

    graph = ig.Graph(num_vert, edges)
    graph.vs["type"] = types
    graph.vs["name"] = names

    lay = graph.layout(layout='grid')

    ig.plot(
        graph,
        target = IMG_NAME,
        layout = lay,
        vertex_size = VERTEX_SIZE,
        vertex_color = "lightblue",
        vertex_frame_width = VERTEX_FRAME_WIDTH,
        vertex_frame_color = "white",
        vertex_label = graph.vs["name"],
        vertex_label_size = VERTEX_LABEL_SIZE,
        edge_width = EDGE_WIDTH,
        edge_color = "black",
    )

    node_coords = {}

    for vert in range(num_vert):
        node_coords.update({graph.vs["name"][vert]:lay.coords[vert]})

    return node_coords


def pad_img(img_name):
    '''Adds margins to a given image'''

    img = Image.open(img_name)
    img_with_border = ImageOps.expand(img, border = MARGIN, fill = 'white')
    img_with_border.save(img_name)


def resize_img(img_name):
    '''Resizes a given image'''

    img = Image.open(img_name)
    img_resize = img.resize(RESIZE_VALUE)
    img_resize.save(img_name)


def preprocess_graph(img_name, num_vert, edges, types, names):
    '''Preprocesses a graph to output an image'''

    node_coords = create_graph(num_vert, edges, types, names)
    pad_img(img_name)
    resize_img(img_name)

    return node_coords
