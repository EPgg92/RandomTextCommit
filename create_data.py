#!/usr/bin/env python3


import json


import pathlib


HERE = pathlib.Path(__file__).parent


BOOK_PATH = HERE / "miroir_pecheresse.txt"
DATA_PATH = HERE / "data.json"

STOP_PONCTUATION = ".!?"

with BOOK_PATH.open("r") as stream:
    text = stream.read()

text = text.replace("\n", " ").strip() + "."

sentences = []


while text:
    # print(text[:100])
    ponc_index = (
        min([text.index(ponc) for ponc in STOP_PONCTUATION if ponc in text]) + 1
    )
    sentence, text = text[:ponc_index], text[ponc_index:]
    sentences.append(sentence)


print("Number of sentence\t\t", len(sentences))

femme_sentences = set(
    [sentence for sentence in sentences if "femme" in sentence.lower()]
)
dieu_sentences = set([sentence for sentence in sentences if "dieu" in sentence.lower()])

print("Number of femme sentences\t\t", len(femme_sentences))
print("Number of dieu sentence\t\t", len(dieu_sentences))
intersection = set(femme_sentences).intersection(set(dieu_sentences))
print("Number of both sentence\t\t", len(intersection))

femme_sentences.difference_update(intersection)
dieu_sentences.difference_update(intersection)
print("Number of femme uniq sentences\t\t", len(femme_sentences))
print("Number of dieu uniq sentence\t\t", len(dieu_sentences))

data = {
    "both": list(intersection),
    "femme": list(femme_sentences),
    "dieu": list(dieu_sentences),
}


DATA_PATH.write_text(
    json.dumps(
        data,
        indent=4,
    ),
)
