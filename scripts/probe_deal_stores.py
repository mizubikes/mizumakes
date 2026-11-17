import requests, re, json
H={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36","Accept":"text/html"}
for h in ["p2s","a1-mini","h2d","ams-2-pro"]:
    t=requests.get(f"https://us.store.bambulab.com/products/{h}",headers=H,timeout=30).text
    print("== product",h, [m for m in re.findall(r'<script[^>]*ld\+json[^>]*>',t)])
    for b in re.findall(r'<script[^>]*ld\+json[^>]*>(.*?)</script>',t,re.S):
        try:
            j=json.loads(b)
        except Exception as e:
            print("bad",e,b[:200]); continue
        items=j if isinstance(j,list) else [j]
        for it in items:
            if it.get("@type") in ("Product","ProductGroup"):
                print(" name:",it.get("name"),"| type",it.get("@type"),"| image:",str(it.get("image"))[:100])
                offs=it.get("offers") or []
                offs=offs if isinstance(offs,list) else [offs]
                for o in offs[:12]: print("   offer:",o.get("name") or o.get("sku"),o.get("price"),o.get("availability","")[-10:],json.dumps(o.get("priceSpecification"))[:300])
                for v in (it.get("hasVariant") or [])[:12]:
                    o=v.get("offers") or {}; print("   variant:",v.get("name"),v.get("sku"),o.get("price"),json.dumps(o.get("priceSpecification"))[:300])
