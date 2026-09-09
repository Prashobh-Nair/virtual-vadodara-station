from .base_model import Mesh3D

class ParkingAndGatesModel(Mesh3D):
    """
    3D Procedural Mesh Generator for Parking Zone, Entrance Arch & Security Gates.
    Includes tarmac parking lot, parking bays, barrier arms, entrance arch, security booths, turnstiles, and perimeter fencing.
    """
    def __init__(self):
        super().__init__(name="ParkingAndGates")
        self.build_model()

    def build_model(self):
        COLOR_TARMAC = (50, 50, 55)         # Dark Asphalt Parking Ground
        COLOR_MARKING = (240, 240, 245)     # White Parking Bay Markings
        COLOR_ARCH = (120, 40, 30)          # Red Ornamental Brick Arch Pillars
        COLOR_IRON = (30, 30, 35)           # Wrought Iron Arch & Fence
        COLOR_BOOTH = (220, 220, 210)       # Security Check Booth
        COLOR_BARRIER = (220, 50, 40)       # Red/White Security Barrier Arm

        # 1. Tarmac Parking Lot & Circulating Area (120m wide, 20m deep, Z = -25m)
        self.add_box(center=(0, 0.05, -25.0), size=(120.0, 0.1, 20.0), color=COLOR_TARMAC)

        # 2. Marked Vehicle Parking Slots (Left Parking & Right Parking)
        for slot_x in range(-50, -10, 5):
            self.add_box(center=(slot_x, 0.11, -25.0), size=(0.3, 0.02, 12.0), color=COLOR_MARKING)
        for slot_x in range(15, 55, 5):
            self.add_box(center=(slot_x, 0.11, -25.0), size=(0.3, 0.02, 12.0), color=COLOR_MARKING)

        # 3. Main Station Entrance Arch Gate (Z = -15m)
        # 2 Large Stone/Brick Pillars
        self.add_box(center=(-8.0, 3.5, -15.0), size=(2.0, 7.0, 2.0), color=COLOR_ARCH)
        self.add_box(center=(+8.0, 3.5, -15.0), size=(2.0, 7.0, 2.0), color=COLOR_ARCH)
        # Overhead Grand Ornamental Arch Frame
        self.add_box(center=(0, 7.5, -15.0), size=(18.0, 1.2, 1.5), color=COLOR_IRON)

        # 4. Security Check Points & Toll/Barrier Arms
        self.add_box(center=(-10.5, 1.5, -18.0), size=(2.5, 3.0, 3.0), color=COLOR_BOOTH)
        self.add_box(center=(+10.5, 1.5, -18.0), size=(2.5, 3.0, 3.0), color=COLOR_BOOTH)
        # Security Barrier Arm
        self.add_box(center=(-5.0, 1.2, -18.0), size=(8.0, 0.2, 0.2), color=COLOR_BARRIER)
        self.add_box(center=(+5.0, 1.2, -18.0), size=(8.0, 0.2, 0.2), color=COLOR_BARRIER)

        # 5. Perimeter Safety Fence (120m spanning Z = -15m)
        for fx in range(-60, 61, 4):
            if abs(fx) > 10:  # Exclude main entrance gate gap
                self.add_cylinder(center=(fx, 1.2, -15.0), radius=0.1, height=2.4, segments=6, color=COLOR_IRON)
        self.add_box(center=(-35.0, 2.3, -15.0), size=(50.0, 0.1, 0.1), color=COLOR_IRON)
        self.add_box(center=(+35.0, 2.3, -15.0), size=(50.0, 0.1, 0.1), color=COLOR_IRON)
