.. _landscape:

Landscape
==========

`Landscape <Landscape_>`_ is Canonical’s system management tool for Ubuntu machines and is included in every tier of Ubuntu Pro.

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

Landscape SaaS
~~~~~~~~~~~~~~
Before you can access your Landscape SaaS account for the first time, you need to follow the steps under :doc:`Account set-up <account-setup>`.

Self-hosted Landscape
~~~~~~~~~~~~~~~~~~~~~

We currently have two licensing mechanisms for self hosted Landscape: the new, Pro client method and the old, licence.txt file method.

**Pro client method**

For customers running Landscape version 23.03 or newer and landscape-client version 23.02 or newer, please use the Pro client method to license your Landscape server.

1. Ensure the Pro client is :ref:`installed and attached to your Pro token <get_token_and_attach>` on the system you wish to register to Landscape.
2. Then :ref:`enable Landscape <manage-landscape>` to initiate the registration process.
3. Landscape will detect your Pro entitlement via the Pro token and create a licence for your machine.

**Licence.txt file method**

For customers on an older version of Landscape or landscape-client than the versions specificed above, please download your ``licence.txt`` file from your Landscape SaaS account. You will need to re-download and apply new ``licence.txt`` files every time you purchase new Ubuntu Pro licences and after every renewal.

.. tip::

   New ``licence.txt`` files become available on their start date. For renewal customers, this is the day after your old licences expire.

* `Landscape documentation <https://ubuntu.com/landscape/docs>`_: our main set of documentation on Landscape SaaS and self-hosted Landscape
* `Knowledge Base - Landscape section <https://support-portal.canonical.com/knowledge-base?topic=Landscape&search=>`_: content published by Canonical Support, typically addressing FAQs and providing workarounds for bugs
* `GitHub - script repository for Landscape <https://github.com/canonical/landscape-scripts>`_: a collection of scripts to make Landscape more powerful
