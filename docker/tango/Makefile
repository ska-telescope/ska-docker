DIRS = tango-builder tango-dependencies tango-db tango-cpp tango-java tango-rest tango-dsconfig ska-python-buildenv tango-pogo tango-starter tango-libtango tango-jive ska-python-runtime tango-admin tango-databaseds tango-test tango-itango tango-vscode tango-vnc tango-pytango mariadb_hdbpp tango-archiver hdbpp_viewer
TEST = ska-python-buildenv tango-itango tango-rest tango-db tango-cpp tango-archiver
BUILDDIRS = $(DIRS:%=build-%)
TESTDIRS = $(TEST:%=test-%)
CHECKSTATUSDIRS = $(DIRS:%=checkstatus-%)
SHOWVERDIRS = $(DIRS:%=showver-%)
PUSHDIRS = $(DIRS:%=push-%)

.DEFAULT_GOAL := help

build: $(DIRS)  ## build all images
$(DIRS): $(BUILDDIRS)
$(BUILDDIRS):
	$(MAKE) -C $(@:build-%=%) build

test: $(TESTDIRS)
$(TESTDIRS):
	$(MAKE) -C $(@:test-%=%) test

check-status: $(CHECKSTATUSDIRS) ## check whether subdirectories have uncommitted changes
$(CHECKSTATUSDIRS):
	$(MAKE) -C $(@:checkstatus-%=%) check-status

showver: $(SHOWVERDIRS)  ## show image versions
$(SHOWVERDIRS):
	$(MAKE) -C $(@:showver-%=%) showver

push: $(PUSHDIRS)  ## push images to Docker hub
$(PUSHDIRS):
	$(MAKE) -C $(@:push-%=%) push

help:  ## show this help.
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: subdirs $(DIRS)
.PHONY: subdirs $(BUILDDIRS)
.PHONY: subdirs $(CHECKSTATUSDIRS)
.PHONY: subdirs $(PUSHDIRS)
.PHONY: subdirs $(SHOWVERDIRS)
.PHONY: build check-status showver push help

