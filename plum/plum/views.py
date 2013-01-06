from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    MyModel,
    )

from trumpet.views.base import BaseViewer
from trumpet.views.base import prepare_layout

def prepare_main_layout(request):
    layout = request.layout_manager.layout
    prepare_layout(layout)
    layout.left_menu.set_header('Leaflet Menu')
    #url = request.route_url('hubby_context', context='dbmeetings', id=None)
    #layout.left_menu.append_new_entry('hubby', url)
    url = request.route_url('view_wiki')
    layout.left_menu.append_new_entry('wiki', url)
    url = request.route_url('rssviewer', context='listfeeds', feed=None)
    layout.left_menu.append_new_entry('rss', url)
    layout.title = 'Leaflet'
    layout.header = 'Leaflet'
    layout.subheader = 'Revealed from opening a small mailbox.'
    
class MainViewer(BaseViewer):
    def __init__(self, request):
        super(MainViewer, self).__init__(request)
        prepare_main_layout(self.request)
        
        


def my_view(request):
    DBSession = request.db
    try:
        one = DBSession.query(MyModel).filter(MyModel.name == 'one').first()
    except DBAPIError:
        return Response(conn_err_msg, content_type='text/plain', status_int=500)
    return {'one': one, 'project': 'plum'}

conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_plum_db" script
    to initialize your database tables.  Check your virtual 
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

