import itertools
from subprocess import check_output

passfound = False
for i in range(4):
    g = itertools.product('qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*+-*/', repeat=1)

    for password in g:
        try:
            check_output(r'"C:\Program Files\WinRAR\UnRAR.exe" x  "D:\pass.rar" -p'
                         + ''.join(password), shell=True)

            print("Pass i found : " + ''.join(password))
            passfound = True
            break
        except:
            print("Trying " + ''.join(password))
            continue
    if passfound:
        break

