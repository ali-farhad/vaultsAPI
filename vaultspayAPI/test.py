import requests

url = "https://vaultspay.com/api/v1/get-default-wallet-balance?user_id=12"

payload = {}
headers = {
  'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI3IiwianRpIjoiYjM1MzM0OThmNTZkNDA2ZjlhYTUwMWQ3MGRkYjQwNjk5MDYzZDk4NWQ2YjAxNTI4ZjM1MDAzMzk3NzY2NTc3ZDVhMzhlNmZkNTg3NTZkMzIiLCJpYXQiOjE2MDM3MTkwNjEsIm5iZiI6MTYwMzcxOTA2MSwiZXhwIjoxNjE5NDQzODYwLCJzdWIiOiIxMyIsInNjb3BlcyI6W119.GgNv9bk6vzoDFxQzrLMiuww33TTNw2EeZv3fzV2LsoqStldAtXTQ5M1aGb1nWAYs_QPeMVA5Ni55j6qkCJoaU45lY2Q-dOfDatTLtlOvD50D0tdzIFfKLDhhBQxQtA2u9-wk5-IkkJgkV_OfeEpv2u839uVznJaOu6JVT2TnX787SDBqm9IJ7ElTi5u0Pv1jUt6Tf0aTFg28OzKtjpVxfvCpSQCF_SDqWd8UlBigkXhoeByeQm9eLN01xkuZMdj5n59kjQnC_YSDmrMZip4Dl6ljhMldsMZ-FTpB0Huwt5z1GDMIMKiQ8vQH-eeKJ7Rn9H-xPKIKzoqkCx3C0X_HdQqmztqKVhVy22GKuF3uIHdg7MBOZxgajounVI1vXWFeKO8OoMnKDtpoPkFmTXbfkAshYXPHdW-gFiWbk6OyUaOkha5LYe6vu73cZ9MTEeUQrc6IGt0gRCaAOoeFgSh-VG0mRsijwKgxOPk_HwF7VeD1dJdKTIsplfTdqe0RtTMjBMviLndyLZCi8rC2LCiXB8_6fKqkNdRvdGwOsXL9uyuOnRYHPPWc8qEumNXNjE5zWToxvYPo8v7a529sZOPhwk6nNL2-dbyi0mYH7Uc0yMo-Xa4vp5N8QLkRdJncr8qvUv3yFdtD1t_x3UvQOkjk5jtZH6Oti6PVbN6xQwIIxMU'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))