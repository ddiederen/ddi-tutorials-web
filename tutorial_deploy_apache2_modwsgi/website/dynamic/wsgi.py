#!/usr/bin/env python
#%% Globals ####
# Libraries ----
from urllib.parse import parse_qs
import cgi

# Functions ----
#def funCoastline(image):
def dumpclean(obj):
    retStr = ''
    if type(obj) == dict:
        for k,v in obj.items():
            if hasattr(v,'__iter__'):
                retStr = retStr + '<br>' + str(k)
                dumpclean(v)
            else:
                bla = '%s : %s' % (k, v)
                retStr = retStr + '<br>' + bla
    elif type(obj) == list:
        for v in obj:
            if hasattr(v,'__iter__'):
                dumpclean(v)
            else:
                retStr = retStr + '<br>' + str(v)
    else:
        retStr = retStr + str(obj)
    return retStr


# root folder where files are
root = 'D:/Work/python/WSGI/tutorial/'



#%% Input ####
# HTML template
html = u"""
<html>
    <body>
        <fieldset>
            <form name="test" method="post" action="">
                Name: <input type="text" name="studentname" />
                Date excercise: <input type="date" name="date" />
                <input type="submit" name="submit" value="Submit" />
            </form>
        </fieldset>

        <p>
            Name: %(studentname)s<br>
            Date: %(date)s<br>
        </p>
    </body>
</html>
"""


#%%  Application #####
def application(environ, start_response):
    # Input (request) ----
    if environ['REQUEST_METHOD'] == 'POST':    
        # get data from request
        post_env = environ.copy()
        post_env['QUERY_STRING'] = ''
        post = cgi.FieldStorage(
            fp=environ['wsgi.input'],
            environ=post_env,
            keep_blank_values=True
        )
        print(post)
        
        studentname = post['studentname'].value
        print(studentname)
        date = post['date'].value
        print(date)
        
        # Handle ----
        # Fill in the html template
        response_body = html % {
            'studentname':  studentname,
            'date':  date,
        }
    else:
        response_body = html % {
            'studentname': "",
            'date': "",
        }

    # Output ----
    start_response(
        '200 OK',
        [
            ('Content-type', 'text/html; charset=utf8'),
            ('Content-Length', str(len(response_body))),
        ]
    )
    return [response_body.encode('utf8')]


#%% Test environment ----
from wsgiref.simple_server import make_server    
if __name__ == '__main__':
    try:
        httpd = make_server('', 8051, application)
        print('Serving on port 8051...')
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('Goodbye.')