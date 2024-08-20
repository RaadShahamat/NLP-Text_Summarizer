import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s: %(message)s:]')

project_name = "text_summarizer"

folder_list = [
    '.github/workflow/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/logging/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'params.yaml',
    'app.py',
    'requirement.txt',
    'Dockerfile',
    'setup.py',
    'main.py',
    'research/trials.ipynb'
]

for filepath in folder_list:
    file_path = Path(filepath)
    filedir , filename = os.path.split(file_path)

    if filedir != '':
        os.makedirs(filedir, exist_ok=True)
        logging.info(f'creating directory {filedir} for file {filename}')

    
    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f'creating file {filename}')
    else:
        logging.info(f'{filename} already exists')

        
