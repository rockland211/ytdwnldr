# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 10:28:54 2021

@author: rockl
"""

import logging
import sys
from flask import Flask, request, send_file
from pytube import YouTube

logging.basicConfig(string=sys.stderr, level=logging.DEBUG)

app = Flask(__name__)


@app.route("/")
def YouTube_Downloader():
        html_page = f"""<%<html><head>
        <Title> YouTube Downloader </Title></head>
        <body  
            style="background-color:DodgerBlue;" >
            <h2> <font face = "Verdana"> Enter YouTube URL: </font><br /></h2> 
            <div class="form">
            <form action= "download_video" method="post">
            <input type="text" name="URL">
            <input type="submit" value="Submit">
        </form></div> <br><br>
        </body></html>%>"""
        return html_page

@app.route('/download_video', methods=['GET', 'POST'])
def download_video():
    youtube_url = request.form['URL']
    download_path = YouTube(
        youtube_url).streams.get_highest_resolution().download()

    fp = download_path.split('//')[-1]
    return send_file(fp, as_attachment=True)

