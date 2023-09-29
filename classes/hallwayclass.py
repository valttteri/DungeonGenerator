import itertools
import pygame

GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
LIGHTGRAY = (211, 211, 211)
GRAY = (128, 128, 128)

class Hallway:
    """Class for visualizing a hallway"""
    new_id = itertools.count()

    def __init__(self, start_room: object, end_room: object, display):
        self.start_room = start_room
        self.end_room = end_room
        self.display = display
        self.hallway_id = next(self.new_id)
        self.start_node = start_room.center()
        self.end_node = end_room.center()

        self.start_room_width = start_room.width
        self.start_room_height = start_room.height

        self.end_room_width = end_room.width
        self.end_room_height = end_room.height

    def __str__(self):
        return f"Hallway between rooms {self.start_room.center()}, and {self.end_room.center()}"

    def __repr__(self):
        return f"Hallway between rooms {self.start_room.center()}, and {self.end_room.center()}"
    
    def plot(self):
        pygame.draw.line(self.display, RED, self.start_node, self.end_node)

def generate_hallways(graph: dict, rooms: list, display):
    used_nodes = set()
    hallways = []

    for start_node, end_nodes in graph.items():
        if start_node in used_nodes:
            continue
        for end_node in end_nodes:
            if end_node[0] in used_nodes:
                continue
            starting_room, ending_room = find_hallways_rooms(start_node, end_node[0], rooms)
            hallways.append(Hallway(starting_room, ending_room, display))
        used_nodes.add(start_node)
    
    return hallways

def find_hallways_rooms(start_node, end_node, rooms):
    starting_room = None
    ending_room = None

    for room in rooms:
        #print(f"room center: {room.center()}")
        if room.center() == start_node:
            starting_room = room
        elif room.center() == end_node:
            ending_room = room
    
    if starting_room != None != ending_room:
        return starting_room, ending_room
    print(f"no hallway found between nodes {start_node} and {end_node}")


        

"""
käytävä tarvitsee tiedot
- alkusolmun koordinaatit
- loppusolmun koordinaatit
- alkusolmuun liitettävän huoneen mitat
- loppusolmuun liitettävän huoneen mitat
- anna syötteenä alkupään ja loppupään huoneet

plottaaminen
- jos käytävä on lähes suora, plottaa suora viiva
- vertaa y/x koordinaatteja ja sen perusteella päätä kummasta päästä viiva lähtee

- jos käytävä ei ole suora, plottaa kaksi viivaa joiden välillä 90 asteen kulma
- jos viiva on nosuseva, plottaa ensin suoraan ylöspäin ja sitten vasemmalle/oikealle
"""