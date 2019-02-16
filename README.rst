Gihub Pages hosted documentation
--------------------------------
Publishing
==========
This documentation is built using Sphinx and a Sphinx based tool sphinxcontrib-versioning. This additional tool makes it easier to host documentation for every release we would like to host documentation for in the same place.

Install these tools via pip. An older version of Sphinx is needed to work with sphinxcontrib-versioning. ::

    pip install sphinx-rtd-theme sphinx==1.5.6 sphinxcontrib-versioning

This documentation is not hard-set. Be sure to know what these tools do with ::

    sphinx-versioning build --help
    sphinx-versioning push --help

Then, from the branch which contains /docs, this will likely be master ::

    sphinx-versioning build docs/source docs/build/html
    sphinx-versioning push docs/source gh-pages .

