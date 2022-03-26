from sys import stdout
for i in range(1,8):
    for j in range(abs(i-4)):
        stdout.write(' ')
    for k in range(7-2*abs(i-4)):
        stdout.write('*')
    print('')
