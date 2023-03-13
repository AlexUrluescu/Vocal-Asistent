import tensorflow as tf  #import the module
import numpy as np  # numpy make the manipulation of numbers easier

# celsius degrees = fahrenheit degrees ( 1 Celsius = 33.8 Fahr.  etc)
celsius = np.array([1, 10, 25, 43, 76, 100, 126, 13], dtype=float)
fahrenheit = np.array([33.8, 50, 77, 109.4, 168.8, 212, 258.8, 55.4], dtype=float)

# creating connection with the neurons
capa = tf.keras.layers.Dense(units=1, input_shape=[1])
modelo = tf.keras.Sequential([capa])

modelo.compile(
    optimizer = tf.keras.optimizers.Adam(0.22),  # the AI will learn with a 0.2 marge of learn
    loss="mean_squared_error"
)

print("Start training ...")

# the AI will take the celsius and fahrenheit values and train with them
historial = modelo.fit(celsius, fahrenheit, epochs=1000, verbose=False)  # training the AI 1000 times

print("Model trained")

print("Prediction")

resultado = modelo.predict([43]) # here the AI after learned, will give us a prediction, 
                                    # in this case a prediction for 13 C degrees in Fahrenheit

print(f"The result is {resultado} + fahrenheit")