import requests, re, json
H={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36","Accept":"text/html"}
def flight(t):
    parts=re.findall(r'self\.__next_f\.push\(\[1,"((?:[^"\\]|\\.)*)"\]\)',t)
    return "".join(json.loads('"'+p+'"') for p in parts)
for u in ["https://us.store.bambulab.com/collections/black-friday","https://store.creality.com/collections/3d-printers"]:
    t=requests.get(u,headers=H,timeout=30).text; f=flight(t)
    print("==",u,len(t),"flight",len(f))
    keys=collections=None
    import collections as C
    ks=C.Counter(re.findall(r'"([A-Za-z_]*(?:[Pp]rice|[Cc]ompare)[A-Za-z_]*)"\s*:',f)); print("  keys:",ks.most_common(15))
    for k in ["compareAtPrice","compare_at_price","originalPrice","marketPrice","price"]:
        for m in list(re.finditer('"'+k+'"',f))[:2]:
            print("   ",k,"::",f[max(0,m.start()-250):m.start()+200].replace("\n"," "))
    print("  handles:",re.findall(r'"handle"\s*:\s*"([^"]+)"',f)[:25])
t=requests.get("https://us.store.bambulab.com/products/p2s",headers=H,timeout=30).text
for b in re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>',t,re.S): print("LD:",b[:1500])
