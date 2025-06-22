import cv2

video = cv2.VideoCapture(0)
tracker = cv2.TrackerKCF_create()

ret, frame = video.read()
bbox = cv2.selectROI("Tracking", frame, False)
tracker.init(frame, bbox)

while True:
    ret, frame = video.read()
    success, box = tracker.update(frame)

    if success:
        (x, y, w, h) = [int(v) for v in box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0,255,0), 2)

    cv2.imshow("Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
