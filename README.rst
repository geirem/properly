Properly
#########

.. image:: https://github.com/geirem/properly/actions/workflows/python-app.yml/badge.svg
   :target: https://github.com/geirem/properly/actions/workflows/python-app.yml
   :alt: Build Status

Best practices layout and configurations.

Documentation
-----
`docs <docs/Index.rst>`_

TODO
----
https://github.com/geirem/properly/issues



Sphinx
------

- ``src/properly/`` - The module itself.
- ``src/docs`` - Documentation configuration.
- ``docs/`` - Documentation.
- ``build/`` - Build files (Git-ignored).


::

    usage: sphinx-build [OPTIONS] SOURCEDIR OUTPUTDIR [FILENAMES...]

    Generate documentation from source files. sphinx-build generates documentation from the
    files in SOURCEDIR and places it in OUTPUTDIR. It looks for 'conf.py' in SOURCEDIR for
    the configuration settings. The 'sphinx-quickstart' tool may be used to generate
    template files, including 'conf.py' sphinx-build can create documentation in different
    formats. A format is selected by specifying the builder name on the command line; it
    defaults to HTML. Builders can also perform other tasks related to documentation
    processing. By default, everything that is outdated is built. Output only for selected
    files can be built by specifying individual filenames.

    positional arguments:
      sourcedir         path to documentation source files
      outputdir         path to output directory
      filenames         a list of specific files to rebuild. Ignored if -a is specified

    options:
      -h, --help        show this help message and exit
      --version         show program's version number and exit

    general options:
      -b BUILDER        builder to use (default: html)
      -a                write all files (default: only write new and changed files)
      -E                don't use a saved environment, always read all files
      -d PATH           path for the cached environment and doctree files (default:
                        OUTPUTDIR/.doctrees)
      -j N              build in parallel with N processes where possible (special value
                        "auto" will set N to cpu-count)

    build configuration options:
      -c PATH           path where configuration file (conf.py) is located (default: same as
                        SOURCEDIR)
      -C                use no config file at all, only -D options
      -D setting=value  override a setting in configuration file
      -A name=value     pass a value into HTML templates
      -t TAG            define tag: include "only" blocks with TAG
      -n                nit-picky mode, warn about all missing references

    console output options:
      -v                increase verbosity (can be repeated)
      -q                no output on stdout, just warnings on stderr
      -Q                no output at all, not even warnings
      --color           do emit colored output (default: auto-detect)
      -N, --no-color    do not emit colored output (default: auto-detect)
      -w FILE           write warnings (and errors) to given file
      -W                turn warnings into errors
      --keep-going      with -W, keep going when getting warnings
      -T                show full traceback on exception
      -P                run Pdb on exception

    For more information, visit <https://www.sphinx-doc.org/>.
