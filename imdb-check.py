#!/usr/bin/python3

from imdbpie import Imdb
import logging, PTN, sys, urllib.request

torrent_name = sys.argv[1:][0]
torrent_url = sys.argv[1:][1]
torrent_dir = sys.argv[1:][2]
required_rating = sys.argv[1:][3]

download_path = torrent_dir + "/" + torrent_name + '.torrent'

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

imdb = Imdb()

movie_info = PTN.parse(torrent_name)

if movie_info is not None:
    try:
        rating = imdb.get_title_by_id(imdb.search_for_title(movie_info['title'])[0]['imdb_id']).rating
        if rating >= float(required_rating):
            urllib.request.urlretrieve(torrent_url, download_path)
            
    except:
        logging.exception("Something went wrong")
