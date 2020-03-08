import requests, json, socket
host = input('Please enter an ip or host: ')
ip_addr = socket.gethostbyname(host)
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
fields = (
    ("Status", "status"),
    ("Continent", "continent"),
    ("Continent Code", "continentCode"),
    ("Country", "country"),
    ("Country Code", "countryCode"),
    ("Region", "region"),
    ("Region Name", "regionName"),
    ("City", "city"),
    ("District", "district"),
    ("Zipcode", "zip"),
    ("Latitude", "lat"),
    ("Longitude", "lon"),
    ("Timezone", "timezone"),
    ("Currency", "currency"),
    ("ISP", "isp"),
    ("Organization", "org"),
    ("AS", "as"),
    ("AS Name", "asname"),
    ("Reverse DNS", "reverse"),
    ("Mobile", "mobile"),
    ("Proxy", "proxy"),
    ("Hosting", "hosting"),
    ("IP", "query"),
)
req = requests.get(f'http://ip-api.com/json/{ip_addr}?fields={",".join([key for _, key in fields])}', headers=headers).json()
final_formatting = "\n".join([f"{title}: {{{key}}}" for title, key in fields]).format(**req)
print(final_formatting)
