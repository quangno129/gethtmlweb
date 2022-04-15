import requests

URL = 'https://dems.spsvietnam.vn:8443/dems/displayManageSchedule.action'
LOGIN_URL = 'https://dems.spsvietnam.vn:8443/dems/logout.action'

session = requests.session()

login_data = {
              'username': 'lvnguyen_1',
              'password': 'Sunday@1995!'}
session.post(LOGIN_URL, data=login_data)

req = session.get(URL)
print req.content