# Lesson 07: 文件读写 — 处理真实数据文件

---

## 1. 为什么需要文件读写

前面的练习数据都写在代码里。现实中数据来自**文件**：
- 车载 CAN 总线记录的 `.csv` 日志
- 传感器采集的 `.txt` 时序数据
- 仿真软件导出的 `.dat` 文件

---

## 2. 读取文件的基本流程

```python
# 1. 打开文件
f = open("data/sample.txt", "r", encoding="utf-8")

# 2. 读取内容
content = f.read()

# 3. 关闭文件
f.close()

print(content)
```

---

## 3. 用 with — 推荐写法（自动关闭）

```python
# with 语句：离开 with 块时自动关闭，不会忘
with open("data/sample.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)
```

---

## 4. 三种读取方式

```python
with open("data/sample.txt", "r") as f:
    # 方式 1: 一次性全读
    text = f.read()

    # 方式 2: 按行读取到列表
    f.seek(0)  # 回到文件开头
    lines = f.readlines()

    # 方式 3: 逐行迭代（文件大时省内存）
    f.seek(0)
    for line in f:
        print(line.strip())
```

---

## 5. 写文件

```python
report = """车速分析报告
最高车速: 95 km/h
平均车速: 72.3 km/h
"""

with open("data/report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print("报告已保存！")
```

| 模式 | 含义 |
|------|------|
| `"r"` | 读取（默认） |
| `"w"` | 写入（覆盖原内容！） |
| `"a"` | 追加（接在原文件末尾） |
| `"r+"` | 读写 |

---

## 6. 实战：解析 CSV 格式的 CAN 数据

```python
"""
典型的 CAN 日志 CSV:
timestamp,signal,value
0.0,speed,0
0.5,speed,12
1.0,speed,25
1.5,speed,38
"""

with open("data/can_data.csv", "r") as f:
    lines = f.readlines()

# 跳过标题行
speeds = []
for line in lines[1:]:          # 从第 2 行开始
    parts = line.strip().split(",")
    timestamp = float(parts[0])
    signal = parts[1]
    value = float(parts[2])
    if signal == "speed":
        speeds.append(value)

print(f"车速序列: {speeds}")
print(f"最高车速: {max(speeds)} km/h")
```

---

## 7. strip() + split() — 解析每一行

```python
line = "1.5,speed,38\n"

line.strip()           # "1.5,speed,38"（去换行符）
line.strip().split(",")  # ["1.5", "speed", "38"]
```

`.split(",")` 按逗号切开，这是解析 CSV 的核心操作。

---

## 8. 实战：处理真实工况数据

```python
"""对一个完整的行驶循环，提取关键指标"""

with open("data/drive_cycle.csv", "r") as f:
    header = f.readline()           # 跳过标题行
    speeds, accels = [], []

    for line in f:
        t, v, a = line.strip().split(",")
        speeds.append(float(v))
        accels.append(float(a))

v_max = max(speeds)
v_avg = sum(speeds) / len(speeds)
a_max = max(accels)

report = f"""
==================
行驶工况分析报告
==================
数据点数: {len(speeds)}
最高车速: {v_max:.1f} km/h
平均车速: {v_avg:.1f} km/h
最大加速度: {a_max:.2f} m/s²
"""

print(report)

# 保存报告
with open("data/report.txt", "w") as f:
    f.write(report)
```

---

## 今日要点

| 学了什么 | 关键写法 |
|----------|----------|
| 打开文件 | `with open("路径", "r") as f:` |
| 读全部 | `f.read()` |
| 按行读 | `f.readlines()` 或 `for line in f` |
| 写文件 | `with open("路径", "w") as f: f.write(内容)` |
| 解析 CSV | `line.strip().split(",")` |
