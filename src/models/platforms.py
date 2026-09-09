from .base_model import Mesh3D

class PlatformModel(Mesh3D):
    """
    3D Procedural Mesh Generator for Platforms 1, 2, 3, and 4.
    Includes concrete bases, safety tactile borders, canopy roofs, benches, and signs.
    """
    def __init__(self):
        super().__init__(name="Platforms_1_to_4")
        self.build_model()

    def build_model(self):
        COLOR_CONCRETE = (160, 160, 165)
        COLOR_SAFETY = (230, 190, 20)      # Yellow Safety Tactile Border
        COLOR_PILLAR = (60, 70, 90)        # Dark Steel Pillars
        COLOR_CANOPY = (70, 120, 180)      # Blue Corrugated Roof
        COLOR_BENCH = (140, 70, 30)        # Wooden Benches
        COLOR_SIGN = (20, 100, 180)        # Platform Designation Sign

        # Platform Configurations: (Name, Center_Z, Width)
        platforms_config = [
            ("Platform_1", 30.0, 8.0),
            ("Platform_2_3", 50.0, 10.0),
            ("Platform_4", 72.0, 8.0)
        ]

        for p_name, pz, p_width in platforms_config:
            # 1. Elevated Concrete Base (160m length, 0.8m height)
            self.add_box(center=(0, 0.4, pz), size=(160, 0.8, p_width), color=COLOR_CONCRETE)

            # 2. Yellow Tactile Safety Line along platform edges
            edge_z_offset = p_width / 2.0 - 0.2
            self.add_box(center=(0, 0.81, pz - edge_z_offset), size=(160, 0.02, 0.4), color=COLOR_SAFETY)
            self.add_box(center=(0, 0.81, pz + edge_z_offset), size=(160, 0.02, 0.4), color=COLOR_SAFETY)

            # 3. Steel Canopy Support Pillars & Pitched Shelter Roof (120m long canopy)
            roof_height = 4.5
            for px in range(-55, 60, 15):
                self.add_cylinder(center=(px, 0.8 + roof_height / 2.0, pz), radius=0.3, height=roof_height, segments=8, color=COLOR_PILLAR)
                self.add_box(center=(px, 0.8 + roof_height, pz), size=(0.4, 0.4, p_width - 1.0), color=COLOR_PILLAR)

            # Pitched Canopy Roof
            self.add_box(center=(0, 0.8 + roof_height + 0.3, pz), size=(120, 0.3, p_width + 1.0), color=COLOR_CANOPY)

            # 4. Passenger Benches (10 Benches per platform)
            for bx in range(-50, 55, 20):
                self.add_box(center=(bx, 1.1, pz - 1.5), size=(3.0, 0.6, 0.8), color=COLOR_BENCH)
                self.add_box(center=(bx, 1.1, pz + 1.5), size=(3.0, 0.6, 0.8), color=COLOR_BENCH)

            # 5. Station / Platform Name Signage Boards
            for sx in [-40, 0, 40]:
                self.add_box(center=(sx, 3.8, pz), size=(6.0, 1.2, 0.2), color=COLOR_SIGN)
