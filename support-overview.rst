.. _support-overview:

Canonical Support: overview and process
========================================

Ubuntu Pro includes self-service support, that can be upgraded to comprehensive support contract.

.. _knowledge-base: 

Knowledge Base
----------------

As an paying Ubuntu Pro Customer, you get access to our Knowledge Base that is found in the `Canonical Support Portal <https://support-portal.canonical.com/>`_ (if you need help setting up your account, go to the :ref:`initial account setup page <account-setup>`). It contains articles on troubleshooting open source software written by our experts. 

When you run into an issue or have a question regarding one of the Canonical products, we recommend searching the Knowledge Base first to see if there is already an article addressing your question or concern. You can use the search bar to find the desired topic and filter results by date published, relevance and product type. For each article you will see when it was published, the number of views and which topics are addressed.
Each article will provide you with a quick summary at the top, a problem description followed by the solution, known issues (if any) and links to related documents.

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

For further information about what is covered under your support contract, refer to the `Ubuntu Pro Service Description <https://ubuntu.com/legal/ubuntu-pro-description>`_.


Support case lifecycle
----------------------

.. mermaid::
    :zoom:
    
    flowchart TD
        Start(Customer experiences an issue on a covered machine & troubleshoots)-->Search(Customer searches Knowledge Base for resolution)
        Search -->  D{Solution found?}
            D --> |No| Case
            D --> |Yes| End
        Case(Case opened by customer via phone or Support Portal)
        Case --> F(Support Case is triaged and actioned with severity level set appropriately)
        F --> G(Case is assigned to TSE,TAM or DSE)
        G --> H{Problem solved?}
            H --> |Yes| I(Case set to 'Closed - resolved' after customer agreement)
            H --> |No| K(Case escalated to Sustaining Engineering Group)
        I --> J[Customer  satisfaction survey is sent] --> End
        K --> L{Problem solved?}
            L --> |Yes| I
            L --> |No| K
        End(End)
 
