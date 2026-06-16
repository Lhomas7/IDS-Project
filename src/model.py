import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix
#This file will contain the structuring and build of the Neural Network

def build_model(input_dim):

    #create the three layers of the neural network and output a single number, the percent
    #that the model believes the answer is 'yes'
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(input_dim,)),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    #compile the model
    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    return model




