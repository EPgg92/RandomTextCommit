# RandomLiteraryExtract


## Quick setup for a given Gutenberg project

Retrieve the text from `https://www.gutenberg.org` and select only desired lines. 

```sh
curl https://www.gutenberg.org/files/43/43-0.txt | awk 'NR>=59 && NR<=2583 { print }' > jekyll_hyde.txt
```

Use the next command line to create `data.json`:

```sh
./create_date
```

The output the script shoud be: 

```txt
Number of sentence               1375
Number of jekyll sentences               91
Number of hyde sentence          91
Number of both sentence          19
Number of jekyll uniq sentences          72
Number of hyde uniq sentence             72
```


## Usages

### SentenceOf script

```txt
usage: sentence_of.py [-h] -c {both,jekyll,hyde}

Select a random sentence containing given word from data.json

optional arguments:
  -h, --help            show this help message and exit
  -c {both,jekyll,hyde}, --contains {both,jekyll,hyde}
```

### To use as commit messager writer

#### Setup

```sh
https://github.com/EPgg92/RandomLiteraryExtract
cd RandomLiteraryExtract
echo """
alias cjekyll='git commit -m \"\$($PWD/sentence_of.py -c jekyll)\"' 
alias chyde='git commit -m \"\$($PWD/sentence_of.py -c hyde)\"' 
alias cjekyllhyde='git commit -m \"\$($PWD/sentence_of.py -c both)\"' 
""" >> $HOME/.zshrc
source $HOME/.zshrc
```

#### Commit with it 

First add your changes:

```sh
git add my_files_changed.txt
```

Then just used `cjekyll` or `chyde` or `cjekyllhyde`
