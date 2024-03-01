Landscape
===========

Landscape is Canonical’s system management tool for Ubuntu machines.

There are 3 versions of Landscape:

+------------------------------------------+----------------+-------------------+-----------------------+
| Feature Comparison                       |Landscape SaaS  | Managed Landscape | Self-hosted Landscape |
+==========================================+================+===================+=======================+
| Managed by Canonical                     | Y              | Y                 | N                     |
| Canonical SLA                            | N              | Y                 | N                     |
| Works without Internet                   | N              | N                 | Y                     |
| Repository Management                    | N              | Y                 | Y                     |
| Bring your own SSO and IAM               | N              | Y                 | Y                     |
| Multi-tenant (users in multiple orgs.)   | Y              | N                 | N                     |
| Software & Hardware Inventory            | Y              | Y                 | Y                     |
| Security, Hardening, Compliance, Reports | Y              | Y                 | Y                     |
+------------------------------------------+----------------+-------------------+-----------------------+


Getting started with Landscape
-------------------------------

Before you can access your Landscape SaaS account for the first time, you need to follow the steps under :doc:`<account-setup>`.

For customers using self-hosted Landscape, your ``licence.txt`` file is available in your Landscape SaaS account. You will need to re-download and apply new ``licence.txt`` files every time you purchase new Ubuntu Pro licences and after every renewal.

.. tip::
    New ``licence.txt`` files become available on their start date. For renewal customers, this is the day after your old licences expire.

* `Landscape documentation <https://ubuntu.com/landscape/docs>`_: our main set of documentation on Landscape SaaS and self-hosted Landscape
* `Knowledge Base - Landscape section <https://portal.support.canonical.com/ua/s/topic/0TOD00000006dHKOAY/landscape>`_: content published by Canonical Support, typically addressing FAQs and providing workarounds for bugs
* `GitHub - script repository for Landscape <https://github.com/canonical/landscape-scripts>`_: a collection of scripts to make Landscape more powerful

