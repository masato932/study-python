# test_str = 'python-izm'
# print(test_str.replace('izm', 'ism'))
# test_str = 'python-izm'
# print(test_str.split('-'))
# test_str = '1234'
# print(test_str.rjust(8, '0'))
# print(test_str.rjust(8, '!'))
# test_str = '1234'
# print(test_str.zfill(8))
# print(test_str.zfill(2))

# test_str = 'python-izm'
# print(test_str.startswith('python'))
# print(test_str.startswith('izm'))

# test_str = 'python-izm'
# print('p' in test_str)
# print('e' in test_str)

# test_str = 'Python-Izm.Com'
# print(test_str.upper())
# print(test_str.lower())

print('----------------------------------')
test_str = '     python-izm.com'
print(test_str)
test_str = test_str.lstrip()
print(test_str)
test_str = test_str.lstrip('python')
print(test_str)

print('----------------------------------')
test_str = 'python-izm.com     '
print(test_str + '/')
test_str = test_str.rstrip()
print(test_str + '/')
test_str = test_str.rstrip("com")
print(test_str)