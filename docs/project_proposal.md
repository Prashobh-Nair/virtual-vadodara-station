# Virtual Vadodara Railway Station: An Interactive 3D Visualization

## Project Details
- **Course**: Computer Graphics and Image Processing (CMP513 + CMP514)
- **Project Title**: Virtual Vadodara Railway Station: An Interactive 3D Visualization
- **Primary Category**: Computer Graphics
- **Secondary Category**: Image Processing

### Team Members
1. **Mayank Adi** (Enrollment No. 24000858)
2. **Zeel Vasoya** (Enrollment No. 24001018)
3. **Prashobh Nair** (Enrollment No. 24001026)

---

## 1. Project Overview
Vadodara Railway Station is a major transit hub on the Western Railway network. This project proposes the design and development of an interactive 3D virtual environment that realistically visualizes the Vadodara Railway Station complex, including:
- Main station building
- Platforms & railway tracks
- Foot overbridge (FOB)
- Ticket booking hall & waiting areas
- Circulating area, parking zone, and entrance/exit gates

The application uses computer graphics techniques such as 3D modelling, texture mapping, Phong lighting, perspective projection, and first-person camera navigation. A supplementary Image Processing module is integrated for post-processing screenshot captures (enhancement, edge detection, filtering).

---

## 2. Objectives
1. Construct a realistic 3D model of Vadodara Railway Station main building and platforms.
2. Recreate key station elements (railway tracks, foot overbridge, concourse, booking hall, parking zone).
3. Implement texture mapping and Phong lighting for visual realism.
4. Develop a free-roam camera navigation system (keyboard W/A/S/D movement, mouse look).
5. Integrate an image processing module (Gaussian blur, Canny edge detection, histogram equalization) for screenshot analysis.
6. Ensure smooth real-time rendering performance.

---

## 3. System Architecture & Modules
- **GUI Module (`src/gui/`)**: Renders viewport, captures keyboard & mouse input for first-person camera navigation.
- **Processing Module (`src/processing/`)**: Performs image enhancement and edge detection on captured scenes.
- **Visualization Engine (`src/main.py`)**: Ties together 3D rendering pipeline (OpenGL), camera controllers, and processing modules.

---

## 4. Technology Stack
- **Programming Language**: Python 3.x / C++
- **Graphics Library**: PyOpenGL / OpenGL (GLFW, GLSL)
- **GUI & Display**: PyQt5 / OpenCV / CustomTkinter
- **Image Processing**: OpenCV, NumPy
- **3D Modelling & Asset Creation**: Blender
- **Visualization & Plotting**: Matplotlib
