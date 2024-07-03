import numpy as np 
import tensorflow as tf
from keras.api.models import Sequential
from keras.api.layers import Conv2D, MaxPooling2D, Flatten, Dense, Rescaling

from util import IMG_SHAPE

data_dir = "./pictures/"
BATCH_SIZE = 256

train_ds, val_ds = tf.keras.utils.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="both",
  seed=123,
  image_size=IMG_SHAPE,
  batch_size=BATCH_SIZE)

print(train_ds.class_names)

model = Sequential(layers=[
    Rescaling(1./255),
    Conv2D(32,3,activation = 'relu'),
    MaxPooling2D(),
    Conv2D(32,3,activation = 'relu'),
    MaxPooling2D(),
    Flatten(),
    Dense(128,activation='relu'),
    Dense(len(train_ds.class_names))]
)

model.compile(loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              optimizer = 'adam',
              metrics = ['accuracy'])

print("FITTING")
model.fit(train_ds, validation_data=val_ds, epochs = 5)
print("FITTING DONE")

model.summary()
print(model.summary())

print("VALIDATION")
valid_loss, valid_accuracy = model.evaluate(val_ds)
print(f"Accuracy: {valid_accuracy}\nLoss: {valid_loss}")

model.save('digit_model_v2.h5')
print("Saved")