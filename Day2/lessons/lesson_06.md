# Lesson 06: 函数 — 把代码变成工具

---

## 1. 什么是函数

函数是**一段有名字的可复用代码块**。你之前已经用过很多内置函数：`print()`, `len()`, `enumerate()`...

为什么需要自己写函数？
- **同样的计算**不要写两三遍
- **把复杂逻辑装进一个名字**，代码更清晰

---

## 2. 定义和调用

```python
# 定义一个函数
def calculate_ttc(distance, ego_speed, obj_speed):
    """计算碰撞时间 TTC (Time-To-Collision)"""
    rel_speed = ego_speed - obj_speed
    if rel_speed <= 0:
        return float("inf")   # 不会碰撞，返回无穷大
    return distance / rel_speed

# 调用函数
result = calculate_ttc(50, 25, 10)
print(f"TTC = {result:.1f}s")   # TTC = 3.3s
```

---

## 3. 参数和返回值

```python
def motor_power(torque, rpm):
    """计算电机功率 (kW)
    参数:
        torque: 扭矩 Nm
        rpm:    转速 r/min
    返回:
        功率 kW
    """
    omega = rpm * 3.14159 / 30     # rad/s
    power_w = torque * omega       # W
    return power_w / 1000          # kW


# 调用
p = motor_power(350, 4500)
print(f"电机功率: {p:.1f} kW")     # 电机功率: 164.9 kW
```

---

## 4. 多个返回值

```python
def speed_stats(speeds):
    """返回 (最小值, 最大值, 平均值)"""
    return min(speeds), max(speeds), sum(speeds) / len(speeds)


data = [60, 72, 85, 90, 78]
v_min, v_max, v_avg = speed_stats(data)
print(f"最低: {v_min}, 最高: {v_max}, 平均: {v_avg:.1f}")
```

---

## 5. 默认参数

```python
def calc_brake_distance(speed, mu=0.8, g=9.81):
    """计算制动距离
    speed: km/h
    mu: 摩擦系数（默认 0.8 干沥青路面）
    g: 重力加速度
    """
    v_ms = speed / 3.6
    return v_ms ** 2 / (2 * mu * g)


# 用默认 mu
print(calc_brake_distance(100))     # 49.2m

# 湿滑路面
print(calc_brake_distance(100, mu=0.4))  # 98.3m ← 几乎翻倍！
```

---

## 6. 函数 + 列表 = 批量处理

```python
def assess_ttc(ttc):
    """根据 TTC 返回风险等级"""
    if ttc < 2:
        return "DANGER"
    elif ttc < 5:
        return "WARNING"
    else:
        return "SAFE"


ttc_list = [0.8, 3.2, 6.0, 1.5, 4.8]

# 用函数处理整个列表
for t in ttc_list:
    level = assess_ttc(t)
    print(f"TTC {t}s → {level}")
```

---

## 7. 实战：完整 TTC 评估系统

```python
def calculate_ttc(distance, ego_v, obj_v):
    """计算 TTC，不会碰撞返回 -1"""
    rel_v = ego_v - obj_v
    if rel_v <= 0:
        return -1
    return distance / rel_v


def ttc_warning(ttc):
    """TTC → 风险等级"""
    if ttc < 0:
        return "不会碰撞"
    elif ttc < 2:
        return "🔴 危险"
    elif ttc < 5:
        return "🟡 警告"
    else:
        return "🟢 安全"


def evaluate_targets(targets, ego_v):
    """批量评估前方目标，返回评估结果列表"""
    results = []
    for i, t in enumerate(targets):
        dist, obj_v, obj_type = t
        ttc = calculate_ttc(dist, ego_v, obj_v)
        level = ttc_warning(ttc)
        results.append({
            "id": i + 1,
            "type": obj_type,
            "ttc": ttc if ttc > 0 else None,
            "level": level
        })
    return results


# 一键评估
targets = [
    [50.0, 20.0, "car"],
    [8.0, 2.0, "pedestrian"],
    [100.0, 30.0, "truck"],
]
ego_v = 25.0

report = evaluate_targets(targets, ego_v)
for r in report:
    ttc_str = f"{r['ttc']:.1f}s" if r['ttc'] else "—"
    print(f"目标{r['id']} ({r['type']}): TTC={ttc_str} → {r['level']}")
```

---

## 今日要点

| 学了什么 | 关键写法 |
|----------|----------|
| 定义函数 | `def 函数名(参数):` |
| 返回值 | `return 结果` |
| 多返回值 | `return a, b, c`（用 `x, y, z =` 接） |
| 默认参数 | `def f(a, b=0):` |
| 文档字符串 | `"""说明"""` 写在函数第一行 |
