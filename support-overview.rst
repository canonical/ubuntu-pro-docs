Canonical Support: overview and process
===================================================

Ubuntu Pro includes self-service support, that can be upgraded to comprehensive support contract.


Support contract options
------------------------

Your account will include different levels of support according to the options in your organisation's contract:

**Response options**

* *24/5*: Monday to Friday (in your timezone)
* *24/7*: any time of day, every day

**Coverage options**

* *Infra-only*: Ubuntu main repository (~2,300 packages)
* *Full Pro*: Ubuntu main and universe repositories (~25,000 packages)

**Storage**: up to 192TB of Ceph or Swift raw storage per covered machine

**Products covered**: Kubernetes, OpenStack, Ceph, MAAS, LXD



Severity levels and response times
----------------------------------

For support contracts only; self-service support does not qualify.

+-------------------------------------------------------+-------------------------------------+----------+
|                    Severity Level                     |               Weekday               |   24.7   |
+=======================================================+=====================================+==========+
| 1 - Core functionality critical impact / service down | 4 hours excl. weekends and holidays |  1 hour  |
+-------------------------------------------------------+-------------------------------------+----------+
|       2 - Core functionality severely degraded        |          8 business hours           | 2 hours  |
+-------------------------------------------------------+-------------------------------------+----------+
|             3 - Standard support request              |          12 business hours          | 6 hours  |
+-------------------------------------------------------+-------------------------------------+----------+
|                4 - Non-urgent request                 |          24 business hours          | 12 hours |
+-------------------------------------------------------+-------------------------------------+----------+

Business hours are defined as 08:00 to 18:00 Monday to Friday, local to the customer HQ, unless another location has been agreed.

For further information about what is covered under your support contract, refer to the `Ubuntu Pro Service Description <https://ubuntu.com/legal/ubuntu-pro-description#ubuntu-pro-description>`_.


Support case lifecycle
----------------------

.. mermaid::
    :zoom:
    
    flowchart TD
        A(Customer experiences an issue on a covered machine & troubleshoots)-->B(Customer searches Knowledge Base for resolution)
        B --> C(Case opened by customer via phone or Support Portal)
        B --> D{Problem solved?}
        C --> F(Support Case is triaged and actioned with severity level set appropriately)
        F --> G(Case is assigned to TSE,TAM or DSE)
        G --> H{Problem solved?}
            H --> |Yes| I(Case set to 'Closed - resolved' after customer agreement)
            H --> |No| K(Case escalated to Sustaining Engineering Group)
        I --> J[Customer  satisfaction survey is sent]
        K --> L{Problem solved?}
            L --> |Yes| I
            L --> |No| K
 

Sosreports
-------------

Canonical uses sosreports, or "state of system" reports, to diagnose and resolve problems. These comprise system logs and configuration data.
When you report a problem with your Ubuntu machine, you can generate and send a sosreport from the affected machine straight away.

Refer to the following articles for information on using sosreports:

* `Installing the sosreport tool and generating a sosreport <https://support-portal.canonical.com/knowledge-base/canonical-support-data-collection-sosreport>`_
* `Sending a sosreport to Canonical <https://support-portal.canonical.com/knowledge-base/sending-files-sts>`_
* `Sosreports, data and security <https://support-portal.canonical.com/knowledge-base/sosreport-data-security>`_
