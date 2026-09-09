from .base_model import Mesh3D

class RailwayTrackModel(Mesh3D):
    """
    3D Procedural Mesh Generator for Railway Tracks & Rail Infrastructure.
    Includes steel rails, concrete/wooden sleepers (ties), ballast gravel bed, and switches.
    """
    def __init__(self):
        super().__init__(name="RailwayTracks")
        self.build_model()

    def build_model(self):
        COLOR_BALLAST = (90, 85, 80)       # Gravel Ballast Bed
        COLOR_SLEEPER = (110, 110, 115)    # Concrete Cross-Ties
        COLOR_RAIL = (180, 185, 195)       # Steel Rail Bars
        COLOR_CHAIR = (40, 40, 45)         # Fasteners & Plates

        # Track Center Z Coordinates (Track Pair 1 & 2 between P1 and P2/3; Track Pair 3 & 4 between P2/3 and P4)
        track_centers_z = [38.0, 44.0, 58.0, 68.0]
        gauge = 1.676  # Indian Broad Gauge width (1.676 meters)

        for track_z in track_centers_z:
            # 1. Gravel Ballast Bed (180m length, 0.3m height, 3.2m width)
            self.add_box(center=(0, 0.15, track_z), size=(180, 0.3, 3.2), color=COLOR_BALLAST)

            # 2. Concrete Sleepers (Ties) spaced every 1.5 meters across 180 meters
            for sleeper_x in range(-88, 90, 2):
                self.add_box(center=(sleeper_x, 0.35, track_z), size=(0.4, 0.15, 2.5), color=COLOR_SLEEPER)
                # Fastener chairs on left & right rails
                self.add_box(center=(sleeper_x, 0.44, track_z - gauge / 2.0), size=(0.3, 0.05, 0.3), color=COLOR_CHAIR)
                self.add_box(center=(sleeper_x, 0.44, track_z + gauge / 2.0), size=(0.3, 0.05, 0.3), color=COLOR_CHAIR)

            # 3. Parallel Steel Rails (180m length)
            rail_height = 0.2
            self.add_box(center=(0, 0.45 + rail_height / 2.0, track_z - gauge / 2.0), size=(180, rail_height, 0.12), color=COLOR_RAIL)
            self.add_box(center=(0, 0.45 + rail_height / 2.0, track_z + gauge / 2.0), size=(180, rail_height, 0.12), color=COLOR_RAIL)

        # 4. Crossover Track Switches (linking Track 2 to Track 3)
        self.add_box(center=(70, 0.45, 51.0), size=(25, 0.15, 0.12), color=COLOR_RAIL)
        self.add_box(center=(-70, 0.45, 51.0), size=(25, 0.15, 0.12), color=COLOR_RAIL)
