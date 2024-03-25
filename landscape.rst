.. _landscape:

Landscape
===========

`Landscape <Landscape_>`_ is Canonical’s system management tool for Ubuntu machines.

There are 3 versions of Landscape:

+------------------------------------------+----------------+-------------------+-----------------------+
|            Feature comparison            | Landscape SaaS | Managed Landscape | Self-hosted Landscape |
+==========================================+================+===================+=======================+
|           Managed by Canonical           |     Yes        |       Yes         |          No           |
+------------------------------------------+----------------+-------------------+-----------------------+
|              Canonical SLA               |      No        |       Yes         |          No           |
+------------------------------------------+----------------+-------------------+-----------------------+
|          Works without internet          |      No        |        No         |         Yes           |
+------------------------------------------+----------------+-------------------+-----------------------+
|          Repository management           |      No        |       Yes         |         Yes           |
+------------------------------------------+----------------+-------------------+-----------------------+
|        Bring your own SSO and IAM        |      No        |       Yes         |          Yes          |
+------------------------------------------+----------------+-------------------+-----------------------+
|               Multi-tenant               |     Yes        |        No         |          No           |
+------------------------------------------+----------------+-------------------+-----------------------+
|     Software and hardware inventory      |     Yes        |       Yes         |         Yes           |
+------------------------------------------+----------------+-------------------+-----------------------+
| Security, compliance, hardening, reports |      Yes       |       Yes         |         Yes           |
+------------------------------------------+----------------+-------------------+-----------------------+


Getting started with Landscape
------------------------------

Before you can access your Landscape SaaS account for the first time, you need to follow the steps under :doc:`Account set-up <account-setup>`.

For customers using self-hosted Landscape, your ``licence.txt`` file is available in your Landscape SaaS account. You will need to re-download and apply new ``licence.txt`` files every time you purchase new Ubuntu Pro licences and after every renewal.

.. tip::

   New ``licence.txt`` files become available on their start date. For renewal customers, this is the day after your old licences expire.

* `Landscape documentation <https://ubuntu.com/landscape/docs>`_: our main set of documentation on Landscape SaaS and self-hosted Landscape
* `Knowledge Base - Landscape section <https://support-portal.canonical.com/knowledge-base?topic=Landscape&search=>`_: content published by Canonical Support, typically addressing FAQs and providing workarounds for bugs
* `GitHub - script repository for Landscape <https://github.com/canonical/landscape-scripts>`_: a collection of scripts to make Landscape more powerful

