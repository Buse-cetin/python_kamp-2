dosya=open("odev.txt","r")
dizi=dosya.readlines()
for i in dizi:
    temiz_dizi="".join(filter(lambda x: x.isdigit() not,i))
    x=temiz_dizi.replace("=","")
    y=x.replace("+","")
    z=y.replace("-","")
    t=z.replace("(","")
    u=t.replace(")","")
    v=u.replace("?","")
    m=v.rstrip("\n")
    print(m)