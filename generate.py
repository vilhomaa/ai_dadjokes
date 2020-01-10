from __future__ import absolute_import, division, print_function, unicode_literals


import tensorflow as tf

import numpy as np
import os
import time
import pandas as pd 

path_to_file = "Z:\python\dadjokeai\dadjokevenv\dadjokes.txt"
os.chdir('Z:\python\dadjokeai\dadjokevenv')

checkpoint_dir = './training_checkpoints'
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')
vocab = sorted(set(text))
# Read, then decode for py2 compat.
text = open(path_to_file, 'rb').read().decode(encoding='utf-8')

def build_model(vocab_size, embedding_dim, rnn_units, batch_size):
  model = tf.keras.Sequential([
    tf.keras.layers.Embedding(vocab_size, embedding_dim,
                              batch_input_shape=[batch_size, None]),
    tf.keras.layers.GRU(rnn_units,
                        return_sequences=True,
                        stateful=True,
                        recurrent_initializer='glorot_uniform'),
    tf.keras.layers.Dense(vocab_size)
  ])
  return model

# Batch size
BATCH_SIZE = 64

# Length of the vocabulary in chars
vocab_size = len(vocab)

# The embedding dimension
embedding_dim = 256

# Number of RNN units
rnn_units = 1024

# Creating a mapping from unique characters to indices
char2idx = {u:i for i, u in enumerate(vocab)}
idx2char = np.array(vocab)

model = build_model(
  vocab_size = len(vocab),
  embedding_dim=embedding_dim,
  rnn_units=rnn_units,
  batch_size=BATCH_SIZE)
checkpoint_dir
print(tf.train.latest_checkpoint(checkpoint_dir))

model = build_model(vocab_size, embedding_dim, rnn_units, batch_size=1)

model.load_weights(tf.train.latest_checkpoint(checkpoint_dir))

model.build(tf.TensorShape([1, None]))

model.summary()


# ===============================================================
#       Generate Text
# ===============================================================

def generate_text(model, start_string):
  # Evaluation step (generating text using the learned model)

  # Number of characters to generate
  num_generate = 30000

  # Converting our start string to numbers (vectorizing)
  input_eval = [char2idx[s] for s in start_string]
  input_eval = tf.expand_dims(input_eval, 0)

  # Empty string to store our results
  text_generated = []

  # Low temperatures results in more predictable text.
  # Higher temperatures results in more surprising text.
  # Experiment to find the best setting.
  temperature = 0.75

  # Here batch size == 1
  model.reset_states()
  for i in range(num_generate):
      predictions = model(input_eval)
      # remove the batch dimension
      predictions = tf.squeeze(predictions, 0)

      # using a categorical distribution to predict the word returned by the model
      predictions = predictions / temperature
      predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

      # We pass the predicted word as the next input to the model
      # along with the previous hidden state
      input_eval = tf.expand_dims([predicted_id], 0)

      text_generated.append(idx2char[predicted_id])

  return (start_string + ''.join(text_generated))


# GENERATER!!!
jokes = generate_text(model, start_string=u"joke:")
print(jokes)


# Seuraava koodi splittaa generoidun tekstin yksittäisiin vitsehin
# ja tekee siitä listan

# ettii indeksit - alkaa joke:sta ja ottaa sitä edeltävän indeksin breakkaamista varten

def find_all_indexes(input_str, substring):
    l2 = []
    length = len(input_str)
    index = 0
    while index < length:
        i = input_str.find(substring, index)
        if i == -1:
            return l2
        l2.append(i)
        index = i + 1
    return l2



print(find_all_indexes(jokes, 'joke:'))

indexes = find_all_indexes(jokes, 'joke:')
jokelist = []
for i in range(len(indexes)-1):
    jokelist.append(jokes[indexes[i]:indexes[i+1]-1].replace('�', "'"))


## SEURAAVAKSI: PÄÄTÄ MINNE NOI VITSIT TALLENTAIS JA MITEN NE SAIS KUVIKS

## ettii liian lyhyet vitsit ja poistaa ne

# ettii kaikkien vaitsi liian lyhyiden indeksit
jokelist = list(set([x for x in jokelist if len(find_all_indexes(x, "\r\n")) > 2]))

for x in jokelist:
    print(x)


len(jokelist)

#poistaa duplikaatit
jokelist = list( dict.fromkeys(jokelist) )
len(jokelist)

## pistää jokelistin dataframeksi, 
df = pd.DataFrame(jokelist)
df.to_csv(r'Z:\python\dadjokeai\jokelist.csv')

