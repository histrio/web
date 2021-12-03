TMPFILE := `mktemp` 

sync:
    ssh gem.org.ru "sqlite3 -csv /var/www/gem.org.ru/writefreely.db 'select created,slug,title,content from posts'" > {{ TMPFILE }}
    ./writefreely.py {{ TMPFILE }}
    unlink {{ TMPFILE }}
