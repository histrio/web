+++
date = "2017-04-08T20:02:43+03:00"
title = "Save as root in vim"
tags = ["snippets", "vim"]

+++

**TLDR**
```
:w !sudo tee %
```

It is a very common situation when for some remote session you are running vim with your default user to make some quick changes for some of your config files. After spending some time on it you are trying to save the result and getting this:

> `E45: 'readonly' option is set (add ! to override)`

or

> `"/etc/zsh/zshenv" E212: Can't open file for writing`

After that, you realize that you forgot to use `sudo` and all your work is tending to be pointless. To avoid this type:

`:w !sudo tee %`

It will pipe file content (`:w`) to the `tee` command which will write it to the `%` file with `sudo` wrapper.

It's not very comprehenseble and memorable string though, so it could be configured as a shortcut in your vim config like that:

```
cmap w!! w !sudo tee > /dev/null %
```

with that you could just type `w!!`. Thats all.


{{< public-inbox \>}}
