# Lesson 01: 你的第一行 Python 代码

---

## 1. 什么是变量

变量就是一个**贴了标签的盒子**，里面可以放东西。

```python
# 左边是标签名，右边是放进去的值
speed = 80          # 车速 80 km/h
brand = "NIO"       # 品牌字符串
is_on = True        # 开关状态，True 或 False
```

**不需要像 C 语言那样写 `int speed = 80;`，Python 自己猜类型。**

| 类型 | 示例 | 干什么用 |
|------|------|----------|
| `int` 整数 | `80` | 计数、转速 |
| `float` 小数 | `2.92` | 轴距、车速 |
| `str` 字符串 | `"ET5"` | 车名、VIN 码 |
| `bool` 布尔 | `True` / `False` | 开关、故障标志 |

---

## 2. print() — 让电脑说话

```python
print("Hello World")
print(80)
print("车速:", 80, "km/h")
```

运行结果：
```
Hello World
80
车速: 80 km/h
```

---

## 3. f-string — 最常用的打印方式

```python
name = "ET5"
speed = 80
print(f"车型 {name} 当前车速 {speed} km/h")
```

`f"..."` 里面的 `{变量名}` 会被替换成变量的值。**这是 Python 3.6+ 最推荐的写法。**

---

## 4. 注释

```python
# 这是单行注释，电脑不会执行

speed = 80   # 行内注释：车速 km/h

"""
这是多行注释（其实是多行字符串）
可以写很多行
"""
```

---

## 5. 你的第一个程序

```python
# 定义一些车辆参数
wheelbase = 2.92       # 轴距 m
mass = 1580            # 整备质量 kg
brand = "NIO ET5"
is_electric = True

# 打印出来
print(f"车型: {brand}")
print(f"轴距: {wheelbase} m")
print(f"质量: {mass} kg")
print(f"纯电: {is_electric}")
```

运行结果：
```
车型: NIO ET5
轴距: 2.92 m
质量: 1580 kg
纯电: True
```

---

## 今日要点

| 学了什么 | 一句话 |
|----------|--------|
| 变量 | 贴标签的盒子，`x = 10` |
| int / float / str / bool | 四种基本类型 |
| print() | 让电脑输出内容 |
| f-string | `f"车速{speed}km/h"` |
| 注释 | `#` 后面的内容不执行 |
