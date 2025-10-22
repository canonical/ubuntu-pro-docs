.. _active-machine-count:

Active machine count
====================

The Ubuntu Pro dashboard displays an "active machine" count for each subscription to Ubuntu Pro. This is the number of online machines attached to your Pro token that have pinged Canonical servers within the last 24 hours.

Consumption of the following services is registered under active machines:

* ESM-Infra and ESM-Apps
* Livepatch
* USG
* CIS
* FIPS

Machines registered to Landscape are not included.

Occasionally after attaching new machines to your token, you may observe that the active machine count is doubled, e.g. you have attached 10 machines but the active machine count shows 20. Over time the count will stabilize to the correct number of machines, usually within 48 hours.

.. tip::

   If you detach a machine from your Ubuntu Pro token, the reduction in active machine count will take place 24 hours later.

Customers with unlimited guest support
---------------------------------------

If you have licensed an entire virtual cluster to Ubuntu Pro at the physical host level, you are eligible for unlimited guest support. The Ubuntu Pro dashboard will display your license type as physical, however you should use the Pro token associated with that subscription on your virtual machines.

For example, suppose you have 5 physical non-Ubuntu hosts in a cluster, all of which are licensed and covered by Ubuntu Pro. To deploy guests on this cluster, attach the token associated with your subscription to the guests. You do not need to attach the physical non-Ubuntu hosts to Ubuntu Pro.

As you attach machines, you will see your active machine count go above your license count. This is expected behaviour and will not impact your access to the Pro services.

