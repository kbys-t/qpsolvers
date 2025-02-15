************
Installation
************

Linux
=====

The simplest way to install the package on a recent Debian-based system with
Python 3 is:

.. code:: bash

    sudo apt install python3-dev
    pip3 install qpsolvers

You can add the ``--user`` parameter for a user-only installation.

If you have an older system with Python 2, for instance Ubuntu 16.04, try:

.. code:: bash

    sudo apt install python-dev
    pip install -r requirements2.txt

Windows
=======

- First, install the `Visual C++ Build Tools <https://visualstudio.microsoft.com/visual-cpp-build-tools/>`_
- Install your Python environment, for instance `Anaconda <https://docs.anaconda.com/anaconda/install/windows/>`_
- Open a terminal configured for Python, for instance from the Anaconda Navigator, and run:

.. code:: bash

    pip install qpsolvers

Installing all open solvers
===========================

To install at once all open QP solvers available from `PyPI
<https://pypi.org/>`_, run ``pip`` from the requirements file:

.. code:: bash

    pip3 install --user -r requirements.txt

.. _gurobi-install:

Specific solvers
================

Gurobi
------

Gurobi comes with a `one-line pip installation
<https://www.gurobi.com/documentation/9.1/quickstart_linux/cs_using_pip_to_install_gr.html>`_
where you can fetch the solver directly from the company servers:

.. code:: bash

    python -m pip install -i https://pypi.gurobi.com gurobipy

This version comes with limitations. For instance, trying to solve a problem
with 500 optimization variables fails with the following warning:

.. code:: python

    Warning: Model too large for size-limited license; visit https://www.gurobi.com/free-trial for a full license

.. _qpoases-install:

qpOASES
-------

Check out the `official qpOASES installation page
<https://projects.coin-or.org/qpOASES/wiki/QpoasesInstallation>`_ for
instructions. You might run into errors at the ``make python`` step. If so, you
can check out qpOASES from `this fork
<https://github.com/stephane-caron/qpOASES>`_, or check out its 4–5 last
commits to see how to cope with these issues.
