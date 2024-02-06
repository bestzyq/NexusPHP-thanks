import aiohttp
import asyncio

headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 填入cookie
    'Cookie': '',
    'Host': 'hudbt.hust.edu.cn',
    'Origin': 'hudbt.hust.edu.cn',
    'Sec-Ch-Ua': '"Not A(Brand";v="99", "Microsoft Edge";v="121", "Chromium";v="121"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0',
    'X-Requested-With': 'XMLHttpRequest'
}

async def send_post_request(session, url, data):
    async with session.post(url, headers=headers, data=data) as response:
        return await response.text(), response.status
    
# 起始和结束值，start_value必须大于end_value
start_value = 3000
end_value = 1

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(start_value, end_value - 1, -1):  # 注意：range不包含结束值，所以这里是end_value - 1
            data = {'id': str(i)}
            task = asyncio.ensure_future(send_post_request(session, 'https://hudbt.hust.edu.cn/thanks.php', data))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        for response_text, status_code in zip(responses, range(start_value, end_value - 1, -1)):
            if status_code == 200:
                print(f"成功发送{i}的POST请求")
            else:
                print(f"发送{i}的POST请求失败，状态码：{status_code}")

asyncio.run(main())