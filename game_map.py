import numpy as np  # type: ignore
from tcod.console import Console

import tile_types


class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

        # Tiles the player can currently see
        self.visible = np.full((width, height), fill_value=False, order="F")

        # Tiles the player has seen before, but are not currently visible
        self.explored = np.full((width, height), fill_value=False, order="F")

        self.tiles[30:33, 22] = tile_types.wall

    def in_bounds(self, x: int, y: int) -> bool:
        """
        Return true if x and y are inside the bounds of this map.
        :param x: x cell to check
        :param y: y cell to check.
        :return: True if in bounds.
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """
        Renders the map. If a tile is visible, then it's drawn with the "light" color.
        Otherwise, if it's explored, it's drawn "dark." All others are in the SHROUD.
        :param console:
        :return:
        """
        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tile_types.SHROUD
        )
