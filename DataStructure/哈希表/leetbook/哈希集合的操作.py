

# 1. 初始化集合
hashset = set()
# 2. 新增键
hashset.add(3)
hashset.add(2)
hashset.add(1)
# 3. 删除键
hashset.remove(2)
# 4. 查询键是否包含在集合中
if (2 not in hashset):
    print("2 不在集合中")
# 5. 集合的大小
print("集合的大小为：", len(hashset))
# 6. 遍历集合
for x in hashset:
    print(x, end=" ")
print("在集合中")
# 7. 清空集合
hashset.clear()
print("集合的大小为：", len(hashset))
