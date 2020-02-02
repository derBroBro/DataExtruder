from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'DataExtruder',         # How you named your package folder (MyLib)
  packages = ['DataExtruder','DataExtruder.directus_api','DataExtruder.directus_api.utils'], 
  version = '0.1.3',
  license='MIT', 
  description = 'Render data from diffrent data-sources and jinaj2 template',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Malte Brodersen',  
  author_email = 'malte.brodersen@exoit.de', 
  url = 'https://github.com/derBroBro/DataExtruder',
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['jinja2', 'directus'], 
  scripts=['bin/dataextruder'],
  install_requires=[           
          'cookiecutter',
          'click',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',    
    'Intended Audience :: Developers',   
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7',
  ],
)