# RandomTextCommit Marguerite de Navarre


## Quick setup for a given Gutenberg project

Retrieve the text from `https://ws-export.wmcloud.org/?lang=fr&title=Le_Miroir_de_l’âme_pécheresse.txt` and export the text in .txt format with the name "miroir_pecheresse" and save the file in the repo. 

Your now have a file "miroir_pecheresse" at the root.

Use the next command line to create `data.json`:

```sh
./create_data.py
```

The output the script shoud be: 

```txt
Number of sentence               698
Number of femme sentences                7
Number of dieu sentence          67
Number of both sentence          1
Number of femme uniq sentences           6
Number of dieu uniq sentence             66
```


## Usages

### SentenceOf script

```txt
usage: sentence_of.py [-h] -c {both,femme,dieu}

Select a random sentence containing given word from data.json

optional arguments:
  -h, --help            show this help message and exit
  -c {both,femme,dieu}, --contains {both,femme,dieu}
```

### To use as commit messager writer

#### Setup

```sh
https://github.com/EPgg92/RandomLiteraryExtract
cd RandomLiteraryExtract
echo """
alias cfemme='git commit -m \"\$($PWD/sentence_of.py -c femme)\"' 
alias cdieu='git commit -m \"\$($PWD/sentence_of.py -c dieu)\"' 
alias cfemmedieu='git commit -m \"\$($PWD/sentence_of.py -c both)\"' 
""" >> $HOME/.zshrc
source $HOME/.zshrc
```

#### Commit with it 

First add your changes:

```sh
git add my_files_changed.txt
```

Then just used `cfemme` or `cdieu` or `cfemmedieu`
