GDATA:=gdata-2.0.17
ARCHIVE:=$(GDATA).zip

all: run

$(ARCHIVE):
	curl http://gdata-python-client.googlecode.com/files/$@ > $@

$(GDATA): $(ARCHIVE)
	unzip $(ARCHIVE)

install: $(GDATA)
	cd $(GDATA) && sudo python setup.py install

clean:
	sudo rm -rf $(ARCHIVE) $(GDATA)

run:
	python weight_monitor.py
