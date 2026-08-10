# Lesson 04: if 条件判断 — 让代码会思考

---

## 1. 基本 if 语句

```python
speed = 85

if speed > 80:
    print("超速警告!")
```

---

## 2. if-elif-else

```python
speed = 85

if speed > 120:
    print("严重超速")
elif speed > 80:
    print("轻微超速")
elif speed > 60:
    print("正常行驶")
else:
    print("低速行驶")
```

**从上到下依次判断，第一个满足的条件执行后，后面的都不看了。**

---

## 3. 比较运算符

| 符号 | 含义 | 示例 |
|------|------|------|
| `>` | 大于 | `speed > 80` |
| `<` | 小于 | `dist < 5` |
| `>=` | 大于等于 | `speed >= 60` |
| `<=` | 小于等于 | `soc <= 20` |
| `==` | 等于 | `gear == "D"` |
| `!=` | 不等于 | `status != "OK"` |

---

## 4. 逻辑运算符: and, or, not

```python
# and: 两个条件同时满足
if speed > 60 and dist < 10:
    print("高速近距离 — 危险!")

# or: 任意一个满足
if soc < 10 or temp > 80:
    print("需要停车")

# not: 取反
if not ready:
    print("系统未就绪")
```

---

## 5. 车辆实战: AEB 触发逻辑

```python
"""
AEB (自动紧急制动) 简化逻辑:
- TTC < 1.0s: 全力制动
- TTC < 2.5s: 部分制动 + 声音警告
- TTC < 4.0s: 仅声音警告
- 其他: 无动作
"""

ttc = 1.8   # Time-To-Collision (秒)

if ttc < 1.0:
    action = "全力制动!!!"
elif ttc < 2.5:
    action = "部分制动 + 警告"
elif ttc < 4.0:
    action = "声音警告"
else:
    action = "正常行驶"

print(f"TTC={ttc}s → {action}")
```

---

## 6. if 嵌套

```python
speed = 90
lane = "left"

if speed > 80:
    if lane == "left":
        print("高速快车道，注意保持车距")
    else:
        print("高速行驶中")
else:
    print("速度正常")
```

---

## 7. 实战: 多条件碰撞风险评估

```python
"""
风险等级:
- TTC < 2s     OR  dist < 3m  → 危险 (红色)
- TTC < 5s     AND dist < 20m → 警告 (黄色)
- 其他                         → 安全 (绿色)
"""

ttc = 3.0
dist = 12.0

if ttc < 2 or dist < 3:
    level = "DANGER"
elif ttc < 5 and dist < 20:
    level = "WARNING"
else:
    level = "SAFE"

print(f"TTC={ttc}s, dist={dist}m → {level}")
```

---

## 今日要点

| 学了什么 | 关键写法 |
|----------|----------|
| if-elif-else | 条件分支 |
| 比较运算符 | `> < >= <= == !=` |
| 逻辑与 | `and` — 两个都对才行 |
| 逻辑或 | `or` — 一个对就行 |
| 逻辑非 | `not` — 反过来 |
| 嵌套 if | if 里面套 if |
