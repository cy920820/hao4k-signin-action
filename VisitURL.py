import requests
import re
import os
import time

requests.packages.urllib3.disable_warnings()
headers = {'Connection': 'close',
           'Cache-Control': 'max-age=0',
           'Upgrade-Insecure-Requests': '1',
           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, sdch',
           'Accept-Language': 'zh-CN,zh;q=0.8',
           }

# 推广链接
sponsoredURL = os.environ["HAO4K_URL"]


def run(validIPs):
    success, fail = 0, 0
    for IP in validIPs:
        proxies = {"http": "http://{proxy}".format(proxy=IP),
                   "https": "https://{proxy}".format(proxy=IP)}
        try:
            r = requests.get(sponsoredURL, headers=headers, proxies=proxies)
        except Exception as e:
            fail += 1
            continue

        if r.status_code == 200:
            time.sleep(1)
            success += 1

    print("访问成功{0}次，访问失败{1}次!!!".format(success, fail))


def getfreeIPs():
    validIPs = set()
    test_url = "https://ip.chinaz.com/"

    while True:
        url = "http://www.66ip.cn/mo.php?sxb=&tqsl=50&port=80&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea="
        r = requests.get(url, headers=headers)
        time.sleep(0.5)
        if r.status_code != 200:
            break
        IPs = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', r.text)

        # 验证IP是否可用
        for IP in IPs:
            proxies = {"http": "http://{proxy}".format(proxy=IP),
                       "https": "https://{proxy}".format(proxy=IP)}

            try:
                req = requests.get(test_url, proxies=proxies, timeout=1.5, verify=False)
                time.sleep(0.2)
            except Exception as e:
                continue

            if re.findall(r'<dd class="fz24">(.*)</dd>', req.text)[0] == IP.split(':')[0]:
                validIPs.add(IP)
        if len(validIPs) >= 5:
            break
    print(validIPs)
    return list(validIPs)


if __name__ == '__main__':
    validIPs = getfreeIPs()
    run(validIPs)
