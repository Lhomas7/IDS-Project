import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix
#This file will contain the structuring and build of the Neural Network

#create the three layers of the neural network and output a single number, the percent
#that the model believes the answer is 'yes'
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(X_train.shape[1],)),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

#compile the model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

#then train the model on the data
history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=32,
    validation_split=0.2
)

#Now we will evaluate the model and report the metrics
y_pred = (model.predict(X_test) > 0.5).astype("int32")

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))



