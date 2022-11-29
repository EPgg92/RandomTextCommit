#!/usr/bin/env python3

import json

import pathlib

HERE = pathlib.Path(__file__).parent


BOOK_PATH = HERE / "[title_file].txt"
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

[term1]_sentences = set(
    [sentence for sentence in sentences if "[term1]" in sentence.lower()]
)
[term2]_sentences = set([sentence for sentence in sentences if "[term2]" in sentence.lower()])

print("Number of [term1] sentences\t\t", len([term1]_sentences))
print("Number of [term2] sentence\t\t", len([term2]_sentences))
intersection = set([term1]_sentences).intersection(set([term2]_sentences))
print("Number of both sentence\t\t", len(intersection))

[term1]_sentences.difference_update(intersection)
[term2]_sentences.difference_update(intersection)
print("Number of [term1] uniq sentences\t\t", len([term1]_sentences))
print("Number of [term2] uniq sentence\t\t", len([term2]_sentences))

data = {
    "both": list(intersection),
    "[term1]": list([term1]_sentences),
    "[term2]": list([term2]_sentences),
}


DATA_PATH.write_text(
    json.dumps(
        data,
        indent=4,
    ),
)
