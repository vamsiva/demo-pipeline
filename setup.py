from setuptools import setup,find_packages

setup(name="census_income",
      version="0.0.1",
      author="vamsi krishna paila",
      author_email="vamsikrishnap436@gmail.com",
      packages=find_packages(),
      install_requires=['pandas','numpy','flask']
    )
