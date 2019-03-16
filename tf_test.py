### Basic Keras tutorial test ###

from keras.models import Sequential
model = Sequential ()

from keras.layers import Dense

# ##Stacking layers
# model.add(Dense(units=64, activation='relu', input_dim=100))
# model.add(Dense(units=10, activation='softmax'))

# ##Configure learning process
# model.compile(loss='categorial_crossentropy', optimizer='sgd', metrics['accuracy'])

# ##Iterate on training data
# #x_train and y_train are numpy arrays
# model.fit(x_train, y_train, epochs=5, batch_size=32)

# ##Evaluate performance
# loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)

# ##Generate prediction
# classes = model.predict(x_test, batch_size=128)