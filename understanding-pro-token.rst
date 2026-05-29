.. _understanding-pro-token:

Understanding the Ubuntu Pro token
==================================

The Ubuntu Pro token is needed to access most of the services included in Ubuntu Pro. This page explains how the Ubuntu Pro token works, including the relationship between your token and your Ubuntu Pro subscriptions and how active machine count is calculated.

How does the Ubuntu Pro token work?
-----------------------------------

When you attach an Ubuntu Pro token to an Ubuntu machine, you authenticate that machine to access the packages and services available under Ubuntu Pro. The following services are accessible only via the Ubuntu Pro token:

* ESM Infra and Apps
* Livepatch
* Ubuntu Security Guide
* FIPS
* Active Directory for Ubuntu desktop
* Online machines registered to Landscape using the Pro client, i.e. by running <pro enable landscape>

How does my token relate to my Ubuntu Pro subscription?
-------------------------------------------------------

Customers and users have one Ubuntu Pro token per subscription to a specific tier of Ubuntu Pro. This means that for customers who have multiple subscriptions to a single tier of Ubuntu Pro, for example if you add additional seats during your contract, each of those subscriptions will share a single token.

For customers who have subscriptions to different tiers of Ubuntu Pro, you will have 2 or more tokens to manage, for example if you have phone and ticket support for your production environment but not for your non-production environment. It is important to use the right token for each environment; please check with your license management team if you are not sure which subscription relates to which environment.

Your tokens will remain the same as long as you remain subscribed to the same tiers of Ubuntu Pro, including if you renew your subscription late and if you renew via a different channel.

If you change your tier of Ubuntu Pro, your token will change too and :ref:`you will need to update it <update-token>`.

After a subscription update, e.g. after renewal or after adding additional seats, you may need to run <pro refresh> to get the Ubuntu Pro client to pick up your new contract.

.. _active-machine-count:

Active machine count
--------------------

The Ubuntu Pro dashboard displays an “active machine” count for each subscription to Ubuntu Pro. This is the number of online machines attached to your Pro token that have pinged Canonical servers within the last 24 hours.

If you have multiple subscriptions to the same tier of Ubuntu Pro, these subscriptions will share a single token and a combined active machine count.

Consumption of the following services is registered under active machines:

* ESM-Infra and ESM-Apps
* Livepatch
* USG
* CIS
* FIPS
* Online machines registered to Landscape using the Pro client, i.e. by running <pro enable landscape>

Machines registered to Landscape using license.txt files are not included.

Occasionally after attaching new machines to your token, you may observe that the active machine count is doubled, e.g. you have attached 10 machines but the active machine count shows 20. Over time the count will stabilise to the correct number of machines, usually within 48 hours.


.. tip::

   If you detach a machine from your Ubuntu Pro token, the reduction in active machine count will take place 24 hours later.

Customers with unlimited guest support
--------------------------------------

If you have licensed an entire virtual cluster to Ubuntu Pro at the physical host level, you are eligible for unlimited guest support. The Ubuntu Pro dashboard will display your license type as physical, however you should use the Pro token associated with that subscription on your virtual machines.

For example, suppose you have 5 physical non-Ubuntu hosts in a cluster, all of which are licensed and covered by Ubuntu Pro. To deploy guests on this cluster, attach the token associated with your subscription to the guests. You do not need to attach the physical non-Ubuntu hosts to Ubuntu Pro.

As you attach machines, you will see your active machine count go above your license count. This is expected behaviour and will not impact your access to the Pro services.

