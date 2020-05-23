import hashlib




def readInChunks(fileObj):
    while True:
        data = fileObj.readline()
        heshad_country = hashlib.md5(data.encode()).hexdigest()
        yield heshad_country, data
        if not data:
            break
        yield heshad_country, data


f = open('country.txt', encoding='utf-8')
for chuck, m in readInChunks(f):
    print(f'Строка {m}Хеш {chuck} \n')
f.close()