from ultralytics import YOLO
# from ultralytics.yolo.v8.detect.predict import Detection
import cv2

model = YOLO("/Users/hari/AndroidStudioProjects/Tflite/Computer-Vision/best.pt")
# model.predict(source="0", show=True, conf=0.5)


model.train(data="coco128.yaml", epochs=3)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
success = model.export(format="onnx")  # export the model to ONNX format