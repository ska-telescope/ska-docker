DIRS = tango-dependencies tango-db tango-cpp tango-java tango-starter tango-pogo tango-rest ska-python-buildenv ska-python-runtime tango-itango mariadb_hdbpp tango-archiver tango-vscode tango-vnc hdbpp_viewer
BUILDDIRS = $(DIRS:%=build-%)
CHECKSTATUSDIRS = $(DIRS:%=checkstatus-%)
SHOWVERDIRS = $(DIRS:%=showver-%)
PUSHDIRS = $(DIRS:%=push-%)

.DEFAULT_GOAL := help

build: $(DIRS)  ## build all images
$(DIRS): $(BUILDDIRS)
$(BUILDDIRS):
	$(MAKE) -C $(@:build-%=%) build

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

