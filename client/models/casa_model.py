import keras
from keras.layers import Conv2D, MaxPooling2D
from keras.layers import Dense, Dropout, Flatten
from keras.models import Sequential
from keras.layers import LSTM
import os


import tempfile

# Create an initial LSTM Model
def create_seed_model():
    model = Sequential()
    model.add(LSTM(100, input_shape=(1,36)))
    model.add(keras.layers.Dense(72, activation='relu'))
    model.add(keras.layers.Dense(50, activation='relu'))
    model.add(keras.layers.Dense(36, activation='relu'))
    model.add(keras.layers.Dense(28, activation='relu'))
    model.add(Dense(10, activation='softmax'))
    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adam(),
                  metrics=['accuracy'])
    return model
