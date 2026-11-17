import requests, re, json
H={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0 Safari/537.36","Accept":"text/html"}
def flight(t):
    parts=re.findall(r'self\.__next_f\.push\(\[1,"((?:[^"\\]|\\.)*)"\]\)',t)
    return "".join(json.loads('"'+p+'"') for p in parts)
sm=requests.get("https://store.creality.com/sitemap.xml",headers=H,timeout=30).text
print("SITEMAPS:",re.findall(r"<loc>([^<]+)</loc>",sm)[:10])
cs=[u for u in re.findall(r"<loc>([^<]+)</loc>",sm) if "collection" in u]
if cs:
    x=requests.get(cs[0].replace("&amp;","&"),headers=H,timeout=30).text
    print("COLLECTIONS:",re.findall(r"<loc>([^<]+/collections/[^<]+)</loc>",x)[:80])
t=requests.get("https://store.creality.com/collections/3d-printers",headers=H,timeout=30).text; f=flight(t)
i=f.find('compareAtPrice'); print("CARD:",f[max(0,i-2600):i+400])
print("PAGINATION:",re.findall(r'"(?:totalCount|total|pageInfo|hasNextPage|page)"\s*:\s*[^,}]{1,40}',f)[:10])
t=requests.get("https://store.creality.com/products/k2-combo-3d-printer",headers=H,timeout=30).text
for b in re.findall(r'<script[^>]*ld\+json[^>]*>(.*?)</script>',t,re.S): print("LD:",re.sub(r"\s+"," ",b)[:900])
