from .base_model import Mesh3D

class FootOverbridgeModel(Mesh3D):
    """
    3D Procedural Mesh Generator for Foot Overbridge (FOB) & Pedestrian Stairs.
    Includes elevated walkway span, covered roof, safety railings, staircases, and support pillars.
    """
    def __init__(self):
        super().__init__(name="FootOverbridge")
        self.build_model()

    def build_model(self):
        COLOR_TRUSS = (40, 90, 160)       # Royal Blue Steel Truss Frame
        COLOR_FLOOR = (140, 140, 145)     # Walkway Concrete Deck
        COLOR_ROOF = (200, 220, 240)      # Translucent Roof Canopy
        COLOR_RAILING = (220, 220, 225)   # Safety Railings & Mesh
        COLOR_STEPS = (120, 120, 125)     # Staircase Steps

        # FOB Main Span parameters: Center X = 0m, Bridge Deck Y = 5.5m, Z spans from Platform 1 (Z=30) to Platform 4 (Z=72)
        bridge_width = 8.0
        bridge_deck_y = 5.5
        bridge_center_z = 51.0
        bridge_length_z = 52.0  # Spans Z=25m to Z=77m

        # 1. Main Pedestrian Walkway Deck
        self.add_box(center=(0, bridge_deck_y, bridge_center_z), size=(bridge_width, 0.4, bridge_length_z), color=COLOR_FLOOR)

        # 2. Side Safety Railings & Translucent Covered Roof
        roof_height = 3.5
        self.add_box(center=(0, bridge_deck_y + roof_height, bridge_center_z), size=(bridge_width + 0.4, 0.3, bridge_length_z + 0.4), color=COLOR_ROOF)

        # Side Truss Frames & Railings (Left X=-4m and Right X=+4m)
        for side_x in [-bridge_width / 2.0, bridge_width / 2.0]:
            self.add_box(center=(side_x, bridge_deck_y + roof_height / 2.0, bridge_center_z), size=(0.2, roof_height, bridge_length_z), color=COLOR_RAILING)

        # 3. Vertical Support Pillars anchored on Platform 1, Platform 2/3, and Platform 4
        pillar_z_positions = [30.0, 50.0, 72.0]
        for pz in pillar_z_positions:
            self.add_cylinder(center=(-3.5, bridge_deck_y / 2.0, pz), radius=0.4, height=bridge_deck_y, segments=8, color=COLOR_TRUSS)
            self.add_cylinder(center=(+3.5, bridge_deck_y / 2.0, pz), radius=0.4, height=bridge_deck_y, segments=8, color=COLOR_TRUSS)

        # 4. Double-Flight Staircases connecting FOB down to each Platform (P1, P2/3, P4)
        for pz in pillar_z_positions:
            # Staircase sloping down along X axis (Left flight & Right flight)
            for stair_dir in [-1, 1]:  # Left (-X) and Right (+X)
                for step in range(10):
                    sx = stair_dir * (4.2 + step * 0.6)
                    sy = bridge_deck_y - (step + 1) * 0.48
                    sz = pz + (stair_dir * 1.5)
                    self.add_box(center=(sx, sy, sz), size=(0.65, 0.45, 2.5), color=COLOR_STEPS)
                    # Staircase Railing
                    self.add_box(center=(sx, sy + 1.0, sz + 1.25), size=(0.65, 0.1, 0.1), color=COLOR_RAILING)
