from .base_model import Mesh3D

class WaitingAreaModel(Mesh3D):
    """
    3D Procedural Mesh Generator for Passenger Waiting Area & Lounge.
    Includes concourse lounge, seating rows, LED information screens, and luggage zone.
    """
    def __init__(self):
        super().__init__(name="PassengerWaitingArea")
        self.build_model()

    def build_model(self):
        COLOR_WALL = (225, 220, 210)       # Concourse Interior Wall
        COLOR_FLOOR = (190, 195, 200)      # Granite Tile Floor
        COLOR_SEAT = (160, 165, 175)       # Stainless Steel Seating
        COLOR_TV = (15, 15, 25)            # Overhead LED Train Display
        COLOR_LUGGAGE = (180, 100, 40)     # Luggage Storage Rack

        # Waiting Area Dimensions: Center (+65, 3.0, 5.0), Size (30, 6.0, 15.0)
        cx, cy, cz = 65.0, 3.0, 5.0

        # 1. Hall Structure & Floor
        self.add_box(center=(cx, 0.1, cz), size=(30.0, 0.2, 15.0), color=COLOR_FLOOR)
        self.add_box(center=(cx + 15.0, cy, cz), size=(0.4, 6.0, 15.0), color=COLOR_WALL)  # Outer Wall
        self.add_box(center=(cx, 6.0, cz), size=(30.0, 0.4, 15.0), color=COLOR_WALL)        # Ceiling

        # 2. Rows of 4-Seater Stainless Steel Passenger Chairs (6 Rows)
        for rx in range(55, 78, 8):
            for rz in [-1.0, 4.0, 9.0]:
                # Bench Support Beam
                self.add_box(center=(rx, 0.4, rz), size=(6.0, 0.1, 0.4), color=(60, 60, 65))
                # 4 Individual Chair Seats
                for seat_idx in range(4):
                    sx = rx - 2.25 + seat_idx * 1.5
                    self.add_box(center=(sx, 0.75, rz), size=(1.2, 0.5, 0.8), color=COLOR_SEAT)
                    self.add_box(center=(sx, 1.25, rz - 0.35), size=(1.2, 0.6, 0.1), color=COLOR_SEAT)

        # 3. Central Overhead LED Train Information Displays
        self.add_box(center=(cx, 4.5, cz), size=(8.0, 1.8, 0.3), color=COLOR_TV)

        # 4. Corner Luggage Storage Zone
        self.add_box(center=(cx - 11.0, 1.2, cz + 5.5), size=(5.0, 2.4, 2.0), color=COLOR_LUGGAGE)
