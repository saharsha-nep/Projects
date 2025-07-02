import numpy as np
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt

model = tf.keras.models.load_model("cat_dog_model.h5")

path = input("Enter path for image file: ").strip('"')

img = cv2.imread(path)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()

if img is None:
    print("No image found.")
    exit()
else:
    resize = tf.image.resize(img,(256,256))
    input_img = np.expand_dims(resize/255.0, axis=0)

output = model.predict(input_img)
if output[0][0] >0.5:
    print("It's a dog.")
else:
    print("its a cat.")