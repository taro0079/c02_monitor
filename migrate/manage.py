#!/usr/bin/env python
from migrate.versioning.shell import main

DATABASE = 'mysql://%s:%s@%s/%s?charset=utf8' % (
    "root",
    "takano0820",
    "localhost",
    "db",
)
if __name__ == '__main__':
    main(debug='False',url=DATABASE, repository='.')
