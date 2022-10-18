import pygame
from graph import preprocess_graph
from constants import IMG_NAME, OFFSET_LABEL_X_NAME, OFFSET_LABEL_X_TYPE,\
    OFFSET_LABEL_Y_TYPE, OFFSET_LABEL_Y_NAME, WIDTH_DISPLAY, HEIGHT_DISPLAY, MARGIN_DISPLAY,\
    IMG_SIZE, DEVIATION_FACTOR, WHITE_COLOR, BLACK_COLOR, CAPTION, HELVETICA_FONT_SIZE_NAME,\
    HELVETICA_FONT_SIZE_TYPE


NUM_VERT = 8
EDGES = [[0, 1], [2, 3], [1, 2], [1, 3], [4, 2], [4, 5], [6, 7], [7, 5]]
TYPES = ["H", "H", "P", "H", "H", "P", "H", "H"]
NAMES = ["hab1", "hab2", "pas1", "hab3", "hab4", "paaaaaa2", "hab5", "hab6"]


class Simulation(object):
    '''Class for the house simulation'''

    def __init__(self, num_vert, edges, types, names):
        node_coords = preprocess_graph(IMG_NAME, num_vert, edges, types, names)

        self.node_coords = node_coords
        self.name_type = {}

        for i in range(len(types)):
            self.name_type.update({names[i]:types[i]})


    def run(self):
        '''Runs the simulation'''

        pygame.init()

        display_surface = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))
        display_surface.fill(WHITE_COLOR)
        pygame.display.set_caption(CAPTION)

        center_img = pygame.image.load(r'images/BaseRoom.png')
        house_img = pygame.image.load(r'house_graph.png')

        display_surface.blit(house_img, (0, 0))
        pygame.draw.line(display_surface, BLACK_COLOR, (HEIGHT_DISPLAY,0),
            (HEIGHT_DISPLAY,HEIGHT_DISPLAY), 5)

        self.mark_centers(display_surface, center_img)
        self.add_labels(display_surface)

        running = True

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()


    def mark_centers(self, display_surface, center_img):
        '''Adds an image in the center of each node'''

        max_row, max_col = self.get_max_row_col_coords()
        for coords in self.node_coords.values():
            if coords[1] < max_row:
                display_surface.blit(center_img,
                    ((MARGIN_DISPLAY + (IMG_SIZE/max_row) * coords[0]) \
                        - DEVIATION_FACTOR * coords[0],
                    (MARGIN_DISPLAY + (IMG_SIZE/max_col) * coords[1]) \
                        - DEVIATION_FACTOR * coords[1]))
            else:
                if [coords[0],coords[1]] in self.node_coords.values():
                    display_surface.blit(center_img,
                    ((MARGIN_DISPLAY + (IMG_SIZE/max_row) * coords[0]) \
                        - DEVIATION_FACTOR * coords[0],
                    (MARGIN_DISPLAY + (IMG_SIZE/max_col) * coords[1]) \
                        - DEVIATION_FACTOR * coords[1]))


    def add_labels(self, display_surface):
        '''Adds the necessary labels to the simulation'''

        max_row, max_col = self.get_max_row_col_coords()

        for name, coords in self.node_coords.items():

            # Type labels
            helvetica_font = pygame.font.SysFont('helvetica', HELVETICA_FONT_SIZE_TYPE)
            type_room = self.name_type[name]
            type_label = helvetica_font.render(type_room, HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)

            first_coord = (MARGIN_DISPLAY + (IMG_SIZE/max_row) * coords[0]) \
                - DEVIATION_FACTOR * coords[0] + OFFSET_LABEL_X_TYPE
            second_coord = (MARGIN_DISPLAY + (IMG_SIZE/max_col) * coords[1]) \
                - DEVIATION_FACTOR * coords[1] + OFFSET_LABEL_Y_TYPE

            display_surface.blit(type_label, (first_coord, second_coord))

            # Name labels
            if len(name) > 7:
                name = name[:6] + '...'

            helvetica_font = pygame.font.SysFont('helvetica', HELVETICA_FONT_SIZE_NAME)
            name_label = helvetica_font.render(name, HELVETICA_FONT_SIZE_NAME, BLACK_COLOR)

            first_coord = (MARGIN_DISPLAY + (IMG_SIZE/max_row) * coords[0]) \
                - DEVIATION_FACTOR * coords[0] + OFFSET_LABEL_X_NAME
            second_coord = (MARGIN_DISPLAY + (IMG_SIZE/max_col) * coords[1]) \
                - DEVIATION_FACTOR * coords[1] + OFFSET_LABEL_Y_NAME

            display_surface.blit(name_label, (first_coord, second_coord))


    def get_max_row_col_coords(self):
        '''Gets the number of rows and columns in the graph'''

        max_row = 0
        max_col = 0

        for coords in self.node_coords.values():
            if coords[0] > max_row:
                max_row = coords[0]

            if coords[1] > max_col:
                max_col = coords[1]

        return max_row, max_col


if __name__ == "__main__":
    sim = Simulation(NUM_VERT, EDGES, TYPES, NAMES)
    sim.run()
