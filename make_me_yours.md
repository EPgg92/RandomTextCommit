# Make RTC your Own

## Quick setup for a Corpus

*We recommand to use texts with free licence of use.*

You will find some on [Wikisource](https://en.wikisource.org/wiki/Main_Page) or [Gutenberg project](https://www.gutenberg.org/).

- If you text do have a download link with .txt extension :

Retrieve the text from `$URL` and select only desired lines. 

```sh
curl $URL | awk 'NR>=59 && NR<=2583 { print }' > $FILENAME.txt
```

- If you text does not have one :

Retrieve the text from `$URL` and export the text in .txt format with the name `${FILENAME}.txt` and save the file in the repo.

Your now have a file `${FILENAME}.txt` at the root.

## Choose the Adversity

In the file `./create_data.py` you may change `[term1]` and `[term2]` by any terms qui vous semblent à propos pour le texte importé (10 replacements for each term).

> in jekyll_hyde branch, importants terms are "jekyll" and "hyde"; in jekyll_hyde branch, importants terms are "jekyll" and "hyde"; etc.

Make sure to change the name of the file de référence at line 10 :

```python
BOOK_PATH = HERE / "${FILENAME}.txt"
```

## Create your Data

Use the next command line to create `data.json`:

```sh
./create_data.py
```

The output the script shoud be:

```txt
Number of sentence               [incredible number]
Number of [term1] sentences               [incredible number]
Number of [term2] sentence          [incredible number]
Number of both sentence          [incredible number]
Number of [term1] uniq sentences          [incredible number]
Number of [term2] uniq sentence             [incredible number]
```

## Use Me

### SentenceOf Script

```txt
usage: sentence_of.py [-h] -c {both,[term1],[term2]}

Select a random sentence containing given word from data.json

optional arguments:
  -h, --help            show this help message and exit
  -c {both,[term1],[term2]}, --contains {both,[term1],[term2]}
```

### To use as Commit Messager Writer

#### Setup

In your version of RTC local repository : 

```sh
echo """
alias c[term1]='git commit -m \"\$($PWD/sentence_of.py -c [term1]])\"' 
alias c[term2]='git commit -m \"\$($PWD/sentence_of.py -c [term2])\"' 
alias c[term1][term2]='git commit -m \"\$($PWD/sentence_of.py -c both)\"' 
""" >> $HOME/.zshrc
source $HOME/.zshrc
```

#### Just RandomCommitText with It 

First add your changes:

```sh
git add my_files_changed.txt
```

Then just used `c[term1]` or `c[term2]` or `cjekyllhyde`

## Help Me Please

If you have problems, difficulties or fears with the setting up of RTC, you can :

- refer to the usage examples: [RTC_Jekyll_Hyde](https://github.com/EPgg92/RandomTextCommit/tree/jekyll_hyde), [RTC_Marguerite](https://github.com/EPgg92/RandomTextCommit/tree/marguerite_navarre), [RTC_Romeo_Juliet](https://github.com/EPgg92/RandomTextCommit/tree/romeo_juliet)
- create an issue on the [present repository](https://github.com/EPgg92/RandomTextCommit/issues)
- cry in front of the screen watching the rain on a Saturday in November (not recommanded).