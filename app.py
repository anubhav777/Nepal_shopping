from bs4 import BeautifulSoup
import requests,lxml
import json
import re
def ebay(name):
    url=f"https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw={name}&_sacat=0"
    source=requests.get(url).text

    soup=BeautifulSoup(source,'lxml')
    art=soup.find(id='mainContent')
    child_art=art.find('div',id='srp-river-main')
    ul_par=child_art.find('div',id='srp-river-results')
    ul=ul_par.find('ul',class_='srp-results')
    li=ul.find_all('li',class_='s-item')
    newarr=[]
    for new_li in li:
        try:
            txtli=new_li.text
            img_class=new_li.find('img', class_='s-item__image-img')['src']
            a_tag=new_li.find('a',class_='s-item__link').h3.text
            price_span=new_li.find('span',class_='s-item__price').text
            new_obj={'img_src':img_class,'discription':a_tag,'price_span':price_span}
            newarr.append(new_obj)
            
        except Exception as e:
            print(e)
    return newarr

def amazon(name):
    newarr=[]
    headers = {'authority': 'www.amazon.com',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'}
    search_attr=None
    if " " in name:
        search_attr=name.replace(" ","+")
    else:
        search_attr=name
    url=f"https://www.amazon.com/s?k={search_attr}&ref=nb_sb_noss_1"
    source=requests.get(url,headers=headers).text
    
    soup=BeautifulSoup(source,'lxml')
    art=soup.find_all('div',class_='s-result-item')
    for parent in art:
        try:
            first_par=parent.find('div',class_='s-include-content-margin')
            img_src=first_par.find('div',class_='s-image-fixed-height').img['src']
            disc=first_par.find('span',class_='a-size-medium').text
            price=first_par.find('span',class_='a-offscreen').text
            if price:
                new_obj={'img_src':img_src,'discription':disc,'price':price}
                newarr.append(new_obj)
            
        except Exception as e:
            pass

    return newarr



# print(amazon('hp laptop'))


def daraz(name):
    newarr=[]
    search_attr=None
    if " " in name:
        search_attr=name.replace(" ","+")
    else:
        search_attr=name
    url=f"https://www.daraz.com.np/catalog/?q={name}&_keyori=ss&from=input&spm=a2a0e.11779170.search.go.36c42d2b2Nkfy8"
    source=requests.get(url).text
    soup=BeautifulSoup(source,'lxml')
    art=soup.find_all('script')
    art_child=None
    for par in art:
        try:
            fg=str(par)
            if 'window.pageData' in fg:
                art_child=fg
            
        except Exception as e:
            pass
    fistsplit=art_child.split("=",1)[1]
    sec_split=fistsplit.replace("</script>","")

    new_json=json.loads(sec_split)
    first_child=new_json['mods']
    main_child=first_child['listItems']


    # notes for finding key of a large object
    # for k,v in first_child.items():
    
    #        print(k)
    for parent in main_child:
        try:
            discription=parent['name']
            image=parent['image']
            price=parent['priceShow']
            newobj={'discription':discription,'image':image,'price':price}
            newarr.append(newobj)

        except Exception as e:
            pass
    return newarr

def walmart(name):
    newarr=[]
    search_attr=None
    if " " in name:
        search_attr=name.replace(" ","%20")
    else:
        search_attr=name
    url=f"https://www.walmart.com/search/?query={search_attr}"
    source=requests.get(url).text
    soup=BeautifulSoup(source,'lxml')
    art=soup.find_all('div',class_='search-result-gridview-item')
    for parent in art:
        try:
            img_src=parent.find('div',class_='orientation-square').img['src']
            discription=parent.find('a',class_='product-title-link').span.text
            price=parent.find('span',class_='price-main-block').span.find('span').text
            newobj={'discription':discription,'img':img_src,'price':price}
            newarr.append(newobj)
        except Exception as e:
            pass
        
    return newarr

def sastodeal(name):
    newarr=[]
    search_attr=None
    if " " in name:
        search_attr=name.replace(" ","+")
    else:
        search_attr=name
    url=f"https://www.sastodeal.com/catalogsearch/result/?q={search_attr}"
    source=requests.get(url).text
    soup=BeautifulSoup(source,'lxml')
    art=soup.find('ol',class_='product-items').find_all('li')
    for parent in art:
        # try:
            img=parent.find('span',class_='product-image-wrapper').img['src']
            discription=parent.find('a',class_='product-item-link').text
            discription=discription.strip()
            price=parent.find_all('span',class_='price-final_price')[-1].text
            newobj={'discription':discription,'img':img,'price':'price'}
            newarr.append(newobj)
        # except Exception as e:
        #     pass

   
    return newarr

def tudoholic():
    newarr=[]
    headers={
       
        'Referer': 'https://tudoholic.com/search?type=product&q=shoes',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'ss=29be291bot; tawkUUID=D898KeZOSb3TnV6h1HiTTMpAde2sj4VU0gqqcQFKOUuFqhnPsdYX2U9sQJbRRIyf%7C%7C2',
        'origin': 'https://tudoholic.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
        'accessToken':'07e05537bb67d15b19460a6539dfe3b4'
    }
    source=requests.get('https://tudoholic.com/search?type=product&q=shoes',headers=headers).text
    soup=BeautifulSoup(source,'lxml')
    art=soup.find('div',class_='grid-uniform').text
    newarr.append(art)
    return newarr

def gyapyu(obj):
    source=requests.get(f'https://www.gyapu.com/api/search?q={obj}&size=30&page=1').text
    new_data = json.loads(source)
    # soup=BeautifulSoup(source,'lxml')
    # parent = soup.find('div',{'class':'SrchRightTop flex flex-wrap border border-primary p-1'})
    newarr=[]
    parent = new_data['data']['products']
    for i in parent:
        name = i['name']
        try:
            name = re.sub('</*b>','',name)
        except:
            pass
        image = i['image'][0]['document']['path']
        image_path = f'https://www.gyapu.com/{image}'
        price=i['max_sales_price']
        newobj={'discription':name,'img':image_path,'price':price}
        newarr.append(newobj)
    return 

def thulo():
    newarr=[]
    url=f"https://thulo.com/search/?subcats=Y&pcode_from_q=Y&pshort=Y&pfull=Y&pname=Y&pkeywords=Y&search_performed=Y&cid=0&q=cream&security_hash=c668b5ba536be95262021e0ee4078303"
    source=requests.get(url).text
    soup=BeautifulSoup(source,'lxml')
    parent=soup.find('div',{'class':'grid-list et-grid-list'})
    child=parent.find_all('div',{'class':'et-column4 et-grid-item-wrapper'})
    for i in child:
        image = i.find('div',{'class':'ty-grid-list__image'}).find('img').get('src')
        name = i.find('div',{'class':'et-grid-info-wrapper'}).find('div',{'class':'et-grid-product-name'}).text
        price = i.find('div',{'class':'et-grid-info-wrapper'}).find_all('span',{'class':'ty-price-num'})[1].text
        new_name = name.replace('\n','')
        newobj={'discription':new_name,'img':image,'price':price}
        newarr.append(newobj)
    
    return newarr
    
 


print(thulo())