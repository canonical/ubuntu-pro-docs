Ubuntu Pro: services overview
==============================

Overview
---------


+-------------------------------------------------------------------------------------------------------------------+-------------------------+-------------+
|                                                      Service                                                      | Ubuntu Pro (infra-only) | Ubuntu Pro  |
+===================================================================================================================+=========================+=============+
|                       Security patching for Ubuntu Main repository for 10 years (ESM-infra)                       |           Yes           |     Yes     |
+-------------------------------------------------------------------------------------------------------------------+-------------------------+-------------+
|       Security patching for Ubuntu Universe repository for 10 years (ESM-apps) (Ubuntu 16.04 LTS onwards)         |           No            |     Yes     |
+-------------------------------------------------------------------------------------------------------------------+-------------------------+-------------+
|                                  Kernel Livepatch to avoid unscheduled reboots                                    |           Yes           |     Yes     |
+-------------------------------------------------------------------------------------------------------------------+-------------------------+-------------+
|                                    Real-time kernel (Ubuntu 22.04 LTS onwards)                                    |           Yes           |     Yes     |
+-------------------------------------------------------------------------------------------------------------------+-------------------------+-------------+
|                         NIST-certified FIPS crypto-modules (pending for Ubuntu 22.04 LTS)                         |           Yes           |     Yes     |
+-------------------------------------------------------------------------------------------------------------------+-------------------------+-------------+
| USG hardening with CIS and DISA-STIG profiles (DISA-STIG tooling & automation for Ubuntu 20.04 LTS and 22.04 LTS) |           Yes           |     Yes     |
+-------------------------------------------------------------------------------------------------------------------+-------------------------+-------------+
|                              Systems Management with Landscape (SaaS or self-hosted)                              |           Yes           |     Yes     |
+-------------------------------------------------------------------------------------------------------------------+-------------------------+-------------+


Security feature focus
---------------------------

Expanded Security Maintenance Infra + Apps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are two `Expanded Security Maintenance <https://ubuntu.com/security/esm>`_  streams offered by Canonical:

**ESM infra**: this stream expands the scope of security maintenance for Ubuntu LTS releases for packages in the Ubuntu Main repository from 5 years to 10 years;

**ESM apps**: this stream expands the scope of security maintenance to include packages in the Ubuntu Universe repository for the full 10 years of an Ubuntu LTS release’s lifecycle. That’s around 25,000 additional packages per Ubuntu LTS release.

These commands show the source of packages on your Ubuntu system, how many packages are from the Ubuntu Universe or Ubuntu Main repositories, as well as how many security patches are already available for those packages under the ESM services.

.. code-block:: bash

  $ pro security-status

  $ pro security-status --esm-apps

  $ pro security-status --esm-infra


The expected security maintenance dates for Ubuntu LTS releases since 14.04 LTS, including ESM periods:

+------------------------+-------------------------------+--------------------------+
|      **Release**       |        **Patched Until**      |     **Repositories**     |
+------------------------+-------------------------------+--------------------------+
|       14.04 LTS        |           April 2024          |           Main           |
+------------------------+-------------------------------+--------------------------+
|       16.04 LTS        |           April 2026          |      Main & Universe     |
+------------------------+-------------------------------+--------------------------+
|       18.04 LTS        |            May 2028           |      Main & Universe     |
+------------------------+-------------------------------+--------------------------+
|       20.04 LTS        |           April 2030          |      Main & Universe     |
+------------------------+-------------------------------+--------------------------+
|       22.04 LTS        |           April 2032          |      Main & Universe     |
+------------------------+-------------------------------+--------------------------+



Livepatch
~~~~~~~~~

The `Ubuntu Livepatch service <https://ubuntu.com/security/livepatch/docs>`_ is designed to help you remain secure while avoiding unscheduled reboots. It does this by providing patches for High and Critical CVEs in the Ubuntu Kernel, which are applied while the system is running.

Ubuntu Livepatch addresses vulnerabilities in the running Linux kernel, in memory. Livepatch does not write these patches to disk, which means the package has to be updated separately for the security patch to survive a reboot. The expectation is that you will use the normal update tools to install all available updates to the Linux kernel, including lower severity vulnerabilities or vulnerabilities that cannot be live patched. This means that when you do eventually reboot into that newer kernel, there are no vulnerabilities that need live patching. To check whether a Livepatch has been applied to a specific CVE, run:

.. code-block:: bash

   $ canonical-livepatch status --verbose


Livepatch documentation: `https://ubuntu.com/security/livepatch/docs <https://ubuntu.com/security/livepatch/docs>`_


Compliance features
---------------------

Your Ubuntu Pro subscription includes several services and tools that address compliance and regulatory requirements: FIPS, the Ubuntu Security Guide, and the CIS hardening tool.


FIPS
~~~~~~~

Canonical has FIPS 140-2 modules for Ubuntu 16.04 LTS, 18.04 LTS and 20.04 LTS. We are currently in the process of obtaining FIPS 140-3 modules for 22.04 LTS. We will announce on our `blog <https://ubuntu.com/blog>`_ and in the `Ubuntu Pro newsletter <https://portal.support.canonical.com/selfservice/s/article/Subscribe-to-or-Unsubscribe-from-the-Ubuntu-Advantage-Newsletter>`_ when the validation process for 22.04 LTS is complete - make sure to subscribe if you want to be kept updated.

To enable FIPS and install the validated packages run:

``pro enable fips-updates`` to enable the validated packages, but also receive regular security updates. This is the FIPS stream that we recommend to most customers.

``pro enable fips`` to install the FIPS validated packages. These will not be updated until the next re-certification. Only rarely should a customer choose this option because you cannot receive security updates on this stream.

`FIPS documentation <https://ubuntu.com/security/certifications/docs/fips>`_ 


USG for hardening Ubuntu 20.04 LTS and 22.04 LTS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The `Ubuntu Security Guide (USG) <https://ubuntu.com/security/certifications/docs/usg>`_ provides tooling for the auditing and hardening of Ubuntu systems to meet **CIS** (for Ubuntu 20.04 LTS and 22.04 LTS) and **DISA STIG benchmarks** (for Ubuntu 20.04 LTS). The USG also allows for environment-specific customisation.

This tooling is designed to help you to harden Ubuntu systems quickly and correctly, versus manual hardening which is slow and error-prone. We recommend using the tool to create a golden image, hardened to meet your requirements, which you can then disseminate across your organisation. The tool can also audit your compliance after hardening.


CIS hardening tool for Ubuntu 16.04 LTS and 18.04 LTS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you need to harden Ubuntu systems running either 16.04 LTS or 18.04 LTS, you will need to use an older version of our tooling, the `CIS hardening tool <https://ubuntu.com/security/certifications/docs/16-18/cis>`_. The tool also has an audit function, enabling you to monitor the ongoing compliance of Ubuntu instances after hardening is complete.


