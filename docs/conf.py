import datetime
import os

# Configuration for the Sphinx documentation builder.
# All configuration specific to your project should be done in this file.
#
# This project uses the extension-based Sphinx Stack. Behaviour that is common
# to all Canonical documentation is provided by the 'canonical_sphinx' extension
# and its dependencies; only Ubuntu Pro-specific configuration lives here.
#
# A complete list of built-in Sphinx configuration values:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# The Sphinx Stack uses the Canonical Sphinx theme to keep all documentation
# consistent and on brand:
# https://github.com/canonical/canonical-sphinx

#######################
# Project information #
#######################

# Project name
project = "Ubuntu Pro"

# Author name; used in the default copyright statement in the page footer
author = "Canonical Group Ltd"

# The year in the copyright statement
copyright = "%s, %s" % (datetime.date.today().year, author)

# Sidebar documentation title
# To disable the title, set it to an empty string.
html_title = project + " documentation"

# Documentation website URL
#
# NOTE: The Ubuntu Pro documentation is published at ubuntu.com/pro/docs, so the
# canonical and Open Graph URLs are set explicitly rather than derived from
# READTHEDOCS_CANONICAL_URL.
ogp_site_url = "https://ubuntu.com/pro/docs/"

# Preview name of the documentation website
ogp_site_name = project

# Preview image URL
ogp_image = "https://assets.ubuntu.com/v1/253da317-image-document-ubuntudocs.svg"

# Dictionary of values to pass into the Sphinx context for all pages:
# https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_context
html_context = {
    # Product page URL; can be different from product docs URL
    "product_page": "https://ubuntu.com/pro",
    # Product tag image; the orange part of the logo, shown in the page header
    "product_tag": "_static/tag.png",
    # Discourse instance URL
    "discourse": "https://discourse.ubuntu.com/c/ubuntu-pro/116",
    # Mattermost channel URL
    "mattermost": "https://chat.canonical.com/canonical/channels/documentation",
    # Documentation GitHub repository URL
    "github_url": "https://github.com/canonical/ubuntu-pro-docs",
    # Docs branch in the repo; used in links for viewing the source files
    "repo_default_branch": "main",
    # Docs location in the repo; used in links for viewing the source files
    "repo_folder": "/docs/",
    # Enable or disable the Previous / Next buttons at the bottom of pages
    # Valid options: none, prev, next, both
    "sequential_nav": "none",
    # Required for the feedback button and the issue link in the footer
    "github_issues": "enabled",
    # Passes the top-level 'author' value to the theme
    "author": author,
    # Header links used by the custom Ubuntu Pro header template
    "client_docs": "https://documentation.ubuntu.com/pro-client/en/latest/",
    "pro_service_esm": "https://ubuntu.com/security/esm",
    "pro_service_livepatch": "https://ubuntu.com/security/livepatch",
    "pro_service_fips": "https://ubuntu.com/security/fips",
    "pro_service_usg": "https://ubuntu.com/security/certifications/docs/usg",
    "pro_service_cc": "https://ubuntu.com/security/cc",
    "pro_service_landscape": "https://ubuntu.com/landscape",
    "pro_service_anbox": "https://anbox-cloud.io/",
    "pro_service_ros": "https://ubuntu.com/robotics/ros-esm",
    "pro_service_realtime": "https://ubuntu.com/realtime-kernel",
}

# Enable the edit button on pages, pointing at the documentation GitHub repo.
html_theme_options = {
    "source_edit_link": "https://github.com/canonical/ubuntu-pro-docs",
}

# Project slug
# This documentation is hosted on https://ubuntu.com/pro/docs/.
slug = "pro/docs"

#######################
# Sitemap configuration: https://sphinx-sitemap.readthedocs.io/
#######################

# The base URL is set explicitly because the Ubuntu Pro documentation is served
# from ubuntu.com/pro/docs (it was changed during the Read the Docs domain
# migration).
html_baseurl = "https://ubuntu.com/pro/docs/"

# sphinx-sitemap uses html_baseurl to generate the full URL for each page:
sitemap_url_scheme = "{link}"

# Custom sitemap filename for the ubuntu.com/pro/docs publishing path:
sitemap_filename = "doc-sitemap.xml"

# Include `lastmod` dates in the sitemap:
sitemap_show_lastmod = True

# Pages excluded from the sitemap:
sitemap_excludes = [
    "404/",
    "genindex/",
    "search/",
]

# The base URL for references built by sphinx-markdown-builder (llms.txt).
# The trailing slash is stripped because the builder joins this value with a
# leading-slash path, which would otherwise produce a doubled slash.
if os.environ.get("READTHEDOCS"):
    markdown_http_base = html_baseurl.rstrip("/")

################################
# Template and asset locations #
################################

# The custom Ubuntu Pro header (Pro services dropdown) and footer templates.
templates_path = ["_templates"]

# Custom static assets (Pro tag image, Pro header CSS/JS overrides and the
# Read the Docs link rewriting script).
html_static_path = ["_static"]

#############
# Redirects #
#############

# Internal (rediraffe) redirects. Add mappings to the 'redirects.txt' file.
# https://sphinxext-rediraffe.readthedocs.io/en/latest/
rediraffe_redirects = "redirects.txt"
rediraffe_branch = "main"

# Strips '/index.html' from destination URLs when building with 'dirhtml'
rediraffe_dir_only = True

# Client-side page redirects (sphinx-reredirects). These redirect legacy
# pro-client pages that used to live in this repo to the Ubuntu Pro Client docs.
# https://documatt.gitlab.io/sphinx-reredirects/usage.html
redirects = {
    "pro-client/basic_commands": "https://documentation.ubuntu.com/pro-client/en/latest/tutorials/basic_commands/",
    "pro-client/configure_proxies": "https://documentation.ubuntu.com/pro-client/en/latest/howtoguides/configure_proxies/",
    "pro-client/enable_anbox": "https://documentation.ubuntu.com/pro-client/en/latest/howtoguides/enable_anbox/",
    "pro-client/enable_cis": "https://documentation.ubuntu.com/pro-client/en/latest/howtoguides/enable_cis/",
    "pro-client/enable_esm_infra": "https://documentation.ubuntu.com/pro-client/en/latest/howtoguides/enable_esm_infra/",
    "pro-client/enable_fips": "https://documentation.ubuntu.com/pro-client/en/latest/howtoguides/enable_fips/",
    "pro-client/enable_landscape": "https://documentation.ubuntu.com/pro-client/en/latest/howtoguides/enable_landscape/",
    "pro-client/enable_livepatch": "https://documentation.ubuntu.com/pro-client/en/latest/howtoguides/enable_livepatch/",
    "pro-client/enable_realtime_kernel": "https://documentation.ubuntu.com/pro-client/en/latest/howtoguides/enable_realtime_kernel/",
    "pro-client/how_to_attach": "https://documentation.ubuntu.com/pro-client/en/latest/howtoguides/how_to_attach/",
    "pro-client/how_to_attach_with_config_file": "https://documentation.ubuntu.com/pro-client/en/latest/howtoguides/how_to_attach_with_config_file/",
    "pro-client/purging_services": "https://documentation.ubuntu.com/pro-client/en/latest/explanations/purging_services/",
    "pro-client/trusty_legacy_support": "https://documentation.ubuntu.com/pro-client/en/latest/howtoguides/trusty_legacy_support/",
}

###########################
# Link checker exceptions #
###########################

# A regex list of URLs that are ignored by 'make linkcheck'
linkcheck_ignore = [
    "http://127.0.0.1:8000",
    "https://support-portal.canonical.com/*",
]

# A regex list of URLs where anchors are ignored by 'make linkcheck'
linkcheck_anchors_ignore_for_url = [r"https://github\.com/.*"]

# Give linkcheck multiple tries on failure
linkcheck_retries = 3

########################
# Configuration extras #
########################

# Custom Sphinx extensions; see
# https://www.sphinx-doc.org/en/master/usage/extensions/index.html
# NOTE: 'canonical_sphinx' provides the theme and the common Canonical
# configuration. 'sphinxcontrib.mermaid' is added on top of the default stack
# because Ubuntu Pro docs use Mermaid diagrams (e.g. support-overview).
extensions = [
    "canonical_sphinx",
    "notfound.extension",
    "sphinx_design",
    "sphinx_rerediraffe",
    "sphinx_reredirects",
    "sphinx_tabs.tabs",
    "sphinxcontrib.jquery",
    "sphinxext.opengraph",
    "sphinx_config_options",
    "sphinx_contributor_listing",
    "sphinx_filtered_toctree",
    "sphinx_llm.txt",
    "sphinx_related_links",
    "sphinx_roles",
    "sphinx_terminal",
    "sphinx_ubuntu_images",
    "sphinx_youtube_links",
    "sphinxcontrib.cairosvgconverter",
    "sphinx_last_updated_by_git",
    "sphinx.ext.intersphinx",
    "sphinx_sitemap",
    "sphinxcontrib.mermaid",
]

# Excludes files or directories from processing
exclude_patterns = [
    "doc-cheat-sheet*",
    ".venv*",
]

# Adds custom CSS files, located in 'html_static_path' or remotely.
# The remote cookie-banner stylesheet restores the Ubuntu cookie policy styling;
# 'pro-header.css' styles the Ubuntu Pro "Pro services" header dropdown.
html_css_files = [
    "https://assets.ubuntu.com/v1/d86746ef-cookie_banner.css",
    "pro-header.css",
]

# Adds custom JavaScript files, located in 'html_static_path' or remotely.
# The remote bundle.js provides the cookie policy banner and analytics;
# 'pro-header-nav.js' toggles the Ubuntu Pro "Pro services" header dropdown;
# 'overwrite_links.js' rewrites the Read the Docs-hosted domain to the published
# ubuntu.com/pro/docs domain in the header and Read the Docs addons.
html_js_files = [
    "https://assets.ubuntu.com/v1/287a5e8f-bundle.js",
    "pro-header-nav.js",
    "overwrite_links.js",
]

# NOTE: Reusable Ubuntu Pro link definitions live in 'reuse/links.txt'. They are
# pulled into individual pages with an explicit '.. include:: /reuse/links.txt'
# rather than a global 'rst_epilog', to preserve the original per-page link
# resolution behaviour (e.g. the 'landscape' page label).

# Specifies a reST snippet to be prepended to each .rst file.
# This defines a :center: role that centers table cell content.
rst_prolog = """
.. role:: center
   :class: align-center
"""

# Configuration for Intersphinx projects
intersphinx_mapping = {
    "pro-client": ("https://documentation.ubuntu.com/pro-client/en/latest/", None),
}

intersphinx_disabled_reftypes = ["*"]
