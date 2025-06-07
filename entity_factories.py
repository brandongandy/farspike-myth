from entity import Entity

player = Entity(char="@", color=(255, 255, 255), name="Player", blocks_movement=True)

orc = Entity(char="o", color=(80, 129, 34), name="Orc", blocks_movement=True)
troll = Entity(char="T", color=(0, 129, 0), name="Troll", blocks_movement=True)