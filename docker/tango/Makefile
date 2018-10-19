TRGTS = tango-dependencies tango-db tango-cpp tango-java tango-python tango-starter tango-pogo

.PHONY: all build tango-dependencies tango-db tango-cpp tango-java tango-python tango-starter tango-starter tango-pogo

all: build

build: $(TRGTS)

$(TRGTS):
	$(MAKE) --directory=$@ $(TARGET)
	$(if $(TARGET), $(MAKE) $(TARGET))


tango-dependencies:
	$(MAKE) -C tango-dependencies

tango-db:
	$(MAKE) -C tango-db

tango-cpp: tango-dependencies
	$(MAKE) -C tango-cpp

tango-java: tango-dependencies
	$(MAKE) -C tango-java

tango-python: tango-dependencies
	$(MAKE) -C tango-python

tango-starter: tango-cpp
	$(MAKE) -C tango-starter

tango-pogo: tango-java
	$(MAKE) -C tango-pogo

