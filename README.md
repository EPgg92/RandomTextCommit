# RandomLiteraryExtract


## Quick setup for a given Gutenberg project

Retrieve the text from `https://www.gutenberg.org/` and select only desired lines. 

```sh
curl https://www.gutenberg.org/cache/epub/1777/pg1777.txt | awk 'NR>=59 && NR<=2583 { print }' > romeo_juliet.txt
```

For a more peculiar use : change terms in `./create_data.py` : in romeo_juliet branch, importants terms are "romeo" and "juliet"; in jekyll_hyde branch, importants terms are "jekyll" and "hyde"; etc.

Use the next command line to create `data.json`:

```sh
./create_data.py
```

The output the script shoud be: 

```txt
Number of sentence               2192
Number of romeo sentences                99
Number of juliet sentence                30
Number of both sentence          4
Number of romeo uniq sentences           95
Number of juliet uniq sentence           26
```


## Usages

### SentenceOf script

```txt
usage: sentence_of.py [-h] -c {both,romeo,juliet}

Select a random sentence containing given word from data.json

optional arguments:
  -h, --help            show this help message and exit
  -c {both,romeo,juliet}, --contains {both,romeo,juliet}
```

### To use as commit messager writer

#### Setup

```sh
https://github.com/EPgg92/RandomLiteraryExtract
cd RandomLiteraryExtract
echo """
alias cromeo='git commit -m \"\$($PWD/sentence_of.py -c romeo)\"' 
alias cjuliet='git commit -m \"\$($PWD/sentence_of.py -c juliet)\"' 
alias cromeojuliet='git commit -m \"\$($PWD/sentence_of.py -c both)\"' 
""" >> $HOME/.zshrc
source $HOME/.zshrc
```

#### Commit with it 

First add your changes:

```sh
git add my_files_changed.txt
```

Then just used `cromeo` or `cjuliet` or `cromeojuliet`
