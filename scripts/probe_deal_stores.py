import requests, re, json
H={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36","Accept":"text/html"}
def flight(t):
    parts=re.findall(r'self\.__next_f\.push\(\[1,"((?:[^"\\]|\\.)*)"\]\)',t)
    return "".join(json.loads('"'+p+'"') for p in parts)
for h in ["p2s","a1-mini","h2d"]:
    t=requests.get(f"https://us.store.bambulab.com/products/{h}",headers=H,timeout=30).text; f=flight(t)
    print("== product",h,len(t),len(f))
    for b in re.findall(r'<script type="application/ld\+json"[^>]*>(.*?)</script>',t,re.S): print("LD:",re.sub(r"\s+"," ",b)[:1200])
    for k in ["msrp_price","compareAtPrice","compare_at_price","originalPrice","typicalPrice","\"price\":"]:
        for m in list(re.finditer(re.escape(k) if k.endswith(":") else '"'+k+'"',f))[:2]:
            print("   ",k,"::",f[max(0,m.start()-200):m.start()+220].replace("\n"," "))
t=requests.get("https://us.store.bambulab.com/sitemap.xml",headers=H,timeout=30).text; print("SITEMAP",t[:800])
