# Virtual Vadodara Railway Station: An Interactive 3D Visualization

[![Course](https://img.shields.io/badge/Course-CMP513%20%2B%20CMP514-blue.svg)](https://github.com/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-green.svg)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Week%201--5-100%25%20Completed-brightgreen.svg)](https://github.com/Prashobh-Nair/DSSQUAD)
[![License](https://img.shields.io/badge/License-MIT-orange.svg)](LICENSE)

## 📌 Executive Project Overview
**Virtual Vadodara Railway Station** is an interactive 3D virtual walkthrough application created for the Computer Graphics & Image Processing (CMP513 + CMP514) course.

Vadodara Railway Station is one of the major transit hubs in Gujarat. This project constructs an interactive 3D digital twin of the station complex—including the main station building facade, grand central dome, arches, clock tower, platform sheds (Platforms 1-4), parallel railway tracks, covered foot overbridge (FOB) with staircases, ticket booking hall, passenger waiting lounge, tarmac parking lot, and entrance arch gates—enabling ground-level first-person exploration. Additionally, an integrated **Image Processing** module handles real-time post-processing, screenshot enhancement, and Canny edge detection.

---

## 👥 Team Members (DSQUAD)

| Sr. No. | Enrollment No. | Name | Primary Role & Contributions |
|:---:|:---:|:---:|:---|
| 1 | 24000858 | Mayank Adi | Station Building, Dome & Platform 3D Modelling |
| 2 | 24001018 | Zeel Vasoya | Texturing, Lighting, Track & FOB Asset Creation |
| 3 | 24001026 | Prashobh Nair | Camera Navigation, 3D Renderer GUI & Image Processing Pipeline |

---

## 🗓️ 10-Week Project Progress Timeline

| Week | Activity | Deliverable Status |
|:---:|:---|:---:|
| **1** | Literature survey and requirement analysis | **COMPLETED (100%)** |
| **2** | Reference collection and station layout planning | **COMPLETED (100%)** |
| **3** | Station building and platform modelling | **COMPLETED (100%)** |
| **4** | Railway tracks and foot overbridge modelling | **COMPLETED (100%)** |
| **5** | Modelling of ticket hall, waiting areas, parking, and gates | **COMPLETED (100%)** |
| **6** | Texture mapping and material application | Upcoming |
| **7** | Lighting setup and camera navigation system development | Upcoming |
| **8** | Image processing module integration | Upcoming |
| **9** | Testing, optimization, and bug fixing | Upcoming |
| **10** | Documentation and final presentation preparation | Upcoming |

---

## 📂 Project Directory Structure

```text
DSQUAD/
├── docs/
│   ├── week1_survey_and_requirements.md     # Literature survey & requirement analysis (Week 1)
│   ├── week2_layout_planning.md             # 3D spatial coordinate map & layout (Week 2)
│   ├── week3_5_modelling_report.md          # 3D technical modelling report (Weeks 3-5)
│   └── PROJECT_STATUS_WEEK_5.md             # Executive status report for Professor
├── src/
│   ├── models/                              # 3D Procedural Mesh Generators
│   │   ├── __init__.py
│   │   ├── base_model.py                    # 3D Mesh base class & Wavefront OBJ exporter
│   │   ├── station_building.py             # Main building, dome, arches, clock tower (Week 3)
│   │   ├── platforms.py                    # Platforms 1-4, canopy roofs, benches (Week 3)
│   │   ├── railway_tracks.py               # Steel rails, sleepers, ballast bed (Week 4)
│   │   ├── foot_overbridge.py              # Covered FOB bridge, staircases, railings (Week 4)
│   │   ├── ticket_hall.py                  # Booking hall, counters, windows (Week 5)
│   │   ├── waiting_area.py                 # Concourse lounge, seating rows, displays (Week 5)
│   │   ├── parking_and_gates.py            # Parking lot, entrance arch, security gates (Week 5)
│   │   └── scene_assembler.py              # Master 3D scene assembler
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── window.py                        # GUI Viewport window
│   │   └── renderer_3d.py                  # 3D Scene renderer & multi-view camera engine
│   ├── processing/
│   │   ├── __init__.py
│   │   └── image_processor.py              # Image processing module (Canny Edge Detection)
│   └── main.py                              # Master 3D Station viewer & snapshot generator
├── tests/
│   ├── __init__.py
│   ├── test_pipeline.py                     # Pipeline integration unit tests
│   └── test_models.py                       # 3D Geometry unit tests
├── requirements.txt                         # Python dependencies
└── README.md                                # Project documentation & status
```

---

## ⚙️ Environment Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Prashobh-Nair/DSSQUAD.git
cd DSQUAD
```

### 2. Activate Virtual Environment
- **Windows (PowerShell)**:
  ```powershell
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
- **Linux / macOS**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Master 3D Station Application

To execute the complete 3D Virtual Vadodara Railway Station pipeline for Weeks 1–5:

```bash
python src/main.py
```

### What this executes:
1. **Assembles Master 3D Scene**: Merges all 7 sub-models into a unified 3D spatial scene.
2. **Exports 3D Mesh**: Exports `station_week5.obj` Wavefront 3D model.
3. **Renders Multi-Angle 3D Snapshots**:
   - `render_week5_overview.png` (Isometric station overview)
   - `render_week5_building.png` (Main station building & entrance)
   - `render_week5_platforms_tracks.png` (Platforms, tracks & FOB)
   - `render_week5_ticket_parking.png` (Ticket hall, waiting lounge & parking)
4. **Applies Image Processing**: Runs Canny edge detection and output image saving.

---

## 🧪 Running Automated Unit Tests

To run the full unit test suite covering all 3D models, scene graph, and processing modules:

```bash
python -m unittest discover -s tests
```

---

## 🌿 Git Branching Strategy & Workflow

- **`main`**: Protected production branch.
- **Feature Branches**:
  - `feature/ui-setup`
  - `feature/image-loader`
  - `feature/3d-models`

---

## 📝 License
Developed for academic purposes under the CMP513 + CMP514 course curriculum.
