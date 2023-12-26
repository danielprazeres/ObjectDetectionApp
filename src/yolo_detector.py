import cv2
import numpy as np

class YoloDetector:
    def __init__(self, weights_path, cfg_path, names_path):
        # Carregar os nomes das classes
        with open(names_path, "r") as f:
            self.classes = [line.strip() for line in f.readlines()]

        # Carregar a rede YOLO
        self.net = cv2.dnn.readNet(weights_path, cfg_path)

    def detect(self, img):
        height, width, _ = img.shape
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), swapRB=True, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.get_output_layers(self.net))

        class_ids = []
        confidences = []
        boxes = []

        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # Objeto detectado
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    # Coordenadas do retângulo
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

        results = []
        if len(indexes) > 0:
            # Flatten the array if the indexes are not already flat
            indexes = np.array(indexes).flatten()

            for i in indexes:
                x, y, w, h = boxes[i]
                label = str(self.classes[class_ids[i]])
                results.append((label, x, y, w, h))
        return results

    def get_output_layers(self, net):
        layer_names = net.getLayerNames()
        output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
        return output_layers
