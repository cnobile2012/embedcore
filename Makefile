#
# Makefile for the Embeded Serial Interface package.
#
# Development by Carl J. Nobile
#

include include.mk

PREFIX		= $(shell pwd)
BASE_DIR	= $(shell echo $${PWD\#\#*/})
PACKAGE_DIR	= ${PREFIX}/embedcore
BOARDS_DIR	= ${PACKAGE_DIR}/boards
RPI_DIR		= ${BOARDS_DIR}/rpi
BB_DIR		= ${BOARDS_DIR}/beagleboard
INTERFACES_DIR	= ${PACKAGE_DIR}/interfaces
I2C_DIR		= ${INTERFACES_DIR}/i2c
#DOCS_DIR	= ${PREFIX}/docs

#----------------------------------------------------------------------
all	: doc tar

#----------------------------------------------------------------------
doc	:
	@(cd $(DOCS_DIR); make)
#----------------------------------------------------------------------
tar	: clean
	@(cd ..; tar -czvf ${BASE_DIR}-${VERSION}.tar.gz --exclude=".git" \
          ${BASE_DIR})
#----------------------------------------------------------------------
python-api:
	@python setup.py build
#----------------------------------------------------------------------
egg	: python-api
	@python setup.py bdist_egg
#----------------------------------------------------------------------
tests	:
	@echo "Testing the ${BOARDS_DIR}..."
	@(. ${PREFIX}/setup_settings; python ${BOARDS_DIR}/tests.py)
	@echo "Testing the ${RPI_DIR}..."
	@(. ${PREFIX}/setup_settings; python ${RPI_DIR}/tests.py)
	@echo "Testing the ${BB_DIR}..."
	@(. ${PREFIX}/setup_settings; python ${BB_DIR}/tests.py)
#----------------------------------------------------------------------
clean	:
	@rm -f *~ \#* .\#* *.pyc
	@(cd ${PACKAGE_DIR}; rm -f *~ \#* .\#* *.pyc)
	@(cd ${BOARDS_DIR}; rm -f *~ \#* .\#* *.pyc)
	@(cd ${RPI_DIR}; rm -f *~ \#* .\#* *.pyc)
	@(cd ${BB_DIR}; rm -f *~ \#* .\#* *.pyc)
	@(cd ${I2C_DIR}; rm -f *~ \#* .\#* *.pyc)
	#@(cd ${DOCS_DIR}; make clean)

clobber	: clean
	#@(cd $(DOCS_DIR); make clobber)
	@rm -rf build dist EmbedCore.egg-info
