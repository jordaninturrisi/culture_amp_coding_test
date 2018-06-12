import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import itertools

# Plot the train/val loss/accuracy as a function of epoch
# Include test loss & accuracy
def plot_loss(history):

	# Set size of figure
	plt.figure(figsize=(16,6))

	# Subplot 1: Loss
	# Logarithmic y axis, indicating test loss and lowest validation loss
	plt.subplot(1, 2, 1)
	plt.semilogy(history.history['loss'], color='r')
	plt.semilogy(history.history['val_loss'], color='g')
	# plt.semilogy([score[0]]*len(history.history['loss']), color='k', linestyle=':')
	plt.axvline(np.argmin(history.history['val_loss']), color='k', linestyle=':')
	plt.title('Model Loss')
	plt.ylabel('Loss')
	plt.xlabel('Epoch')
	plt.legend(['Train', 'Val', 'Test'], loc='upper right')

	# Subplot 2: Accuracy
	# Indicating test accuracy
	plt.subplot(1, 2, 2)
	plt.plot([i*100 for i in history.history['acc']], color='r')
	plt.plot([i*100 for i in history.history['val_acc']], color='g')
	# plt.plot([i*100 for i in [score[1]]*len(history.history['loss'])], color='k', linestyle=':')
	plt.title('Model Accuracy')
	plt.ylabel('Accuracy')
	plt.xlabel('Epoch')
	plt.legend(['Train', 'Val', 'Test'], loc='lower right')

	# Accommodate for tight layout & show image
	plt.show()

	return
