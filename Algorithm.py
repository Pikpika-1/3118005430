import jieba
import sys
import math

try:
    orig_path, orig_add_path, orig_out_path = sys.argv[1:4]
except ValueError as e:
    print("\n输入错误!", e, "请重新输入参数！")

# orig_path = 'E:\test\orig.txt'
# orig_add_file = 'E:\test\orig_0.8_add'

orig_file = open(orig_path, 'r', encoding="utf-8")
orig_add_file = open(orig_add_path, 'r', encoding="utf-8")
orig_out_file = open(orig_out_path, 'w', encoding='utf-8')

orig_file = orig_file.read()
orig_add_file = orig_add_file.read()

words1 = jieba.lcut(orig_file, cut_all=True)
words2 = jieba.lcut(orig_add_file, cut_all=True)

vec1 = {}
vec2 = {}

for word in words1:
    vec1[word] = 0

for word in words1:
    vec1[word] += 1

# for key in vec1:
# print(key + ":" + str(vec1[key]))

for word in words2:
    vec2[word] = 0

for word in words2:
    vec2[word] += 1

# for key in vec2:
# print(key + ":" + str(vec2[key]))

up = 0
for key in vec1:
    if key in vec2:
        up += vec1[key] * vec2[key]

down1 = 0
for key in vec1:
    down1 += vec1[key] * vec1[key]

down1 = math.sqrt(down1)

down2 = 0
for key in vec2:
    down2 += vec2[key] * vec2[key]

down2 = math.sqrt(down2)

Similarity = up / (down1 * down2)

orig_out_file.write(str(Similarity))


def cut(num, c):
    c = 10 ** (-c)
    return (num // c) * c


print("\nsimilarity：")
print(cut(Similarity, 2))
