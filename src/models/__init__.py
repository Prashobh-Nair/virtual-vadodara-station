"""
3D Models Package for Virtual Vadodara Railway Station.
Provides 3D procedural geometry generators for Weeks 1 to 5 deliverables.
"""
from .base_model import Mesh3D
from .station_building import StationBuildingModel
from .platforms import PlatformModel
from .railway_tracks import RailwayTrackModel
from .foot_overbridge import FootOverbridgeModel
from .ticket_hall import TicketHallModel
from .waiting_area import WaitingAreaModel
from .parking_and_gates import ParkingAndGatesModel
from .scene_assembler import VadodaraStationScene

__all__ = [
    'Mesh3D',
    'StationBuildingModel',
    'PlatformModel',
    'RailwayTrackModel',
    'FootOverbridgeModel',
    'TicketHallModel',
    'WaitingAreaModel',
    'ParkingAndGatesModel',
    'VadodaraStationScene'
]
