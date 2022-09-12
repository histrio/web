---
title: "How to fix Rust tools that bind libgit2.so"
date: 2022-09-08 11:26:51.355827901+00:00
canonical: https://gem.org.ru/how-to-fix-rust-tools-that-bind-libgit2-so
---
 Recently, after a system update, I became not able to run some of the system tools written on Rust, like `exa` and `bat`
``` bash
$ bat --version                                                                ~
bat: error while loading shared libraries: libgit2.so.1.4: cannot open shared object file: No such file or directory
```
The fix was easy: rebuild a binary
```
$ cargo install exa bat --force
```
 

 {{< public-inbox \>}}