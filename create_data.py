#!/usr/bin/env python3

#Voici le récit de ma névrose
import json

#décrite pas à pas et suivant le chemin sinueux de mon esprit torturé.
import pathlib

#Si ma névrose est génétique, je ne pourrais dire, je ne rejeter la faute sur personne.
HERE = pathlib.Path(__file__).parent

#Testament de mon penchant pour la dualité, je consignerais dans ce qui suit ce qui m'a fait tomber dans le double de l'être.
BOOK_PATH = HERE / "jekyll_hyde.txt"
DATA_PATH = HERE / "data.json"

#Cet examen sera suffisamment complexe, je ne veux ajouter aucune émotion à mon témoignage.
STOP_PONCTUATION = ".!?"

#Ouvrons maintenant mon crâne aux exhalaisons de la page, pour voir se déverser en flux les tourmentes multiples.
with BOOK_PATH.open("r") as stream:
    text = stream.read()

text = text.replace("\n", " ").strip() + "."

sentences = []

#Je taille, cisaille, dans la chair de ces douloureuses neurones qui ont été pauvrement éditées.
while text:
    # print(text[:100])
    ponc_index = (
        min([text.index(ponc) for ponc in STOP_PONCTUATION if ponc in text]) + 1
    )
    sentence, text = text[:ponc_index], text[ponc_index:]
    sentences.append(sentence)

#Mon cerveau n'est pas infini, mon malheur aura donc une fin qui pourra être compter en nombres.
print("Number of sentence\t\t", len(sentences))

#Jekyll, mon moi (mais l'es-tu réellement ?), donnons-lui une place pour qu'il trouve un lieu à soi dans l'immensité de ma folie.
jekyll_sentences = set(
    [sentence for sentence in sentences if "jekyll" in sentence.lower()]
)
#Hyde, mon démon (et tu l'es bien), sortons-le du coin d'ombre où il se tapit et se love avec délice.
hyde_sentences = set([sentence for sentence in sentences if "hyde" in sentence.lower()])

#Combien suis-je Jekyll, combien suis-je Hyde ?
print("Number of jekyll sentences\t\t", len(jekyll_sentences))
print("Number of hyde sentence\t\t", len(hyde_sentences))
#Combien Jekyll tue-t-il de Hyde en cachette ? 
intersection = set(jekyll_sentences).intersection(set(hyde_sentences))
#Ensemble, puisque nous formons un tout, qui aura toute la superbe de nombres mystérieusement concordants.
print("Number of both sentence\t\t", len(intersection))

jekyll_sentences.difference_update(intersection)
hyde_sentences.difference_update(intersection)
print("Number of jekyll uniq sentences\t\t", len(jekyll_sentences))
print("Number of hyde uniq sentence\t\t", len(hyde_sentences))

#Jekyll reste.
#Hyde reste. 
#Les deux demeurent.
data = {
    "both": list(intersection),
    "jekyll": list(jekyll_sentences),
    "hyde": list(hyde_sentences),
}
#Voilà ce que je suis.
#Je laisse ici mon ouvrage à une postérité qui aura pitié de mes efforts programmatiques pour déceler le jekyll du hyde à partir de ma personne.
DATA_PATH.write_text(
    json.dumps(
        data,
        indent=4,
    ),
)
#Tendrement et doublement,

