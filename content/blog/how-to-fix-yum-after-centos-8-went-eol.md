---
title: "How to fix yum after CentOS 8 went EOL "
date: 2022-07-01 07:57:56.971026738+00:00
---
 > Error: Failed to download metadata for repo 'appstream': Cannot prepare internal mirrorlist: No URLs in mirrorlist

So now we have the same issues that we had for Centos 6. And therefore we can fix it like it was described in [previous post](/deprecated-centos-6).

```
$ sed -i 's,baseurl=http://vault.centos.org,baseurl=http://vault.epel.cloud|g' /etc/yum.repos.d/CentOS-Linux-*
```

<!--more-->

## Alternative (AlmaLinux)

The issue with the fix above is that now we have a frozen repo that never will be updated. If your want to have the latest security updates you may consider a migration to one of Cento's successors. An AlmaLinux migration script is located [here](https://github.com/AlmaLinux/almalinux-deploy). Basically, it looks like this:
```bash
$ sudo dnf -y upgrade
$ curl -O https://raw.githubusercontent.com/AlmaLinux/almalinux-deploy/master/almalinux-deploy.sh
$ sudo bash almalinux-deploy.sh
``` 

 {{< public-inbox \>}}