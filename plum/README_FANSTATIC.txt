pyramid_fanstatic installation
==============================

To finalize your installation you'll need to follow those steps.

Add those line the ``app:main`` section of your development.ini::

    [app:main]

    fanstatic.bottom = true
    fanstatic.debug = true

Add some requirements to your setup.py::


    requires = ['pyramid', 'pyramid_debugtoolbar',
                'pyramid_fanstatic',
                # if you want to use lesscss
                #'js.lesscss'
                ]


Also add those entry points to the same file bellow the paste.app_factory::

      # Fanstatic resource library
      [fanstatic.libraries]
      plum = plum.resources:library

      # A console script to serve the application and monitor static resources
      [console_scripts]
      pserve-fanstatic = plum.resources:pserve

You also need to add pyramid_fanstatic tween to your application. Add the
following to your __init__.py file::

    config.include('pyramid_fanstatic')

Run ``python setup.py develop`` to get the ``pserve-fanstatic`` script
available.
