import pygame
from graph import preprocess_graph
from constants import IMG_NAME, OFFSET_ICON_Y, OFFSET_LABEL_X_NAME, OFFSET_LABEL_X_TYPE,\
    OFFSET_LABEL_Y_TYPE, OFFSET_LABEL_Y_NAME, OFFSET_VIEW_X, ROOM_FULL_SIZE, WIDTH_DISPLAY,\
    IMG_SIZE, DEVIATION_FACTOR, WHITE_COLOR, BLACK_COLOR, CAPTION, HEIGHT_DISPLAY,\
    HELVETICA_FONT_SIZE_TYPE, HELVETICA_FONT_SIZE_NAME, ROOM_OFFSET, MARGIN_DISPLAY
from ExampleRooms import ROOMS, NAMES, GLOBAL_SENSORS, GLOBAL_ACTUATORS


NUM_VERT = 8
EDGES = [[0, 1], [2, 3], [1, 2], [1, 3], [4, 2], [4, 5], [6, 7], [7, 5]]
TYPES = ["H", "H", "P", "H", "H", "P", "H", "H"]
ROOMS_USED = ROOMS
NAMES_USED = NAMES


class Simulation(object):
    '''Class for the house simulation'''

    def __init__(self, num_vert, edges, types, names, rooms):
        node_coords = preprocess_graph(IMG_NAME, num_vert, edges, types, names)

        self.node_coords = node_coords
        self.name_type = {}
        self.name_room = {}
        self.room_coords = {}
        self.viewing = {}
        self.presence = {}

        self.names = names
        self.edges = edges

        for i in range(len(names)):
            self.name_type.update({names[i]:types[i]})
            self.name_room.update({names[i]:rooms[i]})

            if i == 0:
                self.viewing.update({names[i]:True})
                self.presence.update({names[i]:True})
            else:
                self.viewing.update({names[i]:False})
                self.presence.update({names[i]:False})


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
        pygame.draw.line(display_surface, BLACK_COLOR, (WIDTH_DISPLAY/2, HEIGHT_DISPLAY/3),
            (WIDTH_DISPLAY, HEIGHT_DISPLAY/3), 5)
        pygame.draw.line(display_surface, BLACK_COLOR, (WIDTH_DISPLAY/2, HEIGHT_DISPLAY/3*2),
            (WIDTH_DISPLAY, HEIGHT_DISPLAY/3*2), 5)

        # Preprocess display
        self.name_room[self.names[0]].presence = True
        self.mark_centers(display_surface, center_img)
        self.add_labels(display_surface)
        self.print_info(display_surface)

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

                                self.reset_view()
                                self.viewing[desired_name] = True

                                #TODO: remove info
                                self.print_info(display_surface)

                            # Presence cell
                            if position[0] >= selected_coords[0] and \
                                position[0] <= selected_coords[0] + OFFSET_VIEW_X and \
                                position[1] >= selected_coords[1] + OFFSET_ICON_Y and \
                                position[1] <= selected_coords[1] + ROOM_FULL_SIZE:

                                current_presence = None
                                for name_it, current_bool in self.presence.items():
                                    if current_bool:
                                        current_presence = name_it

                                if self.is_possible_move(
                                        self.node_coords[current_presence],[actual_x,actual_y]):
                                    self.reset_presence()

                                    self.presence[desired_name] = True
                                    self.name_room[desired_name].presence = True

                                    #TODO: remove info
                                    self.print_info(display_surface)


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


    def print_info(self, display_surface):
        '''Prints in the right part of the screen the necessary info'''

        helvetica_font = pygame.font.SysFont('helvetica', HELVETICA_FONT_SIZE_TYPE, bold = True)

        variables_label = helvetica_font.render('Variables', HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)
        sensors_label = helvetica_font.render('Sensores', HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)
        actuators_label = helvetica_font.render('Actuadores', HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)

        display_surface.blit(variables_label, (850, 10))
        display_surface.blit(sensors_label, (850, 212))
        display_surface.blit(actuators_label, (850, 412))

        self.print_variables(display_surface)
        self.print_sensors(display_surface)
        self.print_actuators(display_surface)


    def print_variables(self, display_surface):
        '''Prints in the right part the information regarding variables'''

        helvetica_font = pygame.font.SysFont('helvetica', HELVETICA_FONT_SIZE_TYPE-5)

        current_room = ''
        for name, value in self.viewing.items():
            if value:
                current_room = name

        room = self.name_room[current_room]
        
        name_label = helvetica_font.render('Habitación: ' + room.id,
            HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)

        if room.rain:
            rain_label = helvetica_font.render('Lluvia: sí',
                HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)
        else:
            rain_label = helvetica_font.render('Lluvia: no',
                HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)

        light_label = helvetica_font.render('Intensidad luminosa: ' + str(room.light_intensity) + ' cd',
            HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)
        time_label = helvetica_font.render('Hora: ' + str(room.time),
            HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)
        temp_label = helvetica_font.render('Temperatura: ' + str(room.temperature) + 'ºC',
            HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)

        if room.smoke:
            smoke_label = helvetica_font.render('Humo: sí',
                HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)
        else:
            smoke_label = helvetica_font.render('Humo: no',
                HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)

        wind_label = helvetica_font.render('Viento: ' + str(room.wind) + ' km/h',
            HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)

        if room.gas:
            gas_label = helvetica_font.render('Presencia de gas: sí',
                HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)
        else:
            gas_label = helvetica_font.render('Presencia de gas: no',
                HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)

        if room.intruders:
            intruders_label = helvetica_font.render('Intrusos: sí',
                HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)
        else:
            intruders_label = helvetica_font.render('Intrusos: no',
                HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)

        if room.flood:
            flood_label = helvetica_font.render('Inundación: sí',
                HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)
        else:
            flood_label = helvetica_font.render('Inundación: no',
                HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)

        display_surface.blit(name_label, (625, 45))
        display_surface.blit(rain_label, (625, 75))
        display_surface.blit(light_label, (625, 105))
        display_surface.blit(time_label, (625, 135))
        display_surface.blit(temp_label, (625, 165))

        display_surface.blit(smoke_label, (925, 45))
        display_surface.blit(wind_label, (925, 75))
        display_surface.blit(gas_label, (925, 105))
        display_surface.blit(intruders_label, (925, 135))
        display_surface.blit(flood_label, (925, 165))


    def print_sensors(self, display_surface):
        '''Prints in the right part the information regarding sensors'''

        current_room = ''
        for name, value in self.viewing.items():
            if value:
                current_room = name

        room = self.name_room[current_room]
        sensors = GLOBAL_SENSORS + room.sensors

        if len(sensors) > 10:
            helvetica_font = pygame.font.SysFont('helvetica',
                int(HELVETICA_FONT_SIZE_TYPE-5-((len(sensors)-6)/2)))
        else:
            helvetica_font = pygame.font.SysFont('helvetica', HELVETICA_FONT_SIZE_TYPE-5)

        for i in range(len(sensors)):
            actuator_label = helvetica_font.render(str(sensors[i]), HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)

            if len(sensors) < 10:
                if i < 5:
                    display_surface.blit(actuator_label, (625, 245 + 30*i))
                else:
                    display_surface.blit(actuator_label, (925, 245 + 30*(i-5)))
            else:
                if i < len(sensors)/2:
                    display_surface.blit(actuator_label, (625, 245 + 12*i))
                else:
                    display_surface.blit(actuator_label, (925, 245 + 12*(i-len(sensors)/2)))


    def print_actuators(self, display_surface):
        '''Prints in the right part the information regarding actuators'''

        current_room = ''
        for name, value in self.viewing.items():
            if value:
                current_room = name

        room = self.name_room[current_room]
        actuators = GLOBAL_ACTUATORS + room.actuators

        if len(actuators) > 10:
            helvetica_font = pygame.font.SysFont('helvetica',
                int(HELVETICA_FONT_SIZE_TYPE-5-((len(actuators)-6)/2)))
        else:
            helvetica_font = pygame.font.SysFont('helvetica', HELVETICA_FONT_SIZE_TYPE-5)

        for i in range(len(actuators)):
            actuator_label = helvetica_font.render(str(actuators[i]), HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)

            if len(actuators) < 10:
                if i < 5:
                    display_surface.blit(actuator_label, (625, 445 + 30*i))
                else:
                    display_surface.blit(actuator_label, (925, 445 + 30*(i-5)))
            else:
                if i < len(actuators)/2:
                    display_surface.blit(actuator_label, (625, 445 + 12*i))
                else:
                    display_surface.blit(actuator_label, (925, 445 + 12*(i-len(actuators)/2)))


    def reset_view(self):
        '''Sets every value in the viewing dictionaire to false'''

        for name in self.viewing.keys():
            self.viewing[name] = False


    def reset_presence(self):
        '''Sets every value in the presence dictionaire to false'''

        for name in self.presence.keys():
            self.presence[name] = False

        for room in self.name_room.values():
            room.presence = False


    def is_possible_move(self, current, target):
        '''Checks if a move is possible to do'''

        coords = []
        for value in self.node_coords.values():
            coords.append(value)

        ind_1 = coords.index(current)
        ind_2 = coords.index(target)

        return [ind_1,ind_2] in self.edges or [ind_2,ind_1] in self.edges


if __name__ == "__main__":
    sim = Simulation(NUM_VERT, EDGES, TYPES, NAMES_USED, ROOMS_USED)
    sim.run()
