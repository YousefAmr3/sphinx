# -*- coding: utf-8 -*-
"""untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/adamlinux99/8524c69c0a9f92b8d8577a1996fd3a04/untitled0.ipynb
"""

#JPG:used with many social media platforms and very small size, some information is loset when compressed
#GIF: compression without lost, Limited 256
#TIFF: high quality image, very large size

#AVI: high quality format, very large size need more storage
#mp4: very common used with social media suported from many browsers, Lossy format
#mkv: good quality, not very good with mobiles devices

#mp3: sound quality decreased heavily
#wav:oldest audio formats. used with CDs, sound quaity of signal is retained
#AAC:used with games and mobile devices

#csv: csv file is about half size of json and xml files so we used it to reduce bandwidth, comma seperatd value, use for huge da
#xml: represnt data in hirecichal structure
#json: best exchange format becuase it is light weight
#xlsx: tabular contains cells used for complex data

# !pip install Pillow
# !pip install matplotlib

#opencv-python pip install opencv-python & import cv2, install matplotlib--> import matplotlib.pyplot as plt #pillow pip install Pillow & from PIL import Image ---> Image.open(r'path')
#sicikt-image--> skimage.io.imread()
import skimage

from PIL import Image
import matplotlib.pyplot as plt

image=Image.open(r"/content/512px-PNG_transparency_demonstration_1.webp")
plt.imshow(image)
image.save("try.png")

#audio
# !pip install pydub
# conda install -c conda-forg ffmpeg
import pydub
audio_input = r"/content/y2mate.com - No Copyright Fuzzeke  Time Decimator Sound Design Trailer Music30 SEC.mp3"
audio_output = r"try.wav"
sound = pydub.AudioSegment.from_mp3(audio_input)
sound.export(audio_output, format="avi")

import subprocess
subprocess.call(["ffmpeg","-i", "30 Second Timer.mp4", "hello.avi"])

# !pip install dict2xml
from dict2xml import dict2xml

student = {
    "age" : 19,
    "gender" : "male"
}

xml = dict2xml(student)

print(xml)

# coco yolo pascal convert


# Coco:
# Format [x_min, y_min, width, height]

# The coordinates (x_min, y_min) are the top-left corner along with the width and height of the bounding box.

# Pascal_VOC :
# Format: [x_min, y_min, x_max, y_max]

# x_min and y_min are coordinates of the top-left corner and x_max and y_max are coordinates of bottom-right corner of the bounding box.

# Yolo:
# Format: [x_center, y_center, width, height]

# x_center and y_center are the normalized coordinates of the centre of the bounding box. The width and height are the normalized length. To convert YOLO in Coco or Pascal or vice versa it is important to have the size of the image to calculate the normalization.


# convert code

# Convert Coco bb to Pascal_Voc bb
def coco_to_pascal_voc(x1, y1, w, h):
    return [x1,y1, x1 + w, y1 + h]

# Convert Coco bb to Yolo
def coco_to_yolo(x1, y1, w, h, image_w, image_h):
    return [((2*x1 + w)/(2*image_w)) , ((2*y1 + h)/(2*image_h)), w/image_w, h/image_h]


# Convert Pascal_Voc bb to Coco bb
def pascal_voc_to_coco(x1, y1, x2, y2):
    return [x1,y1, x2 - x1, y2 - y1]


# Convert Pascal_Voc bb to Yolo
def pascal_voc_to_yolo(x1, y1, x2, y2, image_w, image_h):
    return [((x2 + x1)/(2*image_w)), ((y2 + y1)/(2*image_h)), (x2 - x1)/image_w, (y2 - y1)/image_h]

# Convert Yolo bb to Coco bb
def yolo_to_coco(x_center, y_center, w, h,  image_w, image_h):
    w = w * image_w
    h = h * image_h
    x1 = ((2 * x_center * image_w) - w)/2
    y1 = ((2 * y_center * image_h) - h)/2
    return [x1, y1, w, h]



# Convert Yolo bb to Pascal_voc bb
def yolo_to_pascal_voc(x_center, y_center, w, h,  image_w, image_h):
    w = w * image_w
    h = h * image_h
    x1 = ((2 * x_center * image_w) - w)/2
    y1 = ((2 * y_center * image_h) - h)/2
    x2 = x1 + w
    y2 = y1 + h
    return [x1, y1, x2, y2]

#compare between COCO, YOLO and PASCAL VOC

# Coco is a huge image dataset collected for object detection, segmentation.
# Coco dataset store the annotation of images in JSON file that's consist of block
# blocks are info, license, categories, images, annotations
# In YOLO labeling format, a .txt file with the same name is created for each image file in the same directory. Each .txt file cont <object-class> <x> <y> <width> <height>
# 2 0.31071276376 0.86768627 0.123444
# 1 0.31323276376 0.2343327 0.33244
# 0.213133 8.213133
# PASCAL VOC is a data annotation format that stores annotation information in XML format.
# In PASCAL VOC, each image requires an XML file. This format was generated as.
# a part of the challenge for classification and detection competition.
# PASCAL VOC provides image datasets for over 20 classes that used object detection, semantic segmentation, and other classification tasks

#What is text annotation?

"""Text annotation is the process of assigning labels to a text document or different elements of its content. As intelligent as machines can get, human language is sometimes hard to decode, even for humans. In text
annotation, sentence components or structures are highlighted by certain criteria to prepare datasets to train a model that can effectively recognize the human language, intent, or the emotion behind the words."""

#waht are types of text annotation

# 1. Entity annotationi. En
# 2. Entity linking
# 3. Text classification
# 4. Sentiment annotation
# 5. Linguistic annotation.

import cv2
import matplotlib.pyplot as plt

image = cv2.imread('/content/image.jpg')
output_image_png = cv2.imwrite('output.png', image)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image_rgb)
plt.show()

# !pip install pylabel
from pylabel import importer
dataSet= importer.ImportVOC(r"sample_data")
dataSet.export.ExportToCoco(r"sample_data/output.json")



