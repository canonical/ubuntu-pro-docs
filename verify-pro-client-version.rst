.. _verify-pro-client-version:

Verify that your Pro client is up-to-date
=========================================

Ubuntu Pro is a service that can be controlled using an Ubuntu Pro client -- a CLI tool that is preinstalled on Ubuntu distribitions.

Before you can attach your subscription, you must check if the client is up to date.

Prerequisites
-------------

* An Ubuntu machine running an Ubuntu LTS release.

* sudo access on your Ubuntu user account

1. Make sure that your systme is up to date:

    $ sudo apt update && sudo apt upgrade

2. Check the verison of your Pro client:

.. code-block:: bash

    $ pro --version
    35.1ubuntu0~25.04

The lateest versions of Pro is ``35``. If you do no have the latest version, update it by running:

.. code-block:: bash
    
    $ sudo apt install ubuntu-advantage-tools
    $ sudo apt update

