# Задание:
# https://i.gyazo.com/6ada8d1e4c25a0602c6c127b64929936.png

# Решение:
def get_domain_name(url):
    if "www" in url:
        return url[url.find(".")+1:url.rfind(".")]
    else:
        return url[url.find("/")+2:url.find(".")]
# код ниже не стоит удалять, он нужен для проверки
assert get_domain_name("http://google.com") == "google"
assert get_domain_name("http://google.co.jp") == "google"
assert get_domain_name("www.xakep.ru") == "xakep"
assert get_domain_name("https://youtube.com") == "youtube"

assert get_domain_name("http://github.com/carbonfive/raygun") =='github'
assert get_domain_name("http://www.zombie-bites.com") == 'zombie-bites'
assert get_domain_name("https://www.siemens.com") == 'siemens'
assert get_domain_name("https://www.whatsapp.com") == 'whatsapp'
assert get_domain_name("https://www.mywww.com") == 'mywww'
print('Проверки пройдены')

# Альтернатива (not_mine):
# def domain_name(url:str) -> str:
#     url = url.replace("http://", "").replace("https://", "").replace("www.", "")
#     return url.split('.')[0]