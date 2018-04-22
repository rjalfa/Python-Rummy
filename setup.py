from setuptools import setup, find_packages

readme = open('README.md', 'r')
README_TEXT = readme.read()
readme.close()

setup(
    name='rummy',
    version='0.1.0',
    url='https://github.com/sarcoma/Python-Rummy',
    license='MIT',
    author='sarcoma',
    author_email='sean@orderandchaoscreative.com',
    description='Console Rummy game',
    long_description=README_TEXT,
    long_description_content_type='text/markdown',
    entry_points={
        'console_scripts': ['rummy=rummy.command_line:main'],
    },
    include_package_data=True,
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    package_data={'rummy':"templates/*.txt"},
    install_requires=['colorama', 'text_template', 'ansi_colours'],
    project_urls={
        'Order & Chaos Creative': 'https://orderandchaoscreative.com',
    }
)