#!/usr/bin/env python3

if __name__ == "__main__":
    import sys
    import os
    _, fname = sys.argv
    root = os.path.dirname(os.path.abspath(__file__))
    with open(fname, 'r') as f:
        import csv
        for updated, slug, title, content in csv.reader(f):
            cname = os.path.join(root, 'content', 'blog', slug+'.md')
            with open(cname, 'w') as cf:
                cf.write(f'---\ntitle: "{title}"\ndate: {updated}\n---\n {content} \n\n {{{{< public-inbox \>}}}}')
    
