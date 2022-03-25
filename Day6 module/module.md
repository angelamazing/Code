mycompany
├─ __init__.py
├─ abc.py
└─ xyz.py

1. abc.py: mycompany.abc
2. 每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包

mycompany
 ├─ web
 │  ├─ __init__.py
 │  ├─ utils.py
 │  └─ www.py
 ├─ __init__.py
 ├─ abc.py
 └─ utils.py

1. www.py: mycompany.web.www    