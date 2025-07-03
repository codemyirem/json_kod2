import requests
import csv

url = 'https://sch.sachane.com/product.json'
response = requests.get(url)
data = response.json()

headers = ['main_url', 'default_code', 'sch_id', 'status', 'g_category', 'large_image', 'small_image', 'medium_image', 'product', 'categories']

with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=headers)
    csv_writer.writeheader()

    # data['data'] listesini döneceğiz
    for item in data['data']:
        csv_writer.writerow({
            'main_url': item.get('main_url', ''),
            'default_code': item.get('default_code', ''),
            'sch_id': item.get('sch_id', ''),
            'status': item.get('status', ''),
            'g_category': item.get('g_category', ''),
            'large_image': item.get('large_image', ''),
            'small_image': item.get('small_image', ''),
            'medium_image': item.get('medium_image', ''),
            'product': item.get('product', ''),
            'categories': ', '.join(item.get('categories', []))
        })

print("CSV dosyasına dönüştürme işlemi tamamlandı!")


             
     
