---
title: "Syncthing reappearing conflicts with the 'receive only' node"
date: 2023-04-05 07:14:07.788692567+00:00
canonical: https://gem.org.ru/syncthing-reappearing-conflicts-with-the-receive-only-node
---
 Ok, for a long time, I'm recreating my home setup in my new place. An increasing amount of new devices led me to use syncing tools again. A [syncthing](https://syncthing.net/) was the obvious but not easy way. 

I have a Raspberry Pi with a storage HDD and a desktop with my [Calibre](https://calibre-ebook.com/) library.  The setup is simple, and it's supposed to be easy: desktop as an introducer (Send&Recieve) and storage mounted to RPi as "Recieve Only". It should prevent any local changes to be synced.

The initial sync was ok, but further attempts to modify files there led to massive conflicted files appearing. Constantly pressing the "Revert Local Changes" button had little effect: new conflicts after file modification. 

I've applied my favorite tactic -- press all buttons and set all flags till it begin to work. The magic parameter was "Ignore Permissions" for the receiving side. No conflicts after  

 {{< public-inbox \>}}