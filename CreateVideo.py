import os
import cv2

path = "Images"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext in ['.gif', '.png', '.jpg', '.jpeg', '.jfif']:
        file_name = path+"/"+file
        print(file_name)
        images.append(file_name)
        
print(len(images))
count = len(images)

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)

print("Please enter either sunset or sunrise")
print("or 1 for sunset and 2 for sunrise")
video_type = input(": ")

if video_type == "sunset" or video_type == "sunset" or video_type == "1" or video_type == "2":
    print("")
else:
    print("Wrong input")
    exit(0)

out = cv2.VideoWriter('sunset.mp4' if video_type.lower() == "sunset" or "1" else 'sunrise.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

# sunrise
if video_type.lower() == "sunset" or "1":
    for i in range(count-1, 0, -1):
        frame = cv2.imread(images[i])
        out.write(frame)
else:
    for i in range(0, count-1):
        frame = cv2.imread(images[i])
        out.write(frame)

out.release()
print("Done")
