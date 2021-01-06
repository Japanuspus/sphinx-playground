===========
Test sphinx
===========

.. This file is in reStructuredText format, see e.g. http://docutils.sourceforge.net/docs/user/rst/quickstart.html

This is an example of using sphinx with internal and external plantUML for a multi-package project.

The project contains two packages: :doc:`my_package/index` and :doc:`my other package <my_other_package/modules/my_other_package>`.
The `my_package.my_module` has examples of advanced docstrings.

.. See toctree docs at http://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html

.. toctree::
  :maxdepth: 2
  :caption: Contents:

  my_package/index
  my_other_package/modules/my_other_package

