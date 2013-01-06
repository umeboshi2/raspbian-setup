from fanstatic import Library
from fanstatic import Resource
from fanstatic import Group
#from js.lesscss import LessResource

library = Library('plum', 'resources')

css_resource = Resource(library, 'main.css')

js_resource = Resource(library, 'main.js', bottom=True)

#less_resource = LessResource(library, 'main.less')

plum = Group([css_resource, js_resource,
#                     less_resource,
                    ])


def pserve():
    """A script aware of static resource"""
    import pyramid.scripts.pserve
    import pyramid_fanstatic
    import os

    dirname = os.path.dirname(__file__)
    dirname = os.path.join(dirname, 'resources')
    pyramid.scripts.pserve.add_file_callback(
                pyramid_fanstatic.file_callback(dirname))
    pyramid.scripts.pserve.main()
