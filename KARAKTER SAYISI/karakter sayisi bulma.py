kelime = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
kume = set()
for i in kelime:
    kume.add(i)
liste = list(kume)
for i in liste:
    print("Kelimede {} harfinden {} tane vardir.".format(i,kelime.count(i)))