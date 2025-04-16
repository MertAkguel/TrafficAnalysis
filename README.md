# Traffic Analysis

Ever wondered how many vehicles cross a road every day - and on which side? In this computer vision project, I used YOLOv8, SORT and OpenCV to detect, track and count vehicles in real time.

![Demo GIF](video/demo.gif)

## 📦 Features

- Real-time vehicle detection with YOLOv8
- Tracking of individual vehicles using SORT
- Counts vehicles separately for left and right side of the road
- Visualization of the results directly in the video (bounding boxes, lines, IDs, counters)

## 🧠 How It Works

This project uses the Eye Aspect Ratio (EAR) method to detect whether your eye is open or closed. Based on six landmark points around each eye, we track and count blink events per eye.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/MertAkguel/TrafficAnalysis.git
cd TrafficAnalysis
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Place your click sound

Download the video I used [here](https://youtu.be/KBsqQez-O4w?si=iUbXmv8Q1dlnzm69) and put it in the root folder.


### 4. Run the application

```bash
python CountCars.py
```

Press `Q` to exit.

---

## 🛠️ Technologies Used

- [OpenCV](https://opencv.org/) – image processing & webcam capture
- [MediaPipe](https://google.github.io/mediapipe/) – facial landmark detection
- [NumPy](https://numpy.org/) – distance calculations
- [Ultralytics](https://www.ultralytics.com/de) – Object Detection with YOLO

---

## 📈 Possible Improvements

- Usage of ByteTrack or DeepSORT Algorithm
- calculate speed
- analysis direction of vehicles

---

## 🧑‍💻 Author

**[Mert Akgül]** – *Computer Vision & AI Enthusiast*  
[Portfolio](https://medium.com/@Mert.A/list/projects-6f9bb92a3c21) | [Blog](https://medium.com/@Mert.A) | [LinkedIn](https://www.linkedin.com/in/mert-akgül)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
