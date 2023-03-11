import os
import sys

RESOURCE_TYPES = {
    1: ['client/lua', 'cl_main.lua'],
    2: ['server/lua', 'sv_main.lua'],
    3: ['shared/lua', 'sh_main.lua'],
    4: ['client,shared,server/lua', 'cl_main.lua', 'sh_main.lua', 'sv_main.lua'],
    5: ['client/js', 'cl_main.js'],
    6: ['server/js', 'sv_main.js'],
    7: ['shared/js', 'sh_main.js'],
    8: ['client,shared,server/js', 'cl_main.js', 'sh_main.js', 'sv_main.js']
}

while True:
    access_code = input('Access Code:')
    if access_code == 'access!@':
        break
    else:
        print('Invalid Access Code!')

os.system('cls' if os.name == 'nt' else 'clear')
resource_name = input('Resource Name: ')
resource_type = int(input('Resource Type (1-8): '))
desktop_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
resource_path = os.path.join(desktop_path, resource_name)
os.makedirs(resource_path)

fxmanifest_contents = f'''
fx_version 'cerulean'
game 'gta5'

{name: lower()} '{resource_type[0]}'
{{
    {"client_script 'client/lua/cl_main.lua'" if 'client' in resource_type else ''}
    {"client_script 'client/js/cl_main.js'" if 'js' in resource_type and 'client' in resource_type else ''}
    {"shared_script 'shared/lua/sh_main.lua'" if 'shared' in resource_type else ''}
    {"shared_script 'shared/js/sh_main.js'" if 'js' in resource_type and 'shared' in resource_type else ''}
     {"server_script 'server/lua/sv_main.lua'" if 'server' in resource_type else ''}
    {"server_script 'server/js/sv_main.js'" if 'js' in resource_type and 'server' in resource_type else ''}
}}
'''

with open(os.path.join(resource_path, 'fxmanifest.lua'), 'w') as f:
    f.write(fxmanifest_contents)

for folder in RESOURCE_TYPES[resource_type][0].split(','):
    os.makedirs(os.path.join(resource_path, folder))

    if folder.startswith('client'):
        with open(os.path.join(resource_path, folder, RESOURCE_TYPES[resource_type][1]), 'w') as f:
            f.write('-- Client Script')
    elif folder.startswith('server'):
        with open(os.path.join(resource_path, folder, RESOURCE_TYPES[resource_type][1]), 'w') as f:
            f.write('-- Server Script')
    elif folder.startswith('shared'):
        with open(os.path.join(resource_path, folder, RESOURCE_TYPES[resource_type][1]), 'w') as f:
            f.write('-- Shared Script')
    else:
        raise ValueError(f'Invalid folder name: {folder}')
