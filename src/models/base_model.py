import math
from typing import List, Tuple

class Mesh3D:
    """
    Core 3D Mesh class supporting procedural geometry creation, 
    bounding box computation, vertex/face transformations, and OBJ export.
    """
    def __init__(self, name: str = "Mesh3D"):
        self.name = name
        self.vertices: List[Tuple[float, float, float]] = []
        self.faces: List[List[int]] = []
        self.colors: List[Tuple[int, int, int]] = []  # RGB colors per face
        self.face_normals: List[Tuple[float, float, float]] = []

    def add_vertex(self, x: float, y: float, z: float) -> int:
        self.vertices.append((float(x), float(y), float(z)))
        return len(self.vertices) - 1

    def add_face(self, vertex_indices: List[int], color: Tuple[int, int, int] = (200, 200, 200)):
        self.faces.append(vertex_indices)
        self.colors.append(color)

    def add_box(self, center: Tuple[float, float, float], size: Tuple[float, float, float], color: Tuple[int, int, int] = (200, 200, 200)):
        """
        Adds a 3D rectangular box to the mesh.
        """
        cx, cy, cz = center
        dx, dy, dz = size[0] / 2.0, size[1] / 2.0, size[2] / 2.0

        v0 = self.add_vertex(cx - dx, cy - dy, cz - dz)
        v1 = self.add_vertex(cx + dx, cy - dy, cz - dz)
        v2 = self.add_vertex(cx + dx, cy + dy, cz - dz)
        v3 = self.add_vertex(cx - dx, cy + dy, cz - dz)
        v4 = self.add_vertex(cx - dx, cy - dy, cz + dz)
        v5 = self.add_vertex(cx + dx, cy - dy, cz + dz)
        v6 = self.add_vertex(cx + dx, cy + dy, cz + dz)
        v7 = self.add_vertex(cx - dx, cy + dy, cz + dz)

        # 6 quad faces
        self.add_face([v0, v3, v2, v1], color)  # Front
        self.add_face([v4, v5, v6, v7], color)  # Back
        self.add_face([v0, v4, v7, v3], color)  # Left
        self.add_face([v1, v2, v6, v5], color)  # Right
        self.add_face([v3, v7, v6, v2], color)  # Top
        self.add_face([v0, v1, v5, v4], color)  # Bottom

    def add_cylinder(self, center: Tuple[float, float, float], radius: float, height: float, segments: int = 12, color: Tuple[int, int, int] = (150, 150, 150)):
        """
        Adds a vertical cylinder to the mesh.
        """
        cx, cy, cz = center
        half_h = height / 2.0

        bottom_indices = []
        top_indices = []

        for i in range(segments):
            angle = 2.0 * math.pi * i / segments
            x = cx + radius * math.cos(angle)
            z = cz + radius * math.sin(angle)
            bottom_indices.append(self.add_vertex(x, cy - half_h, z))
            top_indices.append(self.add_vertex(x, cy + half_h, z))

        # Side quad faces
        for i in range(segments):
            next_i = (i + 1) % segments
            b1, b2 = bottom_indices[i], bottom_indices[next_i]
            t1, t2 = top_indices[i], top_indices[next_i]
            self.add_face([b1, b2, t2, t1], color)

        # Top and Bottom caps
        self.add_face(top_indices, color)
        self.add_face(list(reversed(bottom_indices)), color)

    def add_dome(self, center: Tuple[float, float, float], radius: float, height: float, segments: int = 12, rings: int = 6, color: Tuple[int, int, int] = (212, 175, 55)):
        """
        Adds a hemispherical dome to the mesh.
        """
        cx, cy, cz = center
        ring_vertices = []

        for r in range(rings + 1):
            phi = (math.pi / 2.0) * (r / rings)
            y = cy + height * math.sin(phi)
            ring_r = radius * math.cos(phi)
            current_ring = []

            for s in range(segments):
                theta = 2.0 * math.pi * s / segments
                x = cx + ring_r * math.cos(theta)
                z = cz + ring_r * math.sin(theta)
                current_ring.append(self.add_vertex(x, y, z))
            ring_vertices.append(current_ring)

        for r in range(rings):
            for s in range(segments):
                next_s = (s + 1) % segments
                v1 = ring_vertices[r][s]
                v2 = ring_vertices[r][next_s]
                v3 = ring_vertices[r + 1][next_s]
                v4 = ring_vertices[r + 1][s]
                self.add_face([v1, v2, v3, v4], color)

    def get_bounding_box(self) -> Tuple[Tuple[float, float, float], Tuple[float, float, float]]:
        if not self.vertices:
            return ((0.0, 0.0, 0.0), (0.0, 0.0, 0.0))
        min_x = min(v[0] for v in self.vertices)
        min_y = min(v[1] for v in self.vertices)
        min_z = min(v[2] for v in self.vertices)
        max_x = max(v[0] for v in self.vertices)
        max_y = max(v[1] for v in self.vertices)
        max_z = max(v[2] for v in self.vertices)
        return ((min_x, min_y, min_z), (max_x, max_y, max_z))

    def export_obj(self, filename: str) -> None:
        """
        Exports mesh data to standard Wavefront .obj file format.
        """
        with open(filename, 'w') as f:
            f.write(f"# Wavefront OBJ exported for {self.name}\n")
            for v in self.vertices:
                f.write(f"v {v[0]:.4f} {v[1]:.4f} {v[2]:.4f}\n")
            for face in self.faces:
                idx_str = " ".join(str(idx + 1) for idx in face)
                f.write(f"f {idx_str}\n")
