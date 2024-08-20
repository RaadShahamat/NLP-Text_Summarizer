import setuptools

with open('README.md','r', encoding='utf-8') as f:
    long_description = f.read()


Name='Text_Summarizer'
Version='0.0.0'
Author='Raad Shahamat Alif'
AuthorEmail='raadalif25@gmail.com'

setuptools.setup(
    name=Name,
    version=Version,
    author=Author,
    author_email=AuthorEmail,
    description='A simple text summarizer(under developed by Raad)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/RaadShahamat/NLP-Text_Summarizer',
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    package_dir = {"": "src"},
    project_url = "https://github.com/RaadShahamat/NLP-Text_Summarizer/issues"
)

