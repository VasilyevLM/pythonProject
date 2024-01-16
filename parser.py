from bs4 import BeautifulSoup
import requests
import xlsxwriter
import re

# class Competitors:
#     def __init__(self, site, sitemap, name, sitemap_url):
#         self.name = name
#         self.site = site
#         self.sitemap = sitemap
#         self.sitemap_url = sitemap_url


domain = 'https://forintek.ru/catalog/printer-etiketok-snbc-btp-7400/'
# sitemap = 'sitemap.xml'

sitemap_url = domain
r = requests.get(sitemap_url)
# print(r.status_code)
# print(r.text)
soup = BeautifulSoup(r.text, 'lxml')

a = soup.find_all('h1')
# print(a)
xml_list = []

for i in a:
    xml_list.append(i.text)
    print(i)

# b = soup.find_all('td', class_='font-weight-bold')
c = soup.find_all('td')

attrs = []
counter = 1

# for i in b:
#     attrs[f'parameter{counter}'] = i.text
#     counter += 1
#     print(i)

for i in c:
    attrs.append(i.text)
    print(i.text)




workbook = xlsxwriter.Workbook('forintek.xlsx')
worksheet = workbook.add_worksheet()
for i in range(10):
    for j in range(5):
        worksheet.write(i, j, i+j)
workbook.close()






# print(xml_list)
#
# for i in xml_list:
#     print(i)
#     try:
#         b = requests.get(i)
#         soup1 = BeautifulSoup(b.text, 'lxml')
#         h1 = soup1.find('h3')
#         print(h1.text)
#         with open('h1.txt', mode='a', encoding='utf-8') as file:
#             file.write(f'{h1.text}\n{i}\n')
#
#     except Exception as err:
#         print(err)



























# url = 'https://meridiant.ru/'
#
# sitemap = 'sitemap.xml'
# sitemap_list = list()
#
# sitemap_url = requests.get(url + sitemap)
# print(sitemap_url)
# sitemap_list.append(sitemap_url)
# print(sitemap_list)
#
# page_html = BeautifulSoup(sitemap.content, 'lxml')
# print(page_html)


# competitors = {
# 'Меридиан':	'https://meridiant.ru/',
# 'Векас': 'https://vekas-automation.ru/',
# 'Тензор': 'https://alfacont.ru/',
# 'Вайландт': 'https://weilandt-elektronik.ru/',
# 'Антарес':	'https://antaresvision.su/',
# 'Трекмарк':	'https://trekmark.ru/',
# 'Оператор ЦРПТ':	'https://crpt.ru/',
# 'Инавтоматика':	'https://inautomatic.ru/',
# 'Альфа технологии': 'http://xn----7sbanjtasdtlb1czat0i.xn--p1ai/',
# 'Контур': 'https://kontur.ru/',
# 'Первый бит': 'https://www.1cbit.ru/',
# 'Эксель': 'https://diar-mark.ru/',
# 'РЭЙ': 'https://chmark.ru/',
# 'ИнСофтРитейл':	'https://insoftretail.ru/',
# 'Мотрум': 'https://www.motrum.ru/',
# 'ОКТО':	'https://okto.ru/',
# 'Ютрейс':	'https://utrace.ru/',
# 'Промышленная маркировка':	'https://www.markprom.ru/',
# # ООО "РБС-Групп"	https://rbsgr.ru/
# # ООО "ИТ-Кластер"	https://it-klaster.com/
# # ООО "Техно Групп"	https://tehnogrupp.com/
# # ООО "ИД Раша"	https://id-russia.ru/
# # ООО "Компания "Тензор" 	https://tensor.ru/
# # АО "Центроинформ"	https://center-inform.ru/
# # ООО "Алкософттрейд"	https://www.alco-dec.ru/
# # Евроконвейер	https://euroconveyor-st.ru/
# # Окзо Ост	https://okzo-ost.ru/
# # КранДеталь	https://kran-dt.ru/
# # ГК "ПОРТ"	https://www.conveyery.ru/
# # Ярославский конвейер	https://gkmash.ru/
# # ООО «ТРАЯНА»	https://zavod-conveyer.ru/
# # OOO "СТиЛ" 	https://konveyery.ru/
# # Satom.ru, ИП Томащик Галина Васильевна	https://moskva.satom.ru/
# # IPC2U	https://ipc2u.ru/
# # ООО «Встраиваемые Системы»	https://empc.ru/
# # Ниеншанц-Автоматика	https://nnz-ipc.ru/
# # ГК "Пром-ПК"	https://prom-pc.ru/
# #  IPC2U	https://aveon.ru/
# # Hualian Machinery Co., Ltd 	https://hmru.ru/
# # Скейл Энтерпрайз, ООО	https://xn--b1afbatd0c9b3b.xn--p1ai/
# # КДМ Трейдинг	https://kdm-trading.ru/
# # Фаспак	https://faspack.ru/
# # Модуль Веса	https://modul-ves.ru/
# # Аспром	https://aspromservis.ru/
# # ООО "Витэк-Автоматика"	https://www.vitec.ru/
# # Оптимус драйв	https://optimusdrive.ru/
# # IPC2U	https://aveon.ru/
# # ООО Видящие машины \Vision Machines 	https://visionmachines.ru/
# # Промфорт	https://promfort.com/
# # Сенсотек	https://sensotek.ru/
# # Hikrobot	https://hikrobot.mallenom.ru/
# # «ЧИП и ДИП» 	https://www.chipdip.ru/
# # РусАвтоматизация	https://rusautomation.ru/
# # Сенсорен Электро, ООО	https://sensoren.ru/
# #  ООО «Эффективное производство» 	https://cnc360.ru/
# # Элрус	https://elrus.ru/
# # Маркджет	https://markjet.ru/
# # ООО "РБС-Групп" (21 в списке)	https://rbs-id.ru/
# # ООО «Упаковочные Системы»	https://packsyst.ru/
# # Профпринт	https://www.profiprint.ru/
# # ООО Арни-Групп	https://print-apply.ru/
# # ИноксДрайв	https://inox-drive.ru/
# # Европактрейд	https://www.pack-euro.ru/
# # Новые Решения	https://oborud-m.ru/
# # Вега Проект 	https://vegatm.ru/
# # Стэн Холдинг	https://stan-upakovka.ru/
# # ПостПромТех	https://postpromteh.ru/
# # Центр КТ	https://shtrih-center.ru/
# # БристольГрупп	https://upakovka-markirovka.ru/
# # Современные технологии	https://www.labelprinter.ru/
# # ООО «Лейблпак»	https://labelpack.ru/
# # Интер Ай Ди	https://interid.ru/
# # Элайтс	smartcode.ru/
# # СТАНДАРТПАК	https://standartpak.ru/
# }










