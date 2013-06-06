#
# Makefile for the Embeded Serial Interface package.
#
# Development by Carl J. Nobile
#

include include.mk

PREFIX		= $(shell pwd)
PACKAGE_DIR	= $(shell echo $${PWD\#\#*/})
BOARDS_DIR	= ${PREFIX}/boards
RPI_DIR		= ${BOARDS_DIR}/rpi
BB_DIR		= ${BOARDS_DIR}/beagleboard
#DOCS_DIR	= ${PREFIX}/docs

#----------------------------------------------------------------------
all	: doc tar

#----------------------------------------------------------------------
doc	:
	@(cd $(DOCS_DIR); make)
#----------------------------------------------------------------------
tar	: clean
	@(cd ..; tar -czvf ${PACKAGE_DIR}-${VERSION}.tar.gz --exclude=".git" \
          ${PACKAGE_DIR})
#----------------------------------------------------------------------
python-api:
	@python setup.py build
#----------------------------------------------------------------------
egg	: python-api
	@python setup.py bdist_egg
#----------------------------------------------------------------------
tests	:
	#@echo "Testing the ${BOARDS_DIR}..."
	#@(. ${PREFIX}/setup_settings; python ${BOARDS_DIR}/tests.py)
	@echo "Testing the ${RPI_DIR}..."
	@(. ${PREFIX}/setup_settings; python ${RPI_DIR}/tests.py)
	@echo "Testing the ${BB_DIR}..."
	@(. ${PREFIX}/setup_settings; python ${BB_DIR}/tests.py)
#----------------------------------------------------------------------
clean	:
	@rm -f *~ \#* .\#* *.pyc
	@(cd ${BOARDS_DIR}; rm -f *~ \#* .\#* *.pyc)
	@(cd ${RPI_DIR}; rm -f *~ \#* .\#* *.pyc)
	@(cd ${BB_DIR}; rm -f *~ \#* .\#* *.pyc)
	#@(cd ${DOCS_DIR}; make clean)

clobber	: clean
	#@(cd $(DOCS_DIR); make clobber)
	@rm -rf build dist EmbedCore.egg-info
