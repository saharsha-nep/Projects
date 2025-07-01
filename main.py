import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import numpy as np
import os

# Load and scale image data
batch_size =32
data = tf.keras.utils.image_dataset_from_directory("dataset", image_size=(256, 256),batch_size=batch_size)
data = data.map(lambda x, y: (x / 255.0, y))

# Data augmentation layer
data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomZoom(0.05),
    tf.keras.layers.RandomRotation(0.05)
])

# Apply augmentation to training data
augmented_data = data.map(lambda x, y: (data_augmentation(x, training=True), y))

# Split the dataset
dataset_size = len(data)  # Number of batches
train_size = int(dataset_size * 0.7)
val_size = int(dataset_size * 0.2) + 1
test_size = int(dataset_size *0.1) + 1

# Prepare training, validation, and test sets
train = augmented_data.take(train_size).repeat()
val = data.skip(train_size).take(val_size).repeat()
test = data.skip(train_size + val_size).take(test_size)

# Build model
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(256, 256, 3)),
    tf.keras.layers.Conv2D(16, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Conv2D(64,(3,3),activation ='relu'),
    tf.keras.layers.MaxPooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile
model.compile(optimizer='adam', loss=tf.losses.BinaryCrossentropy(), metrics=["accuracy"])

# Train
result = model.fit(
    train,
    epochs=10,
    steps_per_epoch=train_size,
    validation_data=val,
    validation_steps=val_size
)

# Plot accuracy
plt.plot(result.history['accuracy'], label='Train Accuracy', color='red')
plt.plot(result.history['val_accuracy'], label='Validation Accuracy', color='blue')
plt.legend()
plt.show()

#Test1
img = cv2.imread("dog.test.jpg")
resize = tf.image.resize(img,(256,256))
plt.imshow(resize.numpy().astype(int))
plt.show()

yhat = model.predict(np.expand_dims(resize/255,0))
if yhat[0][0] > 0.5:
    print("it's a dog")
else:
    print("it's a cat")

#Test2
img = cv2.imread("cat.test.jpg")
resize = tf.image.resize(img,(256,256))
plt.imshow(resize.numpy().astype(int))
plt.show()

yhat = model.predict(np.expand_dims(resize/255,0))
if yhat[0][0] > 0.5:
    print("it's a dog")
else:
    print("it's a cat")