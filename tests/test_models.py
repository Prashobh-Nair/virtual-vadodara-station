import unittest
import sys
import os

# Add src to python path for testing
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from models.base_model import Mesh3D
from models.station_building import StationBuildingModel
from models.platforms import PlatformModel
from models.railway_tracks import RailwayTrackModel
from models.foot_overbridge import FootOverbridgeModel
from models.ticket_hall import TicketHallModel
from models.waiting_area import WaitingAreaModel
from models.parking_and_gates import ParkingAndGatesModel
from models.scene_assembler import VadodaraStationScene

class TestVadodaraStationModels(unittest.TestCase):

    def test_base_mesh3d_primitives(self):
        mesh = Mesh3D("TestMesh")
        mesh.add_box((0, 0, 0), (10, 10, 10))
        self.assertEqual(len(mesh.vertices), 8)
        self.assertEqual(len(mesh.faces), 6)

        bbox_min, bbox_max = mesh.get_bounding_box()
        self.assertEqual(bbox_min, (-5.0, -5.0, -5.0))
        self.assertEqual(bbox_max, (5.0, 5.0, 5.0))

    def test_station_building_model(self):
        building = StationBuildingModel()
        self.assertTrue(len(building.vertices) > 0)
        self.assertTrue(len(building.faces) > 0)
        self.assertEqual(building.name, "MainStationBuilding")

    def test_platforms_model(self):
        platforms = PlatformModel()
        self.assertTrue(len(platforms.vertices) > 0)
        self.assertTrue(len(platforms.faces) > 0)

    def test_railway_tracks_model(self):
        tracks = RailwayTrackModel()
        self.assertTrue(len(tracks.vertices) > 0)
        self.assertTrue(len(tracks.faces) > 0)

    def test_foot_overbridge_model(self):
        fob = FootOverbridgeModel()
        self.assertTrue(len(fob.vertices) > 0)
        self.assertTrue(len(fob.faces) > 0)

    def test_ticket_hall_and_waiting_area(self):
        ticket_hall = TicketHallModel()
        waiting_area = WaitingAreaModel()
        parking = ParkingAndGatesModel()
        self.assertTrue(len(ticket_hall.vertices) > 0)
        self.assertTrue(len(waiting_area.vertices) > 0)
        self.assertTrue(len(parking.vertices) > 0)

    def test_master_scene_assembler(self):
        scene = VadodaraStationScene()
        summary = scene.get_scene_summary()
        self.assertEqual(summary['total_sub_models'], 7)
        self.assertTrue(summary['total_vertices'] > 100)
        self.assertTrue(summary['total_faces'] > 50)

    def test_obj_export(self):
        scene = VadodaraStationScene()
        test_obj_file = "test_export.obj"
        scene.export_obj(test_obj_file)
        self.assertTrue(os.path.exists(test_obj_file))
        if os.path.exists(test_obj_file):
            os.remove(test_obj_file)

if __name__ == '__main__':
    unittest.main()
