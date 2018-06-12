import numpy as np
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

def load_data(verbose=True):
    ref_q = np.loadtxt('data/reference_questions.csv', dtype=str, delimiter='|', skiprows=1)
    ref_q = np.char.strip(ref_q)

    inputs = np.loadtxt('data/labeled_data_clean.csv', dtype=str, delimiter='|', skiprows=1)
    inputs = np.char.strip(inputs)

    if verbose:
        print('Reference questions:\n', ref_q)
        print('\nLabelled data:\n', inputs[:5])

    return ref_q, inputs


def prepare_test_data(tokenizer, max_length, verbose=True):
    x_test = np.loadtxt('data/test_questions.txt', dtype=str, delimiter=',')
    x_test = np.char.strip(x_test)

    if verbose:
        print('Test data:\n', x_test)

    x_test = tokenizer.texts_to_sequences(x_test)
    x_test = pad_sequences(x_test, maxlen=max_length, padding='post')

    return x_test


def create_training_vectors(inputs):
    x_train, tokenizer, max_length, vocab_size = vectorise_inputs(inputs)

    # x_train = inputs[:,0]
    print('Inputs shape: ', x_train.shape)
    y_train = np.zeros([inputs.shape[0], 4])

    for i in range(inputs.shape[0]):
        if (inputs[i,1] == 'TEA.2'):
            y_train[i,0] = 1
        elif (inputs[i,1] == 'ENA.3'):
            y_train[i,1] = 1
        elif (inputs[i,1] == 'ALI.5'):
            y_train[i,2] = 1
        elif (inputs[i,1] == 'INN.2'):
            y_train[i,3] = 1

    print('Targets shape: ', y_train.shape)

    return x_train, y_train, tokenizer, max_length, vocab_size


def vectorise_inputs(inputs):
    tokenizer = Tokenizer()

    x_train = inputs[:,0]
    tokenizer.fit_on_texts(x_train)
    # tokenizer.word_index
    # tokenizer.word_counts

    # Transform each text to sequence of integers
    # Integers correspond to tokenizer dictionary
    x_train = tokenizer.texts_to_sequences(x_train)

    # Pad sequences
    max_length = len(max(x_train, key=len))
    x_train = pad_sequences(x_train, maxlen=max_length, padding='post')

    vocab_size = len(tokenizer.word_index)+1

    return x_train, tokenizer, max_length, vocab_size
