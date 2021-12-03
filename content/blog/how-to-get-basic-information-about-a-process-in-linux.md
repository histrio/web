---
title: "How to Get Basic Information About a Process in Linux"
date: 2020-05-16 14:11:22+00:00
---
 There is a way to get information about any process (with according permissions) using filesystem operations only. You need no additional tools besides what you already have on your system. In most cases `cat` will be enough.

Actually, for this post, we will familiarise with such files that can be displayed with `cat` and we will begin with the real simple ones

`/proc/<pid>/cmdline`

It will produce an output with a full command line with the process being run.

```bash
$ cat /proc/33439/cmdline
/bin/sh/usr/bin/fakeroot--bash-hB/usr/bin/makepkg-F-cf--noconfirm--noextract--noprepare--holdver%
```

`/proc/<pid>/comm`

That file contains a command name that was runned

```bash
$ cat /proc/33439/comm
fakeroot
```

`/proc/environ`

Will output all environment variables for the process


```bash
$ cat /proc/30306/environ
ALACRITTY_LOG=/tmp/Alacritty-30279.logBINARYEN=/usrBINARYEN_ROOT=/usrCOLORTERM=truecolorDBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/busDISPLAY=:0.0GTK_MODULES=canberra-gtk-moduleHG=/usr/bin/hg
``` 

 {{< public-inbox \>}}