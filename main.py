from __future__ import unicode_literals
import YtDown.youtube_dl.YoutubeDL as YoutubeDL
import sys
import json
import logging

if __name__ == '__main__':
   ydl_opts = {
        'usenetrc': None,
        'username': None,
        'password': None,
        'twofactor': None,
        'videopassword': None,
        'quiet': True,
        'no_warnings': True,
        'forceurl': False,
        'forcetitle': False,
        'forceid': False,
        'forcethumbnail': False,
        'forcedescription': False,
        'forceduration': False,
        'forcefilename': False,
        'forceformat': False,
        'forcejson': False,
        'dump_single_json': False,
        'simulate': False,
        'skip_download': True,
        'format': 'all',
        'listformats': True,
        'outtmpl': '',
        'autonumber_size': '',
        'restrictfilenames': False,
        'ignoreerrors': True,
        'force_generic_extractor': False,
        'ratelimit': False,
        'nooverwrites': False,
        'retries': 3,
        'fragment_retries': 3,
        'buffersize': 4196,
        'noresizebuffer': False,
        'continuedl': True,
        'noprogress': True,
        'progress_with_newline': False,
        'playliststart': 1,
        'playlistend': None,
        'playlistreverse': False,
        'noplaylist': False,
        'logtostderr': False,
        'consoletitle': None,
        'nopart': False,
        'updatetime': None,
        'writedescription': False,
        'writeannotations': False,
        'writeinfojson': False,
        'writethumbnail': True,
        'write_all_thumbnails': False,
        'writesubtitles': False,
        'writeautomaticsub': False,
        'allsubtitles': True,
        'listsubtitles': False,
        'subtitlesformat': None,
        'subtitleslangs': None,
        'matchtitle': None,
        'rejecttitle': None,
        'max_downloads': None,
        'prefer_free_formats': False,
        'verbose': False,
        'dump_intermediate_pages': False,
        'write_pages': False,
        'test': False,
        'keepvideo': False,
        'min_filesize': None,
        'max_filesize': None,
        'min_views': 0,
        'max_views': -1,
        'daterange': None,
        'cachedir': None,
        'youtube_print_sig_code':None,
        'age_limit': None,
        'download_archive': None,
        'cookiefile': None,
        'nocheckcertificate': True,
        'prefer_insecure': True,
        'proxy': None,
        'socket_timeout': '45',
        'bidi_workaround': False,
        'debug_printtraffic': False,
        'prefer_ffmpeg': False,
        'include_ads': False,
        'default_search': '',
        'youtube_include_dash_manifest':False,
        'encoding': 'utf8',
        'extract_flat': False,
        'mark_watched': False,
        'merge_output_format': None,
        'postprocessors': [],
        'fixup': None,
        'source_address': '',
        'call_home': None,
        'sleep_interval': 10,
        'external_downloader': None,
        'list_thumbnails': True,
        'playlist_items': None,
        'xattr_set_filesize': False,
        'match_filter': None,
        'no_color': True,
        'ffmpeg_location': None,
        'hls_prefer_native': None,
        'hls_use_mpegts': None,
        'external_downloader_args': None,
        'postprocessor_args': None,
        'cn_verification_proxy': [],

        'logger' : logging.getLogger()
    }

   downProxy = None
   if 'youtube' in sys.argv[1]:
       ydl_opts['proxy'] = '127.0.0.1:8787'
       downProxy = {'host' : '127.0.0.1', 'port' : 8787 }

   with YoutubeDL(ydl_opts) as ydl:
       all = ydl.extract_info(sys.argv[1], download=False, process=False)
#       newAll = ydl.process_ie_result(all, True )
#       if newAll:
#       	   all = newAll
       if isinstance(all,dict):
           all['downProxy'] = downProxy      
       print(json.dumps(all,ensure_ascii=True))
