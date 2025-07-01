import tensorflow as tf
import matplotlib.pyplot as plt

data = tf.keras.utils.image_dataset_from_directory("dataset") #basically preprocessing stuff, batch size, image res, all done based on whatever they have as usual values
data_iterator = data.as_numpy_iterator() #index to access data
batch = data_iterator.next() #32 images as numpy arrays

# Display the first 4 images and their labels
fig, ax = plt.subplots(ncols=4, figsize=(20, 20))

for idx, image in enumerate(batch[0][:4]):
    ax[idx].imshow(image.astype('uint8'))  # Convert image for display
    label = data.class_names[batch[1][idx]]
    ax[idx].title.set_text(f"Label: {label}")

plt.show()

