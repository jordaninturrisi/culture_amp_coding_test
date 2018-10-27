# Imports
from __future__ import print_function

# Hide warnings
import os
import warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' #Hide messy TensorFlow warnings
warnings.filterwarnings("ignore") #Hide messy Numpy warnings

# Keras
import keras
import numpy as np
import matplotlib.pyplot as plt

from keras.callbacks import ModelCheckpoint
from keras.models import load_model

from utils.prepare_data import*
from utils.model import *
from utils.plots import *
from utils.results import*


# Load data & create input/output vectors
ref_q, inputs = load_data(verbose=True)

x_train, y_train, tokenizer, max_length, vocab_size = create_training_vectors(inputs)


# Create / Load Model
if not os.path.isfile('model/model'):
    # Build & Compile Model
    print('\n\nBuilding model...')
    model = build_model(vocab_size, max_length, verbose=True)

    # Callbacks
    checkpointer = ModelCheckpoint('model/model', monitor='val_loss', verbose=0, save_best_only=True, \
                                   save_weights_only=False, mode='auto', period=1)

   # Train Model
    print('Training model...')
    print('This should take around 5 minutes...')
    history = model.fit(x_train, y_train,
                       batch_size=32, epochs=250,
                       verbose=0,
                       validation_split=0.2,
                       shuffle=True,
                       callbacks=[checkpointer])

   # Visualise training
    plot_loss(history)

    print('\n\nLoading best model...')
    model = load_model('model/model')

else:
    # Load Model
    print('\n\nLoading pretrained model...')
    model = load_model('model/model')
    print('Pretrained model loaded')


# Evalute Model
print('\n\nEvaluating model...')
score = model.evaluate(x_train, y_train, verbose=0)
print('Overall Loss: %.4f' % score[0])
print('Overall Accuracy: %.2f%%' % (score[1]*100))


# Import test data & create input vector
x_test, test_inputs = prepare_test_data(tokenizer, max_length, verbose=True)

# Employ model on test data
test_probs = predict_with_model(x_test, model)

# Find 1st & 2nd most correlated reference questions
# Display results
display_results(test_probs, test_inputs, ref_q)
