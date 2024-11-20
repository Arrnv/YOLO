from ultralytics import YOLO

model = YOLO("yolov8x")

results = model.predict("/Users/arnavlahane/YOLO/inputvideos/D35bd9041_1 (25).mp4",save=True)

print(results[0])
print("======================")
for boxes in results[0].boxes:
    print(boxes)