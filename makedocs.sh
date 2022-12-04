#!/usr/bin/env sh
rm -rf docs/
mkdir docs/
rm -rf build/docs/
mkdir build/docs/
sphinx-apidoc -f -o build/docs/source/Api-Docs/  src/
cp -r src/docs/source/ build/docs/source/
sphinx-build build/docs/source/ docs -E -d build/docs/.doctrees -c build/docs/source/ -b rst -vv
