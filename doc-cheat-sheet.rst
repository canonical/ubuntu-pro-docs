:orphan:

.. _cheat-sheet:

reStructuredText cheat sheet
============================

This file contains the syntax for commonly used reST markup.
Open it in your text editor to quickly copy and paste the markup you need.

See the `reStructuredText style guide <https://canonical-documentation-with-sphinx-and-readthedocscom.readthedocs-hosted.com/style-guide/>`_ for detailed information and conventions.

Also see the `Sphinx reStructuredText Primer <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_ for more details on reST, and the `Canonical Documentation Style Guide <https://docs.ubuntu.com/styleguide/en>`_ for general style conventions.

H2 heading
----------

H3 heading
~~~~~~~~~~

H4 heading
^^^^^^^^^^

H5 heading
..........

Inline formatting
-----------------

- :guilabel:`UI element`
- ``code``
- :file:`file path`
- :command:`command`
- :kbd:`Key`
- *Italic*
- **Bold**

Code blocks
-----------

Start a code block::

     code:
       - example: true

.. code::

     # Demonstrate a code block
     code:
       - example: true

.. code:: yaml

     # Demonstrate a code block
     code:
       - example: true

.. _a_section_target:

Links
-----

- `Canonical website <https://canonical.com/>`_
- `Canonical website`_ (defined in ``reuse/links.txt`` or at the bottom of the page)
- https:\ //canonical.com/
- :ref:`a_section_target`
- :ref:`Link text <a_section_target>`
- :doc:`index`
- :doc:`Link text <index>`

Intersphinx
-----------

With Intersphinx we can include references to docs and objects in other
repositories. 

We need to add the repository to the ``custom_conf.py`` file like so:

.. code::

    intersphinx_mapping = {
        "pro-client": ("https://canonical-ubuntu-pro-client.readthedocs-hosted.com/en/latest/", None),
        "repo-name": ("URL/to/docs", None),
    }

We can then use Intersphinx to reference the content in the following way:

.. code::

    - :ref:`repo-name:ref-role`
    - :ref:`:ref: role <repo-name:ref-role>`
    - :doc:`repo-name:path/to/object`
    - :doc:`Intersphinx <repo-name:path/to/object>`

More details about how to use it can be `found here <https://docs.readthedocs.io/en/stable/guides/intersphinx.html>`_.

Navigation
----------

Use the following syntax::

  .. toctree::
     :hidden:

     sub-page1
     sub-page2


Lists
-----

1. Step 1

   - Item 1

     * Sub-item
   - Item 2

     i. Sub-step 1
     #. Sub-step 2
#. Step 2

   a. Sub-step 1

      - Item
   #. Sub-step 2

Term 1:
  Definition
Term 2:
  Definition

Tables
------

+----------------------+------------+
| Header 1             | Header 2   |
+======================+============+
| Cell 1               | Cell 2     |
|                      |            |
| Second paragraph     |            |
+----------------------+------------+
| Cell 3               | Cell 4     |
+----------------------+------------+

+----------------------+------------------+
| :center:`Header 1`   | Header 2         |
+======================+==================+
| Cell 1               | Cell 2           |
|                      |                  |
| Second paragraph     |                  |
+----------------------+------------------+
| Cell 3               | :center:`Cell 4` |
+----------------------+------------------+

.. list-table::
   :header-rows: 1

   * - Header 1
     - Header 2
   * - Cell 1

       Second paragraph
     - Cell 2
   * - Cell 3
     - Cell 4

.. rst-class:: align-center

   +----------------------+------------+
   | Header 1             | Header 2   |
   +======================+============+
   | Cell 1               | Cell 2     |
   |                      |            |
   | Second paragraph     |            |
   +----------------------+------------+
   | Cell 3               | Cell 4     |
   +----------------------+------------+

.. list-table::
   :header-rows: 1
   :align: center

   * - Header 1
     - Header 2
   * - Cell 1

       Second paragraph
     - Cell 2
   * - Cell 3
     - Cell 4

Notes
-----

.. note::
   A note.

.. tip::
   A tip.

.. important::
   Important information

.. caution::
   This might damage your hardware!

Images
------

.. image:: https://assets.ubuntu.com/v1/b3b72cb2-canonical-logo-166.png

.. figure:: https://assets.ubuntu.com/v1/b3b72cb2-canonical-logo-166.png
   :width: 100px
   :alt: Alt text

   Figure caption

Mermaid diagrams
----------------

You can create flow diagrams and similar visual elements using Mermaid. The
`live editor`_ allows you to create and tweak your diagrams, and provides you
with the code snippet that allows you to include it in your documentation. 

To include a Mermaid diagram, use the following:

.. code::

    .. mermaid::
        :alt: (optional) allows you to include alt text
        :align: (optional) options are left, right, or center
        :caption: (optional) includes a caption
        :zoom: (optional) allows the figure to be zoomed
           
        <Paste your diagram's code input here. Make sure you leave an empty
        line under `.. mermaid::`, and indent your diagram's code with at
        least 3 empty spaces as shown here. Anything indented will be included
        in the diagram.>
        
Here's an example:

.. code::

    .. mermaid::
        :zoom:
        
        flowchart TD
            A[Christmas] -->|Get money| B(Go shopping)
            B --> C{Let me think}
            C -->|One| D[Laptop]
            C -->|Two| E[iPhone]
            C -->|Three| F[fa:fa-car Car]
    

Reuse
-----

.. |reuse_key| replace:: This is **included** text.

|reuse_key|

.. include:: index.rst
   :start-after: include_start
   :end-before: include_end

Tabs
----

.. tabs::

   .. group-tab:: Tab 1

      Content Tab 1

   .. group-tab:: Tab 2

      Content Tab 2


Glossary
--------

.. glossary::

   example term
     Definition of the example term.

:term:`example term`

More useful markup
------------------

- .. versionadded:: X.Y
- | Line 1
  | Line 2
  | Line 3
- .. This is a comment
- :abbr:`API (Application Programming Interface)`

----

Custom extensions
-----------------

Related links at the top of the page::

  :relatedlinks: https://github.com/canonical/lxd-sphinx-extensions, [RTFM](https://www.google.com)
  :discourse: 12345

Terms that should not be checked by the spelling checker: :spellexception:`PurposelyWrong`

A terminal view with input and output:

.. terminal::
   :input: command
   :user: root
   :host: vampyr

   the output

A link to a YouTube video:

.. youtube:: https://www.youtube.com/watch?v=iMLiK1fX4I0
          :title: Demo



.. LINKS
.. _Canonical website: https://canonical.com/
.. _live editor: https://mermaid.live/
