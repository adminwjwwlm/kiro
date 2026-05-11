#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
调整仓储报价，将总价从570.21万降至约400万
策略：只选择性调整部分功能项，保留大部分项目原价不变
"""

import csv

# 读取UTF-8版本的CSV
rows = []
with open('仓储报价_utf8.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)

header = rows[0]

data_rows = []
for i, row in enumerate(rows):
    if i == 0:
        continue
    try:
        seq = int(row[0])
        data_rows.append((i, row))
    except (ValueError, IndexError):
        pass

# 只调整部分功能项，其余保持原价
# 调价策略：
# 1. 13.5万档(3项) - 技术复杂度高的智能设备类，降至8万
# 2. 13.365万档(1项) - 设备树双向同步，降至8万
# 3. 8.355万档(14项) - 选10项调整，4项保持原价
# 4. 4.725万档(12项) - 选6项调整
# 5. 4.2万档(56项) - 选20项调整
# 6. 其余项目全部保持原价

adjustments = {}

# === 13.5万档 → 8万 (智能设备/RFID类，技术实现简化) ===
adjustments[141] = (8.0, "连接智能设备简化协议适配层，采用标准蓝牙通信协议替代私有协议，减少底层驱动开发")
adjustments[142] = (8.0, "盘点标签数据采集改为顺序扫描模式，取消多标签并发识别，降低硬件兼容性开发复杂度")
adjustments[143] = (8.0, "盘点异常分析采用规则匹配方式替代AI模型，减少模型训练和调优工作量")

# === 13.365万档 → 8万 ===
adjustments[127] = (8.0, "设备树双向同步改为单向主同步+定时对账，取消实时双向锁定机制，减少冲突处理开发")

# === 8.355万档 选10项调整 → 5万 ===
adjustments[1] = (4.5, "取消每日定时自动刷新机制，改为手动触发同步，简化定时任务和异常重试逻辑开发")
adjustments[2] = (4.5, "预付款校验采用标准化模板展示，减少多场景自定义校验规则的开发工作量")
adjustments[21] = (4.5, "信息回传采用轮询方式替代WebSocket实时推送，降低长连接维护和断线重连的开发复杂度")
adjustments[67] = (4.5, "合并多轮独立校验为统一校验引擎，减少逐一开发各校验节点的工作量")
adjustments[68] = (4.5, "协议储备预核对采用标准化比对引擎，不再为每种协议类型开发独立匹配算法")
adjustments[75] = (4.5, "本部审批简化多级串行审批为并行会签模式，减少复杂流程节点配置开发")
adjustments[76] = (4.5, "代保管物资信息采用扁平化展示，不再开发多层级钻取交互")
adjustments[84] = (4.5, "操作记录仅记录关键业务节点变更，不再追踪全量字段级操作日志")
adjustments[118] = (4.5, "财务主数据改为定时批量同步，取消与ERP的实时双向推送通道开发")
adjustments[119] = (4.5, "供应商数据采用主数据优先策略，不再开发多源冲突自动合并算法")
adjustments[120] = (4.5, "物料主数据维护采用批量导入+抽检方式，取消逐条在线审核流程开发")
adjustments[121] = (4.5, "仓库主数据采用扁平化编码管理，取消多层级树形架构的动态维护功能开发")
adjustments[122] = (4.5, "HPMS库存同步改为定时增量同步，取消实时事件驱动同步和冲突自动解决机制")
adjustments[123] = (4.5, "非结构化数据传输采用文件中转方式，取消流式实时传输通道开发")
adjustments[124] = (4.5, "领料工单出库复用标准出库流程，取消与HPMS的深度字段级联动定制")
adjustments[125] = (4.5, "预留领料单绑定采用异步消息对接，取消双系统实时状态锁定机制开发")
adjustments[126] = (4.5, "紧急借料同步改为批量定时推送，取消实时通知通道和确认回执机制开发")

# === 4.725万档 选10项调整 → 3万 ===
adjustments[128] = (3.0, "移动审批采用H5页面嵌入方式复用PC端逻辑，不再开发原生审批组件")
adjustments[129] = (3.0, "审批结果同步复用已有消息回调通道，不再独立开发同步模块")
adjustments[130] = (3.0, "待办提醒复用现有推送通道，不再独立开发消息推送模块")
adjustments[131] = (3.0, "预制签名采用图片叠加方式，不再集成第三方电子签章SDK")
adjustments[132] = (3.0, "扫码识别直接调用系统相机API，不再开发自定义扫码界面")
adjustments[133] = (3.0, "入库任务复用PC端逻辑，移动端仅做响应式界面适配")
adjustments[135] = (3.0, "出库管理复用PC端业务逻辑，移动端仅做交互适配")
adjustments[138] = (3.0, "物资借用简化为两级审批，不再支持动态多级审批链配置")
adjustments[139] = (3.0, "物资归还复用借用模块逆向流程，不再独立开发归还业务逻辑")
adjustments[140] = (3.0, "盘点录入改为逐一扫码确认，取消批量识别和异常自动标记功能")

# === 4.2万档 选33项调整 → 2.8万 ===
adjustments[8] = (2.8, "材料清单管理简化批量编辑功能，仅支持单条录入和Excel导入")
adjustments[9] = (2.8, "复用材料清单管理架构，仅调整展示字段配置")
adjustments[10] = (2.8, "WBS元素采用标准树形展示，取消拖拽排序和批量调整功能")
adjustments[11] = (2.8, "特征项源数据采用静态配置管理，取消动态加载和实时校验")
adjustments[16] = (2.8, "设备清单查询简化高级筛选，仅保留关键字段组合查询")
adjustments[17] = (2.8, "采购订单管理复用已有物资管理框架，减少独立开发工作量")
adjustments[20] = (2.8, "设备清单上传取消在线预览校验，仅做格式和必填字段基础校验")
adjustments[22] = (2.8, "流程配置采用预设模板选择方式，取消可视化自由拖拽编排功能")
adjustments[23] = (2.8, "人员节点维护复用组织架构数据，取消自定义人员权限矩阵")
adjustments[25] = (2.8, "技术变更录入采用固定表单模板，取消动态字段配置能力")
adjustments[26] = (2.8, "数据校验采用统一规则配置，取消逐字段自定义校验脚本")
adjustments[27] = (2.8, "商务变更确认复用技术变更页面框架，仅做字段替换")
adjustments[28] = (2.8, "单据管理采用通用模板引擎，取消每类单据独立样式开发")
adjustments[29] = (2.8, "技术变更审批复用统一审批流，取消独立审批逻辑开发")
adjustments[30] = (2.8, "商务变更录入复用技术变更框架，仅替换业务字段")
adjustments[31] = (2.8, "商务变更审批复用统一审批组件，配置化实现")
adjustments[32] = (2.8, "审批待办接入统一消息中心，取消独立待办模块开发")
adjustments[34] = (2.8, "预付结算校验复用已有支付校验逻辑，仅增加预付款特有规则")
adjustments[35] = (2.8, "到货款结算提醒采用定时任务触发，取消实时事件监听机制")
adjustments[36] = (2.8, "投运款支付跟踪复用结算跟踪框架，仅调整数据维度配置")
adjustments[37] = (2.8, "结清款待办接入统一待办中心，取消独立模块开发")
adjustments[40] = (2.8, "台账管理采用固定格式报表，取消用户自定义列和筛选条件功能")
adjustments[41] = (2.8, "投运款台账复用到货款台账框架，仅调整数据源配置")
adjustments[42] = (2.8, "结清款台账复用通用台账组件，仅做字段映射调整")
adjustments[44] = (2.8, "合同执行监控采用固定阈值告警，取消用户自定义规则引擎")
adjustments[46] = (2.8, "合同报表采用固定模板报表引擎，取消自定义报表设计器")
adjustments[50] = (2.8, "材料清单选取简化多条件联动筛选，改为分步选择方式")
adjustments[59] = (2.8, "采购项目匹配库存改为精确匹配，取消模糊匹配和智能推荐")
adjustments[66] = (2.8, "利库结果统计采用固定维度报表，取消自定义统计维度功能")
adjustments[71] = (2.8, "文件上传取消多格式自动转换，仅支持标准Excel模板导入")
adjustments[78] = (2.8, "固定资产入库单据采用固定模板，取消自定义字段扩展能力")
adjustments[85] = (2.8, "超市化物资统计采用预设报表模板，取消多维度自由组合分析")
adjustments[95] = (2.8, "废旧物资总览采用列表+详情模式，取消多视图切换功能")
adjustments[98] = (2.8, "视频监控采用标准RTSP流接入，取消自定义播放器和回放功能开发")
adjustments[103] = (2.8, "代管到期入库复用标准入库流程，仅增加到期触发判断逻辑")
adjustments[113] = (2.8, "领料单后补简化单据关联校验，仅做基础数据一致性检查")
adjustments[51] = (2.5, "采购清单创建复用订单创建框架，简化独立开发工作量")
adjustments[52] = (2.5, "采购清单管理采用通用列表组件，简化批量操作功能")
adjustments[60] = (2.5, "可利库物资填报采用Excel导入方式，取消在线逐条编辑功能")
adjustments[63] = (2.5, "利库计划清单管理采用通用模板，取消自定义清单样式")
adjustments[79] = (2.5, "库存总览详细页面采用分层懒加载，取消一次性全量渲染")
adjustments[99] = (2.5, "温湿度记录导出采用定时采集+标准报表，取消实时曲线图表开发")
adjustments[100] = (2.5, "危废仓环境监控复用温湿度框架，仅增加传感器数据源适配")
adjustments[104] = (2.5, "在库物资完整率采用固定统计口径，取消多维度自定义分析")
adjustments[105] = (2.5, "在库物资超期统计复用完整率框架，仅调整时间维度筛选")
adjustments[116] = (2.5, "人员禁用采用黑名单配置方式，取消动态权限实时联动控制")

# 生成新的CSV
new_rows = []

header_new = list(header)
while len(header_new) < 9:
    header_new.append('')
header_new[8] = '调价说明'
new_rows.append(header_new)

total_new = 0.0
adjusted_count = 0
for idx, row in data_rows:
    new_row = list(row)
    while len(new_row) < 9:
        new_row.append('')
    
    seq = int(new_row[0])
    old_price = float(new_row[7]) if new_row[7] else 0
    
    if seq in adjustments:
        new_price, reason = adjustments[seq]
        new_row[7] = str(new_price)
        new_row[8] = f"原报价{old_price}万，调整为{new_price}万。{reason}"
        total_new += new_price
        adjusted_count += 1
    else:
        total_new += old_price
        new_row[8] = ''  # 未调整项不填调价说明

    new_rows.append(new_row)

# 合计行
total_row = ['合计', '', '', '', '', '', '', f'{total_new:.2f}', '']
while len(total_row) < len(new_rows[0]):
    total_row.append('')
new_rows.append(total_row)

# 备注行
note = '备注：\n1.本报价基于需求文档描述进行初步估算，详细报价需在需求调研确认后进行二次核定。\n2.ERP系统、数据管理池、水电生产管理系统（HPMS）等第三方对接费用已纳入估算；如涉及额外接口开发量需重新评估。\n3.不含服务器或其他硬件及第三方软件测试费用。\n4.不包含团队驻场的费用，例如交通费用、差旅费用等。'
note_row = [note]
while len(note_row) < len(new_rows[0]):
    note_row.append('')
new_rows.append(note_row)

# 写入GBK版本
with open('仓储报价_调整后.csv', 'w', encoding='gbk', newline='') as f:
    writer = csv.writer(f)
    for row in new_rows:
        writer.writerow(row)

# 写入UTF8版本
with open('仓储报价_调整后_utf8.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    for row in new_rows:
        writer.writerow(row)

print(f"原总价: 570.21 万")
print(f"调整后总价: {total_new:.2f} 万")
print(f"降幅: {570.21 - total_new:.2f} 万 ({(570.21 - total_new) / 570.21 * 100:.1f}%)")
print(f"\n调整项数: {adjusted_count} / 143 项（{adjusted_count/143*100:.0f}%项目调价，其余保持原价）")
print(f"\n文件已生成:")
print(f"  - 仓储报价_调整后.csv (GBK编码)")
print(f"  - 仓储报价_调整后_utf8.csv (UTF-8编码)")
