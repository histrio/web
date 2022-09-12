---
title: "How to fix yum after CentOS 6 went EOL"
date: 2020-12-06 10:47:30+00:00
canonical: https://gem.org.ru/deprecated-centos-6
---
 Centos 6 isn't able to get its full updates since May 10th, 2017 and there are no even Maintainance updates since November 30th, 2020. For most of us that version of Centos, released July 20th, 2011 is objectively outdated but still, a huge amount of servers are using it and there are no plans or opportunities to migrate it further.

<!--more-->

Now, Centos 6 repository looks like a singular file with a message:

> This directory (and version of CentOS) is deprecated.

Also any attempt to make `yum update` will end with 

```raw
YumRepo Error: All mirror URLs are not using ftp, http[s] or file.
 Eg. Invalid release/repo/arch combination/
removing mirrorlist with no valid mirrors: /var/cache/yum/x86_64/6/base/mirrorlist.txt
Error: Cannot find a valid baseurl for repo: base
```

Luckily, we still have that repo in a [vault](https://vault.centos.org/6.10/) and we can replace the default one with it.

``` bash
$ sed -i 's,^#baseurl=http://mirror.centos.org/centos/\$releasever/,baseurl=http://vault.centos.org/6.10/,' \
    /etc/yum.repos.d/CentOS-Base.repo
```

After that, we are still not able to get actual updates for packages but at least update attempts will not fail.

## Epel

With [EPEL repositories](https://dl.fedoraproject.org/pub/epel/6/) situation is the same (no maintainable repo) and Fedora does provide vault-like alternative located [here](https://archives.fedoraproject.org/pub/archive/epel/). 
 

 {{< public-inbox \>}}