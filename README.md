# autodl-imdb-check
Python script to cross check torrent with IMDb rating and if it is greater than required rating, download the torrent.

Add the following in your autodl.cfg in global [options] or [filter <name>] header.

```
upload-type = exec
upload-command = /path/to/imdb-check.py
upload-args = "$(TorrentName)" "$(TorrentUrl)" 'TORRENT_WATCH_DIR' 'REQUIRED_IMDB_RATING'
```
