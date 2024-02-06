import requests
from urllib.parse import urlencode

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 填入cookie
    'Cookie': '',
    'Host': 'public.ecustpt.eu.org',
    'Origin': 'public.ecustpt.eu.org',
    'Sec-Ch-Ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    'X-Requested-With': 'XMLHttpRequest'
}

data = {'id': ''}  # 初始化数据字典，键为'id'

# 遍历ID范围
for i in range(4737, 4700, -1):  # 从4737递减到4701（包括4701）
    data['id'] = str(i)  # 更新'id'值
    response = requests.post('https://public.ecustpt.eu.org/thanks.php', headers=headers, data=data)

    # 检查响应状态码，确保请求成功
    if response.status_code == 200:
        print(f"成功发送{i}的POST请求")  # 使用f-string将变量i插入字符串中
    else:
        print(f"发送{i}的POST请求失败，状态码：{response.status_code}")