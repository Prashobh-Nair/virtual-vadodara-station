from .base_model import Mesh3D

class StationBuildingModel(Mesh3D):
    """
    3D Procedural Mesh Generator for Vadodara Railway Station Main Building.
    Includes facade, central dome, entrance arches, pillars, clock tower, and signage.
    """
    def __init__(self):
        super().__init__(name="MainStationBuilding")
        self.build_model()

    def build_model(self):
        # Color Palette
        COLOR_FACADE = (180, 70, 50)     # Terracotta Red Brick
        COLOR_TRIM = (240, 235, 210)     # Cream Sandstone Trim
        COLOR_DOME = (212, 175, 55)      # Gold / Bronze Finish
        COLOR_ROOF = (100, 100, 110)     # Slate Gray Roof
        COLOR_PILLAR = (220, 215, 200)   # Cream Pillars
        COLOR_CLOCK = (255, 255, 255)    # White Dial
        COLOR_SIGN = (20, 120, 40)       # Indian Railways Green

        # 1. Main Concourse Base Building (90m wide, 18m high, 20m deep)
        self.add_box(center=(0, 9, 0), size=(90, 18, 20), color=COLOR_FACADE)

        # 2. Roof Slab & Moldings
        self.add_box(center=(0, 18.5, 0), size=(94, 1.0, 22), color=COLOR_TRIM)
        self.add_box(center=(0, 19.5, 0), size=(88, 1.0, 18), color=COLOR_ROOF)

        # 3. Grand Central Portico Dome Base & Dome
        self.add_box(center=(0, 20.5, 0), size=(20, 3, 20), color=COLOR_TRIM)
        self.add_dome(center=(0, 22.0, 0), radius=8.0, height=7.0, segments=16, rings=8, color=COLOR_DOME)

        # 4. Clock Tower & Official Station Name Sign
        self.add_box(center=(0, 26.5, 0), size=(5, 6, 5), color=COLOR_TRIM)
        self.add_cylinder(center=(0, 26.5, 2.6), radius=1.5, height=0.2, segments=12, color=COLOR_CLOCK)
        self.add_box(center=(0, 15.0, 10.5), size=(36, 2.5, 0.5), color=COLOR_SIGN)

        # 5. Entrance Arches & Support Pillars (8 Columns)
        pillar_positions_x = [-35, -25, -15, -5, 5, 15, 25, 35]
        for px in pillar_positions_x:
            self.add_cylinder(center=(px, 6.0, 10.5), radius=0.8, height=12.0, segments=8, color=COLOR_PILLAR)
            self.add_box(center=(px, 12.2, 10.5), size=(2.0, 0.6, 2.0), color=COLOR_TRIM)

        # 6. Windows & Door Frames
        for wx in range(-38, 40, 8):
            if abs(wx) > 6:  # Exclude center entrance area
                self.add_box(center=(wx, 6.0, 10.1), size=(3.0, 5.0, 0.2), color=(40, 50, 70))
                self.add_box(center=(wx, 13.0, 10.1), size=(3.0, 4.0, 0.2), color=(40, 50, 70))
