# -*- coding: utf-8 -*-
"""Sentence_embedding_BERT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ve8IR0U32kKMwA-f52SZ8hj9VMXThVSi
"""

!pip install -U sentence-transformers

from sentence_transformers import SentenceTransformer,util

data = [
    "I went to eat my dinner in A2b",
    "He ate banana for breakfast",
    "On my way back i drank tea",
    "I like to play badminton",
    "A dog was eating waste food near the hotel",
    "Yonex shoes are bit costlier than lining"
        ]

model = SentenceTransformer("sentence-transformers/all-MiniLM-L12-v1")

emb = model.encode(data)

for sentence,embedding in zip(data,emb):
  print("Sentence: ",sentence)
  print("Embedding ",embedding)

#print(util.cos_sim(emb,emb))
similarity = util.cos_sim(emb,emb)

#similarity.sort(reverse = True)
#similarity

all_sent_emb = []

for i in range(len(similarity)-1):
  for j in range(i+1,len(similarity)):
    all_sent_emb.append((similarity[i][j],i,j))

all_sent_emb

all_sent_emb.sort(key = lambda x: x[0] ,reverse = True)
all_sent_emb

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("clips/mfaq")

from sentence_transformers import util

question = "How many models can I host on HuggingFace?"
answer_1 = "All plans come with unlimited private models and datasets."
answer_2 = "AutoNLP is an automatic way to train and deploy state-of-the-art NLP models, seamlessly integrated with the Hugging Face ecosystem."
answer_3 = "Based on how much training data and model variants are created, we send you a compute cost and payment link - as low as $10 per job."

question_emb = model.encode(question)
answer_emb = model.encode([answer_1,answer_2,answer_3])

print(util.semantic_search(question_emb,answer_emb))

from transformers import pipeline

model = pipeline("question-answering")

question = "How many models can I host on HuggingFace?"
corpus = "All plans come with unlimited private models and datasets."
print(model(question,corpus))

from sklearn.cluster import KMeans

cluster = KMeans(n_clusters=4)

corpus = ['A man is eating food.',
          'A man is eating a piece of bread.',
          'Horse is eating grass.',
          'A man is eating pasta.',
          'A Woman is eating Biryani.',
          'The girl is carrying a baby.',
          'The baby is carried by the woman',
          'A man is riding a horse.',
          'A man is riding a white horse on an enclosed ground.',
          'A monkey is playing drums.',
          'Someone in a gorilla costume is playing a set of drums.',
          'A cheetah is running behind its prey.',
          'A cheetah chases prey on across a field.',
          'The cheetah is chasing a man who is riding the horse.',
          'man and women with their baby are watching cheetah in zoo'
          ]

model = SentenceTransformer("all-MiniLM-L6-v2")

corpus_emb=model.encode(corpus)

cluster.fit(corpus_emb)
labels = cluster.labels_

cluster_sentences = {}
for i,label in enumerate(labels):
  if label not in cluster_sentences:
    cluster_sentences[label] = [corpus[i]]
  else:
    cluster_sentences[label].append(corpus[i])
cluster_sentences

