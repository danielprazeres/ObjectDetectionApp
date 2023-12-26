from yolo_detector import YoloDetector
import cv2

def main():
    # Caminhos para os arquivos do YOLO
    weights_path = '/Users/danielprazeres/Desktop/ObjectDetectionApp/yolo_cfg/yolov3.weights'
    cfg_path = '/Users/danielprazeres/Desktop/ObjectDetectionApp/yolo_cfg/yolov3.cfg'
    names_path = '/Users/danielprazeres/Desktop/ObjectDetectionApp/yolo_cfg/coco.names'


    detector = YoloDetector(weights_path, cfg_path, names_path)

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        detections = detector.detect(frame)
        for label, x, y, w, h in detections:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow("Object Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
