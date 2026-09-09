# EXECUTIVE PROJECT STATUS REPORT (WEEK 5)

**Course**: Computer Graphics and Image Processing (CMP513 + CMP514)  
**Project Title**: Virtual Vadodara Railway Station: An Interactive 3D Visualization  
**Submission Milestone**: Week 5 Progress Review  
**Date of Report**: September 9, 2026  

---

## 👥 Team Members (DSQUAD)
1. **Mayank Adi** (Enrollment No. 24000858) — Station Building & Platform Modelling
2. **Zeel Vasoya** (Enrollment No. 24001018) — Texturing, Lighting & Asset Creation
3. **Prashobh Nair** (Enrollment No. 24001026) — Camera Navigation, GUI & Image Processing Pipeline

---

## 📊 Summary of Progress (Weeks 1 to 5 Completed: 100%)

```text
Progress Milestone Tracker (10 Weeks Timeline):
[x] Week 1: Literature survey and requirement analysis (COMPLETED)
[x] Week 2: Reference collection and station layout planning (COMPLETED)
[x] Week 3: Station building and platform modelling (COMPLETED)
[x] Week 4: Railway tracks and foot overbridge modelling (COMPLETED)
[x] Week 5: Ticket hall, waiting areas, parking, and gates (COMPLETED)
[ ] Week 6: Texture mapping and material application (UPCOMING)
[ ] Week 7: Lighting setup and camera navigation system development (UPCOMING)
[ ] Week 8: Image processing module integration (UPCOMING)
[ ] Week 9: Testing, optimization, and bug fixing (UPCOMING)
[ ] Week 10: Documentation and final presentation preparation (UPCOMING)
```

---

## 🎯 Completed Deliverables Matrix

### Week 1: Literature Survey & Requirement Analysis
- **Completed**: Survey of existing 3D tools (Google Earth, Unity, Unreal, Blender, SketchUp).
- **Artifact**: [`docs/week1_survey_and_requirements.md`](file:///c:/Users/Nair%20Prashobh%20Manoj/OneDrive/Desktop/Web/DSQUAD/docs/week1_survey_and_requirements.md) detailing functional & non-functional requirements and system architecture.

### Week 2: Reference Collection & Station Layout Planning
- **Completed**: Defined 3D Cartesian Coordinate System ($200\text{m} \times 150\text{m}$ world grid) and bounding box specifications for all station components.
- **Artifact**: [`docs/week2_layout_planning.md`](file:///c:/Users/Nair%20Prashobh%20Manoj/OneDrive/Desktop/Web/DSQUAD/docs/week2_layout_planning.md) with complete coordinate map and spatial zoning layout.

### Week 3: Station Building & Platform Modelling
- **Completed**: Developed procedural 3D models for Main Station Building ($90\text{m} \times 18\text{m} \times 20\text{m}$ facade, central dome, entrance arches, clock tower) and Platforms 1-4 (concrete bases, yellow safety lines, canopy roofs, benches, signs).
- **Artifact**: [`src/models/station_building.py`](file:///c:/Users/Nair%20Prashobh%20Manoj/OneDrive/Desktop/Web/DSQUAD/src/models/station_building.py) and [`src/models/platforms.py`](file:///c:/Users/Nair%20Prashobh%20Manoj/OneDrive/Desktop/Web/DSQUAD/src/models/platforms.py).

### Week 4: Railway Tracks & Foot Overbridge (FOB)
- **Completed**: Developed 3D models for dual parallel railway tracks (steel rails, wooden/concrete sleepers, ballast bed) and covered Foot Overbridge ($52\text{m}$ span across all platforms with staircases & protective railings).
- **Artifact**: [`src/models/railway_tracks.py`](file:///c:/Users/Nair%20Prashobh%20Manoj/OneDrive/Desktop/Web/DSQUAD/src/models/railway_tracks.py) and [`src/models/foot_overbridge.py`](file:///c:/Users/Nair%20Prashobh%20Manoj/OneDrive/Desktop/Web/DSQUAD/src/models/foot_overbridge.py).

### Week 5: Ticket Hall, Waiting Areas, Parking & Gates
- **Completed**: Developed 3D models for Ticket Booking Hall (booking windows, counters, queue dividers), Passenger Waiting Area (lounge, seating rows, LED screens), Tarmac Parking Lot (bays, barrier arms), and Main Entrance Arch Gate.
- **Artifact**: [`src/models/ticket_hall.py`](file:///c:/Users/Nair%20Prashobh%20Manoj/OneDrive/Desktop/Web/DSQUAD/src/models/ticket_hall.py), [`src/models/waiting_area.py`](file:///c:/Users/Nair%20Prashobh%20Manoj/OneDrive/Desktop/Web/DSQUAD/src/models/waiting_area.py), and [`src/models/parking_and_gates.py`](file:///c:/Users/Nair%20Prashobh%20Manoj/OneDrive/Desktop/Web/DSQUAD/src/models/parking_and_gates.py).

---

## 💻 Source Code Repository Architecture

```text
DSQUAD/
├── docs/
│   ├── week1_survey_and_requirements.md     # Literature survey & requirement analysis
│   ├── week2_layout_planning.md             # 3D coordinate map & layout planning
│   ├── week3_5_modelling_report.md          # 3D modelling technical report (W3-W5)
│   └── PROJECT_STATUS_WEEK_5.md             # Executive status report for Professor
├── src/
│   ├── models/                              # 3D Procedural Mesh Generators
│   │   ├── __init__.py
│   │   ├── base_model.py                    # 3D Mesh base class & Wavefront OBJ exporter
│   │   ├── station_building.py             # Main building, dome, arches, clock tower
│   │   ├── platforms.py                    # Platforms 1-4, canopy roofs, benches
│   │   ├── railway_tracks.py               # Steel rails, sleepers, ballast bed
│   │   ├── foot_overbridge.py              # Covered FOB bridge, staircases, railings
│   │   ├── ticket_hall.py                  # Booking hall, counters, windows
│   │   ├── waiting_area.py                 # Concourse lounge, seating rows, displays
│   │   ├── parking_and_gates.py            # Parking lot, entrance arch, security gates
│   │   └── scene_assembler.py              # Master 3D scene assembler
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── window.py                        # GUI Viewport window
│   │   └── renderer_3d.py                  # 3D Scene renderer & camera views
│   ├── processing/
│   │   ├── __init__.py
│   │   └── image_processor.py              # Image processing module
│   └── main.py                              # Master 3D Station viewer & snapshot generator
└── tests/
    ├── __init__.py
    ├── test_pipeline.py
    └── test_models.py                       # Unit tests for 3D models & scene graph
```

---

## 🔬 Verification & Automated Test Status
- **Unit Tests**: `tests/test_models.py` and `tests/test_pipeline.py` pass 100% of test cases.
- **Wavefront OBJ Export**: Master 3D model exported to `station_week5.obj`.
- **Rendering Snapshots**: Multi-angle 3D renders generated (`render_week5_overview.png`, `render_week5_building.png`, `render_week5_platforms_tracks.png`, `render_week5_ticket_parking.png`).
