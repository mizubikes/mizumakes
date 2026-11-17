import requests, re, json
H={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36","Accept":"text/html"}
U=["https://us.store.bambulab.com/","https://us.store.bambulab.com/collections/black-friday","https://us.store.bambulab.com/collections/3d-printer","https://us.store.bambulab.com/products/p2s","https://store.creality.com/collections/3d-printers","https://store.creality.com/","https://www.prusa3d.com/category/original-prusa-3d-printers/","https://www.flashforge.com/collections/3d-printers"]
for u in U:
    try:
        r=requests.get(u,headers=H,timeout=25); t=r.text
        print("==",u,r.status_code,len(t),r.url[:90])
        print("  next_data:",'__NEXT_DATA__' in t," next_f:",'self.__next_f' in t," ld+json:",t.count('application/ld+json'),
              " robots:", re.findall(r'<meta name="robots"[^>]*>',t)[:1])
        for k in ['"price"','"originalPrice"','"compare_at_price"','"salePrice"','"discountPrice"','"marketPrice"','"spuName"','"productName"']:
            i=t.find(k)
            if i>=0: print("   ",k, t[i:i+160].replace("\n"," "))
    except Exception as e: print("==",u,"ERR",e)
for rb in ["https://us.store.bambulab.com/robots.txt","https://store.creality.com/robots.txt"]:
    try: print("==",rb); print(requests.get(rb,headers=H,timeout=20).text[:900])
    except Exception as e: print(e)
