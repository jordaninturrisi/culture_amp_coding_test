import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM
from keras.models import load_model

# Create and compile network
def build_model(vocab_size, max_length, verbose=True):
    model = Sequential()
    model.add(Embedding(vocab_size, 5, input_length=max_length))
    model.add(LSTM(5))
    model.add(Dense(4, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    if verbose:
        print('Model properties:')
        model.summary()

    return model


# Use model to predict based on test data
# Load model if one is not supplied
def predict_with_model(x_test, model=None):

    if not model:
        model = load_model('model/model')

    test_probs = model.predict(x_test)

    return test_probs
