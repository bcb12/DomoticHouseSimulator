import pygame
import easygui
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

    def __init__(self, num_vert, edges, types, names, rooms, global_sensors, global_actuators):
        node_coords = preprocess_graph(IMG_NAME, num_vert, edges, types, names)

        self.node_coords = node_coords
        self.name_type = {}
        self.name_room = {}
        self.room_coords = {}
        self.viewing = {}
        self.presence = {}

        self.start_index_sensors = 0
        self.end_index_sensors = 9

        self.start_index_actuators = 0
        self.end_index_actuators = 9

        self.names = names
        self.edges = edges

        self.global_sensors = global_sensors
        self.global_actuators = global_actuators

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
        self.update_rooms(display_surface)
        self.mark_centers(display_surface, center_img)
        self.add_labels(display_surface)
        self.print_info(display_surface)

        rect_light = pygame.Rect(625, 105, 175, 15)
        rect_time = pygame.Rect(625, 135, 80, 15)
        rect_temp = pygame.Rect(625, 165, 135, 15)
        rect_wind = pygame.Rect(925, 75, 115, 15)

        running = True

        active_light = False
        active_time = False
        active_temp = False
        active_wind = False

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

                                    self.update_rooms(display_surface)

                        # Apply changes
                        if position[0] >= 1090 and \
                            position[0] <= 1190  and \
                            position[1] >= 168 and \
                            position[1] <= 190:

                            room_to_change = None
                            for name_room, state in self.viewing.items():
                                if state:
                                    room_to_change = name_room

                            if self.check_correct_values_room(self.name_room[room_to_change]):
                                self.update_rooms(display_surface)

                        # Show more sensors
                        if position[0] >= 1150 and \
                            position[0] <= 1170  and \
                            position[1] >= 210 and \
                            position[1] <= 230:

                            current_room = ''
                            for name, value in self.viewing.items():
                                if value:
                                    current_room = name

                            room = self.name_room[current_room]
                            sensors = self.global_sensors + room.sensors

                            if self.start_index_sensors + 10 <= len(sensors) and len(sensors) != 10:
                                if self.end_index_sensors + 10 <= len(sensors):
                                    self.start_index_sensors += 10
                                    self.end_index_sensors += 10
                                else:
                                    self.start_index_sensors += 10
                                    self.end_index_sensors = len(sensors)

                            self.print_info(display_surface)

                        # Show less sensors
                        if position[0] >= 1170 and \
                            position[0] <= 1190  and \
                            position[1] >= 210 and \
                            position[1] <= 230:

                            if self.start_index_sensors != 0:
                                if self.end_index_sensors - self.start_index_sensors == 9:
                                    self.start_index_sensors -= 10
                                    self.end_index_sensors -= 10
                                else:
                                    self.start_index_sensors -= 10
                                    self.end_index_sensors -= self.end_index_sensors % 10 + 1

                            self.print_info(display_surface)

                        # Show more actuators
                        if position[0] >= 1150 and \
                            position[0] <= 1170  and \
                            position[1] >= 410 and \
                            position[1] <= 430:

                            current_room = ''
                            for name, value in self.viewing.items():
                                if value:
                                    current_room = name

                            room = self.name_room[current_room]
                            actuators = self.global_actuators + room.actuators

                            if self.start_index_actuators + 10 <= len(actuators) and len(actuators) != 10:
                                if self.end_index_actuators + 10 <= len(actuators):
                                    self.start_index_actuators += 10
                                    self.end_index_actuators += 10
                                else:
                                    self.start_index_actuators += 10
                                    self.end_index_actuators = len(actuators)

                            self.print_info(display_surface)

                        # Show less actuators
                        if position[0] >= 1170 and \
                            position[0] <= 1190  and \
                            position[1] >= 410 and \
                            position[1] <= 430:

                            if self.start_index_actuators != 0:
                                if self.end_index_actuators - self.start_index_actuators == 9:
                                    self.start_index_actuators -= 10
                                    self.end_index_actuators -= 10
                                else:
                                    self.start_index_actuators -= 10
                                    self.end_index_actuators -= self.end_index_actuators % 10 + 1

                            self.print_info(display_surface)

                        # Rain variable
                        if position[0] >= 625 and \
                            position[0] <= 690  and \
                            position[1] >= 75 and \
                            position[1] <= 90:

                            room_to_change = None
                            for name_room, state in self.viewing.items():
                                if state:
                                    room_to_change = name_room

                            if self.name_room[room_to_change].rain:
                                self.name_room[room_to_change].rain = False
                            else:
                                self.name_room[room_to_change].rain = True

                            self.print_info(display_surface)

                        # Smoke variable
                        if position[0] >= 925 and \
                            position[0] <= 990  and \
                            position[1] >= 45 and \
                            position[1] <= 60:

                            room_to_change = None
                            for name_room, state in self.viewing.items():
                                if state:
                                    room_to_change = name_room

                            if self.name_room[room_to_change].smoke:
                                self.name_room[room_to_change].smoke = False
                            else:
                                self.name_room[room_to_change].smoke = True

                            self.print_info(display_surface)

                        # Gas variable
                        if position[0] >= 925 and \
                            position[0] <= 1060  and \
                            position[1] >= 105 and \
                            position[1] <= 120:

                            room_to_change = None
                            for name_room, state in self.viewing.items():
                                if state:
                                    room_to_change = name_room

                            if self.name_room[room_to_change].gas:
                                self.name_room[room_to_change].gas = False
                            else:
                                self.name_room[room_to_change].gas = True

                            self.print_info(display_surface)

                        # Intruders variable
                        if position[0] >= 925 and \
                            position[0] <= 1000  and \
                            position[1] >= 135 and \
                            position[1] <= 150:

                            room_to_change = None
                            for name_room, state in self.viewing.items():
                                if state:
                                    room_to_change = name_room

                            if self.name_room[room_to_change].intruders:
                                self.name_room[room_to_change].intruders = False
                            else:
                                self.name_room[room_to_change].intruders = True

                            self.print_info(display_surface)

                        # Flood variable
                        if position[0] >= 925 and \
                            position[0] <= 1020  and \
                            position[1] >= 165 and \
                            position[1] <= 180:

                            room_to_change = None
                            for name_room, state in self.viewing.items():
                                if state:
                                    room_to_change = name_room

                            if self.name_room[room_to_change].flood:
                                self.name_room[room_to_change].flood = False
                            else:
                                self.name_room[room_to_change].flood = True

                            self.print_info(display_surface)

                        # Light variable
                        if rect_light.collidepoint(event.pos):
                            active_light = True
                        else:
                            active_light = False

                        # Time variable
                        if rect_time.collidepoint(event.pos):
                            active_time = True
                        else:
                            active_time = False

                        # Temperature variable
                        if rect_temp.collidepoint(event.pos):
                            active_temp = True
                        else:
                            active_temp = False

                        # Wind variable
                        if rect_wind.collidepoint(event.pos):
                            active_wind = True
                        else:
                            active_wind = False

                if event.type == pygame.KEYDOWN:
                    room_to_change = None
                    for name_room, state in self.viewing.items():
                        if state:
                            room_to_change = name_room

                    # Backspace
                    if event.key == pygame.K_BACKSPACE:
                        if active_light:
                            self.name_room[room_to_change].light_intensity = \
                                self.name_room[room_to_change].light_intensity[:-1]
                            self.print_info(display_surface)

                        if active_time:
                            self.name_room[room_to_change].time = \
                                self.name_room[room_to_change].time[:-1]
                            self.print_info(display_surface)

                        if active_temp:
                            self.name_room[room_to_change].temperature = \
                                self.name_room[room_to_change].temperature[:-1]
                            self.print_info(display_surface)

                        if active_wind:
                            self.name_room[room_to_change].wind = \
                                self.name_room[room_to_change].wind[:-1]
                            self.print_info(display_surface)

                    # Other key
                    else:
                        if active_light:
                            if event.unicode.isnumeric() or (event.unicode == '.' and \
                                '.' not in self.name_room[room_to_change].light_intensity):
                                if len(self.name_room[room_to_change].light_intensity) < 10:
                                    self.name_room[room_to_change].light_intensity += event.unicode
                                    self.print_info(display_surface)

                        if active_time:
                            if event.unicode.isnumeric() or (event.unicode == ':' and \
                                ':' not in self.name_room[room_to_change].time):
                                if len(self.name_room[room_to_change].time) < 5:
                                    self.name_room[room_to_change].time += event.unicode
                                    self.print_info(display_surface)

                        if active_temp:
                            if event.unicode.isnumeric() or (event.unicode == '.' and \
                                '.' not in self.name_room[room_to_change].temperature):
                                if len(self.name_room[room_to_change].temperature) < 10:
                                    self.name_room[room_to_change].temperature += event.unicode
                                    self.print_info(display_surface)

                        if active_wind:
                            if event.unicode.isnumeric() or (event.unicode == '.' and \
                                '.' not in self.name_room[room_to_change].wind):
                                if len(self.name_room[room_to_change].wind) < 10:
                                    self.name_room[room_to_change].wind += event.unicode
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

        empty_img = pygame.image.load(r'images/Empty.jpg')
        apply_button = pygame.image.load(r'images/ApplyButton.jpeg')
        signs_button = pygame.image.load(r'images/Signs.png')

        display_surface.blit(empty_img, (605, 0))
        display_surface.blit(empty_img, (605, 205))
        display_surface.blit(empty_img, (605, 405))

        display_surface.blit(apply_button, (1090, 168))
        display_surface.blit(signs_button, (1150, 210))
        display_surface.blit(signs_button, (1150, 410))

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

        light_label = helvetica_font.render \
            ('Intensidad luminosa: ' + str(room.light_intensity) + ' cd',
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
        sensors = self.global_sensors + room.sensors

        helvetica_font = pygame.font.SysFont('helvetica', HELVETICA_FONT_SIZE_TYPE-7)

        if len(sensors) > 10:
            if self.end_index_sensors - self.start_index_sensors == 9:
                limit = 10
            else:
                limit = self.end_index_sensors - self.start_index_sensors
        else:
            limit = len(sensors)

        for i in range(limit):
            actuator_label = helvetica_font.render(str(sensors[i+self.start_index_sensors]), HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)

            if i < 5:
                display_surface.blit(actuator_label, (625, 245 + 30*i))
            else:
                display_surface.blit(actuator_label, (925, 245 + 30*(i-5)))


    def print_actuators(self, display_surface):
        '''Prints in the right part the information regarding actuators'''

        current_room = ''
        for name, value in self.viewing.items():
            if value:
                current_room = name

        room = self.name_room[current_room]
        actuators = self.global_actuators + room.actuators

        helvetica_font = pygame.font.SysFont('helvetica', HELVETICA_FONT_SIZE_TYPE-7)

        if len(actuators) > 10:
            if self.end_index_actuators - self.start_index_actuators == 9:
                limit = 10
            else:
                limit = self.end_index_actuators - self.start_index_actuators
        else:
            limit = len(actuators)

        for i in range(limit):
            actuator_label = helvetica_font.render(str(actuators[i+self.start_index_actuators]), HELVETICA_FONT_SIZE_TYPE, BLACK_COLOR)

            if i < 5:
                display_surface.blit(actuator_label, (625, 445 + 30*i))
            else:
                display_surface.blit(actuator_label, (925, 445 + 30*(i-5)))


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


    def check_correct_values_room(self, room):
        '''Checks if the new values for the variables are correct'''

        message_log = ''

        if room.light_intensity == '':
            message_log += '¡La intensidad luminosa no puede estar vacía!\n'
        else:
            if room.light_intensity[0] == '.' or \
                room.light_intensity[len(room.light_intensity)-1] == '.':
                message_log += '¡El valor para la intensidad luminosa es incorrecto!\n'

        if room.time == '':
            message_log += '¡La hora no puede estar vacía!\n'
        else:
            time_split = room.time.split(':')
            if len(time_split) != 2:
                message_log += '¡El formato de la hora o minutos es incorrecto! (Formato: HH:MM)\n'
            else:
                if len(time_split[0]) != 2 or len(time_split[1]) != 2:
                    message_log += '¡El formato de la hora o minutos es incorrecto! \
                        (Formato: HH:MM)\n'
                else:
                    if int(time_split[0]) > 23 or int(time_split[1]) > 59:
                        message_log += '¡Los valores de la hora o minutos son incorrectos! \
                            (Hora: de 00 a 23 | Minutos: de 00 a 59)\n'

        if room.temperature == '':
            message_log += '¡La temperatura no puede estar vacía!\n'
        else:
            if room.temperature[0] == '.' or \
                room.temperature[len(room.temperature)-1] == '.':
                message_log += '¡El valor para la temperatura es incorrecto!\n'

        if room.wind == '':
            message_log += '¡El valor para el viento no puede estar vacío!\n'
        else:
            if room.wind[0] == '.' or \
                room.wind[len(room.wind)-1] == '.':
                message_log += '¡El valor para el viento es incorrecto!\n'

        if message_log != '':
            easygui.msgbox(message_log, title="¡Errores en los datos introducidos!")
            return False

        easygui.msgbox("¡Cambios aplicados con éxito!", title="¡Cambios aplicados!")
        return True


    def update_rooms(self, display_surface):
        '''Updates every sensor according to the variables'''

        current_room = ''
        for name, value in self.viewing.items():
            if value:
                current_room = name

        hour_to_set = self.name_room[current_room].time 

        for room in self.name_room.values():
            room.time = hour_to_set
            room.update_sensors()
            room.call_automaton()

        self.print_info(display_surface)


if __name__ == "__main__":
    sim = Simulation(NUM_VERT, EDGES, TYPES, NAMES_USED, ROOMS_USED, GLOBAL_SENSORS, \
        GLOBAL_ACTUATORS)
    sim.run()
