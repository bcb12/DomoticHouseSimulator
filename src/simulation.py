import pygame
from graph import create_graph, pad_img


WIDTH = 900
HEIGHT = 900
MARGIN = 48
NODE_RAD = 21
IMG_SIZE = 600
DEVIATION_FACTOR = 20

WHITE_COLOR = (255,255,255)

CAPTION = "Simulación de la casa"

NUM_VERT = 8
EDGES = [[0, 1], [2, 3], [1, 2], [1, 3], [4, 2], [4, 5], [6, 7], [7, 5]]
TYPES = ["H", "H", "P", "H", "H", "P", "H", "H"]
NAMES = ["hab1", "hab2", "pas1", "hab3", "hab4", "pas2", "hab5", "hab6"]


class Simulation(object):
    '''Class for the house simulation'''

    def __init__(self, num_vert, edges, types, names):
        img_name, node_coords = create_graph("house_graph.png",
            num_vert, edges, types, names)
        pad_img(img_name)

        self.node_coords = node_coords


    def run(self):
        '''Runs the simulation'''

        pygame.init()

        display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        display_surface.fill(WHITE_COLOR)
        pygame.display.set_caption(CAPTION)

        center_img = pygame.image.load(r'pm.png')
        house_img = pygame.image.load(r'house_graph.png')

        running = True

        while running:
            display_surface.blit(house_img, (0, 0))

            self.mark_centers(display_surface, center_img)

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
                    ((MARGIN + (IMG_SIZE/max_row) * coords[0]) - DEVIATION_FACTOR * coords[0],
                    (MARGIN + (IMG_SIZE/max_col) * coords[1]) - DEVIATION_FACTOR * coords[1]))
            else:
                if [coords[0],coords[1]] in self.node_coords.values():
                    display_surface.blit(center_img,
                    ((MARGIN + (IMG_SIZE/max_row) * coords[0]) - DEVIATION_FACTOR * coords[0],
                    (MARGIN + (IMG_SIZE/max_col) * coords[1]) - DEVIATION_FACTOR * coords[1]))

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
