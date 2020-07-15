import requests
response = requests.get('http://www.reddit.com/r/programming/')
print (response.status_code)  # 200 significa requisição OK