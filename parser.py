import requests
from bs4 import BeautifulSoup
import xlsxwriter
from urllib.parse import urljoin

def clean_html(element):
    return ''.join(element.stripped_strings)

def steal_and_write_to_excel(links):
    all_data = []
    columns = {}

    for link in links:
        dict_attrs = {}

        r = requests.get(link)
        soup = BeautifulSoup(r.content, 'lxml')

        # Извлечение названия продукта
        name_tag = soup.find('h1')
        if name_tag:
            dict_attrs['Наименование'] = name_tag.text.strip()

        # Извлечение данных таблицы
        table_rows = soup.find_all('tr')
        for row in table_rows:
            cells = row.find_all(['th', 'td'])
            if len(cells) == 2:
                key, value = cells
                key_text = key.text.strip()
                if key_text not in columns:
                    columns[key_text] = len(columns) + 1
                dict_attrs[key_text] = clean_html(value)

        # Извлечение и обработка изображений
        images = soup.find_all('img')
        if images and len(images) >= 4:
            preview_img_url = images[3].get('src')
            if preview_img_url:
                dict_attrs['Превью'] = urljoin(link, preview_img_url)

        images_urls = [urljoin(link, img.get('src')) for img in images if img.get('src')]
        dict_attrs['Картинки'] = ', '.join(images_urls)

        # Извлечение и обработка описания
        description_parts = []
        h3_tags = soup.find_all('h3')
        p_tags = soup.find_all('p', class_="text-justify text-justify-not-xs")
        for h3, p in zip(h3_tags, p_tags):
            combined_text = f"{h3.text.strip()}: {clean_html(p)}"
            description_parts.append(combined_text)
        if description_parts:
            dict_attrs['Описание'] = ' | '.join(description_parts)

        all_data.append(dict_attrs)

    # Запись данных в Excel
    workbook = xlsxwriter.Workbook('forintek.xlsx')
    worksheet = workbook.add_worksheet()

    # Определение и запись заголовков столбцов
    for col_num, header in enumerate(['Наименование', 'Превью', 'Картинки', 'Описание', 'link'] + list(columns.keys())):
        worksheet.write(0, col_num, header)

    # Запись данных
    for row_num, data in enumerate(all_data, start=1):
        for col_num, key in enumerate(['Наименование', 'Превью', 'Картинки', 'Описание', 'link'] + list(columns.keys())):
            value = data.get(key, '')
            worksheet.write(row_num, col_num, value)

    workbook.close()





# Пример использования
links = ['https://forintek.ru/catalog/printer-etiketok-snbc-btp-6300i-plus/',
         'https://forintek.ru/catalog/printer-etiketok-snbc-btp-7400/',
         'https://forintek.ru/catalog/printer-etiketok-snbc-btp-4300e/',
         'https://forintek.ru/catalog/printer-etiketok-novexx-xtp-804/',
         'https://forintek.ru/catalog/printer-etiketok-averydennison-adtp2-ecocut/',
         'https://forintek.ru/catalog/termotransfernyy-printer-savema-svm-32/',
         'https://forintek.ru/catalog/termotransfernyy-printer-savema-svm-53/',
         'https://forintek.ru/catalog/termotransfernyy-printer-savema-svm-107/',
         'https://forintek.ru/catalog/termotransfernyy-printer-savema-svm-128/',
         'https://forintek.ru/catalog/printer-etiketok-novexx-xlp-51x/',
         'https://forintek.ru/catalog/printer-etiketok-novexx-xlp-60x/',
         'https://forintek.ru/catalog/printer-etiketok-novexx-64-0x/',
         'https://forintek.ru/catalog/printer-etiketok-novexx-xtp-804/',
         'https://forintek.ru/catalog/termotransfernyy-printer-coditherm-i-roller/',
         'https://forintek.ru/catalog/termotransfernyy-printer-coditherm-h-pad/',
         'https://forintek.ru/catalog/tekstilnyy-printer-averydennison-snap-500/',
         'https://forintek.ru/catalog/tekstilnyy-printer-averydennison-snap-700/',
         'https://forintek.ru/catalog/printer-etiketok-averydennison-adtp2-ecocut/']



steal_and_write_to_excel(links)
