# advanced-testing-techniques
Repo to learn advanced testing

# Setup Project

 1. Create and source virtual environment

```bash 
virtualenv ~/.advanced-testing
source ~/.advanced-testing/bin/activate
```
 2. Create scaffold 
 ```bash 
 touch Makefile
 touch hello.py
 touch test_hello.py
 touch requirements.txt
 ```

 3. Populate `Makefile`
 ```bash
 install:
		pip install --upgrade pip &&\
				pip install -r requirements.txt
test:
		python -m pytest -vv --cov=hello --cov=hellocli test_hello.py
lint: 
		pylint --disable=R, C hello.py hellocli.py
all: install lint test-
 ```

 ### How to debug 

 *Print
 *pdb
 *testing
 