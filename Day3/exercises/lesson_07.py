"""
================================================================================
  Lesson 07 练习: 文件读写 — 处理真实数据文件
  左边打开 lessons/lesson_07.md，右边写代码
================================================================================
"""

# ============================================================================
# 练习 1: 读取并打印文件内容
# 用 with open 读取 data/can_data.csv，打印全部内容
# ============================================================================

# TODO: 写你的代码
with open("data/can_data.csv", "r", encoding="utf-8") as f:
    content = f.read()

print(content)


# ============================================================================
# 练习 2: 解析 CSV — 提取车速列
# 读取 data/can_data.csv，跳过标题行
# 提取所有 signal=="speed" 的 value，存到 speeds 列表
# 打印: 最高车速、最低车速、车速序列
# ============================================================================

# TODO: 写你的代码
with open("data/can_data.csv", "r") as f:
  lines = f.readlines()#逐行阅读
  speeds = []
for line in lines[1:]:          # 从第 2 行开始
    parts = line.strip().split(",")
    timestamp = float(parts[0])
    signal = parts[1]
    value = float(parts[2])
    if signal == "speed":
        speeds.append(value)
print(f"最低车速: {min(speeds)} km/h")
print(f"最高车速: {max(speeds)} km/h")
print(f"车速序列: {speeds}")
# ============================================================================
# 练习 3: 写入报告文件
# 将练习 2 的结果写入 data/speed_report.txt
# 内容包括: 数据条数、最高车速、最低车速、平均车速
# ============================================================================

# TODO: 写你的代码
count=len(speeds)
vmax=max(speeds)
vmin=min(speeds)
av=sum(speeds)/len(speeds)
report = f"""车速分析报告
数据条数: {count}
最高车速: {vmax} km/h
最低车速: {vmin} km/h
平均车速: {av:.1f} km/h
"""
with open("data/report.txt", "w", encoding="utf-8") as f:
  f.write(report)


# ============================================================================
# 练习 4: 解析完整工况数据
# 读取 data/drive_cycle.csv（有表头: timestamp,speed,accel）
# 统计: 数据点数、最高车速、平均车速、最大加速度
# 打印统计结果peed_report.txt
# ============================================================================

# TODO: 写你的代码
with open("data/drive_cycle.csv", "r") as f:
    lines = f.readlines()
speeds ,accels= [],[]
for line in lines[1:]:          # 从第 2 行开始
    parts = line.strip().split(",")
    timestamp = float(parts[0])
    speed = float(parts[1])
    accel = float(parts[2])
    speeds.append(speed)
    accels.append(accel)
count=len(speeds)
vmax=max(speeds)
vmin=min(speeds)
av=sum(speeds)/len(speeds)
amax=max(accels)
report = f"""车速分析报告
数据条数: {count}
最高车速: {vmax} km/h
平均车速: {av:.1f} km/h
最大加速度 ：{amax:.1f} g
"""
with open("data/report.txt", "w", encoding="utf-8") as f:
  f.write(report)
# ============================================================================
# 练习 5: 综合 — 生成工况分析报告
# 读取 data/drive_cycle.csv
# 写一个函数 analyze_drive_cycle(filepath)，返回字典:
#   {"count": 数据点数, "v_max": 最高速, "v_avg": 平均速, "a_max": 最大加速度}
# 调用函数获取结果，打印报告，并保存到 data/cycle_report.txt
# ============================================================================

# TODO: 写你的代码
def analyze_drive_cycle(filepath):
    """读取工况文件，返回统计字典"""
    with open(filepath, "r") as f:
        lines = f.readlines()

    speeds, accels = [], []
    for line in lines[1:]:
        parts = line.strip().split(",")
        speeds.append(float(parts[1]))
        accels.append(float(parts[2]))

    return {
        "count": len(speeds),
        "v_max": max(speeds),
        "v_avg": sum(speeds) / len(speeds),
        "a_max": max(accels),
    }


# 调用函数
result = analyze_drive_cycle("data/drive_cycle.csv")

# 打印报告
report = f"""行驶工况分析报告
==================
数据点数: {result["count"]}
最高车速: {result["v_max"]} km/h
平均车速: {result["v_avg"]:.1f} km/h
最大加速度: {result["a_max"]:.2f} m/s²
"""
print(report)

# 保存报告
with open("data/cycle_report.txt", "w", encoding="utf-8") as f:
    f.write(report)
