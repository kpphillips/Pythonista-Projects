'''
script for 3 factor login authentication to your Autodesk account. This will save a file in the current project location with response tokens to be used for api calls. "forgeauth_response_keys.py"

This will access A360 hubs and projects as is.  

To access BIM 360 next gen accounts you will need to add a custom integration forge app client_id under account administration web interface. 
'''

from rauth import OAuth2Service
import webbrowser
from urllib.parse import urlparse
import json
import forge_endpoints as c 
import ui
import sys
import datetime
import time
import console

#forge authentication
service = OAuth2Service(
	client_id=c.client_id,
	client_secret=c.client_secret,
	name='forge',
	authorize_url=c.endpointuri,
	access_token_url=c.endpointtoken,
	base_url=c.baseUrl)
params = {'scope': c.scope,
		'response_type': 'code',
		'redirect_uri': c.redirect_uri}
url = service.get_authorize_url(**params)

#decoder for oauth response
def new_decoder(payload):
	return json.loads(payload.decode('utf-8'))

def getCodeFromUrl(loadedUrl):	
	return code

def parseOauthKeys(loadedUrl):			
	print('Parsing Keys')	
	parse=urlparse(loadedUrl)
	codeq=parse.query
	code=codeq.lstrip('code=')				
	data = {'code': code,
			'grant_type': 'authorization_code',
			'redirect_uri': c.redirect_uri}
							
	service.get_raw_access_token(data=data)
	r=service.access_token_response
	if r.ok:				
		rdict=json.loads(r.content.decode('utf-8'))
	
		access_token=rdict['access_token']
		refresh_token=rdict['refresh_token']
		token_type=rdict['token_type']
		expires_in=rdict['expires_in']
				
		exptime=datetime.timedelta(seconds=expires_in)
		now=datetime.datetime.now()
		expires_on=now+exptime
				
		str=f'access_token=\'{access_token}\'\n\n'
		str+=f'refresh_token=\'{refresh_token}\'\n\n'
		str+=f'token_type=\'{token_type}\'\n\n'
		str+=f'expires_in=\'{expires_in}\'\n\n'
		str+=f'expires_on=\'{expires_on}\'\n\n'
				
		out_file_name = sys.argv[0].rstrip('.py') + '_response_keys.py'
		with open(out_file_name, 'w') as out_file:
			print('Writing File')
			out_file.write(str)
			console.hud_alert(f'Access Token saved to file!', 'success', 1.8)
	
	else:
		print('Token not saved, try again')	
	
	pass
			
def webOauth():
	w, h = ui.get_screen_size()
	v = ui.View()
	wv = ui.WebView()
	wv.delegate=MyWebViewDelegate()
	wv.width = w
	wv.height = h
	wv.load_url(url)
	v.add_subview(wv)
	v.present()
	pass
		
class MyWebViewDelegate (object):
	def webview_should_start_load(self, webview, url, nav_type):
		return True
	def webview_did_start_load(self, webview):
		pass
	def webview_did_finish_load(self, webview):
		loadedUrl=webview.evaluate_javascript('window.location.href')
		
		if c.redirect_uri in loadedUrl:
			parseOauthKeys(loadedUrl)	
		pass
	def webview_did_fail_load(self, webview, error_code, error_msg):
		pass

webOauth()
