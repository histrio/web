---
title: "How to Get Information About a Process in Linux"
date: 2020-05-16T21:47:56+03:00
tags: ["linux", "python", "proc"]
draft: true
---


There is a way to get information about any process (with according permissions) using filesystem operations only. You need no additional tools besides you already have on your system. In most cases `cat` will be ehough.

Actually for this post we will familrise with such files that can be displayed with `cat`.

`/proc/<pid>/autogroup`

`/proc/<pid>/cgroup`

`/proc/<pid>/cmdline`

`/proc/comm`

`/proc/cwd`

`/proc/environ`




