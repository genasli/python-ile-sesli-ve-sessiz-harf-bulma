def harf_sayıları_bul(cumle):
    
    sesli_harfler  = "aeıioöuü"
    sessiz_harfler = "zyvtşsrpnmlkjhğgfdçcb"
    
    sesli_sayısı = 0
    sessiz_sayısı = 0

    for harf in cumle:
        if harf.lower() in sesli_harfler:
            sesli_sayısı += 1
        elif harf.lower() in sessiz_harfler:
            sessiz_sayısı += 1

    return sesli_sayısı , sessiz_sayısı

kullanıcıdan_alınan_cumle = input("Bir cümle ya da kelime giriniz: ")
sesli_sayısı,sessiz_sayısı = harf_sayıları_bul(kullanıcıdan_alınan_cumle)
print("Sesli harf sayısı : {} ".format(sesli_sayısı))
print("Sessiz harf sayısı : {} ".format(sessiz_sayısı))
