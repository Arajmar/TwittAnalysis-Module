import os
import csv
from bs4 import BeautifulSoup

#Original by Jean LAPOSTOLLE

csv = open("resYT.csv", "w", encoding="utf-8")

with open("pagetest.html", encoding="utf-8") as html_file:
    soup = BeautifulSoup(html_file, features="html.parser")
print("ok")
coms = soup.findAll("div", {"id" : "body"}, {"class": "style-scope ytd-comment-renderer"})
#print(coms)
    # print("Nombre de commentaires :", len(coms) - 1)
for com in coms:
    text = com.find("div",{"id" : "content"}, {"slot" : "content"})
    #text2 = newsoup.findAll("yt-formated-string")
    #print(text)
    if text != None:
        info = text.get_text().replace(",", "").replace("\n", "").replace('"', '')
        print(info)
        csv.write("{},\n".format(info))

    # print("Nombre de commentaires :", len(coms) - 1)

#style-scope ytd-comment-renderer
'''
<div id="content" class="style-scope ytd-expander">
      
      <yt-formatted-string id="voted-option" slot="content" class="style-scope ytd-comment-renderer" disable-upgrade="" hidden=""></yt-formatted-string><yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">Voici la caverne d'Ali baba version satisfaction insolite 😂 😂 genial ton nouveau décor, continu comme ça.👍👍﻿</yt-formatted-string>
</div>'''

'''
<yt-formatted-string id="content-text" slot="content" split-lines="" class="style-scope ytd-comment-renderer">"C'est joli ça, Émeraude ! C'est comme les nana qui s'appelle Fleur..."
Même pas 1min de vidéo passé et il dit déjà de la merde. Merci pour ce bon moment.</yt-formatted-string>
'''