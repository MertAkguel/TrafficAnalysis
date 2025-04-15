import cv2
from ultralytics import YOLO
from sort import *
from help_func import create_video_writer

BLUE = (255, 0, 0)
RED = (0, 0, 255)
GREEN = (0, 255, 0)

# https://youtu.be/KBsqQez-O4w?si=iUbXmv8Q1dlnzm69
path = r"D:\ML_datasets\CarsVideoObjectTracking\4KVideoOfHighwayTraffic!.mp4"
output_filename = "video/hightraffic_result.mp4"

# class_ids of interest - car, motorcycle, bus and truck
CLASS_ID = [2, 3, 5, 7]

model = YOLO("yolov8l.pt")
tracker = Sort(max_age=20, min_hits=2, iou_threshold=0.3)

cap = cv2.VideoCapture(path)
writer = create_video_writer(cap, output_filename)

pTime = 0

left_road_count = []
right_road_count = []
color = (0, 0, 0)

crossed_line_already = set()

limits = [0, 600, 1280, 600]

print("So it begins")
while True:
    success, img = cap.read()

    if not success:
        break

    height, width, _ = img.shape  # 720, 1280

    results = model.predict(img, classes=CLASS_ID)

    detections = np.empty((0, 5))

    for r in results:
        boxes = r.boxes
        for i, box in enumerate(r.boxes):

            conf = np.ceil((box.conf[0] * 100)) / 100

            x1 = int(box.xyxy[0][0])
            y1 = int(box.xyxy[0][1])
            x2 = int(box.xyxy[0][2])
            y2 = int(box.xyxy[0][3])

            cx = int((x1 + x1 + (x2 - x1)) / 2)
            cy = int((y1 + y1 + (y2 - y1)) // 2)

            if x2 < width // 2:
                color = BLUE
            else:
                color = RED

            currentArray = np.array([x1, y1, x2, y2, conf])
            detections = np.vstack((detections, currentArray))

            # cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)

    resultsTracker = tracker.update(detections)

    color_line = (255, 0, 255)

    for result in resultsTracker:
        x1, y1, x2, y2, id = result
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        # print(result)
        w, h = x2 - x1, y2 - y1

        cx, cy = x1 + w // 2, y1 + h // 2
        color_circle = (255, 0, 255)

        if cx > width // 2 and limits[1] - 15 < cy < limits[1] + 15:
            if right_road_count.count(id) == 0:
                right_road_count.append(id)

                color_line = BLUE
                color_circle = BLUE

        elif cx < width // 2 and limits[1] - 15 < cy < limits[1] + 15:
            if left_road_count.count(id) == 0:
                left_road_count.append(id)
                color_line = RED
                color_circle = RED

        # cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)

    cv2.line(img, (limits[0], limits[1]), (limits[2], limits[3]), color_line, 5)

    # cvzone.putTextRect(img, f' Count: {len(totalCount)}', (50, 50))
    cv2.putText(img, str(len(left_road_count)), (255, 100), cv2.FONT_HERSHEY_PLAIN, 5, RED, 8)
    cv2.putText(img, str(len(right_road_count)), (800, 100), cv2.FONT_HERSHEY_PLAIN, 5, BLUE, 8)
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, GREEN, 2)
    cv2.imshow("Video", img)
    writer.write(img)

    k = cv2.waitKey(1)
    if k == ord('q'):
        break
    """elif k == ord('s'):
        continue"""

writer.release()
cv2.destroyAllWindows()
