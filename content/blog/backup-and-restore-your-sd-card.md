---
title: "Backup and restore your SD card"
date: 2022-09-08 13:29:36.574610625+00:00
---
 ## Backup

To get rid of empty space, we will process it via `gzip`

```bash
$ sudo dd if=/dev/mmcblk0 conv=sync,noerror bs=64K | gzip -c > backup.img.gz
```
## Restore

```
$ gunzip backup.img.gz
$ sudo dd if=backup.img of=/dev/mmcblk0 bs=4M && sync
```
<!--more-->

## Mount image

If you need just to explore the content of your backup or get only one file from it, you can mount it to a folder. First of all, you need to get an offset where your filesystem actually begins
```
$ fdisk -l backup.img                                                                        ~
Disk backup.img: 14.42 GiB, 15485370368 bytes, 30244864 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x93c181e7

Device                          Boot Start      End  Sectors  Size Id Type
backup.img1       8192 30244863 30236672 14.4G 83 Linux
```
As you can see in the example above we have one partition that starts on `8192` sector and each sector is `512` bytes. Now, all we have to do is multiply `8192 * 512 = 4194304` and use it as an offset when mounting as a loop device

```
$ sudo mount -o offset=4194304 backup.img /mnt/backup
``` 

 {{< public-inbox \>}}