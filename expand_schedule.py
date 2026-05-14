# -*- coding: utf-8 -*-
# Adjust work schedules to 2026年7月6日-2026年12月31日
# This file is exec'd from expand_main.py

print("\nAdjusting work schedules...")

# Table 1: Part 1 总体进度计划 (6 rows including header)
# Project period: 2026.7.6 - 2026.12.31 (approximately 26 weeks)
# Original: 30 weeks total
# New schedule:
#   准备阶段: 7月6日-7月19日 (第1-2周)
#   第一次升级: 7月20日-8月16日 (第3-6周)  
#   中期维护: 8月17日-10月25日 (第7-18周)
#   第二次升级: 10月26日-11月22日 (第19-22周)
#   总结归档: 11月23日-12月31日 (第23-26周)

table1 = doc.tables[1]
# Row 1: 准备阶段
table1.cell(1, 1).paragraphs[0].clear()
run = table1.cell(1, 1).paragraphs[0].add_run("2026.7.6-7.19\n（第1-2周）")
run.font.size = Pt(10)
table1.cell(1, 2).paragraphs[0].clear()
run = table1.cell(1, 2).paragraphs[0].add_run("设备信息调查、方案编制、\n升级包准备、人员培训")
run.font.size = Pt(10)

# Row 2: 第一次升级
table1.cell(2, 1).paragraphs[0].clear()
run = table1.cell(2, 1).paragraphs[0].add_run("2026.7.20-8.16\n（第3-6周）")
run.font.size = Pt(10)
table1.cell(2, 2).paragraphs[0].clear()
run = table1.cell(2, 2).paragraphs[0].add_run("19座变电站38台防火墙\n特征库第一次升级")
run.font.size = Pt(10)

# Row 3: 中期维护
table1.cell(3, 0).paragraphs[0].clear()
run = table1.cell(3, 0).paragraphs[0].add_run("中期维护")
run.font.size = Pt(10)
table1.cell(3, 1).paragraphs[0].clear()
run = table1.cell(3, 1).paragraphs[0].add_run("2026.8.17-10.25\n（第7-18周）")
run.font.size = Pt(10)
table1.cell(3, 2).paragraphs[0].clear()
run = table1.cell(3, 2).paragraphs[0].add_run("跟踪升级效果、\n准备第二次升级")
run.font.size = Pt(10)

# Row 4: 第二次升级
table1.cell(4, 1).paragraphs[0].clear()
run = table1.cell(4, 1).paragraphs[0].add_run("2026.10.26-11.22\n（第19-22周）")
run.font.size = Pt(10)
table1.cell(4, 2).paragraphs[0].clear()
run = table1.cell(4, 2).paragraphs[0].add_run("19座变电站38台防火墙\n特征库第二次升级")
run.font.size = Pt(10)

# Row 5: 总结归档
table1.cell(5, 1).paragraphs[0].clear()
run = table1.cell(5, 1).paragraphs[0].add_run("2026.11.23-12.31\n（第23-26周）")
run.font.size = Pt(10)
table1.cell(5, 2).paragraphs[0].clear()
run = table1.cell(5, 2).paragraphs[0].add_run("年度总结、文档归档、\n项目验收")
run.font.size = Pt(10)

print("  Table 1 (Part 1 总体进度) updated")

# Table 2: Part 1 单次升级详细计划 - keep the relative days but context is clear
# This table shows a single upgrade cycle (10 days), which is fine as-is
# Just verify it doesn't need date changes - it uses relative days
print("  Table 2 (Part 1 单次升级计划) - uses relative days, no change needed")

# Table 5: Part 2 总体进度计划
# Project period: 2026.7.6 - 2026.12.31 
# Original: 8 weeks
# New: expand to fit the full period with more detail
# 诊断评估: 7.6-8.2 (第1-4周)
# 核心实施: 8.3-9.27 (第5-12周)
# 优化提升: 9.28-11.8 (第13-18周)
# 验证交付: 11.9-12.31 (第19-26周)

table5 = doc.tables[5]
table5.cell(1, 1).paragraphs[0].clear()
run = table5.cell(1, 1).paragraphs[0].add_run("2026.7.6-8.2\n（第1-4周）")
run.font.size = Pt(10)
table5.cell(1, 2).paragraphs[0].clear()
run = table5.cell(1, 2).paragraphs[0].add_run("设备调研、漏洞扫描、\n现状评估、方案编制和评审")
run.font.size = Pt(10)

table5.cell(2, 1).paragraphs[0].clear()
run = table5.cell(2, 1).paragraphs[0].add_run("2026.8.3-9.27\n（第5-12周）")
run.font.size = Pt(10)
table5.cell(2, 2).paragraphs[0].clear()
run = table5.cell(2, 2).paragraphs[0].add_run("漏洞修复、设备接入、\n端口封堵、安全加固")
run.font.size = Pt(10)

table5.cell(3, 1).paragraphs[0].clear()
run = table5.cell(3, 1).paragraphs[0].add_run("2026.9.28-11.8\n（第13-18周）")
run.font.size = Pt(10)
table5.cell(3, 2).paragraphs[0].clear()
run = table5.cell(3, 2).paragraphs[0].add_run("策略调优、二次辨识、\n代理策略整改、迭代优化")
run.font.size = Pt(10)

table5.cell(4, 1).paragraphs[0].clear()
run = table5.cell(4, 1).paragraphs[0].add_run("2026.11.9-12.31\n（第19-26周）")
run.font.size = Pt(10)
table5.cell(4, 2).paragraphs[0].clear()
run = table5.cell(4, 2).paragraphs[0].add_run("效果验证、观察期监测、\n文档编制、项目验收")
run.font.size = Pt(10)

print("  Table 5 (Part 2 总体进度) updated")

# Tables 6-9: Part 2 详细工作计划 - adjust day numbers
# Table 6: 第一阶段 (第1-4周, 约28天)
table6 = doc.tables[6]
table6.cell(1, 2).paragraphs[0].clear()
run = table6.cell(1, 2).paragraphs[0].add_run("第1天")
run.font.size = Pt(10)
table6.cell(2, 2).paragraphs[0].clear()
run = table6.cell(2, 2).paragraphs[0].add_run("第1-5天")
run.font.size = Pt(10)
table6.cell(3, 2).paragraphs[0].clear()
run = table6.cell(3, 2).paragraphs[0].add_run("第5-10天")
run.font.size = Pt(10)
table6.cell(4, 2).paragraphs[0].clear()
run = table6.cell(4, 2).paragraphs[0].add_run("第8-12天")
run.font.size = Pt(10)
table6.cell(5, 2).paragraphs[0].clear()
run = table6.cell(5, 2).paragraphs[0].add_run("第10-15天")
run.font.size = Pt(10)
table6.cell(6, 2).paragraphs[0].clear()
run = table6.cell(6, 2).paragraphs[0].add_run("第12-18天")
run.font.size = Pt(10)
table6.cell(7, 2).paragraphs[0].clear()
run = table6.cell(7, 2).paragraphs[0].add_run("第16-22天")
run.font.size = Pt(10)
table6.cell(8, 2).paragraphs[0].clear()
run = table6.cell(8, 2).paragraphs[0].add_run("第20-28天")
run.font.size = Pt(10)
print("  Table 6 (Part 2 第一阶段) updated")

# Table 7: 第二阶段 (第5-12周, 约56天, starting from day 29)
table7 = doc.tables[7]
table7.cell(1, 2).paragraphs[0].clear()
run = table7.cell(1, 2).paragraphs[0].add_run("第29-38天")
run.font.size = Pt(10)
table7.cell(2, 2).paragraphs[0].clear()
run = table7.cell(2, 2).paragraphs[0].add_run("第36-48天")
run.font.size = Pt(10)
table7.cell(3, 2).paragraphs[0].clear()
run = table7.cell(3, 2).paragraphs[0].add_run("第29-45天")
run.font.size = Pt(10)
table7.cell(4, 2).paragraphs[0].clear()
run = table7.cell(4, 2).paragraphs[0].add_run("第42-55天")
run.font.size = Pt(10)
table7.cell(5, 2).paragraphs[0].clear()
run = table7.cell(5, 2).paragraphs[0].add_run("第50-70天")
run.font.size = Pt(10)
table7.cell(6, 2).paragraphs[0].clear()
run = table7.cell(6, 2).paragraphs[0].add_run("第65-84天")
run.font.size = Pt(10)
print("  Table 7 (Part 2 第二阶段) updated")

# Table 8: 第三阶段 (第13-18周, starting from day 85)
table8 = doc.tables[8]
table8.cell(1, 2).paragraphs[0].clear()
run = table8.cell(1, 2).paragraphs[0].add_run("第85-92天")
run.font.size = Pt(10)
table8.cell(2, 2).paragraphs[0].clear()
run = table8.cell(2, 2).paragraphs[0].add_run("第90-105天")
run.font.size = Pt(10)
table8.cell(3, 2).paragraphs[0].clear()
run = table8.cell(3, 2).paragraphs[0].add_run("第85-95天")
run.font.size = Pt(10)
table8.cell(4, 2).paragraphs[0].clear()
run = table8.cell(4, 2).paragraphs[0].add_run("第93-108天")
run.font.size = Pt(10)
table8.cell(5, 2).paragraphs[0].clear()
run = table8.cell(5, 2).paragraphs[0].add_run("第100-118天")
run.font.size = Pt(10)
table8.cell(6, 2).paragraphs[0].clear()
run = table8.cell(6, 2).paragraphs[0].add_run("第110-126天")
run.font.size = Pt(10)
print("  Table 8 (Part 2 第三阶段) updated")

# Table 9: 第四阶段 (第19-26周, starting from day 127)
table9 = doc.tables[9]
table9.cell(1, 2).paragraphs[0].clear()
run = table9.cell(1, 2).paragraphs[0].add_run("第127-135天")
run.font.size = Pt(10)
table9.cell(2, 2).paragraphs[0].clear()
run = table9.cell(2, 2).paragraphs[0].add_run("第127-148天")
run.font.size = Pt(10)
table9.cell(3, 2).paragraphs[0].clear()
run = table9.cell(3, 2).paragraphs[0].add_run("第140-160天")
run.font.size = Pt(10)
table9.cell(4, 2).paragraphs[0].clear()
run = table9.cell(4, 2).paragraphs[0].add_run("第155-172天")
run.font.size = Pt(10)
table9.cell(5, 2).paragraphs[0].clear()
run = table9.cell(5, 2).paragraphs[0].add_run("第170-180天")
run.font.size = Pt(10)
print("  Table 9 (Part 2 第四阶段) updated")

# Also update the text paragraphs that mention schedule
# Find and update Part 1 schedule text
for i, para in enumerate(doc.paragraphs):
    if "本项目服务期限为1年" in para.text:
        for run in para.runs:
            if "本项目服务期限为1年" in run.text:
                run.text = run.text.replace("本项目服务期限为1年", "本项目服务期限为2026年7月6日至2026年12月31日")
        print(f"  Updated schedule text at para {i}")
    elif "本项目计划总工期为8周" in para.text:
        for run in para.runs:
            if "本项目计划总工期为8周" in run.text:
                run.text = run.text.replace("本项目计划总工期为8周", "本项目计划总工期为2026年7月6日至2026年12月31日（约26周）")
        print(f"  Updated schedule text at para {i}")

# Update Part 2 phase descriptions
for i, para in enumerate(doc.paragraphs):
    if "第一阶段详细计划（第1-2周）" in para.text:
        for run in para.runs:
            run.text = run.text.replace("第一阶段详细计划（第1-2周）", "第一阶段详细计划（第1-4周，2026.7.6-8.2）")
        print(f"  Updated phase 1 title at para {i}")
    elif "第二阶段详细计划（第3-4周）" in para.text:
        for run in para.runs:
            run.text = run.text.replace("第二阶段详细计划（第3-4周）", "第二阶段详细计划（第5-12周，2026.8.3-9.27）")
        print(f"  Updated phase 2 title at para {i}")
    elif "第三阶段详细计划（第5-6周）" in para.text:
        for run in para.runs:
            run.text = run.text.replace("第三阶段详细计划（第5-6周）", "第三阶段详细计划（第13-18周，2026.9.28-11.8）")
        print(f"  Updated phase 3 title at para {i}")
    elif "第四阶段详细计划（第7-8周）" in para.text:
        for run in para.runs:
            run.text = run.text.replace("第四阶段详细计划（第7-8周）", "第四阶段详细计划（第19-26周，2026.11.9-12.31）")
        print(f"  Updated phase 4 title at para {i}")

# Update Table 11 delivery schedule
table11 = doc.tables[11]
table11.cell(1, 2).paragraphs[0].clear()
run = table11.cell(1, 2).paragraphs[0].add_run("第4周末")
run.font.size = Pt(10)
table11.cell(2, 2).paragraphs[0].clear()
run = table11.cell(2, 2).paragraphs[0].add_run("第4周末")
run.font.size = Pt(10)
table11.cell(3, 2).paragraphs[0].clear()
run = table11.cell(3, 2).paragraphs[0].add_run("第12周末")
run.font.size = Pt(10)
table11.cell(4, 2).paragraphs[0].clear()
run = table11.cell(4, 2).paragraphs[0].add_run("第12周末")
run.font.size = Pt(10)
table11.cell(5, 2).paragraphs[0].clear()
run = table11.cell(5, 2).paragraphs[0].add_run("第12周末")
run.font.size = Pt(10)
table11.cell(6, 2).paragraphs[0].clear()
run = table11.cell(6, 2).paragraphs[0].add_run("第12周末")
run.font.size = Pt(10)
table11.cell(7, 2).paragraphs[0].clear()
run = table11.cell(7, 2).paragraphs[0].add_run("第18周末")
run.font.size = Pt(10)
table11.cell(8, 2).paragraphs[0].clear()
run = table11.cell(8, 2).paragraphs[0].add_run("第18周末")
run.font.size = Pt(10)
table11.cell(9, 2).paragraphs[0].clear()
run = table11.cell(9, 2).paragraphs[0].add_run("第26周末")
run.font.size = Pt(10)
table11.cell(10, 2).paragraphs[0].clear()
run = table11.cell(10, 2).paragraphs[0].add_run("第26周末")
run.font.size = Pt(10)
print("  Table 11 (交付清单) updated")

print("Schedule adjustment complete.")
