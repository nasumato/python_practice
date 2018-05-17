while True:
    print('年齢を入力してください（英数字のみ）:')
    age=input()
    if age.isalnum():
        break
    print('年齢は数字で数字で入力してください')

while True:
    print('新しいパスワードを入力してください（英数字のみ）:')
    password = input()
    if password.isalnum():
        break
    print('パスワードは英数字で入力してください')