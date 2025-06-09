import copy

import tcod

import color
from engine import Engine
import entity_factories
from procgen import generate_dungeon


def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 43

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    max_monsters_per_room = 2

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    player = copy.deepcopy(entity_factories.player)

    engine = Engine(player=player)

    engine.game_map = generate_dungeon(
        max_room_attempts=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_width,
        map_height=map_height,
        max_monsters_per_room=max_monsters_per_room,
        engine=engine
    )
    engine.update_fov()

    engine.message_log.add_message(
        "Welcome, adventurer, to the black tomb.", color.welcome_text
    )

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
            root_console.clear()
            engine.event_handler.on_render(console=root_console)
            context.present(root_console)
            engine.event_handler.handle_events(context)


if __name__ == "__main__":
    main()
