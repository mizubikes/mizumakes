import requests, json, sys
H={"User-Agent":"Mozilla/5.0 (compatible; MizuMakesDealFinder/1.0; +https://mizumakes.com/)","Accept":"application/json"}
C=["us.store.bambulab.com","store.bambulab.com","us.elegoo.com","www.elegoo.com","store.anycubic.com","www.anycubic.com","store.creality.com","www.creality.com","www.sovol3d.com","qidi3d.com","www.qidi3d.com","www.flashforge.com","shop.flashforge.com","us.snapmaker.com","www.snapmaker.com","phrozen3d.com","us.polymaker.com","shop.polymaker.com","store.sunlu.com","www.sunlu.com","esun3dstore.com","overture3d.com","siraya.tech","fusionfilaments.com","www.pushplastic.com","www.printedsolid.com","www.3dxtech.com","www.sliceengineering.com","e3d-online.com","store.micro-swiss.com","www.bondtech.se","biqu.equipment","www.xtool.com","www.creality.com","www.atomstack.net","www.matterhackers.com","www.prusa3d.com","www.elegoo.com/en-us","www.hatchbox3d.com","www.inland3d.com","www.anker.com","www.voxelab3dp.com","www.artillery3d.com","www.creality3dofficial.com","shop.prusa3d.com","www.uniformation.com","www.peopoly.net","www.formlabs.com","www.lulzbot.com","www.ratrig.com","ldomotors.com","www.thingiverse.com","www.3djake.com","www.amolen.com","www.eryone3d.com","www.geeetech.com","kingroon.com","www.kingroon.com","www.longer3d.com","www.sculpfun.com","www.ortur.net","www.glowforge.com","www.bambulab.com"]
out=[]
for h in dict.fromkeys(C):
    u=f"https://{h}/products.json?limit=250&page=1"
    try:
        r=requests.get(u,headers=H,timeout=20)
        n=None; disc=None
        if r.ok and r.text.lstrip().startswith("{"):
            ps=r.json().get("products",[]); n=len(ps)
            disc=sum(1 for p in ps for v in p.get("variants",[])[:1] if v.get("compare_at_price") and float(v["compare_at_price"])>float(v["price"] or 0))
        out.append((h,r.status_code,n,disc,r.url[:80]))
    except Exception as e: out.append((h,"ERR",str(e)[:60],None,""))
for o in out: print(*o, sep=" | ")
