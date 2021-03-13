# from datetime import datetime as dt
# from datetime import timedelta

# # 現在の時間を取得して変数「now」に格納
# now = dt.now()
# print('Now Time:' +str(now)) # Now Time:2018-05-07 06:12:01.008714

# # 変数「now」に 100マイクロ秒 加算
# d = now + timedelta(microseconds=30)
# print(d) # 2018-05-07 06:12:01.008814

# # 変数「now」に 50ミリ秒 加算
# d = now + timedelta(milliseconds=30)
# print(d) # 2018-05-07 06:12:01.058714

# # 変数「now」に 30秒 加算
# d = now + timedelta(seconds=30)
# print(d) # 2018-05-07 06:12:31.008714

# # 変数「now」に 15分 加算
# d = now + timedelta(minutes=15)
# print(d) # 2018-05-07 06:27:01.008714

# # 変数「now」に 10時間 加算
# d = now + timedelta(hours=10)
# print(d) # 2018-05-07 16:12:01.008714

# # 変数「now」に 5日 加算
# d = now + timedelta(days=5)
# print(d) # 2018-05-12 06:12:01.008714

# # 変数「now」に 3週 加算
# d = now + timedelta(weeks=3)
# print(d) # 2018-05-28 06:12:01.008714

# # 5日と10時間15分 加算
# d = now + timedelta(days=5, hours=10, minutes=15)
# print(d) # 2018-05-12 16:27:01.008714

# # 変数「now」から 10時間 減算
# d = now - timedelta(hours=10)
# print(d) # 2018-05-06 20:12:01.008714

# # 変数「now」から 5日 減算
# d = now - timedelta(days=5)
# print(d) # 2018-05-02 06:12:01.008714

# # 変数「now」から 3週 減算
# d = now - timedelta(weeks=3)
# print(d) # 2018-04-16 06:12:01.008714

# # 変数「now」から 10時間 減算
# d = now + timedelta(hours=-10)
# print(d) # 2018-05-06 20:12:01.008714

# # 変数「now」から 5日 減算
# d = now + timedelta(days=-5)
# print(d) # 2018-05-02 06:12:01.008714

# # 変数「now」から 3週 減算
# d = now + timedelta(weeks=-3)
# print(d) # 2018-04-16 06:12:01.008714

# from datetime import datetime as dt
# from datetime import timedelta


# # 現在の時間を取得して変数「now」に格納

# now = dt.now()

# print('Now Time:' +str(now)) # Now Time:2018-05-07 06:12:01.008714


# # 変数「now」に 5日 加算

# d = now + timedelta(days=5)

# print(d) # 2018-05-12 06:12:01.008714


# # 日付間の差分を求める
# print(d-now) # 5 days, 0:00:00

# # 5日と10時間15分100マイクロ秒 加算
# d = now + timedelta(days=5, hours=10, minutes=15, microseconds=100)
# print(d-now) # 5 days, 10:15:00.000100

# # 差分日数のみを取得
# print((d-now).days) # 5

# # 差分秒数のみを取得
# print((d-now).seconds) # 36900

# # 差分マイクロ秒数のみを取得
# print((d-now).microseconds) # 100

# 経過日数を変数「add_day」に格納
add_day = 2.5


# 変数「now」に 2.5日 加算
d = now + (timedelta(days=1) * add_day)

# 日付間の差分を求める
print(d-now) # 2 days, 12:00:00