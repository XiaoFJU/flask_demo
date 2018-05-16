import os
import requests


def crawler(file_name, url):
    # create folder exist
    page_path = 'templates/pages/'
    if not os.path.exists(page_path):
        os.makedirs(page_path)

    # request the page
    response = requests.request('get', url)

    # check that file name is end .html 
    if file_name.split('.')[-1] != 'html':
        file_name += '.html'

    # write file
    with open(page_path+file_name, 'w', encoding='utf-8') as f:
        f.write(response.text)
