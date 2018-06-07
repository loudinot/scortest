cd tests
c:\python365_x64\python -m unittest test_myfirst.py
rem c:\python365_x64\Scripts\sphinx-build --help
cd ..
c:\python365_x64\Scripts\sphinx-build -M html doc build
c:\python365_x64\python setup.py bdist_wheel

