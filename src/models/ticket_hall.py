from .base_model import Mesh3D

class TicketHallModel(Mesh3D):
    """
    3D Procedural Mesh Generator for Ticket Booking Hall.
    Includes booking hall interior, booking counters, glass ticket windows, queue dividers, and fare screens.
    """
    def __init__(self):
        super().__init__(name="TicketBookingHall")
        self.build_model()

    def build_model(self):
        COLOR_WALL = (225, 220, 210)       # Sandstone Hall Interior Wall
        COLOR_FLOOR = (200, 200, 205)      # Polished Marble Floor
        COLOR_COUNTER = (30, 90, 160)      # Indian Railways Blue Counter
        COLOR_GLASS = (180, 220, 240)      # Glass Ticket Partition
        COLOR_STANCHION = (200, 200, 210)  # Stainless Steel Queue Posts
        COLOR_SCREEN = (10, 10, 20)        # Digital Fare Display Screen

        # Ticket Hall Dimensions: Center (-65, 3.0, 5.0), Size (30, 6.0, 15.0)
        cx, cy, cz = -65.0, 3.0, 5.0

        # 1. Hall Structure & Marble Floor
        self.add_box(center=(cx, 0.1, cz), size=(30.0, 0.2, 15.0), color=COLOR_FLOOR)
        self.add_box(center=(cx - 15.0, cy, cz), size=(0.4, 6.0, 15.0), color=COLOR_WALL)  # Outer Wall
        self.add_box(center=(cx, 6.0, cz), size=(30.0, 0.4, 15.0), color=COLOR_WALL)        # Ceiling

        # 2. 6 Ticket Booking Counter Desks & Glass Windows along the back wall (Z = cz - 6m)
        counter_z = cz - 6.0
        for i, bx in enumerate(range(-77, -51, 5)):
            # Counter Base Desk
            self.add_box(center=(bx, 1.0, counter_z), size=(4.0, 2.0, 1.5), color=COLOR_COUNTER)
            # Glass Partition Window
            self.add_box(center=(bx, 2.8, counter_z), size=(3.8, 1.6, 0.1), color=COLOR_GLASS)
            # Transaction Speaks / Opening Slot
            self.add_box(center=(bx, 2.1, counter_z), size=(1.0, 0.2, 0.1), color=(50, 50, 50))
            # Overhead Counter Number & Fare Display Board
            self.add_box(center=(bx, 4.2, counter_z), size=(3.8, 1.0, 0.2), color=COLOR_SCREEN)

        # 3. Passenger Queue Barriers / Stanchions
        for qx in range(-77, -51, 5):
            for qz_offset in [1.5, 3.5, 5.5]:
                self.add_cylinder(center=(qx - 1.2, 0.6, counter_z + qz_offset), radius=0.08, height=1.0, segments=6, color=COLOR_STANCHION)
                self.add_cylinder(center=(qx + 1.2, 0.6, counter_z + qz_offset), radius=0.08, height=1.0, segments=6, color=COLOR_STANCHION)
                # Retractable Queue Belt
                self.add_box(center=(qx, 0.9, counter_z + qz_offset), size=(2.4, 0.08, 0.05), color=(30, 80, 180))
