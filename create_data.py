#!/usr/bin/env python3

#Oh Romeo, Romeo, what does it take to reach you ? 
import json

#Oh Juliet, Juliet, what do I need to climb at you ? 
import pathlib

#Here we will be united
HERE = pathlib.Path(__file__).parent

#and the data.json will be our love contract
BOOK_PATH = HERE / "romeo_juliet.txt"
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

romeo_sentences = set(
    [sentence for sentence in sentences if "romeo" in sentence.lower()]
)
juliet_sentences = set([sentence for sentence in sentences if "juliet" in sentence.lower()])

print("Number of romeo sentences\t\t", len(romeo_sentences))
print("Number of juliet sentence\t\t", len(juliet_sentences))
intersection = set(romeo_sentences).intersection(set(juliet_sentences))
print("Number of both sentence\t\t", len(intersection))

romeo_sentences.difference_update(intersection)
juliet_sentences.difference_update(intersection)
print("Number of romeo uniq sentences\t\t", len(romeo_sentences))
print("Number of juliet uniq sentence\t\t", len(juliet_sentences))

data = {
    "both": list(intersection),
    "romeo": list(romeo_sentences),
    "juliet": list(juliet_sentences),
}


DATA_PATH.write_text(
    json.dumps(
        data,
        indent=4,
    ),
)
