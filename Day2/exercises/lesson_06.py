"""
================================================================================
  Lesson 06 练习: 函数 — 把代码变成工具
  左边打开 lessons/lesson_06.md，右边写代码
================================================================================
"""

# ============================================================================
# 练习 1: 写一个简单函数
# 定义函数 kmh_to_ms(speed)，将 km/h 转 m/s，返回结果
# 然后用它转换 60, 80, 120 三个速度并打印
# ============================================================================

# TODO: 定义 kmh_to_ms 函数，然后调用
def kmh_to_ms(kmh):
    return kmh/3.6

result = kmh_to_ms(60)
print(f"转换后的车速为{result:.2f}")
result = kmh_to_ms(80)
print(f"转换后的车速为{result:.2f}")
result = kmh_to_ms(120)
print(f"转换后的车速为{result:.2f}")
# ============================================================================
# 练习 2: TTC 计算函数
# 定义 calculate_ttc(distance, ego_v, obj_v)
# 返回 TTC，如果不会碰撞（ego_v <= obj_v）返回 -1
# 测试: (50, 25, 10) → 3.3s, (30, 20, 25) → -1
# ============================================================================

# TODO: 定义 calculate_ttc 函数，并测试
def calculate_ttc(distance, ego_v, obj_v):
    if ego_v <= obj_v:
      return -1
    return distance /(ego_v - obj_v)
result = calculate_ttc(50, 25, 10)
print(f"TTC = {result:.1f}s")
result = calculate_ttc(30, 20, 25)
print(f"TTC = {result:.1f}s")
# ============================================================================
# 练习 3: 多返回值 — 速度统计
# 定义 speed_summary(speeds)，返回 (最低速, 最高速, 平均速度)
# 用下面数据测试，用解包接收三个返回值
# ============================================================================
# TODO: 定义 speed_summary 函数，调用并打印
def speed_stats(speeds):
    """返回 (最小值, 最大值, 平均值)"""
    return min(speeds), max(speeds), sum(speeds) / len(speeds)
test_data = [45, 62, 88, 73, 95, 51]
v_min, v_max, v_avg = speed_stats(test_data)
print(f"最低车速: {v_min}, 最高车速: {v_max}, 平均车速: {v_avg:.1f}")


# ============================================================================
# 练习 4: 带默认参数的制动距离函数
# 定义 calc_brake_dist(speed_kmh, mu=0.8)
# 公式: v_ms = speed_kmh / 3.6, dist = v_ms² / (2 * mu * 9.81)
# 分别用干路面(mu=0.8)和湿路面(mu=0.4)计算 100km/h 的制动距离
# ============================================================================

# TODO: 定义 calc_brake_dist，测试两种路面
def calc_brake_dist(speed, mu=0.8, g=9.81):
    v_ms = speed / 3.6
    return v_ms ** 2 / (2 * mu * g)
print(calc_brake_dist(100))  
print(calc_brake_dist(100, mu=0.4))
# ============================================================================
# 练习 5: 综合 — 电池续航判断函数
# 定义函数 battery_advice(soc, distance_to_station)
# soc: 当前电量 %
# distance_to_station: 到最近充电站的距离 km
# 假设每 1% 电量能跑 4km
# 返回建议:
#   soc < 10 → "电量极低，立即靠边！"
#   估算续航 < distance_to_station → "可能无法到达充电站，请节省电量"
#   估算续航 >= distance_to_station → "可安全到达充电站"
# 测试: (25, 80), (8, 50), (60, 100)
# ============================================================================

# TODO: 定义 battery_advice，测试 3 组数据
def battery_advice(soc, distance_to_station):
    dis = 4 * soc 
    if soc < 10:
        return "电量极低，立即靠边！"
    else:
        if dis < distance_to_station:
            return "可能无法到达充电站，请节省电量"
        else:
            return "可安全到达充电站"

result = battery_advice(25, 80)
print(result)
result = battery_advice(8, 50)
print(result)
result = battery_advice(60, 100)
print(result)