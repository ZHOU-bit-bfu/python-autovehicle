# Lesson 03: 列表 & for 循环 — 批量处理数据

---

## 1. 什么是列表

列表是**一组有序数据的容器**，用 `[]` 包起来。

```python
# 一个 Lidar 扫描到的 5 个障碍物距离
distances = [12.5, 3.2, 45.0, 8.7, 1.5]

# 一个速度时间序列
speeds = [0, 15, 32, 48, 55, 60, 60, 58]

# 混合类型也可以（但不推荐）
mixed = [1, "hello", 3.14, True]
```

---

## 2. 列表操作

```python
d = [12.5, 3.2, 45.0, 8.7]

len(d)          # 长度 → 4
d[0]            # 第一个 → 12.5（索引从 0 开始！）
d[1]            # 第二个 → 3.2
d[-1]           # 最后一个 → 8.7
d[-2]           # 倒数第二个 → 45.0

d[0:2]          # 切片 → [12.5, 3.2]（取索引 0,1，不含 2）
d[:3]           # 前 3 个 → [12.5, 3.2, 45.0]
d[2:]           # 从索引 2 开始 → [45.0, 8.7]

d.append(100)   # 末尾添加 → [12.5, 3.2, 45.0, 8.7, 100]
d.remove(3.2)   # 删除值 → [12.5, 45.0, 8.7, 100]
```

---

## 3. for 循环 — 遍历列表

```python
distances = [12.5, 3.2, 45.0, 8.7, 1.5]

# 逐个处理
for d in distances:
    print(f"距离: {d} m")
```

输出：
```
距离: 12.5 m
距离: 3.2 m
距离: 45.0 m
距离: 8.7 m
距离: 1.5 m
```

---

## 4. enumerate — 同时拿序号和值

```python
distances = [12.5, 3.2, 45.0]

for i, d in enumerate(distances):
    print(f"目标 {i+1}: {d} m")
```

输出：
```
目标 1: 12.5 m
目标 2: 3.2 m
目标 3: 45.0 m
```

`enumerate` 是 Python 里最常用的循环技巧之一。

---

## 5. 列表推导式 — Python 的灵魂语法

一行代码生成新列表：

```python
distances = [12.5, 3.2, 45.0, 8.7, 1.5]

# 筛选：所有小于 5m 的距离
danger = [d for d in distances if d < 5.0]
print(danger)  # [3.2, 1.5]

# 变换：把所有距离转为整数
int_dist = [int(d) for d in distances]
print(int_dist)  # [12, 3, 45, 8, 1]

# 这等价于：
danger = []
for d in distances:
    if d < 5.0:
        danger.append(d)
# 但推导式一行搞定，更快更漂亮
```

---

## 6. range — 生成数字序列

```python
range(5)        # 0, 1, 2, 3, 4
range(2, 6)     # 2, 3, 4, 5
range(0, 10, 2) # 0, 2, 4, 6, 8（步长 2）

# 常用：循环 n 次
for i in range(10):
    print(f"第 {i+1} 次循环")
```

---

## 7. 车辆实战：遍历传感器数据

```python
# 前方检测到的目标: [距离(m), 速度(m/s), 类型]
targets = [
    [15.0, 20.0, "car"],
    [8.0,  1.5,  "pedestrian"],
    [5.0,  4.0,  "bicycle"],
    [30.0, 22.0, "truck"],
]

# TTC = 距离 / 相对速度（假设同向，目标速度 ≤ 自车速度 25m/s）
ego_v = 25.0

for i, t in enumerate(targets):
    dist, obj_v, obj_type = t
    rel_v = ego_v - obj_v
    if rel_v > 0:
        ttc = dist / rel_v
        print(f"目标{i+1} ({obj_type}): TTC = {ttc:.1f}s")
    else:
        print(f"目标{i+1} ({obj_type}): 不会碰撞")
```

输出：
```
目标1 (car): TTC = 3.0s
目标2 (pedestrian): TTC = 0.3s     ← 危险！
目标3 (bicycle): TTC = 0.2s        ← 最危险！
目标4 (truck): TTC = 10.0s
```

---

## 今日要点

| 学了什么 | 关键写法 |
|----------|----------|
| 创建列表 | `[1, 2, 3]` |
| 索引 | `d[0]` 第一个, `d[-1]` 最后一个 |
| 切片 | `d[1:3]` |
| for 循环 | `for item in list:` |
| enumerate | `for i, item in enumerate(list):` |
| 列表推导式 | `[x for x in list if 条件]` |
