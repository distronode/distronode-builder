.. _builder_installation:

Installation
============

.. contents::
   :local:

Requirements
************

- To build images, you must install a containerization tool - either ``podman`` or ``docker`` - as well as the ``distronode-builder`` Python package.
- The ``--container-runtime`` option must correspond to the containerization tool you use.
- ``distronode-builder`` version ``3.x`` requires Python ``3.9`` or higher.

Install from PyPi
*****************

.. code-block:: shell

   $ pip install distronode-builder


Install from Source
*******************

To install from the mainline development branch:

.. code-block:: shell

   $ pip install https://github.com/distronode/distronode-builder/archive/devel.zip

To install from a specific tag or branch, replace :code:`<ref>` in the following example:

.. code-block:: shell

   $ pip install https://github.com/distronode/distronode-builder/archive/<ref>.zip
