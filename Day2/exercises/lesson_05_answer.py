"""
================================================================================
  Lesson 05 参考答案 — 做完练习再看！
================================================================================
"""

# ============================================================================
# 练习 1: 创建车辆字典
# ============================================================================
car = {
    "brand": "BYD",
    "speed": 120,
    "wheelbase": 2.92,
    "is_hybrid": True
}
print(car["brand"])
print(car["speed"])

# ============================================================================
# 练习 2: 传感器状态检查
# ============================================================================
sensors = [
    {"name": "front_radar", "type": "radar", "status": "OK"},
    {"name": "front_camera", "type": "camera", "status": "FAULT"},
    {"name": "rear_radar", "type": "radar", "status": "OK"},
    {"name": "lidar_top", "type": "lidar", "status": "WARN"},
]

for s in sensors:
    if s["status"] == "OK":
        print(f"传感器 {s['name']} 状态: OK")
    else:
        print(f"传感器 {s['name']} 状态: 异常！")

# ============================================================================
# 练习 3: 嵌套字典
# ============================================================================
vehicle_state = {
    "timestamp": "2026-08-10 10:30:00",
    "dynamics": {
        "speed": 85.5,
        "accel": 1.2,
        "gear": "D"
    },
    "battery": {
        "soc": 72.5,
        "temp": 38.2
    }
}

print(f"当前车速: {vehicle_state['dynamics']['speed']} km/h")
print(f"SOC: {vehicle_state['battery']['soc']}%")
print(f"档位: {vehicle_state['dynamics']['gear']}")

# ============================================================================
# 练习 4: 列表推导式筛选
# ============================================================================
faulty_names = [s["name"] for s in sensors if s["status"] != "OK"]
print(f"故障传感器: {faulty_names}")

# ============================================================================
# 练习 5: 多车状态管理
# ============================================================================
fleet = [
    {"name": "车A", "speed": 85, "lane": "left"},
    {"name": "车B", "speed": 72, "lane": "middle"},
    {"name": "车C", "speed": 95, "lane": "left"},
    {"name": "车D", "speed": 60, "lane": "right"},
    {"name": "车E", "speed": 78, "lane": "middle"},
]

# 1. 在 left 车道的车
print("left 车道的车:")
for car in fleet:
    if car["lane"] == "left":
        print(f"  {car['name']}")

# 2. 速度最高的车
fastest = fleet[0]
for car in fleet:
    if car["speed"] > fastest["speed"]:
        fastest = car
print(f"最快: {fastest['name']}, 速度 {fastest['speed']} km/h")

# 3. 平均速度
avg = sum(car["speed"] for car in fleet) / len(fleet)
print(f"平均速度: {avg:.1f} km/h")
