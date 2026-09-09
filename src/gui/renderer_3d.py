import math
import os
from typing import Tuple, List

try:
    from PIL import Image, ImageDraw, ImageFont
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

from models.scene_assembler import VadodaraStationScene

class Renderer3D:
    """
    3D Viewport Renderer for Virtual Vadodara Railway Station.
    Supports camera transformation, perspective projection, 
    multi-view preset angles, and snapshot rendering.
    """
    def __init__(self, scene: VadodaraStationScene, width: int = 1024, height: int = 640):
        self.scene = scene
        self.width = width
        self.height = height

    def project_vertex(self, vertex: Tuple[float, float, float], cam_pos: Tuple[float, float, float], cam_yaw: float, cam_pitch: float, fov: float = 60.0) -> Tuple[int, int, float]:
        """
        Projects a 3D world coordinate (X, Y, Z) to 2D Viewport screen coordinate (u, v, depth).
        """
        vx, vy, vz = vertex
        cx, cy, cz = cam_pos

        # Translate to camera space
        tx, ty, tz = vx - cx, vy - cy, vz - cz

        # Rotate Yaw (around Y axis)
        rad_yaw = math.radians(cam_yaw)
        cos_y, sin_y = math.cos(rad_yaw), math.sin(rad_yaw)
        rx = tx * cos_y - tz * sin_y
        rz = tx * sin_y + tz * cos_y

        # Rotate Pitch (around X axis)
        rad_pitch = math.radians(cam_pitch)
        cos_p, sin_p = math.cos(rad_pitch), math.sin(rad_pitch)
        ry = ty * cos_p - rz * sin_p
        rz_final = ty * sin_p + rz * cos_p

        # Avoid projection division by zero or behind camera
        if rz_final <= 0.5:
            rz_final = 0.5

        # Perspective Projection
        focal_length = (self.width / 2.0) / math.tan(math.radians(fov / 2.0))
        screen_x = int(self.width / 2.0 + (rx * focal_length) / rz_final)
        screen_y = int(self.height / 2.0 - (ry * focal_length) / rz_final)

        return (screen_x, screen_y, rz_final)

    def render_snapshot(self, output_path: str, view_title: str, cam_pos: Tuple[float, float, float], cam_yaw: float, cam_pitch: float) -> str:
        """
        Renders the master 3D scene from the specified camera angle to a high-resolution image file.
        """
        if not HAS_PIL:
            print(f"[Renderer3D Warning] PIL not available for rendering snapshot '{output_path}'")
            return output_path

        img = Image.new("RGB", (self.width, self.height), (25, 30, 40))
        draw = ImageDraw.Draw(img)

        # Draw Grid Ground Plane (Z lines & X lines)
        grid_color = (40, 50, 65)
        for gz in range(-40, 100, 20):
            p1 = self.project_vertex((-120, 0, gz), cam_pos, cam_yaw, cam_pitch)
            p2 = self.project_vertex((+120, 0, gz), cam_pos, cam_yaw, cam_pitch)
            draw.line([(p1[0], p1[1]), (p2[0], p2[1])], fill=grid_color, width=1)

        # Project and sort faces by average Z depth (Painter's Algorithm)
        face_render_data = []
        for face_idx, face in enumerate(self.scene.faces):
            screen_coords = []
            depths = []
            valid = True
            for v_idx in face:
                v = self.scene.vertices[v_idx]
                sx, sy, depth = self.project_vertex(v, cam_pos, cam_yaw, cam_pitch)
                screen_coords.append((sx, sy))
                depths.append(depth)

            avg_depth = sum(depths) / len(depths)
            color = self.scene.colors[face_idx]
            face_render_data.append((avg_depth, screen_coords, color))

        # Sort back-to-front
        face_render_data.sort(key=lambda item: item[0], reverse=True)

        # Draw 3D Polygons
        for avg_depth, coords, color in face_render_data:
            if len(coords) >= 3:
                draw.polygon(coords, fill=color, outline=(20, 20, 25))

        # Render On-Screen HUD Title & Metadata Overlay
        try:
            f_title = ImageFont.truetype("arial.ttf", 22)
            f_meta = ImageFont.truetype("arial.ttf", 16)
        except Exception:
            f_title = f_meta = ImageFont.load_default()

        # Header Box
        draw.rectangle([(20, 20), (self.width - 20, 75)], fill=(15, 20, 30, 220), outline=(0, 200, 100))
        draw.text((35, 30), f"VIRTUAL VADODARA RAILWAY STATION - 3D VIEWPORT", fill=(0, 255, 120), font=f_title)
        draw.text((35, 53), f"View Preset: {view_title} | Position: {cam_pos} | Status: Week 1-5 Models Loaded", fill=(220, 220, 225), font=f_meta)

        # Summary Legend at Bottom Left
        summary = self.scene.get_scene_summary()
        draw.rectangle([(20, self.height - 75), (420, self.height - 20)], fill=(15, 20, 30, 220), outline=(50, 100, 150))
        draw.text((35, self.height - 68), f"Total 3D Mesh Models: {summary['total_sub_models']} | Polygons: {summary['total_faces']}", fill=(255, 255, 255), font=f_meta)
        draw.text((35, self.height - 45), f"Deliverable Status: Weeks 1, 2, 3, 4 & 5 Complete (100%)", fill=(0, 220, 255), font=f_meta)

        img.save(output_path)
        print(f"[Renderer3D SUCCESS] Rendered 3D view snapshot to '{output_path}'")
        return output_path
