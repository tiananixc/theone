#!--encode:utf-8--
import sys,time
t = time.strftime('%Y-%m-%d')

filename=raw_input('filename:')
makefilename=raw_input('makefilename:')
def xmlmake(url):
	f2.write("""	<url>
        <loc>"""+url.strip()+"""</loc>
        <lastmod>"""+t+"""</lastmod>
        <changefreq>daily</changefreq>
        <priority>0.8</priority>
    </url>"""+'\n')

f=open(filename,'r')
fl=f.readlines()
f.close()
global f2
f2=open(makefilename,'w')
f2.write("""<?xml version="1.0" encoding="utf-8"?>\n<urlset>\n""")
for url in fl:
	print url
	xmlmake(url)

f2.write("""</urlset>""")
f2.close()

