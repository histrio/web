---
title: "How to Get Basic Information About a Process in Linux"
date: 2020-05-16T21:47:56+03:00
tags: ["linux", "python", "proc"]
draft: false
---


There is a way to get information about any process (with according permissions) using filesystem operations only. You need no additional tools besides you already have on your system. In most cases `cat` will be ehough.

Actually for this post we will familrise with such files that can be displayed with `cat` and we will begin with the real simle ones

`/proc/<pid>/cmdline`

It will produce an output with full command line with the process was runned.

```
cat /proc/33439/cmdline
/bin/sh/usr/bin/fakeroot--bash-hB/usr/bin/makepkg-F-cf--noconfirm--noextract--noprepare--holdver%
```

`/proc/<pid>/comm`

That file contains a command name that was runned

```
cat /proc/33439/comm
fakeroot
```

`/proc/environ`

Will output all environment variables for the process


```
cat /proc/30306/environ
ALACRITTY_LOG=/tmp/Alacritty-30279.logBINARYEN=/usrBINARYEN_ROOT=/usrCOLORTERM=truecolorDBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/busDISPLAY=:0.0GTK_MODULES=canberra-gtk-moduleHG=/usr/bin/hg
```
