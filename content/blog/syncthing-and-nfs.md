---
title: "Syncthing and NFS"
date: 2021-11-26 10:43:37
---
 *TLDR: Dockerised Syncthing using NFS mounted folder is a bad idea.*

About a year ago I've started the process of migration from Dropbox to Syncthing. The structure of a new files synchronization flow was simple: one always online node, and a bunch of consumers.  It was fine at first, but after a couple of months, I've noticed an increased amount of updated-file notifications. Files in the notification were not modified at any device that I'm aware of. Another strange thing is that my tools, which dotfiles were in synching folder started to complain about the lack of config files and reset it to the initial state.
 
First of all, I blamed the android app and excluded it from the flow. I'd had no luck and mess with my dotfiles continued. Nodes were often unsynchronised, logs showed a lot of deleted-created status for the files that nobody touched. A file could be deleted and reappeared again in a matter of hours.
After days of troubleshooting, I was able to locate the source of the issue. It was my main node setup. The Syncthing process in the node was dockerized and the mounted sync folder was also an NFS mount. Changing it to SMB did no effect.

So my current solution is a structural change. Now each node is synced with all others and with no master. Each node uses it's own local filesystem. Works like a charm. 

 {{< public-inbox \>}}