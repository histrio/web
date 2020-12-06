---
title: "Store Files in a CouchDB"
date: 2020-06-19T11:57:15+03:00
draft: false
tags: ["couchdb"]
---

There is a very convinent way to store a files indise CouchDB and by able to get them directly from it. In a simple way, an attachment is a new field in a document.

Lets say we have a document with id `e5f46d968b31e400b5db6426d000024b`.

```bash
$ curl -X GET http://admin:password@127.0.0.1:5984/sandbox/e5f46d968b31e400b5db6426d000024b
{"_id":"e5f46d968b31e400b5db6426d000024b","_rev":"1-967a00dff5e02add41819138abb3284d"}
```

and we want to attach some `index.html` to that document.

We have a two way to attach a file:

### Attach via Fauxton

There is a *Upload attachment* button on a documents page

[http://127.0.0.1:5984/_utils/#database/sandbox/e5f46d968b31e400b5db6426d000024b]()

![fauxton-attachement-1 image](/img/fauxton-attachement-1.png)

### Attach via curl

```bash
curl -vX PUT http://127.0.0.1:5984/sandbox/e5f46d968b31e400b5db6426d000024b/index.html?rev=1-967a00dff5e02add41819138abb3284d --data-binary @index.html -H "ContentType: text/html"
```

### Attachment structure

As a result we will have an addition field `_attachments` which will contain all files that we attached. In our case it's `index.html` only.

```
{
  "_id": "e5f46d968b31e400b5db6426d000024b",
  "_rev": "2-83c73b6b3427d2bb5a8fc5492c6320f8",
  "_attachments": {
    "index.html": {
      "content_type": "text/html",
      "revpos": 2,
      "digest": "md5-MyN94QzefBF07zIZQ7D4jg==",
      "length": 14,
      "stub": true
    }
  }
}
```

It's super easy to get and it's accessible as an simple page

```
curl -X GET http://admin:password@127.0.0.1:5984/sandbox/e5f46d968b31e400b5db6426d000024b/index.html
<html></html>
```


{{< public-inbox \>}}
