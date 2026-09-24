import re

txt = input("Enter a String :")
res = re.findall(r'[a-z A-Z 0-9]',txt)
print(res)
