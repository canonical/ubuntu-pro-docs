import os
import shutil
from git import Repo

############################################################
### Pro Client docs pages 
############################################################

# Import Pro Client docs into temporary folder:
# Remove previous temp folders if they're there - we don't want old content
# hanging around
# If you are adding a new folder for a new doc set, add the folder name as
# per these examples
if os.path.exists('temp'):
    shutil.rmtree('temp/')
if os.path.exists('pro-client/'):
    shutil.rmtree('pro-client/')

# Create the temp and pro-client folders if they don't already exist
# To add a new folder, add a new line like this with your folder name
os.makedirs('temp/', exist_ok=True)
os.makedirs('pro-client/', exist_ok=True)

# Download and link Pro Client docs files into a temp folder:
Repo.clone_from('https://github.com/canonical/ubuntu-pro-client/', 'temp/', single_branch=True, b='docs')

# Move all docs files to pro-client folder
tutorial_source = 'temp/docs/tutorials/'
tutorial_destination = 'pro-client/'
howto_source = 'temp/docs/howtoguides/'
howto_destination = 'pro-client/'
explanation_source = 'temp/docs/explanations/'
explanation_destination = 'pro-client/'
reference_source = 'temp/docs/references/'
reference_destination = 'pro-client'
other_source = 'temp/docs/'
other_destination = ''

# Now filter out the pages we want in the Handbook (and any "include" files and
# folders so that the pages work correctly). Specify the page names, then the 
# 'for' loops below will move those files to the pro-client folder. All other
# files (the ones we don't want) will be deleted again.

tutorial_to_move = [
    'basic_commands.rst',
    'common/'
    ]

for item in tutorial_to_move:
    source_path = os.path.join(tutorial_source, item)
    destination_path = os.path.join(tutorial_destination, item)
    shutil.move (source_path, destination_path)

howto_to_move = [
    'configure_proxies.rst',
    'enable_anbox.rst',
    'enable_cis.rst',
    'enable_esm_infra.rst',
    'enable_fips.rst',
    'enable_landscape.rst',
    'enable_livepatch.rst',
    'enable_realtime_kernel.rst',
    'enable-disable/',
    'how_to_attach.rst',
    'how_to_attach_with_config_file.rst',
    'pro-dashboard-service-toggles.png',
    'trusty_legacy_support.rst',
    ]

for item in howto_to_move:
    source_path = os.path.join(howto_source, item)
    destination_path = os.path.join(howto_destination, item)
    shutil.move(source_path, destination_path)

expl_to_move = [
    'purging_services.rst',
    ]

for item in expl_to_move:
    source_path = os.path.join(explanation_source, item)
    destination_path = os.path.join(explanation_destination, item)
    shutil.move(source_path, destination_path)

reference_to_move = [
    ]

for item in reference_to_move:
    source_path = os.path.join(reference_source, item)
    destination_path = os.path.join(reference_destination, item)
    shutil.move(source_path, destination_path)
    
other_to_move = [
    'links.txt'
    ]

for item in other_to_move:
    source_path = os.path.join(other_source, item)
    destination_path = os.path.join(other_destination, item)
    shutil.move(source_path, destination_path)
    
shutil.rmtree('temp/')

# After files have been copied, adjust the internal links to make sure they
# all work correctly
source_dir = 'pro-client/'
search_string = '../references/'
replace_string = ''

files_to_edit = [
    'enable_fips.rst',
    'enable_livepatch.rst',
    'enable_realtime_kernel.rst'
    ]

for item in files_to_edit:
    filepath = os.path.join(source_dir, item)
    with open(filepath, 'r') as file:
        content = file.read()
        
    if search_string in content:
        content = content.replace(search_string, replace_string)
        
        with open(filepath, 'w') as file:
            file.write(content)

## Adjust the other links so they're using Intersphinx

source_files = [
    'pro-client/basic_commands.rst',
    'pro-client/basic_commands.rst',
    'pro-client/basic_commands.rst',
    'pro-client/enable_esm_infra.rst',
    'pro-client/enable_fips.rst',
    'pro-client/enable_livepatch.rst',
    'pro-client/enable_realtime_kernel.rst'
    ]
    
search_strings = [
    '<pro-status-output>',
    '<expl-pro-refresh>',
    '<how-to>',
    '<expl-ESM>',
    ':doc:`services compatibility matrix <compatibility_matrix>`',
    ':doc:`services compatibility matrix <compatibility_matrix>`',
    ':doc:`services compatibility matrix <compatibility_matrix>`',
    ]

replace_strings = [
    '<pro-client-docs:pro-status-output>',
    '<pro-client-docs:expl-pro-refresh>',
    '<pro-client-docs:how-to>',
    '<pro-client-docs:expl-ESM>',
    '`services compatibility matrix. <https://canonical-ubuntu-pro-client.readthedocs-hosted.com/en/latest/references/compatibility_matrix/>`_',
    '`services compatibility matrix. <https://canonical-ubuntu-pro-client.readthedocs-hosted.com/en/latest/references/compatibility_matrix/>`_',
    '`services compatibility matrix. <https://canonical-ubuntu-pro-client.readthedocs-hosted.com/en/latest/references/compatibility_matrix/>`_',
    ]

for source_file, search_item, replace_item in zip(source_files, search_strings, replace_strings):
    with open(source_file, 'r') as file:
        content = file.read()
        
        if search_item in content:
            content = content.replace(search_item, replace_item)

        with open(source_file, 'w') as file:
            file.write(content)

