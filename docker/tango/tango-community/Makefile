DIRS = tango-libtango tango-pytango tango-admin tango-databaseds tango-test tango-rest tango-db tango-jive
BUILDDIRS = $(DIRS:%=build-%)
PUSHDIRS = $(DIRS:%=push-%)

build: $(DIRS)  ## build all images
$(DIRS): $(BUILDDIRS)
$(BUILDDIRS):
	$(MAKE) -f ../makefile.mk -C $(@:build-%=%) build

push: $(PUSHDIRS)  ## push images to Docker hub
$(PUSHDIRS):
	$(MAKE) -f ../makefile.mk -C $(@:push-%=%) push

