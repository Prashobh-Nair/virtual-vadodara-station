# Week 2 Deliverable: Reference Collection & Station Layout Planning

## 1. Spatial Coordinate System & World Grid
The 3D Virtual Vadodara Railway Station model is constructed using a Right-Handed Cartesian Coordinate System:
- **Origin $(0, 0, 0)$**: Located at ground level at the center of the Main Station Entrance Gate.
- **X-axis**: Horizontal East-West direction across station building width and platform lengths ($-100\text{m}$ to $+100\text{m}$).
- **Y-axis**: Vertical Height direction ($0\text{m}$ to $+25\text{m}$).
- **Z-axis**: Depth North-South direction from entrance gate to outer platforms ($-30\text{m}$ to $+120\text{m}$).
- **Scale Factor**: $1.0\text{ unit} = 1.0\text{ meter}$. Total Grid Size: $200\text{m} \times 150\text{m}$.

---

## 2. Architectural Components & Coordinates Map

| Component | World Position $(X, Y, Z)$ | Bounding Box Dimensions $(W \times H \times D)$ | Primary Material & Color |
|:---|:---|:---|:---|
| **Main Station Building** | $(0, 0, 0)$ | $90\text{m} \times 18\text{m} \times 20\text{m}$ | Terracotta Red Brick & Cream Trim |
| **Grand Central Dome** | $(0, 18, 0)$ | Radius $8\text{m}$, Height $7\text{m}$ | Gold / Bronze Dome Finish |
| **Clock Tower** | $(0, 25, 0)$ | $4\text{m} \times 6\text{m} \times 4\text{m}$ | White Marble Dial & Dark Hands |
| **Platform 1 (Main)** | $(0, 0, 30)$ | $160\text{m} \times 0.8\text{m} \times 8\text{m}$ | Concrete Gray with Yellow Tactile Line |
| **Track Line 1 & 2** | $(0, 0.1, 41)$ | $180\text{m} \times 0.3\text{m} \times 6\text{m}$ | Dark Steel Rails & Concrete Sleepers |
| **Platform 2 & 3 (Island)**| $(0, 0, 50)$ | $160\text{m} \times 0.8\text{m} \times 10\text{m}$ | Concrete Gray & Steel Pillars |
| **Track Line 3 & 4** | $(0, 0.1, 63)$ | $180\text{m} \times 0.3\text{m} \times 6\text{m}$ | Steel Rails & Ballast Gravel Bed |
| **Platform 4 (Outer)** | $(0, 0, 72)$ | $160\text{m} \times 0.8\text{m} \times 8\text{m}$ | Concrete Gray with Canopy Roof |
| **Foot Overbridge (FOB)** | $(0, 5.5, 51)$ | $12\text{m} \times 3.5\text{m} \times 52\text{m}$ | Blue Steel Truss Roof & Glass Side Panels |
| **Ticket Booking Hall** | $(-65, 0, 5)$ | $30\text{m} \times 6\text{m} \times 15\text{m}$ | Interior Glass Windows & Blue Counters |
| **Passenger Waiting Area** | $(+65, 0, 5)$ | $30\text{m} \times 6\text{m} \times 15\text{m}$ | Concourse Lounge & Seating Rows |
| **Parking Zone & Bays** | $(0, 0, -25)$ | $120\text{m} \times 0.1\text{m} \times 20\text{m}$ | Dark Asphalt Tarmac & White Bay Markings |
| **Main Entrance Arch Gate** | $(0, 0, -15)$ | $16\text{m} \times 7\text{m} \times 3\text{m}$ | Ornamental Wrought Iron & Stone Pillars |

---

## 3. Layout Diagram & Spatial Zoning

```text
               +---------------------------------------------------+
               |               PLATFORM 4 (Outer)                  | Z = 72m
               +---------------------------------------------------+
               |             Track Line 3 & Track Line 4           | Z = 63m
               +---------------------------------------------------+
               |               PLATFORM 2 & 3 (Island)             | Z = 50m
  FOB BRIDGE   |===================================================| (X: -6m..+6m)
  SPANNING     |             Track Line 1 & Track Line 2           | Z = 41m
  ALL TRACKS   +---------------------------------------------------+
               |               PLATFORM 1 (Main Station)           | Z = 30m
               +---------------------------------------------------+
                                         |
                                         v
   +-----------------------+-----------------------+-----------------------+
   | TICKET BOOKING HALL   | MAIN STATION BUILDING | PASSENGER WAITING     | Z = 0m
   | (X: -80m .. -50m)     | (X: -45m .. +45m)     | LOUNGE (X: +50m..+80m)|
   +-----------------------+-----------------------+-----------------------+
                                         |
                                         v
               +---------------------------------------------------+
               |          MAIN ENTRANCE ARCH & SECURITY GATES      | Z = -15m
               +---------------------------------------------------+
                                         |
                                         v
               +---------------------------------------------------+
               |         CIRCULATING AREA & PARKING LOT            | Z = -25m
               +---------------------------------------------------+
```
