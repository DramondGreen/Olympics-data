# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 16:26:42 2016

@author: admin
"""
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')
from lxml import etree
import requests
import re

url1='https://www.olympic.org/olympic-results'
urllist=[0]*49
urllist[0]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B535B8008-29D0-44BB-8B14-E2B29CC79DD5%7D'
urllist[1]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B1C3D47A1-714D-458C-8DCD-3C3BBE5B5509%7D'
urllist[2]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B4F0D97B7-E300-4148-9E0D-3AB237E329C3%7D'
urllist[3]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B5670D0F9-E147-4394-A0B3-017B945B4883%7D'
urllist[4]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7BEDB2F1CE-A451-466B-B801-4FB9B1BECFBB%7D'
urllist[5]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B06A8CA86-4B86-4C99-95FE-B9DFEB1D8DBD%7D'
urllist[6]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7BABBCC315-CB07-4396-BC2D-36BF604D9436%7D'
urllist[7]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7BC0240C34-0979-4B26-AD79-7DFB3723A49D%7D'
urllist[8]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B572398FF-F85C-45E6-95E4-10BAC8FDACD1%7D'
urllist[9]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B87E8EB3F-7772-4183-AB34-EFF27175B892%7D'
urllist[10]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7BC5E57EB0-83A5-404F-9B4E-BFE10E78E6CB%7D'
urllist[11]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B5B631904-FE09-47BB-9D84-55BA996C5810%7D'
urllist[12]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B99DCBCDA-B81E-4AD8-81A5-269959387991%7D'
urllist[13]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B88EEEF50-AAD6-4E1E-977F-6DBF978C2F2F%7D'
urllist[14]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7BE871F262-9647-46B7-A5E5-F53F63608EA0%7D'
urllist[15]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B00419E90-DD1D-48A8-AB8A-5A3553890248%7D'
urllist[16]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B15E0AF33-CBB8-4573-B66D-81B98C315784%7D'
urllist[17]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B6BC71B03-81E7-415E-9C55-F1258BC7D698%7D'
urllist[18]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B329D8985-F2ED-4EA2-8E0F-52D6AA32DBF6%7D'
urllist[19]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B5889D495-A6C2-4A08-8F9A-B7F6EEEA80C4%7D'
urllist[20]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B4C95E6AB-811D-432B-A944-B4893926601C%7D'
urllist[21]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B1B628F90-80BA-4068-A539-0214FFFF47DF%7D'
urllist[22]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B6D32C62C-1AF5-4F4B-9ECF-536501A38396%7D'
urllist[23]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7BFA88CD42-558A-481C-89EB-205C16DD0412%7D'
urllist[24]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B4A04C2B5-433A-4363-AE7F-27CDF37088FD%7D'
urllist[25]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7BA209AF10-6E0A-4446-B5FF-BA971481988A%7D'
urllist[26]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7BE5570657-0C6F-42A9-9AF4-69B824AB1261%7D'
urllist[27]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B5EC5FF1F-6B8F-4492-8B39-4388EE06A857%7D'
urllist[28]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B013733CE-11B6-4571-9946-C9F2205254FA%7D'
urllist[29]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B230A5C08-E7BF-4447-91A9-69AD6A014EB9%7D'
urllist[30]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B27422092-430E-4821-B392-B65B7386C543%7D'
urllist[31]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B454B9CCB-D9AF-460E-A271-6A910887C663%7D'
urllist[32]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B5822BB72-52D8-4E24-8B15-CED623D407B3%7D'
urllist[33]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B4D96BD61-7E7F-409A-9229-E7C9EC85F880%7D'
urllist[34]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7BE033A1B8-C101-4E44-87CB-5198A7DF7417%7D'
urllist[35]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B9F5E89B2-69E7-4556-9C9B-B0EE267981D5%7D'
urllist[36]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B060D1917-A635-43F6-9015-18747E3246C1%7D'
urllist[37]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B17D0E11A-A330-4579-9B47-296922662EAC%7D'
urllist[38]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B5374121F-93EC-4A87-8CA7-C262317214F2%7D'
urllist[39]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7BC8D52C85-1F85-411C-951A-A36D6ED0B888%7D'
urllist[40]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B2715E1C6-4FA8-4769-B156-9C29F9C779CB%7D'
urllist[41]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B99F70C7D-658F-40F9-9A23-17E2D6033F3D%7D'
urllist[42]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B5413693A-802A-4674-A8BF-5F1BD8F0F1E2%7D'
urllist[43]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7BEFFE69C4-95EC-48D1-B12C-01A97F8EDE7F%7D'
urllist[44]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7BE04E3AFB-A918-43A5-9BCE-936CBBD42726%7D'
urllist[45]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7BBD4A77F8-DEB3-4644-BB52-3271DC33D251%7D'
urllist[46]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7BEA2D9BED-37A5-465E-87A4-AEDA15A6A4C0%7D'
urllist[47]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7BC3287788-387D-431F-A293-F94F34BDECBF%7D'
urllist[48]='https://www.olympic.org/ajaxscript/getdisciplinebygame/%7B1C6EBA12-999C-4F5F-B194-2ACD5E8BA65D%7D'

def getsource(url):
    html = requests.get(url)
    return html.text


    
def main():
    html = getsource(url1)
    selector = etree.HTML(html)
    name=[]
    gamelist=[]
 
    for i in range(2,51):
        tempname = [selector.xpath('//*[@id="sel-games"]/option['+str(i)+']/text()')[0].replace(" ","-").replace("'","-")]
        name = name + tempname
        
    
    for link in urllist:
        html = getsource(link)
        selector = etree.HTML(html)
        i=0
        j=1
        glist=[]
        while (len(selector.xpath('/html/body/select/option['+str(j)+']/text()'))!=0):
            g= selector.xpath('/html/body/select/option['+str(j)+']/text()')[0].replace(" ","-")
            glist.append(g)
            j=j+1
            
            
        gamelist.append(glist)
    
    print name
    print gamelist
        
    info=[]
    count=0
    for l in name:
        for o in gamelist[count]:
            newurl ="https://www.olympic.org/"+l+'/'+o
            html = getsource(newurl)
            selector = etree.HTML(html)
            print newurl
            for j in range(1,3):
                i=1
                while (len(selector.xpath('//*[@id="main"]/div/div/div['+str(j)+']/section['+str(i)+']/h2/a/text()'))!=0):
                    m=1
                    temp = l+";"+o+";"+selector.xpath('//*[@id="main"]/div/div/div['+str(j)+']/section['+str(i)+']/h2/a/text()')[1].strip()+";"
                    while (len(selector.xpath('//*[@id="main"]/div/div/div['+str(j)+']/section['+str(i)+']/table/tbody/tr['+str(m)+']/td[1]/div/span/text()'))!=0):
                        temp = temp + selector.xpath('//*[@id="main"]/div/div/div['+str(j)+']/section['+str(i)+']/table/tbody/tr['+str(m)+']/td[1]/div/span/text()')[0].strip()+";"
                        if len(selector.xpath('//*[@id="main"]/div/div/div['+str(j)+']/section['+str(i)+']/table/tbody/tr['+str(m)+']/td[2]/div/a/div/div/span/text()'))!=0:
                            temp = temp + selector.xpath('//*[@id="main"]/div/div/div['+str(j)+']/section['+str(i)+']/table/tbody/tr['+str(m)+']/td[2]/div/a/div/div/span/text()')[0].strip()+";"
                        elif len(selector.xpath('//*[@id="main"]/div/div/div['+str(j)+']/section['+str(i)+']/table/tbody/tr['+str(m)+']/td[2]/div/a/div[2]/strong/text()')) !=0 :
                            temp = temp + selector.xpath('//*[@id="main"]/div/div/div['+str(j)+']/section['+str(i)+']/table/tbody/tr['+str(m)+']/td[2]/div/a/div[2]/strong/text()')[0].strip()+";"
                        else:
                            temp = temp + "No Country" + ";"
                        
                        
                        m = m+1

                    info.append(temp)
                    i = i+1
                j=j+1
        count=count+1
    

    

    #print name
    #print urllist
    #print gamelist
    print info
   
    print 1
    
    out = open("C:/Users/pc/Desktop/3.txt","a")
    record= len(info)
    for i in range(0,record):
        out.write(info[i])
        out.write("\n")
    out.close
main()

    