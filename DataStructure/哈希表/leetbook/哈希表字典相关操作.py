# 1. 初始化哈希表
hashmap = {0 : 0, 2 : 3}
# 2. 插入一个新的（键，值）对，或者更新值
hashmap[1] = 1
hashmap[1] = 2
# 3. 获得特定键对应的值
print("键 1 对应的值为: " + str(hashmap[1]))
# 4. 删除键
del hashmap[2]
# 5. 检查键是否存在于哈希表中
if 2 not in hashmap:
    print("键 2 不存在于哈希表中")
# 6. key 和 value 可以拥有不同的类型
hashmap["п"] = 3.1415
# 7. 哈希表的大小
print("哈希表的大小: " + str(len(hashmap)))
# 8. 遍历哈希表中的键
for key in hashmap:
    print("(" + str(key) + "," + str(hashmap[key]) + ")", end=" ")
print("在哈希表中")
# 9. 打印哈希表的所有键
print(hashmap.keys())
# 10. 清空哈希表
hashmap.clear();
print("哈希表的大小为: " + str(len(hashmap)))

