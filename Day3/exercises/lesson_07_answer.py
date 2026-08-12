"""
================================================================================
  Lesson 07 参考答案 — 做完练习再看！
================================================================================
"""

# ============================================================================
# 练习 1: 读取并打印文件
# ============================================================================
with open("data/can_data.csv", "r", encoding="utf-8") as f:
    print(f.read())

# ============================================================================
# 练习 2: 解析 CSV 提取车速
# ============================================================================
speeds = []
with open("data/can_data.csv", "r") as f:
    lines = f.readlines()
    for line in lines[1:]:           # 跳过表头
        timestamp, signal, value = line.strip().split(",")
        if signal == "speed":
            speeds.append(float(value))

print(f"最高车速: {max(speeds)} km/h")
print(f"最低车速: {min(speeds)} km/h")
print(f"车速序列: {speeds}")

# ============================================================================
# 练习 3: 写入报告
# ============================================================================
with open("data/speed_report.txt", "w", encoding="utf-8") as f:
    f.write("===== 车速报告 =====\n")
    f.write(f"数据条数: {len(speeds)}\n")
    f.write(f"最高车速: {max(speeds)} km/h\n")
    f.write(f"最低车速: {min(speeds)} km/h\n")
    f.write(f"平均车速: {sum(speeds) / len(speeds):.1f} km/h\n")
print("报告已保存到 data/speed_report.txt")

# ============================================================================
# 练习 4: 解析完整工况数据
# ============================================================================
times, speeds, accels = [], [], []
with open("data/drive_cycle.csv", "r") as f:
    header = f.readline()            # 跳过表头
    for line in f:
        t, v, a, *_ = line.strip().split(",")
        times.append(float(t))
        speeds.append(float(v))
        accels.append(float(a))

print(f"数据点数: {len(speeds)}")
print(f"最高车速: {max(speeds):.1f} km/h")
print(f"平均车速: {sum(speeds) / len(speeds):.1f} km/h")
print(f"最大加速度: {max(accels):.2f} m/s²")

# ============================================================================
# 练习 5: 综合 — 工况分析报告函数
# ============================================================================
def analyze_drive_cycle(filepath):
    """分析行驶工况，返回统计字典"""
    times, speeds, accels = [], [], []
    with open(filepath, "r") as f:
        f.readline()
        for line in f:
            t, v, a, *_ = line.strip().split(",")
            times.append(float(t))
            speeds.append(float(v))
            accels.append(float(a))
    return {
        "count": len(speeds),
        "v_max": max(speeds),
        "v_avg": sum(speeds) / len(speeds),
        "a_max": max(accels),
    }


result = analyze_drive_cycle("data/drive_cycle.csv")
print(result)

with open("data/cycle_report.txt", "w", encoding="utf-8") as f:
    f.write(f"数据点数: {result['count']}\n")
    f.write(f"最高车速: {result['v_max']:.1f} km/h\n")
    f.write(f"平均车速: {result['v_avg']:.1f} km/h\n")
    f.write(f"最大加速度: {result['a_max']:.2f} m/s²\n")
print("报告已保存到 data/cycle_report.txt")
