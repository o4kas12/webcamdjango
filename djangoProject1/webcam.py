from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def index(request):

    
    

    url = 'http://10.10.3.208/webcam/'
    ext = 'mp4'
    href_list = list(reversed(get_url_paths(url, ext)))
    hrefs=''
    for href in href_list:
        #hrefs+=f'<li><a href="{href}" class="video_href" >{href}</a></li> \n'
        href_name = href[href.find("-") + 1 : ]
        hrefs+=f'<li><a href="{href}" class="video_href" >{href_name[8:10]}:{href_name[10:12]}:{href_name[12:14]}  {href_name[6:8]}-{href_name[4:6]}-{href_name[0:4]}</a></li> \n'

#        print (href)
    return render(request, 'new_web.html', {'hrefs': hrefs})
    

def get_url_paths(url, ext='', params={}):
    response = requests.get(url, params=params)
    if response.ok:
        response_text = response.text
    else:
        return response.raise_for_status()
    soup = BeautifulSoup(response_text, 'html.parser')
    parent = [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext)]
    return parent
