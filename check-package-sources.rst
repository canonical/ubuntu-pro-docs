.. _check-package-sources:

Identify the source repository of your installed packages
=========================================================

Now let’s find out how many packages are installed on your machine and from which source:

.. code-block:: bash

    $ pro security-status
    1919 packages installed:
        1870 packages from Ubuntu Main/Restricted repository
        10 packages from Ubuntu Universe/Multiverse repository
        10 package from a third party
        29 packages no longer available for download

    To get more information about the packages, run
        pro security-status --help
    for a list of available options.

    This machine is receiving security patching for Ubuntu Main/Restricted
    repository until 2025.
    This machine is NOT attached to an Ubuntu Pro subscription.

    Ubuntu Pro with 'esm-infra' enabled provides security updates for
    Main/Restricted packages until 2030.

    Ubuntu Pro with 'esm-apps' enabled provides security updates for
    Universe/Multiverse packages until 2030 and has 1 pending security update.

    Try Ubuntu Pro with a free personal subscription on up to 5 machines.

From the output, you can see that there are 1919 deb packages installed on your machine:

* 1870 packages are from Ubuntu Main/ Restricted repository which means that they receive Ubuntu LTS updates until 2025. This is covered without any subscription but can be expanded with Ubuntu Pro for an additional 5 years, until 2030.
* 10 packages are from Ubuntu Universe/ Multiverse repository and they come with no security assurance from Ubuntu LTS, but they are covered by Ubuntu Pro.
* And there is 1 security update for the Universe repository available with an Ubuntu Pro subscription.

.. note::
    If you are not using any packages from the Ubuntu Universe repository, that line will not be displayed.

Now let's check the packages covered with the security suppoport and see which of them have CVE fixes available:

.. code-block:: bash

    $ pro security-status --esm-apps
    1919 packages installed:
        10 packages from Ubuntu Universe/Multiverse repository

    Ubuntu Pro with 'esm-apps' enabled provides security updates for
    Universe/Multiverse packages until 2030 and has 1 pending security update.

    Run 'pro help esm-apps' to learn more

    Package names in bold currently have an available update
    with 'esm-apps' enabled
    Packages:
    ansible python3-argcomplete python3-kerberos python3-libcloud
    python3-ntlm-auth python3-requests-kerberos python3-requests-ntlm
    python3-selinux python3-winrm python3-xmltodict

    For example, run:
        apt-cache policy ansible
    to learn more about that package.

To be able to recieve these updates, you will need to attach an Ubunti Pro subscription to your machine next. 