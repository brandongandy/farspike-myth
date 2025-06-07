import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler
from procgen import generate_dungeon


def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))

    game_map = generate_dungeon(
        max_rooms,
        room_min_size,
        room_max_size,
        map_width,
        map_height,
        player
    )

    engine = Engine(event_handler=event_handler, game_map=game_map, player=player)

    with tcod.context.new_terminal(
        columns=screen_width,
        rows=screen_height,
        tileset=tileset,
        title="Yet another Roguelike",
        vsync=True
    ) as context:
        # order="F" changes 2D array access from [y,x] to [x,y]
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:  # GAME LOOP
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()
