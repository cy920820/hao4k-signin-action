import requests
import os
import re

username = os.environ["HAO4K_USERNAME"]
password = os.environ["HAO4K_PASSWORD"]

user_url = "https://www.hao4k.cn/member.php?mod=logging&action=login&phonelogin=no"
base_url = "https://www.hao4k.cn/"
signin_url = "https://www.hao4k.cn/plugin.php?id=k_misign:sign&operation=qiandao&formhash={formhash}&format=empty"
form_data = {
    'formhash': "",
    'referer': "https://www.hao4k.cn/",
    'username': username,
    'password': password,
    'questionid': "0",
    'answer': ""
}
inajax = '&inajax=1'


def run(form_data):
    s = requests.Session()
    user_resp = s.get(user_url)
    login_text = re.findall('action="(.*?)"', user_resp.text)
    for loginhash in login_text:
        if 'loginhash' in loginhash:
            login_url = base_url + loginhash + inajax
            login_url = login_url.replace("amp;", "")
            print(login_url)
    form_text = re.search('formhash=(.*?)\'', user_resp.text)
    print(form_text.group(1))
    form_data['formhash'] = form_text.group(1)
    print(form_data)

    login_resp = s.post(login_url, data=form_data)
    test_resp = s.get('https://www.hao4k.cn/k_misign-sign.html')
    if username in test_resp.text:
        print('login!')
    else:
        return 'login failed!'
    signin_text = re.search('formhash=(.*?)"', test_resp.text)
    signin_resp = s.get(signin_url.format(formhash=signin_text.group(1)))
    test_resp = s.get('https://www.hao4k.cn/k_misign-sign.html')
    if '您的签到排名' in test_resp.text:
        print('signin!')
    else:
        return 'signin failed!'


if __name__ == "__main__":
    signin_log = run(form_data)
    if signin_log is None:
        print('Sign in automatically!')
    else:
        print(signin_log)
