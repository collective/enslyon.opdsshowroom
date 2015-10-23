from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='enslyon.opdsshowroom',
      version=version,
      description="Showroom for OPDS Feed",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['enslyon'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'plone.api',
          'setuptools',
          'plone.app.dexterity',
          'requests',
          'lxml',
          'lineage.themeselection',
          # -*- Extra requirements: -*-
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              'plone.app.contenttypes',
              'plone.app.robotframework[debug]',
          ],
      },
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      # The next two lines may be deleted after you no longer need
      # addcontent support from paster and before you distribute
      # your package.
      setup_requires=["PasteScript"],
      paster_plugins = ["ZopeSkel"],

      )
