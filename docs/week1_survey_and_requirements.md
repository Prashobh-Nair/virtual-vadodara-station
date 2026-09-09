# Week 1 Deliverable: Literature Survey & Requirement Analysis

## 1. Project Title & Overview
**Project Title**: Virtual Vadodara Railway Station: An Interactive 3D Visualization  
**Course**: Computer Graphics and Image Processing (CMP513 + CMP514)  
**Primary Category**: Computer Graphics  
**Secondary Category**: Image Processing  

**Team Members**:
1. Mayank Adi (Enrollment No. 24000858)
2. Zeel Vasoya (Enrollment No. 24001018)
3. Prashobh Nair (Enrollment No. 24001026)

---

## 2. Literature Survey & Comparative Analysis
A survey of existing 3D visualization, mapping, and authoring tools was conducted to identify technical capabilities and gaps addressed by this project.

| Existing Tool / Platform | Key Strengths | Fundamental Limitations | Project Differentiation |
|:---|:---|:---|:---|
| **Google Earth** | Global 3D terrain and satellite imagery | Lacks ground-level pedestrian detail; no interior views of platforms or concourses | Provides ground-level first-person exploration of station building, platforms, FOB, and ticket hall |
| **Blender** | High-fidelity 3D modelling and offline rendering suite | Authoring tool only; lacks standalone lightweight end-user interactive navigation runtime | Purpose-built interactive 3D desktop application dedicated to Vadodara Railway Station |
| **Unity 3D** | Cross-platform real-time engine with physics pipeline | Heavy engine footprint; complex asset pipelines for focused course requirements | Lightweight custom PyOpenGL rendering pipeline optimized specifically for public hub orientation |
| **Unreal Engine** | Photorealistic lighting (Lumen/Nanite) | High hardware system requirements; complex setup for academic scope | Lightweight real-time rendering executable on standard desktop/laptop GPUs |
| **SketchUp** | Fast architectural drafting | Limited real-time rendering quality; lacks interactive walkthrough controls | Combined 3D graphics rendering with integrated image processing post-processing module |

---

## 3. Problem Definition & Motivation
Vadodara Railway Station is a major transit hub on the Western Railway network. First-time commuters, visitors, and students frequently experience disorientation when navigating the complex station layout—specifically locating platform numbers, foot overbridges, ticket booking halls, and exit gates during peak hours.

Existing 2D static maps or satellite images do not provide an intuitive, ground-level spatial understanding. Recreating Vadodara Railway Station in a dedicated 3D interactive environment enables users to explore and familiarize themselves with the physical layout at their own pace prior to travel.

---

## 4. Functional Requirements
1. **3D Layout Rendering**: The system shall render a realistic 3D geometric representation of Vadodara Railway Station infrastructure (main building, platforms 1-4, tracks, foot overbridge, ticket hall, waiting area, parking, arch gates).
2. **Camera Navigation**: The system shall provide multiple viewing perspectives (Isometric Overview, Top-Down Plan View, First-Person Walkthrough, Platform View, FOB View).
3. **Lighting & Material Pipeline**: The system shall render ambient, diffuse, and specular lighting (Phong Reflection Model) with material colors for concrete, steel, glass, and asphalt.
4. **Screenshot Capture**: The system shall allow capturing viewport screenshots of any rendered 3D scene view.
5. **Image Processing Post-Processing**: The system shall apply image enhancement (Gaussian blur, Canny edge detection, histogram equalization) to captured station views.

---

## 5. Non-Functional Requirements
1. **Performance**: Maintain real-time frame rates (>= 30 FPS) on standard integrated/dedicated GPUs.
2. **Usability**: Intuitive camera and viewpoint controls.
3. **Modular Architecture**: Clean separation of 3D geometry models (`src/models/`), rendering pipeline (`src/gui/`), and image processing (`src/processing/`).
4. **Portability**: Runs on standard Windows 10/11 operating systems.

---

## 6. System Architecture Diagram

```text
                     +---------------------------------------+
                     |         User Input & Navigation       |
                     |     (Keyboard / Mouse / View Presets) |
                     +-------------------+-------------------+
                                         |
                                         v
                     +-------------------+-------------------+
                     |       Camera Controller Module        |
                     |  (View & Projection Transformations)  |
                     +-------------------+-------------------+
                                         |
                                         v
                     +-------------------+-------------------+
                     |       Master 3D Scene Graph           |
                     |  (VadodaraStationScene Assembler)     |
                     +-------------------+-------------------+
                                         |
       +------------------+--------------+--------------+------------------+
       |                  |                             |                  |
       v                  v                             v                  v
+--------------+  +---------------+             +---------------+  +---------------+
| Main Station |  | Platforms 1-4 |             | Railway Tracks|  | Foot Overbridge|
| Building     |  | & Canopies    |             | & Sleepers    |  | & Stairs      |
+--------------+  +---------------+             +---------------+  +---------------+
       |                  |                             |                  |
       +------------------+--------------+--------------+------------------+
                                         |
                                         v
                     +-------------------+-------------------+
                     |    Ticket Hall, Waiting Lounge,       |
                     |    Parking Zone & Arch Gates          |
                     +-------------------+-------------------+
                                         |
                                         v
                     +-------------------+-------------------+
                     |       3D OpenGL Rendering Engine      |
                     |  (Phong Lighting & Shading Model)     |
                     +-------------------+-------------------+
                                         |
                                         v
                     +-------------------+-------------------+
                     | Screenshot & Image Processing Module  |
                     |  (OpenCV / Canny Edge / Enhancement)  |
                     +---------------------------------------+
```
