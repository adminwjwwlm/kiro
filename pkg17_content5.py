# Final batch - add remaining ~5000 chars to reach 80000+

# --- D1. Add more to Part 1 monitoring device upgrade section ---
idx = find_para_idx('网络安全监测装置批量升级', 50)
if idx > 0 and idx < 65:
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts = [
        '128台监测装置的批量升级需要科学的计划和严密的组织。建议按照"先II区后I区、先35kV后220kV"的顺序分批进行升级，降低升级过程中的系统性风险。每台装置升级前需确认已取得最新版本升级包并验证其完整性（MD5/SHA256校验），升级过程中安排专人监控装置运行状态，升级后立即进行功能验证测试。对于升级失败的装置，需要有成熟的版本回退方案，确保能够在30分钟内恢复正常运行。批量升级工作的关键是严格按计划执行，避免同时升级多台装置导致监测覆盖出现大面积空白。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- D2. Expand Part 2 after 人员配置方案 ---
idx = find_para_idx('项目团队总计11-13人', 600)
if idx > 0:
    ref = doc.paragraphs[idx]
    texts = [
        '人员配置的动态调整机制：项目实施过程中，根据实际进度和工作需要，项目经理有权在总人力预算内进行人员动态调配。例如：在试点阶段集中技术力量确保试点质量；在全面推进阶段根据各区域工作进展调整各组人力配置；在验收阶段增派文档编制和质量检查人员。同时建立人员互为备份机制，确保任何岗位人员缺席时都有合格的替补人员可以接替工作，保障项目连续性不受影响。',
        '人员能力建设方面，在项目实施前期组织内部技术培训，重点培训内容包括：各类电力监控系统设备的操作系统特点和探针安装注意事项；安全策略精细化配置的技术规范和最佳实践；网络安全监测装置的升级流程和故障处理方法；各品牌设备的兼容性问题处理经验。通过系统的内部培训，提升全体施工人员的技术水平和问题处理能力，为高质量完成35座变电站的施工任务奠定人才基础。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- D3. Add more to Part 1 after 地理分区优化施工路线 ---
idx = find_para_idx('地理分区优化施工路线', 95)
if idx > 0 and idx < 115:
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts = [
        '具体的地理分区方案建议如下：将64座变电站按地理位置划分为5个施工区域——奎屯市区域（包括奎屯城区及近郊的变电站，约15座）、沙湾县区域（包括沙湾县及周边乡镇的变电站，约12座）、乌苏市区域（包括乌苏市及周边的变电站，约12座）、独山子区域（包括独山子及周边的变电站，约10座）、偏远牧区区域（包括距离市区较远的山区、牧区变电站，约15座）。每个区域内的变电站按照地理位置就近连续施工，最大限度减少转场时间和交通成本。预计通过优化施工路线，可以节约20%-30%的转场时间，显著提升施工效率。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- D4. Add more detail after Part 2 验收收尾阶段 descriptions ---
idx = find_para_idx('主站联调验证。配合主站网络安全管理平台', 370)
if idx > 0 and idx < 390:
    ref = doc.paragraphs[idx]
    texts = [
        '主站联调验证的具体工作内容包括：（1）探针数据上报验证——确认每台设备的探针能够正常向监测装置上报采集数据，监测装置能够正确解析数据并转发至主站平台；（2）告警联动验证——在厂站侧模拟触发各类告警事件，确认主站平台能够在30秒内正确展示告警信息，且告警内容完整、准确、可理解；（3）资产信息同步验证——确认厂站侧采集的设备资产信息能够与主站平台的资产管理模块正确同步，信息一致无遗漏；（4）指令下发验证——确认主站平台发出的探针核查调阅指令能够正确下达到厂站侧，探针能够正确响应并返回结果；（5）历史数据查询验证——确认主站平台能够正确查询和展示厂站侧上报的历史告警数据和运行日志。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

print("Final content batch (pkg17_content5) completed successfully.")
