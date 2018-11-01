from password import Password

def add_password(account,username,password):
    new_pass = Password(account,username,password)
    new_pass.save_pass()

add_password("df","df","dff")
for password in Password.passwords:
    print (password.account)