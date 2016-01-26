.PONY: clean install

clean:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	rm -rf env

install:
	virtualenv env
	cp /usr/lib/python2.7/dist-packages/cv* env/lib/python2.7/site-packages/
	cp -R /usr/lib/python2.7/dist-packages/numpy env/lib/python2.7/site-packages/
	env/bin/pip install -e .
