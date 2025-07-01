import os
from tensorflow.keras.models import load_model

os.makedirs("models", exist_ok=True)

# Load your trained model first
model = load_model("path_to_your_trained_model.h5")

# Save it again (or save to a new location)
model.save(os.path.join("models", "Dog&CatClassifier.h5"))
