---
title: "Czech Words Frequency List"
date: 2020-05-27 11:53:44+00:00
canonical: https://gem.org.ru/czech-words-frequency-list
---
 I make a decision to learn the Czech language and to procrastinate I've made up a problem for myself:

> I need a deck for the Anki with the most frequently accrued words in that language.

<!--more-->

So my mind considered that problem as a blocker to my further Czech lessons and force me to spend time on it.
First of all, I need data, and a very convenient way to get a *lot* of Czech text was movie subtitles. Luckily it could be gathered as one big archive from [here](https://object.pouta.csc.fi/OPUS-OpenSubtitles/v2018/mono/cs.tok.gz). That file contains lines of tokens that could be easily separated.

First, my implementation was blunt and straight: `python` + `SQLite`. Both are simple and I have some experience. And there was an obvious problem: it was slow. I had some ideas about optimization at first but then decided to change it drastically.

The second implementation was on pure `rust` and in the end, it was even easier. It turned out then there is no need for a database and all collected data could be stored in a memory without any problem.

```rust
use std::io::BufReader;
use std::io::BufRead;
use std::fs::File;

// I'm using an external crate to have an easy way to get the most common items.
use counter::Counter;

fn main() {
    let mut counter: Counter<String> = Counter::new();
    // Create a reader from a file
    let file = BufReader::new(File::open("cs.tok").expect("Cannot open file."));

    // Each line will be splitted by whiltespace
    for line in file.lines() {
        for tok in line.unwrap().split_whitespace(){
            // Skip a token if first character is not a letter.
            if tok.chars().next().unwrap().is_alphabetic() {
                counter[&tok.to_lowercase()] += 1
            }
        }
    }

    // Print first 5000 most common tokens
    for (tok, _) in counter.most_common_ordered().iter().take(5000) {
        println!("{}", tok);
    }
}
```

So, now I have in my hands a list of the most frequently used words. In movies at least. Current list available [here](/czfrq.tar.gz). This method is applyable to any language you can get a decent amount of text.

Next step will be [Anki](https://ankiweb.net/) deck generation.


 

 {{< public-inbox \>}}