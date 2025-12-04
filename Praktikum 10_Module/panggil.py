import BangunRuang as br 
import BangunDatar as bd

print("-----bangun ruang-----")
print(f"volume kubus dengan sisi 3 adalah {br.kubus(3)}")
print(f"volume balok adalah {br.balok(4,6,8)}")
print(f"volume prisma segitiga adalah {br.prisma(6,8,10)}")
print(f"volume kerucut adalah {br.kerucut(6,8)}")

print("----bangun datar-----")
print(f"luas persegi adalah {bd.persegi(5)}")
print(f"luas pesergi panjang adalah {bd.pesergi_panjang(2,8)}")
print(f"luas segitiga adalah {bd.segitiga(5,8)}")
print(f"luas lingkaran adalah {bd.lingkaran(21)}")
print(f"luas jajar genjang adalah {bd.jajargenjang(10,15)}")