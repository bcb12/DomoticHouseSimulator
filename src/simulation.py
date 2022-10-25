import pygame
from graph import preprocess_graph
from constants import IMG_NAME, OFFSET_ICON_Y, OFFSET_LABEL_X_NAME, OFFSET_LABEL_X_TYPE,\
    OFFSET_LABEL_Y_TYPE, OFFSET_LABEL_Y_NAME, OFFSET_VIEW_X, ROOM_FULL_SIZE, WIDTH_DISPLAY,\
    IMG_SIZE, DEVIATION_FACTOR, WHITE_COLOR, BLACK_COLOR, CAPTION, HEIGHT_DISPLAY,\
    HELVETICA_FONT_SIZE_TYPE, HELVETICA_FONT_SIZE_NAME, ROOM_OFFSET, MARGIN_DISPLAY


NUM_VERT = 8
EDGES = [[0, 1], [2, 3], [1, 2], [1, 3], [4, 2], [4, 5], [6, 7], [7, 5]]
TYPES = ["H", "H", "P", "H", "H", "P", "H", "H"]
NAMES = ["hab1", "hab2", "pas1", "hab3", "hab4", "aaaaaaa2", "hab5", "hab6"]


class Simulation(object):
    '''Class for the house simulation'''

    def __init__(self, num_vert, edges, types, names):
        node_coords = preprocess_graph(IMG_NAME, num_vert, edges, types, names)

        self.node_coords = node_coords
        self.name_type = {}
        self.room_coords = {}
        self.viewing = {}
        self.presence = {}

        self.edges = edges

        for i in range(len(names)):
            self.name_type.update({names[i]:types[i]})
            self.presence.update({names[i]:False})

            if i == 0:
                self.viewing.update({names[i]:True})
            else:
                self.viewing.update({names[i]:False})


    def run(self):
        '''Runs the simulation'''

        pygame.init()

        display_surface = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY))
        display_surface.fill(WHITE_COLOR)
        pygame.display.set_caption(CAPTION)

        # Load images
        center_img = pygame.image.load(r'images/BaseRoom.png')
        view_img = pygame.image.load(r'images/Preview.png')
        presence_img = pygame.image.load(r'images/Presence.png')
        blank_img = pygame.image.load(r'images/Blank.png')
        house_img = pygame.image.load(r'house_graph.png')

        display_surface.blit(house_img, (0, 0))
        pygame.draw.line(display_surface, BLACK_COLOR, (HEIGHT_DISPLAY,0),
            (HEIGHT_DISPLAY,HEIGHT_DISPLAY), 5)

        # Preprocess display
        self.mark_centers(display_surface, center_img)
        self.add_labels(display_surface)

        running = True

        while running:
            # Check marked cells
            self.check_viewing(display_surface, view_img, blank_img)
            self.check_presence(display_surface, presence_img, blank_img)

            for event in pygame.event.get():
                # After clicking
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_presses = pygame.mouse.get_pressed()

                    if mouse_presses[0]:
                        # Getting room coordinates after left click
                        rows, columns = self.get_row_col()
                        position = pygame.mouse.get_pos()
                        actual_x = (position[0] - ROOM_OFFSET) \
                            / ((IMG_SIZE - MARGIN_DISPLAY + DEVIATION_FACTOR)/rows)
                        actual_y = (position[1] - ROOM_OFFSET) \
                            / ((IMG_SIZE - MARGIN_DISPLAY + DEVIATION_FACTOR)/columns)

                        actual_x = round(actual_x)
                        actual_y = round(actual_y)

                        desired_name = None
                        for name, coords in self.node_coords.items():
                            if coords == [actual_x, actual_y]:
                                desired_name = name

                        if desired_name is not None:
                            selected_coords = self.room_coords[desired_name]

                            # View cell
                            if position[0] >= selected_coords[0] + OFFSET_VIEW_X and \
                                position[0] <= selected_coords[0] + OFFSET_VIEW_X * 2 and \
                                position[1] >= selected_coords[1] + OFFSET_ICON_Y and \
                                position[1] <= selected_coords[1] + ROOM_FULL_SIZE:

                                current_name = None
                                for name_it, current_bool in self.viewing.items():
                                    if current_bool:
                                        current_name = name_it

                                if self.is_possible_move(self.node_coords[current_name],[actual_x,actual_y]):
                                    self.reset_view()
                                    self.viewing[desired_name] = True

                            # Presence cell
                            if position[0] >= selected_coords[0] and \
                                position[0] <= selected_coords[0] + OFFSET_VIEW_X and \
                                position[1] >= selected_coords[1] + OFFSET_ICON_Y and \
                                position[1] <= selected_coords[1] + ROOM_FULL_SIZE:

                                if self.presence[desired_name] is True:
                                    self.presence[desired_name] = False
                                else:
                                    self.presence[desired_name] = True


                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()


    def mark_centers(self, display_surface, center_img):
        '''Adds an image in the center of each node'''

        rows, columns = self.get_row_col()
        for name, coords in self.node_coords.items():
            first_coord = ROOM_OFFSET + \
                ((IMG_SIZE - MARGIN_DISPLAY + DEVIATION_FACTOR)/rows) * coords[0]
            second_coord = ROOM_OFFSET + \
                ((IMG_SIZE - MARGIN_DISPLAY + DEVIATION_FACTOR)/columns) * coords[1]

            display_surface.blit(center_img, (first_coord, second_coord))

            self.room_coords.update({name:[first_coord,second_coord]})


    def add_labels(self, display_surface):
        '''Adds the necessary labels to the simulation'''

        rows, columns = self.get_row_col()

        for name, coords in self.node_coords.items():

            # Type labels
            helvetica_font = pygame.font.SysFont('helvetica', HELVETICA_FONT_SIZE_TYPE)
            type_room = self.name_type[name]
            type_label = helvetica_font.render(type_room, HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)

            first_coord = ROOM_OFFSET + ((IMG_SIZE - MARGIN_DISPLAY + DEVIATION_FACTOR)/rows) \
                * coords[0] + OFFSET_LABEL_X_TYPE
            second_coord = ROOM_OFFSET + ((IMG_SIZE - MARGIN_DISPLAY + DEVIATION_FACTOR)/columns) \
                * coords[1] + OFFSET_LABEL_Y_TYPE

            display_surface.blit(type_label, (first_coord, second_coord))

            # Name labels
            if len(name) > 7:
                name = name[:6] + '...'

            helvetica_font = pygame.font.SysFont('helvetica', HELVETICA_FONT_SIZE_NAME)
            name_label = helvetica_font.render(name, HELVETICA_FONT_SIZE_NAME, BLACK_COLOR)

            first_coord = ROOM_OFFSET + ((IMG_SIZE - MARGIN_DISPLAY + DEVIATION_FACTOR)/rows) \
                * coords[0] + OFFSET_LABEL_X_NAME
            second_coord = ROOM_OFFSET + ((IMG_SIZE - MARGIN_DISPLAY + DEVIATION_FACTOR)/columns) \
                * coords[1] + OFFSET_LABEL_Y_NAME

            display_surface.blit(name_label, (first_coord, second_coord))


    def get_row_col(self):
        '''Gets the number of rows and columns in the graph'''

        rows = 0
        columns = 0

        for coords in self.node_coords.values():
            if coords[0] > rows:
                rows = coords[0]

            if coords[1] > columns:
                columns = coords[1]

        return rows, columns


    def check_viewing(self, display_surface, view_img, blank_img):
        '''Adds a view icon to whatever room is being watched'''

        for name, coords in self.room_coords.items():
            if self.viewing[name]:
                display_surface.blit(view_img, (coords[0] + OFFSET_VIEW_X, \
                    coords[1] + OFFSET_ICON_Y))
            else:
                display_surface.blit(blank_img, (coords[0] + OFFSET_VIEW_X, \
                    coords[1] + OFFSET_ICON_Y))


    def check_presence(self, display_surface, presence_img, blank_img):
        '''Adds a presence icon to a room'''

        for name, coords in self.room_coords.items():
            if self.presence[name]:
                display_surface.blit(presence_img, (coords[0], coords[1] + OFFSET_ICON_Y))
            else:
                display_surface.blit(blank_img, (coords[0], coords[1] + OFFSET_ICON_Y))


    def reset_view(self):
        '''Sets every value in the viewing dictionaire to false'''

        for name in self.viewing.keys():
            self.viewing[name] = False


    def is_possible_move(self, current, target):
        '''Checks if a move is possible to do'''

        coords = []
        for value in self.node_coords.values():
            coords.append(value)

        ind_1 = coords.index(current)
        ind_2 = coords.index(target)

        return [ind_1,ind_2] in self.edges or [ind_2,ind_1] in self.edges


if __name__ == "__main__":
    sim = Simulation(NUM_VERT, EDGES, TYPES, NAMES)
    sim.run()
