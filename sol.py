from base64 import b64decode

if __name__ == '__main__':
    secret = 'aWFuZ25vVzpOQU06RU5JTDp0YTpzdTpuaW9K'
    ans = b64decode(secret).decode('utf-8')[::-1]
    print(f'The answer is "{ans}"')