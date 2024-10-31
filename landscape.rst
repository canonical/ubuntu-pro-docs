.. _landscape:

Understanding Landscape
=======================

`Landscape <Landscape_>`_ is Canonical’s system management tool for Ubuntu machines. It is available in two versions, Landscape SaaS and Self-hosted Landscape, both of which are included in Ubuntu Pro.

We also offer Managed Landscape for those who want the convenience of Landscape SaaS, but with integration into their IAM infrastructure with customised SSO, localised repository mirrors, and private repositories. `Click here <https://ubuntu.com/landscape/managed>`_ to learn more.

+------------------------------------------+----------------+-----------------------+-----------------------+
|            Feature comparison            | Landscape SaaS | Self-hosted Landscape |   Managed Landscape   |
+==========================================+================+=======================+=======================+
|           Managed by Canonical           |      Yes       |         No            |          Yes          |
+------------------------------------------+----------------+-----------------------+-----------------------+
|              Canonical SLA               |      No        |         No            |          Yes          |
+------------------------------------------+----------------+-----------------------+-----------------------+
|          Works without internet          |      No        |         Yes           |          No           |
+------------------------------------------+----------------+-----------------------+-----------------------+
|          Repository management           |      No        |         Yes           |          Yes          |
+------------------------------------------+----------------+-----------------------+-----------------------+
|        Bring your own SSO and IAM        |      No        |         Yes           |          Yes          |
+------------------------------------------+----------------+-----------------------+-----------------------+
|               Multi-tenant               |     Yes        |         No            |          No           |
+------------------------------------------+----------------+-----------------------+-----------------------+
|     Software and hardware inventory      |     Yes        |         Yes           |          Yes          |
+------------------------------------------+----------------+-----------------------+-----------------------+
| Security, compliance, hardening, reports |     Yes        |         Yes           |          Yes          |
+------------------------------------------+----------------+-----------------------+-----------------------+


Getting started with Landscape
------------------------------

Landscape SaaS
~~~~~~~~~~~~~~
Before you can access your Landscape SaaS account for the first time, you need to follow the steps under :doc:`Account set-up <account-setup>`.

.. _self-hosted-landscape:

Self-hosted Landscape
~~~~~~~~~~~~~~~~~~~~~

After `setting up your self-hosted Landscape server <https://ubuntu.com/landscape/install>`_, you need to choose a licensing mechanism. There are two options for self-hosted Landscape: the new, Pro client method and the old, license.txt file method.

**Pro client method**

For customers running Landscape version 23.03 or newer, and landscape-client version 23.02 or newer on Ubuntu 24.04 LTS instances, please use the Pro client method to license your Landscape server.

1. Ensure the Pro client is :ref:`installed and attached to your Pro token <attach>` on the system you wish to register to Landscape.
2. Then :ref:`enable Landscape <manage-landscape>` to initiate the registration process.
3. Landscape will detect your Pro entitlement via the Pro token and create a licence for your machine.

**License.txt file method**

For customers on an older version of Landscape or landscape-client than those specified above, please download your ``license.txt`` file from your Landscape SaaS account. You will need to re-download and apply new ``license.txt`` files every time you purchase new Ubuntu Pro licences and after every renewal.

.. tip::

   New ``license.txt`` files become available on their start date. For renewal customers, this is the day after your old licences expire.

* `Landscape documentation <https://ubuntu.com/landscape/docs>`_: our main set of documentation on Landscape SaaS and self-hosted Landscape
* `Knowledge Base - Landscape section <https://support-portal.canonical.com/knowledge-base?topic=Landscape&search=>`_: content published by Canonical Support, typically addressing FAQs and providing workarounds for bugs
* `GitHub - script repository for Landscape <https://github.com/canonical/landscape-scripts>`_: a collection of scripts to make Landscape more powerful

