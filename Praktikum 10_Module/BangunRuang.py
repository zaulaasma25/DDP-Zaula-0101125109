import math
def kubus(sisi):
    hasil = math.pow(sisi, 3)
    return hasil

def balok (p,l,t):
    # hasil = p * l * t
    return p * l * t

def prisma (alas, tinggi_segitiga, tinggi_prisma):
    luas_alas = 0.5 * alas * tinggi_segitiga
    hasil = luas_alas * tinggi_prisma
    return hasil

def tabung (jari_jari, tinggi_tabung):
    luas_alas = 3.14 * jari_jari ** 2
    hasil = luas_alas * tinggi_tabung
    return hasil

def kerucut (jari_jari, tinggi_kerucut) :
    luas_alas = 1/3 * 3.14 * jari_jari ** 2
    hasil = luas_alas * tinggi_kerucut
    return hasil

print(kerucut(6,8))
