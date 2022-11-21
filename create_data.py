#!/usr/bin/env python3

import json

import pathlib

HERE = pathlib.Path(__file__).parent

BOOK_PATH = HERE / "jekyll_hyde.txt"
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

jekyll_sentences = set(
    [sentence for sentence in sentences if "jekyll" in sentence.lower()]
)
hyde_sentences = set([sentence for sentence in sentences if "hyde" in sentence.lower()])

print("Number of jekyll sentences\t\t", len(jekyll_sentences))
print("Number of hyde sentence\t\t", len(hyde_sentences))
intersection = set(jekyll_sentences).intersection(set(hyde_sentences))
print("Number of both sentence\t\t", len(intersection))

jekyll_sentences.difference_update(intersection)
hyde_sentences.difference_update(intersection)
print("Number of jekyll uniq sentences\t\t", len(jekyll_sentences))
print("Number of hyde uniq sentence\t\t", len(hyde_sentences))

data = {
    "both": list(intersection),
    "jekyll": list(jekyll_sentences),
    "hyde": list(hyde_sentences),
}


DATA_PATH.write_text(
    json.dumps(
        data,
        indent=4,
    ),
)
