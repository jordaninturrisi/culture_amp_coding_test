# Build & Compile Model
from keras.models import Sequential
from keras.layers import Dense, Embedding, Flatten, Dropout, LSTM
from keras.models import load_model

def build_model(vocab_size, max_length):
    model = Sequential()
    model.add(Embedding(vocab_size, 5, input_length=max_length))
    model.add(LSTM(5))
    model.add(Dense(4, activation='softmax'))

    model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    print('Model properties:')
    model.summary()

    return model


def predict_with_model(x_test):
    model = load_model('model/model')

    test_outputs = model.predict(x_test)

    return test_outputs
