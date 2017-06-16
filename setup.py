try:
    from setuptools import setup
except:
    from distutils.core import setup

# here = os.path.abspath( os.path.dirname( __file__ ) )
# README = open(os.path.join( here, 'README.rst' ) ).read()

setup(name='chibi_command',
      version='0.1',
      description='',
      # long_description=README,
      license='',
      author='',
      author_email='',
      packages=['chibi_command'],
      install_requires=[],
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
      ])
