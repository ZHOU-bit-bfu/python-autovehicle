"""
================================================================================
  Lesson 05 练习: 字典 & 嵌套结构
  左边打开 lessons/lesson_05.md，右边写代码
================================================================================
"""

# ============================================================================
# 练习 1: 创建车辆字典
# 创建一个字典 car，包含: brand(品牌), speed(速度), wheelbase(轴距), is_hybrid(混动)
# 用字典的方式打印 brand 和 speed
# ============================================================================

# TODO: 写你的代码
car = {
    "brand":"BYD",
    "Speed":120,
    "distance":1000
}
print(car.get("brand"))
print(car.get("distance"))
# ============================================================================
# 练习 2: 传感器状态检查
# 下面是一个传感器列表，用 for 循环遍历
# 打印 "传感器 XXX 状态: OK" 或 "传感器 XXX 状态: 异常！"
# ============================================================================

sensors = [
    {"name": "front_radar", "type": "radar", "status": "OK"},
    {"name": "front_camera", "type": "camera", "status": "FAULT"},
    {"name": "rear_radar", "type": "radar", "status": "OK"},
    {"name": "lidar_top", "type": "lidar", "status": "WARN"},
]

# TODO: 写你的代码
for s in sensors:
    n=s["name"]
    TF="YES" if s["status"]=="OK" else "NO"
    print(f"传感器{n},状态：{TF}")

# ============================================================================
# 练习 3: 嵌套字典 — 读取车辆状态
# 从 vehicle_state 中打印: 当前车速、SOC、档位
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

# TODO: 写你的代码
print(vehicle_state["dynamics"]["speed"])
print(vehicle_state["battery"]["soc"])
print(vehicle_state["dynamics"]["gear"])
# ============================================================================
# 练习 4: 列表推导式 — 筛选数据
# sensors 列表中，筛选出 status 不是 "OK" 的传感器名称
# 存到 faulty_names 列表，然后打印
# ============================================================================

# TODO: 写你的代码
sensors = [
    {"name": "front_radar", "type": "radar", "status": "OK"},
    {"name": "front_camera", "type": "camera", "status": "FAULT"},
    {"name": "rear_radar", "type": "radar", "status": "OK"},
    {"name": "lidar_top", "type": "lidar", "status": "WARN"},
]

faulty_name = [s["name"] for s in sensors if s["status"] != "OK"]
print(f"故障传感器: {faulty_name}") 


# ============================================================================
# 练习 5: 综合 — 多车状态管理
# 下方是一个小型车队的状态列表，每辆车有 name, speed, lane
# 完成以下任务:
#   1. 打印所有在 "left" 车道的车
#   2. 找出速度最高的车，打印它的名字和速度
#   3. 计算所有车的平均速度
# ============================================================================

fleet = [
    {"name": "车A", "speed": 85, "lane": "left"},
    {"name": "车B", "speed": 72, "lane": "middle"},
    {"name": "车C", "speed": 95, "lane": "left"},
    {"name": "车D", "speed": 60, "lane": "right"},
    {"name": "车E", "speed": 78, "lane": "middle"},
]

# TODO: 写你的代码
ve=[s["name"] for s in fleet if s["lane"]==  "left"]
print (f"在左道的车子有{ve}")

ms=0
mc=None
for f in fleet:
     if f["speed"]>ms:
          ms=f["speed"]
          mc=f["name"]
else:
     ms=ms
     mc=mc
print(f"最快的车是{mc},此时的车速是{ms}")



su=sum(a["speed"] for a in fleet)
av=su/len(fleet)
print(f"所有车的平均车速为{av}")