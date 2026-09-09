from typing import List
from .base_model import Mesh3D
from .station_building import StationBuildingModel
from .platforms import PlatformModel
from .railway_tracks import RailwayTrackModel
from .foot_overbridge import FootOverbridgeModel
from .ticket_hall import TicketHallModel
from .waiting_area import WaitingAreaModel
from .parking_and_gates import ParkingAndGatesModel

class VadodaraStationScene(Mesh3D):
    """
    Master 3D Scene Graph Assembler for Virtual Vadodara Railway Station.
    Combines all Week 1 to Week 5 sub-models into a unified 3D spatial scene graph.
    """
    def __init__(self):
        super().__init__(name="Virtual_Vadodara_Railway_Station_Week5")
        self.sub_models: List[Mesh3D] = []
        self.assemble_scene()

    def assemble_scene(self):
        # Instantiate sub-models for Week 1 to 5 deliverables
        self.building = StationBuildingModel()
        self.platforms = PlatformModel()
        self.tracks = RailwayTrackModel()
        self.fob = FootOverbridgeModel()
        self.ticket_hall = TicketHallModel()
        self.waiting_area = WaitingAreaModel()
        self.parking_and_gates = ParkingAndGatesModel()

        self.sub_models = [
            self.building,
            self.platforms,
            self.tracks,
            self.fob,
            self.ticket_hall,
            self.waiting_area,
            self.parking_and_gates
        ]

        # Consolidate all vertices and faces into master scene mesh
        for model in self.sub_models:
            vertex_offset = len(self.vertices)
            self.vertices.extend(model.vertices)
            for face in model.faces:
                offset_face = [v_idx + vertex_offset for v_idx in face]
                self.faces.append(offset_face)
            self.colors.extend(model.colors)

    def get_scene_summary(self) -> dict:
        bbox_min, bbox_max = self.get_bounding_box()
        return {
            "scene_name": self.name,
            "total_sub_models": len(self.sub_models),
            "total_vertices": len(self.vertices),
            "total_faces": len(self.faces),
            "bounding_box_min": bbox_min,
            "bounding_box_max": bbox_max,
            "sub_model_names": [m.name for m in self.sub_models]
        }
