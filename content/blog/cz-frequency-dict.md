---
title: "Czech Words Frequency List"
date: 2020-05-27T12:39:54+03:00
draft: false
tags: ["cz", "rust"]
---

I make a decision to learn Czech language and to procrastinate I've made up a problem for myself:

> I need a deck for the Anki with the most frequently accrued words in that language. 

So my mind considered that problem as a blocker to my further Czech lessons and force me to spend time on it. 
First of all, I need a data and very convenient way to get a *lot* of Czech text was a movie subtitle. Luckily it could be gathered as one big archive from [here](https://object.pouta.csc.fi/OPUS-OpenSubtitles/v2018/mono/cs.tok.gz). That file contains lines of tokens that could be easily separated.

First my implementation was blunt and straight: `python` + `SQLite`. Both are simple and I have some experience. And there was an obvious problem: it was slow. I had some ideas about optimization at first but then decided to change it drastically.

The second implementation was on pure `rust` and in the end it was even easier. It turned out then there is no need in a database and all collected data could be stored in a memory without any problem.

```rust
use std::io::BufReader;
use std::io::BufRead;
use std::fs::File;

use counter::Counter;

fn main() {
    let mut counter: Counter<String> = Counter::new();
    let file = BufReader::new(File::open("cs.tok").expect("Cannot open file."));
    for line in file.lines() {
        for tok in line.unwrap().split_whitespace(){
            if tok.chars().next().unwrap().is_alphabetic() {
                counter[&tok.to_lowercase()] += 1
            }
        }
    }
    for (tok, _) in counter.most_common_ordered().iter().take(5000) {
        println!("{}", tok);
    }
}
```

So, now I have in my hands a list of most frequently used words. In movies at least. Current list available [here](/czfrq.tar.gz)


{{< public-inbox \>}}
