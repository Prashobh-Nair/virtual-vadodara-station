# Week 3 to 5 Deliverable: 3D Modelling Technical Report

## 1. Executive Summary
This technical report details the 3D geometry algorithms, procedural mesh generators, and spatial assembly developed for **Weeks 3, 4, and 5** of the **Virtual Vadodara Railway Station** project.

---

## 2. Week 3 Deliverables: Station Building & Platforms

### 2.1 Main Station Building (`src/models/station_building.py`)
- **Facade & Structure**: Constructed using procedural box primitives and extrusions ($90\text{m} \times 18\text{m} \times 20\text{m}$).
- **Central Dome**: Modeled using a hemispherical parametric mesh equation:
  $$x(\theta, \phi) = R \cos\theta \cos\phi, \quad y(\theta, \phi) = R \sin\phi, \quad z(\theta, \phi) = R \sin\theta \cos\phi$$
- **Arched Portico & Pillars**: 8 structural support columns supporting 5 entrance arches.
- **Clock Tower & Name Board**: Elevated tower ($Y = 25\text{m}$) featuring the official station title signage.

### 2.2 Platforms 1 to 4 (`src/models/platforms.py`)
- **Elevated Bases**: Platforms 1, 2, 3, 4 constructed at $Y = 0.8\text{m}$ height above rail track bed.
- **Safety Borders**: Bright yellow tactile warning strip running along the platform edge.
- **Canopy Shelters**: Steel support pillars supporting pitched metal corrugated roofs spanning $160\text{m}$.
- **Platform Amenities**: Passenger benches and illuminated platform designation signs.

---

## 3. Week 4 Deliverables: Railway Tracks & Foot Overbridge (FOB)

### 3.1 Railway Track Lines (`src/models/railway_tracks.py`)
- **Steel Rails**: Parallel I-beam extrusions spaced at standard gauge ($1.676\text{m}$) spanning $180\text{m}$.
- **Concrete/Wooden Sleepers (Ties)**: Cross-ties positioned every $0.6\text{m}$ along the track length.
- **Gravel Ballast Bed**: Tapered trapezoidal ballast base ($Y = 0.1\text{m}$ to $0.4\text{m}$).

### 3.2 Foot Overbridge (`src/models/foot_overbridge.py`)
- **Main Walkway Span**: Elevated covered pedestrian bridge ($Y = 5.5\text{m}$) spanning across all 4 platforms ($52\text{m}$ length).
- **Staircase Modules**: 4 sets of double-flight staircases connecting the FOB walkway directly down to Platforms 1, 2/3, and 4.
- **Enclosure & Protective Railings**: Side safety railings and translucent arch roof canopy.

---

## 4. Week 5 Deliverables: Ticket Hall, Waiting Areas, Parking & Gates

### 4.1 Ticket Booking Hall (`src/models/ticket_hall.py`)
- **Interior Layout**: $30\text{m} \times 6\text{m} \times 15\text{m}$ concourse area located at the western wing ($X = -65\text{m}$).
- **Booking Counters & Glass Windows**: 6 ticket transaction windows with glass partitions and blue counter desks.
- **Queue Stanchions**: Stainless steel posts with blue retractable tape queue dividers.

### 4.2 Passenger Waiting Area (`src/models/waiting_area.py`)
- **Concourse Lounge**: $30\text{m} \times 6\text{m} \times 15\text{m}$ lounge located at the eastern wing ($X = +65\text{m}$).
- **Seating Rows**: Multiple rows of 4-seater stainless steel passenger waiting chairs.
- **Information Displays**: Overhead train arrival/departure electronic LED screens.

### 4.3 Parking Zone & Entrance Arch Gates (`src/models/parking_and_gates.py`)
- **Circulating Area & Parking**: $120\text{m} \times 20\text{m}$ tarmac parking zone with marked parking slots and lane dividers.
- **Main Entrance Arch Gate**: $16\text{m} \times 7\text{m} \times 3\text{m}$ ornamental entrance gate with decorative archway and stone pillars.
- **Security Check Gates**: Entrance security barrier gates, turnstiles, and perimeter safety fencing.
