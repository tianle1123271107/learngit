# Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。
# 什么是摘要算法呢？摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。
#
# 举个例子，你写了一篇文章，内容是一个字符串'how to use python hashlib - by Michael'，并附上这篇文章的摘要是'2d73d4f15c0db7f5ecb321b6a65e5d6d'。
# 如果有人篡改了你的文章，并发表为'how to use python hashlib - by Bob'，你可以一下子指出Bob篡改了你的文章，
# 因为根据'how to use python hashlib - by Bob'计算出的摘要不同于原始文章的摘要。

# 可见，摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest(得到的密文)，目的是为了发现原始数据是否被人篡改过。


# 我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值：
# import hashlib
#
# md5=hashlib.md5()
# md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print(md5.hexdigest())
# 如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：

# import hashlib
#
# md5 = hashlib.md5()
# md5.update('how to use md5 in '.encode('utf-8'))
# md5.update('yython hashlib?'. encode('utf-8'))
# print(md5.hexdigest())

# MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。


# 另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：
# import hashlib
# sha1=hashlib.sha1()
# sha1.update('how to use md5 in python hashlib?'.encode('utf-8'))
# print(sha1.hexdigest())
#
# import hashlib
# sha1 = hashlib.sha1()
# sha1.update('how to use md5 in '.encode('utf-8'))
# sha1.update('python hashlib?'.encode('utf-8'))
# print(sha1.hexdigest())

# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要(得到的密文)长度更长。

# 有没有可能两个不同的数据通过某个摘要算法得到了相同的摘要？完全有可能，因为任何摘要算法都是把无限多的数据集合映射到一个有限的集合中。这种情况称为碰撞，
# 比如Bob试图根据你的摘要反推出一篇文章'how to learn hashlib in python - by Bob'，
# 并且这篇文章的摘要恰好和你的文章完全一致，这种情况也并非不可能出现，但是非常非常困难。

# 摘要算法应用
# 任何允许用户登录的网站都会存储用户登录的用户名和口令。如何存储用户名和口令呢？方法是存到数据库表中：
# name	password
# michael	123456
# bob	abc999
# alice	alice2008
# 如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。此外，网站运维人员是可以访问数据库的，也就是能获取到所有用户的口令。
# 正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5：
# username	password
# michael	e10adc3949ba59abbe56e057f20f883e
# bob	878ef96e86145580c38c87f0410ad153
# alice	99b1c2188db85afee403b1536010c2c9
# 当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正确，如果不一致，口令肯定错误。


#第一题：根据用户输入的口令，计算出存储在数据库中的MD5口令：


import hashlib
# def calc_md5(password):
#     md5=hashlib.md5()
#     md5.update(password.encode('utf-8'))
#     # print(md5.hexdigest())
#     return md5.hexdigest()
# # print(calc_md5('123456'))

# 存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。
# 第二题：设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：

# db1 = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }
# def login(user, password):
#     list_key=list(db.keys())#把取到的user用户放到一个列表里面，并赋值给一个变量
#     if user in list_key:  #r如果是这个列表中的user
#         password_md5_value=calc_md5(password)#把用户输入的密码变成摘要密文
#         if password_md5_value==db[user]:#如果输入的明文密码变成密文后和数据库中存在的一样 则通过
#             return True
#         else:
#             print('密码输入错误，请重新输入')
#     else:
#         print('你输入的用户不正确，请进行检查或注册')
# '''检查'''
# user='michael'
# password='123456'
# print(login(user,password))  #先判断数据改user是否存在数据库中，如果没在 直接提示  用户名不存在   用户名存在的情况下，  2 把用户输入的密码进行加密，再判断这个密文和数据库中存在的密文是否一直
                            #如果一致，则通过  如果不一致  则提示密码错误

# 采用MD5存储口令是否就一定安全呢？也不一定。假设你是一个黑客，已经拿到了存储MD5口令的数据库，如何通过MD5反推用户的明文口令呢？暴力破解费事费力，真正的黑客不会这么干。
# 考虑这么个情况，很多用户喜欢用123456，888888，password这些简单的口令，于是，黑客可以事先计算出这些常用口令的MD5值，得到一个反推表：

# 'e10adc3949ba59abbe56e057f20f883e': '123456'
# '21218cca77804d2ba1922c33e0151105': '888888'
# '5f4dcc3b5aa765d61d8327deb882cf99': 'password'
# 这样，无需破解，只需要对比数据库的MD5，黑客就获得了使用常用口令的用户账号。
# 对于用户来讲，当然不要使用过于简单的口令。但是，我们能否在程序设计上对简单口令加强保护呢？

# 由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：
# import hashlib
# def calc_md6(password):
#     md5=hashlib.md5()
#     md5.update(password.encode('utf-8'))
#     # print(md5.hexdigest())
#     return md5.hexdigest()
# # 经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。
# password='123456'
# print(calc_md6(password))

# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：


# 如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。
#####看不懂
# import hashlib,random
#
# def get_md5(s):
#     return hashlib.md5().update(s.encode('utf-8')).hexdigest()
#
# class User(object):
#     def __init__(self,username,password):
#         self.username=username
#         self.salt=''.join([chr(random.randint(48, 122)) for i in range(20)])
#         self.password=password
#
# db = {
#     'michael': User('michael', '123456'),
#     'bob': User('bob', 'abc999'),
#     'alice': User('alice', 'alice2008')
# }
# def register(username, password):
#     db[username]=User(username,password)
#     return True
#
#
# def login(username, password):
#     User=db[username]

# 摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。
import hashlib,random
def get_md5(s):#定义将输入的密码转变成MD5摘要的函数
    return hashlib.md5(s.encode('utf-8')).hexdigest()
db3 = {}#定义一个空的字典
def register(username, password):#这个函数是为了计算当用户注册时，输入的账号密码，然后将密码变成密文  加入到db中，存储在数据库中
    db3[username] = get_md5(password + username + 'the-Salt')
username='tianle'
password='123456'
print(register(username, password))
print(db3)
# 然后，根据修改后的MD5算法实现用户登录的验证：


import hashlib,random
def get_md6(s):#定义将输入的密码转变成MD5摘要的函数
    return hashlib.md5(s.encode('utf-8')).hexdigest()
class User(object):#定义一个类 ，定义类的属性
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
db = {
    'michael': User('michael', '123456'),  #前面是User.username   后面的是User.password
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}
def login(username, password):
    user=db[username]#这里定义的user就是User的实例对象，User('michael', '123456')
    return user.password==get_md5(password + user.salt)#这里加的盐就是通过把输入的密码和User的salt属性拼接    设置的用户名的密码绑定对应的md5密文就是加盐
# print(login('michael','123456'
