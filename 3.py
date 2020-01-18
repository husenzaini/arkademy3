def cek_kata(sebuahkata):
    if type(sebuahkata) != str:
        return "harus string"

    kata2 = sebuahkata.split()

    jumlah = 0
    for i in (kata2):
        if i.isalpha():
            jumlah = jumlah + 1
    return str(jumlah) + "/" + str(len(kata2))


print(cek_kata("ini adalah sebuah kata"))
print(cek_kata("2 pasang sandal hilang"))
print(cek_kata(234))
