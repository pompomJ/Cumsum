# 10個の整数を要素に持つ配列で、連続する3個の整数の和の最大値を累積和で求める
k = 3
a = [3, 6, 9, 7, 5, 7, 2, 5, 1, 4]

# 累積和
s = [0]
for num in a:
    s.append(s[-1] + num)

# 連続する3個の最大和を調べる
max_sum = 0
for i in range(k, len(a) + 1):
    # 今までの最大和より大きければ更新
    sect_sum = s[i] - s[i -k]
    max_sum = max([max_sum, sect_sum])

# 連続する3個の整数の和の最大値を出力
print(max_sum)
