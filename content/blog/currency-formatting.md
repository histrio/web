---
title: "Currency formatting"
date: 2021-12-02 11:45:23
---
 ```python
def currency(value, group_sep=' ', decimal_sep='.'):
    """Format currency by digits.

    >>> currency(100)
    '100.00'
    >>> currency(3.1415)
    '3.14'
    >>> currency(31415)
    '31 415.00'
    >>> currency(3141500.1)
    '3 141 500.10'
    >>> currency(31415000.1)
    '31 415 000.10'
    """
    head,tail = ('%.2f'%value).split('.')
    l = len(head)
    return group_sep.join([head[r-3:l+r] for r in xrange(0,-l,-3)][::-1]) + decimal_sep + tail
```

[Gist](https://gist.github.com/histrio/ca0885dd8755ef479917172606c442e8#file-currency_formating-py) 

 {{< public-inbox \>}}