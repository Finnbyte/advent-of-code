import hashlib

key = "yzbqklnj"
ans = 0
while True:
    full_key = f"{key}{ans}".encode()
    if hashlib.md5(full_key).hexdigest().startswith("00000"):
        print(ans)
        break
    ans += 1
