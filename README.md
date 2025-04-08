
# Hat Checker Live Streaming App

This project involves creating an Electron-based desktop application that streams live video of a hat detection model powered by YOLOv8. The app utilizes Flask to serve video frames, displaying them within the Electron interface.

## Features
- **Electron-based UI**: A sleek, modern macOS-style interface for watching the live video stream.
- **YOLOv8 Hat Detection**: A pre-trained YOLOv8 model is used to detect hats in the live video feed.
- **Real-time Stream**: The video stream is served via a Flask API from a camera or network video stream.
- **Responsive Design**: The app adapts to various screen sizes and provides smooth transitions and animations.
## UI Screenshots

### Main Screen
![Main Screen](FIRST UI.PNG)

### Stream View
![Stream View](SECOND UI.PNG)

## Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** (for Electron app development): [Install Node.js](https://nodejs.org/)
- **Python**: [Download Python](https://www.python.org/downloads/)
- **Flask**: `pip install Flask`
- **OpenCV**: `pip install opencv-python`
- **Ultralytics YOLO**: `pip install ultralytics`

## Installation

### Step 1: Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-repository/hat-checker-live-stream.git
cd hat-checker-live-stream
```

### Step 2: Backend Setup (Flask + YOLO)

1. **Download YOLOv8 Pre-trained Model**:  
   Download the `hat_model.pt` (or use a custom-trained model) and place it in the project directory.

2. **Install Required Python Packages**:
   Install the dependencies required for the backend:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask Server**:
   To start the video streaming server, run:

   ```bash
   python app.py
   ```

   This will start the Flask server on `http://localhost:5000` that streams the video feed with hat detection.

### Step 3: Frontend Setup (Electron)

1. **Install Electron**:
   In the project directory, run the following to install Electron dependencies:

   ```bash
   npm install
   ```

2. **Run the Electron App**:
   Start the Electron app with:

   ```bash
   npm start
   ```

   This will open the Electron-based desktop app with a live streaming feature.

## How It Works

- The frontend (Electron app) displays a button "Watch Stream". When clicked, it triggers a function to start the video stream from the Flask server (`http://localhost:5000/stream`).
- The backend (Flask server) captures the video feed from a source (camera or network stream) and processes each frame through a YOLOv8 model to detect hats. The frames are then served as a video stream using Flask's `Response` object.
- The frontend receives and displays the video stream within an HTML `img` tag.

## Project Structure

```
hat-checker-live-stream/
│
├── index.html         # Frontend HTML for the Electron app
├── main.js            # Electron main process file
├── app.py             # Flask app serving the video stream
├── requirements.txt   # Python dependencies (Flask, OpenCV, YOLO, etc.)
├── hat_model.pt       # Pre-trained YOLOv8 model for hat detection
└── README.md          # This file
```

## Troubleshooting

- **No Stream Available**: If the video stream isn't displaying, ensure that the Flask server is running correctly and the video source URL is accessible.
- **Slow Performance**: For better performance, consider using a local camera feed rather than a network stream, or optimize the YOLO model's configuration for lower latency.
  

