import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'trumpet>=0.1.1dev', # pull from github
    'hubby>=0.0dev',   # pull from github
    'waitress',
    'Kotti',
    'facebook-sdk',
    'ipython',
    'twill',
    ]

setup(name='plum',
      version='0.0',
      description='plum',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='plum',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = plum:main
      [console_scripts]
      initialize_plum_db = plum.scripts.initializedb:main
      """,
      dependency_links=[
        'https://github.com/umeboshi2/trumpet/archive/master.tar.gz#egg=trumpet-0.1.1dev',
        'https://github.com/umeboshi2/hubby/archive/master.tar.gz#egg=hubby-0.0dev',
        ],
      )
