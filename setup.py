import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='delpro',  
     version='0.0.1',
     scripts=['delpro.py'] ,
     author="Saurabh Bhatia",
     author_email="saurabh.bhatia.phe17@iitbhu.ac.in",
     description="a demonstration of delphi process",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/sb6998",
     packages=setuptools.find_packages(),
     install_requires=[
         'otree'
     ],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
     ],
 )

