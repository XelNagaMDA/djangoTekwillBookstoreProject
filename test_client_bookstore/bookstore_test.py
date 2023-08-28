import requests

url = 'http://127.0.0.1:8000/'


register_user_url = url + '/register/'


response = requests.post(
    register_user_url,
    data={
        'username': 'victort',
        'password': 'aaaaaa'
    }
)

# verificam la consola cum a fost efectuat raspunsul cu succes sau nu
print(response.status_code)
