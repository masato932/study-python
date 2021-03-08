# import os
# print(os.getcwd())

# ch_path = './dir1'
# os.chdir(ch_path)
# print(os.getcwd())
# ch_path = '../'
# os.chdir(ch_path)
# print(os.getcwd())

# # root_path = '.'
# # print(os.listdir(root_path))

# root_path = '.'
# for file in os.scandir(root_path):
# 	print(file)
# 	print(file.name)
# 	print(file.path)

# print(os.system('ls -la'))

# root_path = '.'
# for root, dirs, files in os.walk(root_path):
#     print(root)
#     for file in files:
#         print('┗ ', file)

root_path = '.'
for root, dirs, files in os.walk(root_path):
    for file in files:
        print(os.path.join(root, file))