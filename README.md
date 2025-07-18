# Mech Tayara
# Autonomous DJI Tello Drone Navigation with Obstacle Avoidance

This project implements an autonomous drone navigation system for the DJI Tello quadcopter. It uses a grid-based map, real-time obstacle detection via computer vision, and the A* pathfinding algorithm to enable safe navigation in an indoor prototype environment modeled after TUM Campus Heilbronn.

---

## 🧠 Project Overview

- **Goal**: Enable a DJI Tello drone to autonomously navigate a predefined grid map while dynamically detecting and avoiding obstacles using its onboard camera.
- **Path Planning**: Implemented using the A* algorithm for efficient route finding.
- **Obstacle Detection**: Real-time visual detection using OpenCV with edge detection and brightness thresholding.
- **Execution**: The drone continuously recalculates its path if an obstacle is detected, ensuring collision-free navigation.

---

## 📁 Project Structure

```bash
tello_drone_project/
├── main.py                  # Main execution script
├── drone_controller.py      # Drone initialization and movement functions
├── path_planning.py         # A* algorithm and heuristic function
├── obstacle_detection.py    # Frame processing and obstacle detection logic
├── map_config.py            # Grid map and start/goal coordinates
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

## 🛠 Hardware Requirements

- DJI Tello Drone  
- Computer (with Wi-Fi connection to the Tello)  
- Onboard Tello Camera (1280x720 @ 30 fps)

---

## 💻 Software Requirements

- Python 3.7+
- [`djitellopy`](https://github.com/damiafuentes/DJITelloPy) – Drone control library  
- OpenCV – For image processing  
- NumPy – For matrix and numerical operations  

---

## 🔧 Installation

Clone the project and install dependencies:

```bash
git clone https://github.com/wassim-mezghanni/MechTayara
cd tello-drone-navigation
pip install -r requirements.txt
```

## 🚀 Running the Project
Power on the DJI Tello drone.

Connect your computer to the Tello Wi-Fi network.

Run the main script:

bash
Copier
Modifier
python main.py
The drone will take off, follow the computed path, detect obstacles, and re-plan its route as needed.

