import requests
from bs4 import BeautifulSoup
import xlsxwriter
from urllib.parse import urljoin

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


def get_sitemap_urls(sitemap_url, depth=0):
    if depth > 5:
        return []

    urls = []
    try:
        response = requests.get(sitemap_url, headers=HEADERS)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.content, 'xml')
        sitemap_tags = soup.find_all("sitemap")

        if not sitemap_tags:
            url_tags = soup.find_all("url")
            urls = [url.loc.text for url in url_tags]
        else:
            for sitemap in sitemap_tags:
                sitemap_url = sitemap.findNext("loc").text
                urls.extend(get_sitemap_urls(sitemap_url, depth + 1))

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе к {sitemap_url}: {e}")

    return urls


def count_pages_and_write_to_excel(links):
    data = []

    for link in links:
        sitemap_url = link.rstrip('/') + '/sitemap.xml'
        urls = get_sitemap_urls(sitemap_url)
        domain = link.split("//")[-1].rstrip('/')

        catalog_count = sum(1 for url in urls if "/catalog/" in url)
        services_count = sum(1 for url in urls if "/services/" in url)

        # Извлечение содержимого тега h1
        h1_content = ""
        try:
            response = requests.get(link, headers=HEADERS)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                h1_tag = soup.find('h1')
                if h1_tag:
                    h1_content = h1_tag.text.strip()
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе к {link}: {e}")

        data.append({'domain': domain, 'page_count': len(urls), 'catalog_count': catalog_count,
                     'services_count': services_count, 'h1': h1_content})

    workbook = xlsxwriter.Workbook('website_page_counts.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', 'Домен')
    worksheet.write('B1', 'Количество страниц')
    worksheet.write('C1', 'Количество страниц каталога')
    worksheet.write('D1', 'Количество страниц услуг')
    worksheet.write('E1', 'H1 тег главной страницы')

    for row_num, entry in enumerate(data, start=2):
        worksheet.write(row_num, 0, entry['domain'])
        worksheet.write(row_num, 1, entry['page_count'])
        worksheet.write(row_num, 2, entry['catalog_count'])
        worksheet.write(row_num, 3, entry['services_count'])
        worksheet.write(row_num, 4, entry['h1'])

    workbook.close()


# Пример использования
links = [
"https://prom-mact.ru/",
"https://meridiant.ru/",
"https://vekas-automation.ru/",
"https://alfacont.ru/",
"https://weilandt-elektronik.ru/",
"https://antaresvision.su/",
"https://trekmark.ru/",
"https://crpt.ru/",
"https://inautomatic.ru/",
"https://gk-mact.ru/",
"http://xn----7sbanjtasdtlb1czat0i.xn--p1ai/",
"https://kontur.ru/rekvizity",
"https://www.1cbit.ru/",
"https://diar-mark.ru/kontakty/",
"https://ray.ooo/",
"https://chmark.ru/",
"https://insoftretail.ru/",
"https://www.motrum.ru/",
"https://okto.ru/",
"https://utrace.ru/",
"https://www.markprom.ru/",
"https://rbsgr.ru/",
"https://it-klaster.com/",
"https://tehnogrupp.com/",
"https://id-russia.ru/",
"https://tensor.ru/",
"https://center-inform.ru/",
"https://www.alco-dec.ru/",
"https://euroconveyor-st.ru/",
"https://okzo-ost.ru/",
"https://kran-dt.ru/",
"https://www.conveyery.ru/",
"https://gkmash.ru/",
"https://zavod-conveyer.ru/",
"https://konveyery.ru/",
"https://moskva.satom.ru/",
"https://ipc2u.ru/",
"https://empc.ru/",
"https://nnz-ipc.ru/",
"https://prom-pc.ru/",
"https://aveon.ru/",
"https://hmru.ru/",
"https://xn--b1afbatd0c9b3b.xn--p1ai/",
"https://kdm-trading.ru/",
"https://faspack.ru/",
"https://modul-ves.ru/",
"https://aspromservis.ru/",
"https://www.vitec.ru/",
"https://optimusdrive.ru/",
"https://visionmachines.ru/",
"https://promfort.com/",
"https://sensotek.ru/",
"https://hikrobot.mallenom.ru/",
"https://www.chipdip.ru/",
"https://rusautomation.ru/",
"https://sensoren.ru/",
"https://cnc360.ru/",
"https://elrus.ru/",
"https://markjet.ru/",
"https://rbs-id.ru/",
"https://packsyst.ru/",
"https://www.profiprint.ru/",
"https://print-apply.ru/",
"https://inox-drive.ru/",
"https://www.pack-euro.ru/",
"https://oborud-m.ru/",
"https://vegatm.ru/",
"https://stan-upakovka.ru/",
"https://postpromteh.ru/",
"https://shtrih-center.ru/",
"https://upakovka-markirovka.ru/",
"https://www.labelprinter.ru/",
"https://labelpack.ru/",
"https://interid.ru/",
"https://smartcode.ru/",
"https://standartpak.ru/"
]
count_pages_and_write_to_excel(links)