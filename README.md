# Virtual Vadodara Railway Station: An Interactive 3D Visualization

[![Course](https://img.shields.io/badge/Course-CMP513%20%2B%20CMP514-blue.svg)](https://github.com/)
[![Python](https://img.shields.io/badge/Python-3.9%2B-green.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-orange.svg)](LICENSE)

## 📌 Project Overview
**Virtual Vadodara Railway Station** is an interactive 3D virtual walkthrough application created for the Computer Graphics & Image Processing (CMP513 + CMP514) course. 

Vadodara Railway Station is one of the busiest railway hubs in Gujarat. This project constructs an interactive 3D digital twin of the station complex—including the main station building, platform sheds, tracks, foot overbridge (FOB), ticket booking hall, waiting areas, and entrance gates—enabling ground-level first-person exploration. Additionally, an integrated **Image Processing** module handles real-time post-processing, screenshot enhancement, and Canny edge detection.

---

## 👥 Team Members (DSQUAD)

| Sr. No. | Enrollment No. | Name | Role |
|:---:|:---:|:---:|:---:|
| 1 | 24000858 | Mayank Adi | Station Building & Platform Modelling |
| 2 | 24001018 | Zeel Vasoya | Texturing, Lighting & Asset Creation |
| 3 | 24001026 | Prashobh Nair | Camera Navigation, GUI & Image Processing Pipeline |

---

## 📂 Project Directory Structure

```text
DSQUAD/
├── docs/
│   ├── CG IP - Project in Action.pdf
│   ├── CG_IP_Project_Proposal_-_Vadodara_Railway_Station.docx
│   └── project_proposal.md
├── src/
│   ├── gui/
│   │   ├── __init__.py
│   │   └── window.py
│   ├── processing/
│   │   ├── __init__.py
│   │   └── image_processor.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_pipeline.py
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Environment Setup & Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd DSQUAD
```

### 2. Create and Activate Virtual Environment
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

### 3. Install Required Dependencies
```bash
pip install -r requirements.txt
```

Core libraries installed:
- `opencv-python` (Computer vision & image processing)
- `PyOpenGL` (3D Graphics rendering pipeline)
- `PyQt5` (GUI frameworks & layout rendering)
- `numpy` (Numerical array operations)
- `matplotlib` (Data visualization & plotting)

---

## 🚀 Running the "Hello World" Pipeline Test

To verify that the GUI, Image Processing, and Visualization components are configured correctly, run the smoke test baseline script:

```bash
python src/main.py
```

### Expected Behavior
- Creates a test image canvas (`CG & IP Pipeline OK`).
- Applies grayscale conversion and Canny edge detection.
- Renders the baseline output in an OpenCV display window (`Pipeline Test`).
- Saves the rendered output frame to `pipeline_test_output.png`.

---

## 🧪 Running Automated Unit Tests

To run the unit tests suite covering the processing and GUI modules:

```bash
python -m unittest discover -s tests
```

---

## 🌿 Git Branching Strategy & Rules

To ensure a seamless collaborative workflow:
- **`main`**: Protected production branch. Direct commits are restricted.
- **Feature Branches**: Every feature development takes place on dedicated feature branches:
  - `feature/ui-setup` (GUI window setup & camera controllers)
  - `feature/image-loader` (Texture loader & image processing filters)
  - `feature/3d-models` (Station building, FOB, platform 3D mesh assets)

### Pull Request & Peer Review Guidelines
1. Create a feature branch: `git checkout -b feature/<feature-name>`
2. Push your branch: `git push origin feature/<feature-name>`
3. Open a Pull Request (PR) targeting `main`.
4. At least one peer review approval is required before merging.

---

## 📝 License
This project is developed for academic purposes under the CMP513 + CMP514 course curriculum.
