import tensorflow as tf
import matplotlib.pyplot as plt

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

print(dataset_size)
print(train_size)
print(val_size)
print(test_size)