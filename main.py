import requests


boundary = "----WebKitFormBoundaryRgzhOYLxkUVQut0Z"

# Données du formulaire
pay = (
    f"--{boundary}\r\n"
    "Content-Disposition: form-data; name=\"action\"\r\n\r\n"
    "search_programs\r\n"
    f"--{boundary}\r\n"
    "Content-Disposition: form-data; name=\"addresses\"\r\n\r\n"
    "[]\r\n"
    f"--{boundary}\r\n"
    "Content-Disposition: form-data; name=\"types\"\r\n\r\n"
    "[]\r\n"
    f"--{boundary}\r\n"
    "Content-Disposition: form-data; name=\"rooms\"\r\n\r\n"
    "[]\r\n"
    f"--{boundary}\r\n"
    "Content-Disposition: form-data; name=\"price\"\r\n\r\n"
    "\r\n"
    f"--{boundary}\r\n"
    "Content-Disposition: form-data; name=\"dispositifs\"\r\n\r\n"
    "[]\r\n"
    f"--{boundary}\r\n"
    "Content-Disposition: form-data; name=\"department\"\r\n\r\n"
    "\r\n"
    f"--{boundary}\r\n"
    "Content-Disposition: form-data; name=\"city\"\r\n\r\n"
    "\r\n"
    f"--{boundary}\r\n"
    "Content-Disposition: form-data; name=\"status\"\r\n\r\n"
    "\r\n"
    f"--{boundary}\r\n"
    "Content-Disposition: form-data; name=\"avantPremiere\"\r\n\r\n"
    "false\r\n"
    f"--{boundary}\r\n"
    "Content-Disposition: form-data; name=\"commercialisation\"\r\n\r\n"
    "false\r\n"
    f"--{boundary}\r\n"
    "Content-Disposition: form-data; name=\"travauxEnCours\"\r\n\r\n"
    "false\r\n"
    f"--{boundary}\r\n"
    "Content-Disposition: form-data; name=\"livraisonImmediate\"\r\n\r\n"
    "false\r\n"
    f"--{boundary}\r\n"
    "Content-Disposition: form-data; name=\"offers\"\r\n\r\n"
    "false\r\n"
    f"--{boundary}\r\n"
    "Content-Disposition: form-data; name=\"offer\"\r\n\r\n"
    "\r\n"
    f"--{boundary}--\r\n"
)


payload = {
    "action": "search_programs",
    "addresses": [],
    "types": [],
    "rooms": [],
    "price": "",
    "dispositifs": [],
    "department": "",
    "city": "",
    "status": "",
    "avantPremiere": False,
    "commercialisation": False,
    "travauxEnCours": False,
    "livraisonImmediate": False,
    "offers": False,
    "offer": ""
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'fr',
    'Content-Length': str(len(pay)),
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryRgzhOYLxkUVQut0Z',
    'Cookie': 'i18next=fr',
    'Dnt': '1',
    'Origin': 'https://www.lesnouveauxconstructeurs.fr',
    'Referer': 'https://www.lesnouveauxconstructeurs.fr/immobilier-neuf/',
    'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"macOS"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}


def webhook_send(url_image, name, lieu, permalink):
    url_image = url_image
    data = {
        "embeds": [
        {
            "type": "rich",
            "description": lieu,
            "color": 0x00ff00,
            "image": {
                "url": url_image
                },
            "author": {
                "name": name,
                "url": permalink,
                "icon_url": "https://www.lesnouveauxconstructeurs.fr/wp-content/uploads/2018/07/logo.png"
                },
            }]
    }

    requests.post("https://discord.com/api/webhooks/1219561496229580801/z9P6owVHEW77gLBoNxucRJzOo5h9JAjtZAzQgdhqj6pg0t9sEkZdyLiqLps4TFnk3ScH", json=data)

data = requests.post('https://www.lesnouveauxconstructeurs.fr/wp-admin/admin-ajax.php', headers=headers, data=pay).json()

for i in range(0, len(data)):
    url_image = data[i]['_source']['image']
    name = data[i]['_source']['name']
    lieu = data[i]['_source']['address'][0] + " • " + data[i]['_source']['address'][1] + " • " + data[i]['_source']['address'][2] + " • " + data[i]['_source']['address'][3]
    permalink = data[i]['_source']['permalink']
    webhook_send(url_image, name, lieu, permalink)
    print("Webhook" + str(i) + "sent : code 200")



Webhook = "https://discord.com/api/webhooks/1219561496229580801/z9P6owVHEW77gLBoNxucRJzOo5h9JAjtZAzQgdhqj6pg0t9sEkZdyLiqLps4TFnk3ScH"