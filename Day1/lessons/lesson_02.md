# Lesson 02: 数字运算 & 字符串操作

---

## 1. 数学运算

Python 的加减乘除和计算器一样：

```python
# 基本运算
speed = 80
rpm = 2500

speed + 20      # 加法 → 100
speed - 10      # 减法 → 70
speed * 1.5     # 乘法 → 120
speed / 3       # 除法 → 26.666...（注意结果是 float）
speed // 3      # 整除 → 26（丢掉小数部分）
speed % 3       # 取余 → 2（80 / 3 = 26 余 2）
speed ** 2      # 幂 → 6400
```

---

## 2. 单位换算（车辆最常用）

```python
# km/h ← → m/s
v_kmh = 80
v_ms = v_kmh / 3.6        # → 22.22 m/s
v_kmh_back = v_ms * 3.6   # → 80 km/h

# rpm ← → rad/s
rpm = 2500
omega = rpm * 3.14159 / 30   # → 261.8 rad/s

# 电机功率: P = T × ω
torque = 300      # Nm
power = torque * omega   # W
power_kw = power / 1000  # kW
print(f"功率: {power_kw:.1f} kW")   # .1f 表示保留1位小数
```

---

## 3. 字符串操作

```python
brand = "  NIO ET5  "

brand.upper()       # "  NIO ET5  "（全大写）
brand.lower()       # "  nio et5  "（全小写）
brand.strip()       # "NIO ET5"（去两端空格）
brand.replace("ET5", "ET7")  # "  NIO ET7  "

# 拼接
name = "ET5"
full = "NIO " + name    # "NIO ET5"
```

---

## 4. 格式化数字输出

```python
v = 22.2222

print(f"{v:.2f}")    # 22.22  （保留2位小数）
print(f"{v:.1f}")    # 22.2   （保留1位小数）
print(f"{v:.0f}")    # 22     （取整）
```

---

## 今日要点

| 学了什么 | 关键写法 |
|----------|----------|
| 加减乘除 | `+ - * /` |
| 幂、整除、取余 | `** // %` |
| km/h ↔ m/s | `/ 3.6` 和 `* 3.6` |
| 字符串方法 | `.strip()` `.upper()` `.replace()` |
| 数字格式化 | `f"{x:.2f}"` |
