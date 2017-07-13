from setuptools import setup

setup(name='fabutils',
      version='0.1',
      description='Utility methods for using fabric in sudo environment',
      author='RajaRaviVarma',
      author_email='rajaravivarma.ar@gmail.com',
      license='MIT',
      packages=['fabutils'],
      install_requires=[
          'fabric'
      ],
      zip_safe=False)
