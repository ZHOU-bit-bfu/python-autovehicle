# Lesson 05: 字典 & 嵌套结构 — 表示车辆状态

---

## 1. 什么是字典

字典是**键值对**的容器，用 `{}` 包起来。比列表更适合表示"有名字的属性"。

```python
# 列表表示一辆车（记不住每个位置是啥）
car = ["NIO ET5", 1580, 2.92, True]   # 0=车名 1=质量 2=轴距 3=纯电？好难记

# 字典表示一辆车（每个值有名字）
car = {
    "name": "NIO ET5",
    "mass": 1580,
    "wheelbase": 2.92,
    "is_electric": True
}
```

---

## 2. 字典的增删改查

```python
car = {"brand": "BYD", "speed": 0}

# 查 — 用 key 取值
car["brand"]         # "BYD"
car.get("speed")     # 0
car.get("color", "未知")  # 不存在的 key 返回默认值 "未知"

# 改
car["speed"] = 80    # 修改已有 key

# 增
car["battery"] = 86  # 新增 key-value

# 删
del car["battery"]   # 删除

# 检查 key 是否存在
"brand" in car       # True
```

---

## 3. 遍历字典

```python
car = {"brand": "ET5", "mass": 1580, "wheelbase": 2.92}

# 遍历所有 key
for k in car:
    print(k)          # brand, mass, wheelbase

# 遍历 key + value
for k, v in car.items():
    print(f"{k}: {v}")
# brand: ET5
# mass: 1580
# wheelbase: 2.92
```

---

## 4. 列表 + 字典 组合 — 车辆工程必备

```python
# 传感器集群：每个传感器是一个字典，所有传感器放在一个列表
sensors = [
    {"name": "front_radar", "type": "radar", "range": 250, "status": "OK"},
    {"name": "front_camera", "type": "camera", "range": 150, "status": "OK"},
    {"name": "rear_radar", "type": "radar", "range": 80, "status": "FAULT"},
    {"name": "lidar_top", "type": "lidar", "range": 100, "status": "OK"},
]

for s in sensors:
    status_icon = "✅" if s["status"] == "OK" else "❌"
    print(f"{status_icon} {s['name']}: {s['type']}, {s['range']}m")
```

---

## 5. 嵌套字典 — 完整车辆状态

```python
vehicle_state = {
    "timestamp": "2026-08-10 10:30:00",
    "dynamics": {
        "speed": 85.5,      # km/h
        "accel": 1.2,       # m/s²
        "steering": -3.5,   # ° 方向盘转角
        "gear": "D"
    },
    "battery": {
        "soc": 72.5,         # %
        "temp": 38.2,        # ℃
        "voltage": 396.5     # V
    },
    "adas": {
        "aeb_active": False,
        "acc_on": True,
        "target_speed": 90
    }
}

# 访问嵌套数据
print(vehicle_state["dynamics"]["speed"])     # 85.5
print(vehicle_state["battery"]["soc"])        # 72.5
```

---

## 6. 实战：筛选故障传感器

```python
sensors = [
    {"name": "front_radar", "status": "OK"},
    {"name": "front_camera", "status": "OK"},
    {"name": "rear_radar", "status": "FAULT"},
    {"name": "lidar_top", "status": "WARN"},
]

# 列表推导式筛选
faulty = [s["name"] for s in sensors if s["status"] != "OK"]
print(f"故障传感器: {faulty}")   # ['rear_radar', 'lidar_top']
```

---

## 今日要点

| 学了什么 | 关键写法 |
|----------|----------|
| 创建字典 | `{"key": value}` |
| 取值 | `d["key"]` 或 `d.get("key", 默认值)` |
| 遍历 | `for k, v in d.items()` |
| 列表+字典 | `[{...}, {...}]` |
| 嵌套取值 | `d["a"]["b"]` |
