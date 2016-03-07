'''

Author : Karmesh Maheshwari
Country of Origin: India
Email: karm_ma@yahoo.co.in, karm_apple@icloud.com
Language : Python 2
	

--------------------------------------------------------------------------------------------------------------------	


This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.


    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.


    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.


------------------------------------------------------------------------------------------------------------------------

Sorry for not commenting unused libraries and variables. Get your Bing API key from Microsoft Bing Developer Portal. In case of any assistance, feel free to contact me.

Microsoft and Bing are the Registered Trademarks of the Microsoft Corporation, USA.
The 1024 Stacks Softwares and Pro E are the registered trademarks of The 1024 Stacks Softwares, India. 

 

'''

import urllib
import httplib
#import httplib2
import urllib2
import json
from bs4 import BeautifulSoup   
import requests
import string
import re
from pprint import pprint
from lib2to3.pgen2.token import GREATEREQUAL

flag=0
flag2=0
ue=[]
v=[]

class karmesh:
    
 
    def main():
    
        format="mp3 song download"
        query = raw_input("Search Query>")
        query2=query
        query=query+" "+format
    
        ue=string.split(query2, sep=' ',maxsplit=-1)
    
    
       
        print bing_search(query)
        #l=string.splitfields(query2, sep=1, maxsplit=-1)
        #print l

    def bing_search(query):
        count=0
        ana=0
        
        ka=[]
        #bing api (web) key
        key= 'Enter Key Here'
        temp=query
        query = urllib.quote(query)
        # create credential for authentication
        user_agent = 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322)'
        credentials = (':%s' % key).encode('base64')[:-1]
        auth = 'Basic %s' % credentials

        url = 'https://api.datamarket.azure.com/Bing/SearchWeb/v1/Web?Query=%27'+query+'%27&$top=100&$format=json'
        request = urllib2.Request(url)
        request.add_header('Authorization', auth)
        request.add_header('User-Agent', user_agent)
        request_opener = urllib2.build_opener()
        response = request_opener.open(request)
        response_data = response.read()
        json_result = json.loads(response_data)
    
    
        #enable to see all the content..>>>
        #result_list = json_result['d']['results']
        #print result_list    
    
        for i in json_result['d']['results']:
        
                        
            try:
                r=requests.get(str(i['Url']))
        
                soup=BeautifulSoup(r.content)
            except:
           
                continue

            for link in  soup.find_all('a'):
    
            
                y=link.get("href")
                try:#try to find as much as it can
                    if y.endswith(".mp3"):
                    
                        #changes are here..!!!!!
                        #if (string.find(query,y)):
                        ana=ana+1
                        u=y
                        v=(string.lower(u)).replace('://'," ").replace('%',' ').replace('/'," ").replace('-'," ").replace('_'," ").replace('20',' ').replace('(',' ').replace(')',' 

').replace('.'," ").split()
                        #print v
                        if 'mp3light' in v or 'onlinekaraoke'  in v or "4shared" in v or "sound2mp3" in v or "trendingmp3" in v or "mp3falls" in v or "candymp3" in v:
                            
                            continue
                        else:
                    
                            r=requests.head(y)
                            '''some text/html contain the seeds..get on it bro..!!'''
                    
                            if r.headers['content-type'] == "audio/mpeg" or r.headers['content-type'] == "application/octet-stream" :
                                count=count+1
                                print r.headers['content-type']
                                ka.append(y)
                                print y.encode('utf-8')+"\n"
                      
                except:
                    
                    continue
                
        print ka
         
    if __name__ == "__main__":
    

        main()
