from ss import d

user_name = input('enter user name')
password = input('enter password')

if (user_name,password) in d.items():
    print('wellcome')
else:
    print('bodo boro')
