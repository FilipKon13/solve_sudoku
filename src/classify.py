import tensorflow as tf
from os.path import join
from glob import glob
from PIL import Image
import numpy as np

model = tf.keras.models.load_model(join('models','digit_model.h5'))


file = input()
img = np.array(Image.open(file))
res = np.argmax(model.predict(img[None,:,:,:])[0])
print(res)