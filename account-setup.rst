Ubuntu Pro: general account setup
=================================

This introduction is for:

* direct data centre customers who have purchased a yearly subscription to Ubuntu Pro from Canonical or through a reseller
* public cloud customers who have purchased a yearly subscription (non-metered) to Ubuntu Pro 

Ubuntu Pro customers on a metered plan purchased directly from AWS or Azure should instead refer to:

* `Getting started with Ubuntu Pro on AWS <https://ubuntu.com/engage/aws-pro-onboarding>`_
* `Getting started with Ubuntu Pro on Azure <https://ubuntu.com/engage/azure-pro-onboarding>`_


Ubuntu One
----------

Access to the Ubuntu Pro customer portals is mediated through **Ubuntu One Single Sign On**.

If you do not already have an Ubuntu One account
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will need to know the correct email address for the account (this will be the same email address to which your "Welcome to Ubuntu Pro" message was sent). 

If you don't know the address, ask the person who set up your organisation's Ubuntu Pro subscription.

Go to `Ubuntu One <http://login.ubuntu.com>`_ and select *I do not have an Ubuntu One account*.

Create a new account, using the email address associated with your Ubuntu Pro subscription as the "Preferred email address". 

After verifying your email address, you can access the customer portals. There are three portals: 

* `Ubuntu Pro dashboard <ubuntu.com/pro/dashboard>`_
* `Canonical Support Portal <portal.support.canonical.com>`_ 
* `Landscape <landscape.canonical.com>`_ (additional set-up will be required) 

Ubuntu Pro dashboard
--------------------

Open the `Ubuntu Pro dashboard <http://ubuntu.com/pro/dashboard>`__. This dashboard gives you an overview of your current Ubuntu Pro subscriptions. 

Ubuntu Pro token
~~~~~~~~~~~~~~~~

Here you can see your subscriptions and the **Ubuntu Pro tokens** associated with them. The tokens are required to enable many Ubuntu Pro services. When a service requires your token, get it from here.

For more information about using the Ubuntu Pro token, client, and active machine count, see `Bitstream services: overview & enablement <link tbc>`_.


Add a secondary user
~~~~~~~~~~~~~~~~~~~~

We recommend that all customers with commercial subscriptions have a secondary user on the Ubuntu Pro dashboard, to ensure continuity of access.

Check *Account users* from the main menu. If a secondary user is not already listed, add one now.

Canonical Support Portal
------------------------

Open the `Canonical Support Portal <http://portal.support.canonical.com>`__. The Support Portal provides access to our Knowledge Base. If you have a support contract, this is where to raise support tickets.

Add a secondary user
~~~~~~~~~~~~~~~~~~~~

As before, we recommend adding a secondary user to the portal, to ensure continuity of access.

Check *Account users* from the main menu. If a secondary user is not already listed, add one now. Select the account profile icon, then *My account* > *New user*. Also select the *Active Ubuntu Advantage user* option, so that the new contact is enabled as a Support Portal user.

-----------


Landscape
---------

The final customer portal is `Landscape SaaS <http://landscape.canonical.com/>`_, our system management tool. Landscape is largely used by our customers to manage package configurations, package updates and security updates on Ubuntu instances at scale, but it has lots of other functions, too. To learn more about these, head over to `Landscape module <link tbc>`_ on this course.

Landscape accounts are not automatically provisioned when a new customer purchases Ubuntu Pro. Instead, we send a Landscape invitation email to the technical contact on the new account, with a link that will activate the Landscape account. This email sometimes lands in spam folders, so if you have not seen it, please check there. If you still cannot find it, or if the link has expired, contact your Account Manager or our Customer Success Team to ask for us to send the email again - you can request contact details for the team via Livechat on any web-page at <ubuntu.com>.

After activating your Landscape account, you will be able to sign in. You can then add new users under the “Administrators” tab.

Be aware that you need access to your Landscape SaaS account, even if you are planning to use self-hosted Landscape, because your license.txt files for self-hosted Landscape are downloaded directly from Landscape SaaS.




FAQs
----

1. I’m trying to reset my Ubuntu One password but the reset emails are not arriving. What should I do?

Most of the time, this happens because you have not created an Ubuntu One account. Note that Canonical does not provision Ubuntu One accounts or create usernames and passwords for new Ubuntu Pro users. Try navigating to Ubuntu One, input the email listed against your Ubuntu Pro account and choose “I do not have an Ubuntu One” account. Create a username and password of your choosing. After verifying your email, you should be able to access the Ubuntu Pro portals.

If you have already created an Ubuntu One account and the reset emails are still not arriving and you are a paying customer, contact your Account Manager or the Customer Success Team - our contact details are provided on the Ubuntu Pro welcome email sent after purchase, or navigate to `ubuntu.com <ubuntu.com>`_ and ask for our details using the Livechat service. 


2. My colleague added me to one of the Ubuntu Pro portals, but I can’t access any of the other portals. What’s going on?

User access is not integrated across the Ubuntu Pro portals. This means that you need to be added as a new user on every portal to which you require access. Any current administrator on a portal will be able to add new users as needed.

Not sure who is an admin on your account? Contact your procurement team, your Account Manager at Canonical, or Customer Success. If you need help finding contact details, please navigate to any web-page under `ubuntu.com <ubuntu.com>`_ and ask for help using our Livechat service.

3. I tried adding a new user to my account in `Ubuntu One <http://login.ubuntu.com>`_ but they still can’t access any of the Ubuntu Pro portals. How do I fix it?

Ubuntu One is simply a Single Sign On across the Ubuntu websites, including the Ubuntu Pro portals. It is not a user management system for Ubuntu Pro. You can add new users to your Ubuntu Pro account in each customer portal - the `Ubuntu Pro dashboard <http://ubuntu.com/pro/dashboard>`__, `the Support Portal <http://support.canonical.com>`_, and `Landscape <http://landscape.canonical.com>`__. Please ensure that each individual user on your account creates their own Ubuntu One account - these cannot be shared by multiple users, and trying to share them will often trigger errors.
