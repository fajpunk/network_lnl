env:
	virtualenv --no-site-packages env

deps: env
	env/bin/pip install -r requirements/base.txt
