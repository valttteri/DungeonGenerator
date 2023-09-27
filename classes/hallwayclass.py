import itertools
import pygame

class Hallway:
    """Class for visualizing a hallway"""
    new_id = itertools.count()

    def __init__(self, start_room: object, end_room: object, display):
        self.start_room = start_room
        self.end_room = end_room
        self.display = display
        self.hallway_id = next(self.new_id)
        self.start_node = start_room.center
        self.end_node = end_room.center

        self.start_room_width = start_room.width
        self.start_room_height = start_room.height

        self.end_room_width = end_room.width
        self.end_room_height = end_room.height

def plot_hallways():
    pass

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