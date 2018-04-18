from pelican import signals, contents
import os.path
from os.path import basename
import socket
import json
import pygeoip


'''
This is a skeleton for testing the parsing of a MIRRORS file
to show a list on /downloads/
'''

'''
It's been created by me, Pat David, to do what I need for wgo.
This is based heavily on stuff the LoTR was doing already...
Don't try to make any sense of it.  I don't know what I'm doing.
I am not kidding.
'''

'''
Update 2016-07-20
    Had to change the signal to
    `signals.content_written.connect(do_mirrors)`
    so we actualy catch the rendered .html files
    after they've been through the template.
    This way we can look for <!-- MIRRORS --> to
    replace it with the correct parsed list.
'''

class UnexpectedException(Exception): pass

def html_output( data ):

    html = u"<dl class='download-mirrors'>\n"

    for key, values in sorted(data.iteritems()):

        html += u"<dt>{}</dt>".format( key )

        for value in values:
            if isinstance( value, unicode ):
                tmp = value
            else:
                tmp = unicode( value, 'utf_8')
            html += u"<dd><a href='{}'>{}</a></dd>\n".format( tmp, tmp )

    html += u"</dl>"

    return html


def do_mirrors(path, context):


    # normalize OS path separators to fwd slash
    path = path.replace( os.path.sep, '/' )

    # if we are on a downloads page
    #if '/downloads/index.html' in path:
    if '/downloads/' in path:

        # create mirrors dict
        mirrors = {}
        # instantiate geoip object, load db 
        gi = pygeoip.GeoIP('./plugins/gimp_mirrors/GeoIP.dat')

        # load mirrors2.json file from content
        try:
            with open('./content/downloads/mirrors2.json') as data_file:
                data = json.load(data_file)

                for record in data:
                    #print "####"
                    #print record

                    try:
                        country = gi.country_name_by_name( record )
                        #print country

                        if country in mirrors:
                            mirrors[ country ] += data[ record ]
                        else:
                            mirrors[ country ] = data[ record ]

                    except:
                        print "cannot resolve record: ", record

                try:
                    with open( path, 'r') as f:
                        s = f.read()
                        #print s.decode('utf-8')
                        s = s.decode('utf-8').replace(u"<!-- MIRRORS -->", html_output( mirrors ))

                    with open( path, 'w') as f:
                        f.write( s.encode('utf-8') )

                except:
                    print "Trouble with reading/writing path."

        except IOError:
            print "Cannot open /content/downloads/mirrors.json!"
            try:
                with open( path, 'r') as f:
                    s = f.read()
                    #print s.decode('utf-8')
                    s = s.decode('utf-8').replace(u"<!-- MIRRORS -->", u"<p><small>Cannot open mirrors2.json</small></p>")

                with open( path, 'w') as f:
                    f.write( s.encode('utf-8') )

            except:
                print "Trouble with reading/writing path."



def register():
    # Trying something to read the html after written...
    signals.content_written.connect(do_mirrors)

