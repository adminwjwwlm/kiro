# Content additions for pkg17 document expansion
# This file is exec'd by expand_doc_pkg17.py with doc, find_para_idx, insert_after, insert_after_elem available

# ============================================================
# PART 1: 220kV/35kV (64 stations) - paragraphs 0~273
# ============================================================

# --- 1. Expand 项目背景 (after para 14 area) ---
idx = find_para_idx('从国际形势来看，乌克兰电网遭受网络攻击')
if idx > 0:
    ref = doc.paragraphs[idx]
    texts_bg1 = [
        '从网络安全威胁演进趋势分析，当前电力系统面临的威胁呈现以下特点：一是攻击主体从个人黑客向有组织、有国家背景的高级持续性威胁（APT）组织演变，攻击资源更加丰富、攻击手段更加高明；二是攻击目标从信息窃取向系统破坏转变，攻击者不仅试图窃取敏感数据，更试图通过控制工业控制系统直接造成物理世界的破坏；三是攻击路径更加隐蔽和多样化，通过供应链攻击、水坑攻击、社会工程学等手段绕过传统安全防线；四是攻击工具不断进化，专门针对工控系统的恶意软件层出不穷，如Triton、Industroyer、CrashOverride等。',
        '从国内电力系统实际情况来看，近年来针对我国电力基础设施的网络安全探测和攻击活动明显增多。据国家互联网应急中心（CNCERT）统计，每年发现的针对我国关键信息基础设施的网络攻击事件呈递增趋势。电力行业作为国家安全的重要组成部分，面临的网络安全压力持续加大。特别是在当前复杂的国际形势下，电力系统网络安全已上升为国家安全的重要组成部分，加强电力监控系统网络安全防护已成为迫在眉睫的战略任务。',
        '新疆地区由于其特殊的地理位置和战略地位，电力系统网络安全防护尤为重要。奎屯市作为新疆北疆的重要工业城市和交通枢纽，连接着乌鲁木齐与伊犁河谷，其电力供应的安全稳定直接关系到北疆经济走廊的正常运转。近年来新疆地区经济快速发展，工业企业数量增加，居民用电需求持续增长，对电力系统可靠性和安全性的要求不断提高。在此背景下，加强变电站网络安全监测能力建设，构建全方位、多层次的安全防护体系，对于保障地区电力安全供应具有极其重要的现实意义。',
    ]
    current = ref._element
    for t in texts_bg1:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 2. Expand after policy section (after para with 电调〔2023〕28号) ---
idx = find_para_idx('电调〔2023〕28号', 0)
if idx > 0 and idx < 25:
    ref = doc.paragraphs[idx]
    texts_policy = [
        '2024年，国家能源局进一步发布了关于加强新型电力系统网络安全管理的指导意见，要求各电力企业加快推进网络安全态势感知平台建设，完善厂站侧网络安全监测探针部署，实现电力监控系统网络安全事件的实时监测、快速预警和应急处置。该文件对网络安全监测覆盖率、告警响应时间、系统可用性等关键指标提出了明确的量化要求，为各级电力企业开展网络安全能力建设提供了清晰的目标导向。',
        '从技术发展层面看，随着新型电力系统建设的深入推进，电力监控系统的网络边界日益模糊，传统的基于边界防护的安全策略已难以应对新型安全威胁。网络安全监测探针作为终端侧的主动防御手段，能够实时感知设备运行状态、监控异常行为、发现安全威胁，是构建"零信任"安全架构的重要基础组件。在电力监控系统中部署安全探针，相当于为每台关键设备安装了"安全哨兵"，使安全运维人员能够第一时间发现和响应安全事件。',
    ]
    current = ref._element
    for t in texts_policy:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 3. Expand 项目目标 section ---
idx = find_para_idx('具体目标如下', 0)
if idx > 0 and idx < 35:
    ref = doc.paragraphs[idx]
    texts_goal = [
        '本项目实施周期为2026年7月6日至2026年12月31日，共计约180个日历天。在此时间框架内，项目团队需完成全部64座变电站的网络安全探针接入服务工作，实现从准备到验收的全过程闭环管理。项目执行过程中将严格按照"准备—试点—推广—验收"四阶段模式推进，确保每项工作有计划、有标准、有验收、有记录。',
        '从量化目标角度，本项目需完成的核心工作量指标包括：64座变电站探针全覆盖部署（涉及设备约584台）、安全策略精细化配置（每台设备约需配置15-30条白名单规则）、128台网络安全监测装置版本升级、64座变电站网络设备监测接入、全部设备告警测试验证以及完整的资产信息补录与核对工作。',
    ]
    current = ref._element
    for t in texts_goal:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 4. Expand 项目重难点分析 ---
idx = find_para_idx('项目规模大、工期紧', 0)
if idx > 0 and idx < 75:
    ref = doc.paragraphs[idx]
    texts_diff = [
        '（7）跨安全大区操作风险管控',
        '本项目涉及安全I区和安全II区两个安全大区的设备操作，跨安全大区的操作必须严格遵循电力监控系统安全防护规定，确保横向隔离装置的安全策略不被破坏。在实际施工中，需要分别为I区和II区设备制定独立的施工方案，使用不同的施工设备和工具，严禁出现跨区直连等违规行为。这对施工人员的安全意识和操作规范性提出了极高要求。',
        '（8）季节性施工环境挑战',
        '本项目实施周期为2026年7月至12月，跨越夏季高温和冬季严寒两个极端气候时段。新疆北疆地区夏季高温可达40℃以上，冬季低温可达-30℃以下。高温天气对设备散热和人员体力提出挑战，严寒天气对室外作业和交通出行造成影响。特别是部分偏远地区35kV变电站在冬季可能面临积雪封路的情况，需要提前做好应对预案。',
        '（9）网络安全合规性审查要求严格',
        '所有施工过程中使用的设备、工具、软件包等均需通过严格的网络安全合规性审查。施工用便携式计算机需要经过安全加固和病毒查杀，移动存储介质需要进行格式化和安全检查，探针安装包需要经过代码签名验证。任何未经审查的设备和工具严禁接入电力监控系统网络。这些合规性要求虽然增加了施工准备工作量，但对于保障系统安全至关重要。',
    ]
    current = ref._element
    for t in texts_diff:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)



# --- 5. Update Part 1 schedule (项目实施路径) ---
# Replace schedule text for Part 1
idx = find_para_idx('第一阶段：充分准备阶段（第1-20天）', 0)
if idx > 0 and idx < 80:
    # Update Phase 1 heading
    p = doc.paragraphs[idx]
    for run in p.runs:
        if '第1-20天' in run.text:
            run.text = run.text.replace('第一阶段：充分准备阶段（第1-20天）', '第一阶段：充分准备阶段（2026年7月6日-7月25日，共20天）')

idx = find_para_idx('第二阶段：分类试点阶段（第21-40天）', 0)
if idx > 0 and idx < 90:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if '第21-40天' in run.text:
            run.text = run.text.replace('第二阶段：分类试点阶段（第21-40天）', '第二阶段：分类试点阶段（2026年7月26日-8月14日，共20天）')

idx = find_para_idx('第三阶段：全面推进阶段（第41-110天）', 0)
if idx > 0 and idx < 100:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if '第41-110天' in run.text:
            run.text = run.text.replace('第三阶段：全面推进阶段（第41-110天）', '第三阶段：全面推进阶段（2026年8月15日-11月28日，共106天）')

idx = find_para_idx('第四阶段：验收收尾阶段（第111-130天）', 0)
if idx > 0 and idx < 100:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if '第111-130天' in run.text:
            run.text = run.text.replace('第四阶段：验收收尾阶段（第111-130天）', '第四阶段：验收收尾阶段（2026年11月29日-12月31日，共33天）')

# --- 6. Expand 可行性建议 Part 1 ---
idx = find_para_idx('合理安排窗口期施工', 0)
if idx > 0 and idx < 120:
    ref = doc.paragraphs[idx + 1] if idx + 1 < len(doc.paragraphs) and doc.paragraphs[idx+1].text.strip() else doc.paragraphs[idx]
    # Find the paragraph after the last suggestion content
    last_suggest_idx = find_para_idx('避开用电高峰安排施工', 0)
    if last_suggest_idx > 0:
        ref = doc.paragraphs[last_suggest_idx]
        texts_suggest1 = [
            '（9）建立质量追溯机制',
            '建议为每台设备的施工过程建立完整的质量追溯记录，包括：施工人员、施工时间、安装的软件版本、配置的策略内容、测试结果等。这些记录不仅是验收的依据，更是后续运维排查问题的重要参考。建议采用电子化表单结合纸质签字确认的方式，确保记录的完整性和可追溯性。',
            '（10）制定分级应急响应预案',
            '建议针对施工过程中可能出现的各类异常情况，制定分级应急响应预案：一级（轻微异常）——设备出现告警但不影响业务运行，由施工工程师现场处理；二级（一般异常）——设备功能受到部分影响，需要技术负责人介入处理并通知运维人员；三级（严重异常）——系统功能受到严重影响或设备停运，立即启动回退操作并报告调度和招标方。预案应明确各级别的判定标准、处置流程、责任人和联系方式。',
            '（11）利用项目间隙开展技术培训',
            '建议在项目实施过程中，利用转场间隙和等待工作票审批的时间，向招标方运维人员开展网络安全监测系统的使用培训。培训内容包括：告警信息的解读方法、常见告警的处置流程、策略配置的调整方法、资产信息的维护要求等。通过培训实现知识转移，确保项目完成后招标方能够独立进行日常运维管理。',
        ]
        current = ref._element
        for t in texts_suggest1:
            current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 7. Expand 项目意义 Part 1 ---
idx = find_para_idx('推动形成电力系统网络安全监测的标准化规范', 0)
if idx > 0 and idx < 140:
    ref = doc.paragraphs[idx]
    texts_meaning1 = [
        '（6）促进区域电网协同防御能力建设',
        '本项目完成后，奎屯供电公司辖区内64座变电站将形成统一的网络安全监测体系，与主站网络安全管理平台实现数据互通和告警联动。这将使奎屯地区具备区域级的网络安全态势感知能力，能够从全局视角发现跨站点、跨区域的协同攻击行为。同时，项目积累的数据和经验将为新疆电力有限公司层面的网络安全态势感知平台建设提供重要的数据源和实践参考。',
        '（7）提升电力系统抗风险韧性',
        '通过网络安全探针的全面部署和精细化监测策略配置，电力系统的网络安全防护能力将从"被动应对"向"主动发现"转变，从"单点防护"向"体系防御"提升。即使面对高级持续性威胁（APT）等复杂攻击，也能够通过多维度、多层次的监测手段及时发现异常行为，为安全响应争取宝贵时间，最大程度降低网络攻击对电力系统运行安全的影响。',
    ]
    current = ref._element
    for t in texts_meaning1:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)



# --- 8. Expand 项目实施规模 Part 1 (after para about 584 devices) ---
idx = find_para_idx('项目整体工作量巨大', 0)
if idx > 0 and idx < 160:
    ref = doc.paragraphs[idx]
    texts_scale = [
        '从实施规模的复杂度分析，本项目具有"三大、三多、三高"的显著特点：覆盖范围大（64座变电站遍布奎屯供电公司全部辖区）、设备总量大（约584台各类电力监控系统设备）、施工工作量大（包含探针安装、策略配置、装置升级、告警测试等多项内容）；设备类型多（12种以上设备类型）、涉及厂家多（包括南瑞、许继、四方、积成等多家设备厂商）、电压等级多（220kV和35kV两个电压等级）；技术要求高（策略配置需精确到每台设备的每个端口）、安全要求高（零影响施工、零安全事故）、质量要求高（一次性通过验收）。',
        '在项目组织方面，考虑到64座变电站的庞大规模，需要建立矩阵式的项目管理架构。纵向按照项目阶段设置里程碑节点和交付物要求，横向按照施工区域和专业分工设置工作组和责任人。通过科学的组织架构设计和高效的资源调配机制，确保各项工作有序推进、协调配合。',
    ]
    current = ref._element
    for t in texts_scale:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 9. Expand 项目建设依据 (Part 1) ---
idx = find_para_idx('网络安全监测能力验证评估标准', 0)
if idx > 0 and idx < 195:
    ref = doc.paragraphs[idx]
    texts_basis = [
        '五、相关技术参考标准',
        '（1）GB/T 25058-2019《信息安全技术 网络安全等级保护实施指南》，为网络安全等级保护工作的实施提供了具体指导。',
        '（2）GB/T 28448-2019《信息安全技术 网络安全等级保护测评要求》，明确了等级保护测评的技术要求和管理要求。',
        '（3）DL/T 2569-2022《电力监控系统网络安全监测装置技术规范》，对电力系统网络安全监测装置的功能、性能和接口提出了具体技术要求。',
        '（4）Q/GDW 11445-2022《电力监控系统网络安全管理平台技术规范》，规定了主站侧网络安全管理平台的功能架构和技术指标。',
        '上述法律法规、行业标准和企业管理文件构成了本项目实施的完整制度依据体系，项目实施过程中将严格遵循上述要求，确保各项工作合法合规、技术达标。',
    ]
    current = ref._element
    for t in texts_basis:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 10. Expand 项目服务目标 Part 1 ---
idx = find_para_idx('文档交付：全套项目文档按时', 0)
if idx > 0 and idx < 210:
    ref = doc.paragraphs[idx]
    texts_svc_goal = [
        '为确保上述服务目标的实现，本项目建立以下质量保障体系：',
        '（1）过程质量控制——建立三级质检制度（施工自检、组长复检、质量员终检），每道工序完成后逐项核实，不合格项不得进入下一道工序。',
        '（2）阶段性验收——每完成一个批次的变电站施工后，组织阶段性验收，及时发现和纠正偏差，避免问题累积到最终验收阶段才暴露。',
        '（3）关键指标监控——建立项目关键绩效指标（KPI）监控看板，实时跟踪探针部署进度、策略配置完成率、告警测试通过率、问题处理及时率等核心指标。',
        '（4）持续改进机制——每周召开项目质量分析会议，总结本周施工中发现的质量问题，分析根本原因，制定改进措施并跟踪落实效果。',
    ]
    current = ref._element
    for t in texts_svc_goal:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 11. Expand 220kV施工方案详述 ---
idx = find_para_idx('220kV变电站施工时，必须执行最高等级', 0)
if idx > 0 and idx < 220:
    ref = doc.paragraphs[idx]
    texts_220 = [
        '六、220kV变电站施工质量验收标准',
        '针对220kV变电站的特殊重要性，制定以下严格的施工质量验收标准：（1）探针安装后系统CPU占用率增加不超过5%，内存占用增加不超过100MB；（2）策略配置后连续观察48小时内无误报告警产生；（3）网络白名单配置后所有合法通信不受影响，非法通信能够被准确识别和告警；（4）监测装置升级后所有功能测试项100%通过；（5）告警从触发到主站展示的端到端时延不超过30秒。',
        '七、220kV变电站应急处置方案',
        '为应对220kV变电站施工过程中可能出现的各类异常情况，制定以下应急处置方案：（1）探针安装后设备性能异常——立即停止探针服务，恢复系统至安装前状态，分析原因后重新制定安装方案；（2）策略配置后出现业务通信中断——立即清除新配置的策略规则，恢复默认放行状态，确认业务恢复正常后重新分析通信关系；（3）监测装置升级失败——启动版本回退流程，使用备份的旧版本软件恢复装置功能；（4）施工过程中触发安全告警——立即停止所有操作，通知调度和运维部门，配合排查确认是施工操作触发还是实际安全事件。',
    ]
    current = ref._element
    for t in texts_220:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)



# --- 12. Expand 35kV批量施工方案 ---
idx = find_para_idx('不具备安装条件的设备', 0)
if idx > 0 and idx < 250:
    ref = doc.paragraphs[idx]
    texts_35 = [
        '六、35kV变电站施工进度管控',
        '鉴于58座35kV变电站数量众多、分布广泛，建立以下进度管控机制：（1）每日进度报告——各施工小组每日下班前汇报当日完成情况和次日工作计划；（2）周进度分析——每周对比实际进度与计划进度，分析偏差原因并制定调整措施；（3）里程碑节点管控——设置每完成10座站为一个里程碑节点，节点处组织阶段评审；（4）动态资源调配——根据各组实际进展情况，动态调整人员和物资分配，确保整体进度均衡。',
        '七、35kV变电站施工安全管理',
        '35kV变电站虽然电压等级相对较低，但施工安全同样不容忽视。主要安全管理措施包括：（1）所有施工人员必须持有有效的电工作业资格证书和安全培训合格证；（2）进入变电站前必须正确佩戴安全帽、绝缘手套等个人防护用品；（3）施工期间严禁触碰带电设备和未经确认的接地线路；（4）使用的施工设备必须经过安全检测且在有效期内；（5）施工现场设置明确的安全警示标识和作业范围围栏。',
        '八、35kV变电站通信保障方案',
        '由于部分35kV变电站位于偏远地区，移动通信信号覆盖可能不完善。为保障施工期间的通信联络畅通，采取以下措施：（1）为每个施工小组配备卫星电话作为应急通信手段；（2）提前了解各站点的通信覆盖情况，规划好联络方式；（3）建立每日固定联络时间制度，确保项目管理层能够及时掌握各组工作状态；（4）对于通信条件较差的站点，安排经验丰富的工程师带队，减少对远程技术支持的依赖。',
    ]
    current = ref._element
    for t in texts_35:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 13. Expand 安全策略精细化配置 Part 1 ---
idx = find_para_idx('加固操作必须遵循', 0)
if idx > 0 and idx < 275:
    ref = doc.paragraphs[idx]
    texts_strategy = [
        '六、策略配置质量验证方法',
        '安全策略配置完成后，必须进行系统化的质量验证：（1）关键目录配置验证——通过手动修改被监控目录下的测试文件，确认系统能够产生正确的文件变更告警；（2）危险命令配置验证——在安全环境下执行配置的危险命令（如创建测试用户后立即删除），确认系统能够产生正确的命令执行告警；（3）网络白名单配置验证——通过抓包工具确认所有合法通信均在白名单范围内，同时模拟非法连接确认能够触发告警；（4）服务端口白名单验证——对比实际开放端口与配置的白名单，确认无遗漏无多余。',
        '七、策略配置变更管理',
        '策略配置完成并验证通过后，需建立变更管理机制：（1）所有策略配置以电子文档形式留存，包括配置内容、配置时间、配置人员和验证结果；（2）后续如需修改策略配置，必须经过技术负责人审核批准；（3）策略变更后必须重新进行验证测试，确认变更不影响原有监测效果；（4）定期（建议每季度一次）对策略配置进行复审，确认其是否仍然符合设备当前的运行状态和业务需求。',
    ]
    current = ref._element
    for t in texts_strategy:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# ============================================================
# PART 2: 110kV (35 stations) - paragraphs 274+
# ============================================================

# --- 14. Expand 项目背景 Part 2 ---
idx = find_para_idx('国网新疆奎屯供电公司决定实施110kV长春变', 0)
if idx > 0:
    ref = doc.paragraphs[idx]
    texts_bg2 = [
        '从技术防护体系的角度分析，当前35座110kV变电站的网络安全防护存在"三个不足"：一是监测覆盖不足，部分设备尚未纳入网络安全监测范围，存在监测盲区；二是策略精度不足，已部署探针的设备策略配置粗放，无法有效区分正常操作与异常行为；三是响应能力不足，缺乏有效的安全事件发现和快速响应机制。这些不足严重制约了网络安全防护体系的实际效果，亟需通过本项目进行全面提升和完善。',
        '从项目时间安排来看，本项目实施周期为2026年7月6日至2026年12月31日，共约180个日历天。在此时间窗口内，需要完成全部35座变电站的网络安全探针接入服务工作。项目时间安排需充分考虑新疆北疆地区的气候特点，夏季（7-9月）为施工黄金期，应集中安排大部分现场施工工作；秋冬季节（10-12月）天气逐渐转冷，应优先完成偏远站点的施工，预留充足的验收和整改时间。',
        '从电网安全运行角度分析，35座110kV变电站是奎屯地区110kV主网架的核心组成部分，承担着区域电力的汇集和分配功能。每座变电站都是连接220kV输电网和35kV/10kV配电网的关键节点，一旦因网络安全事件导致变电站保护系统误动或拒动，可能引发连锁故障，影响范围远超单站供电区域。因此，加强110kV变电站的网络安全监测能力，对于维护区域电网安全稳定运行具有极其重要的战略意义。',
    ]
    current = ref._element
    for t in texts_bg2:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 15. Expand 项目目标 Part 2 ---
idx = find_para_idx('通过本项目的实施，使35座变电站', 0)
if idx > 0:
    ref = doc.paragraphs[idx]
    texts_goal2 = [
        '本项目实施时间为2026年7月6日至2026年12月31日。在约180天的实施周期内，项目团队将按照"准备（15天）—试点（15天）—全面实施（101天）—验收收尾（49天）"的四阶段模式有序推进。项目完成后，将形成覆盖35座变电站全部电力监控系统设备的网络安全监测防护体系，实现安全态势的实时感知和威胁的快速预警。',
        '从量化指标来看，本项目的核心交付成果包括：35座变电站约350台电力监控系统设备的探针全覆盖部署、70台（I区35台+II区35台）网络安全监测装置的版本升级和配置优化、35座变电站全部网络设备的监测接入、每台设备的安全策略精细化配置（含关键目录、危险命令、网络白名单、端口白名单四大类策略）、全部设备的告警测试验证和主站核查调阅通过。',
    ]
    current = ref._element
    for t in texts_goal2:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)



# --- 16. Update Part 2 schedule (项目实施路径) ---
idx = find_para_idx('第一阶段：充分准备阶段（第1-15天）', 280)
if idx > 0:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if '第1-15天' in run.text:
            run.text = run.text.replace('第一阶段：充分准备阶段（第1-15天）', '第一阶段：充分准备阶段（2026年7月6日-7月20日，共15天）')

idx = find_para_idx('第二阶段：试点验证阶段（第16-30天）', 280)
if idx > 0:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if '第16-30天' in run.text:
            run.text = run.text.replace('第二阶段：试点验证阶段（第16-30天）', '第二阶段：试点验证阶段（2026年7月21日-8月4日，共15天）')

idx = find_para_idx('第三阶段：全面推进阶段（第31-75天）', 280)
if idx > 0:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if '第31-75天' in run.text:
            run.text = run.text.replace('第三阶段：全面推进阶段（第31-75天）', '第三阶段：全面推进阶段（2026年8月5日-11月13日，共101天）')

idx = find_para_idx('第四阶段：验收收尾阶段（第76-90天）', 280)
if idx > 0:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if '第76-90天' in run.text:
            run.text = run.text.replace('第四阶段：验收收尾阶段（第76-90天）', '第四阶段：验收收尾阶段（2026年11月14日-12月31日，共48天）')

# --- 17. Expand 项目重难点 Part 2 ---
idx = find_para_idx('项目工期紧张与工作量巨大的矛盾', 280)
if idx > 0:
    ref = doc.paragraphs[idx]
    # Find the content paragraph after this heading
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs):
        ref = doc.paragraphs[content_idx]
    texts_diff2 = [
        '（7）冬季施工环境制约',
        '本项目实施周期跨越2026年7月至12月，其中后期施工阶段（10月-12月）正值新疆北疆地区的秋冬季节。北疆地区冬季来临较早，10月中下旬即可能出现降雪和道路结冰现象。部分位于山区或牧区的变电站冬季交通条件恶劣，给现场施工和人员安全带来挑战。因此，在施工计划安排上应尽可能将偏远站点的施工工作安排在前期气候较好的时段，将交通便利的城区站点留在后期实施。',
        '（8）网络安全事件应急处置能力要求高',
        '施工期间，如果某座变电站发生真实的网络安全事件，项目团队需要具备快速判断和正确处置的能力。需要明确区分施工操作触发的正常告警和实际安全事件产生的异常告警，避免因误判导致响应不当。这要求施工人员不仅具备安装配置的技术能力，还需要具备一定的网络安全分析和事件研判能力。',
        '（9）设备原厂技术支持的及时性保障',
        '35座变电站内的设备来源于多家设备厂商，不同厂家的设备在探针安装和策略配置方面可能存在特殊要求或兼容性问题。当施工过程中遇到需要原厂技术支持的问题时，能否获得及时有效的远程或现场支持直接影响施工进度。需要在项目前期就与各设备厂家建立良好的沟通机制和服务响应承诺。',
    ]
    current = ref._element
    for t in texts_diff2:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 18. Expand 可行性建议 Part 2 ---
idx = find_para_idx('合理利用窗口期安排施工', 280)
if idx > 0:
    # Get the content after this heading
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts_suggest2 = [
        '（9）建立项目团队激励机制',
        '建议建立与项目进度和质量挂钩的团队激励机制。根据各施工小组的完成速度、施工质量、安全表现等维度进行综合评价，对表现优秀的团队和个人给予适当奖励。通过正向激励调动施工人员的积极性和主动性，形成"比学赶帮超"的良好工作氛围，确保项目高质量完成。',
        '（10）充分利用数字化管理工具',
        '建议在项目管理中充分运用数字化工具提升管理效率：使用项目管理软件（如Project或同类工具）制定和跟踪施工进度计划；使用电子化表单工具收集和管理施工记录数据；使用即时通讯工具建立多层级的工作沟通群组；使用云存储服务统一管理项目文档和技术资料。数字化管理工具的运用可以显著提高信息传递效率、减少纸质文档管理的负担、方便项目数据的统计分析。',
        '（11）预留充足的验收整改缓冲期',
        '建议在工期安排上预留充足的验收整改缓冲时间。根据以往类似项目经验，首次验收通常会发现一定比例的整改项（通常为5%-15%），需要时间进行排查、整改和复验。建议在计划工期的基础上额外预留15-20天的缓冲期，用于处理验收过程中发现的各类问题，确保项目能够按期高质量交付。',
    ]
    current = ref._element
    for t in texts_suggest2:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)



# --- 19. Expand 项目意义 Part 2 ---
idx = find_para_idx('推动标准化和制度化建设', 280)
if idx > 0:
    ref = doc.paragraphs[idx]
    # Get content after this
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts_meaning2 = [
        '（6）培养属地化网络安全专业人才',
        '本项目实施过程中，通过与招标方运维人员的深度配合和知识传递，将培养一批具备网络安全监测系统运维能力的属地化专业人才。这些人才将成为奎屯供电公司网络安全运维的核心力量，能够在项目完成后独立承担日常监测、策略优化、告警处置等运维工作，减少对外部技术力量的长期依赖，实现网络安全能力的可持续发展。',
        '（7）推动电力行业网络安全生态建设',
        '本项目的实施涉及电力企业、安全厂商、设备厂商等多方主体的深度协作，有助于构建开放、协同、互利的电力网络安全生态体系。通过项目实践，各方在技术对接、标准制定、问题解决等方面积累的经验将推动整个电力行业网络安全水平的共同提升，促进安全产品的持续优化和安全服务模式的不断创新。',
    ]
    current = ref._element
    for t in texts_meaning2:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 20. Update Part 2 work schedule section ---
# Update total schedule overview
idx = find_para_idx('本项目计划总工期为90个日历天', 280)
if idx > 0:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if '90个日历天' in run.text:
            run.text = run.text.replace('本项目计划总工期为90个日历天，划分为四个实施阶段：', '本项目计划实施周期为2026年7月6日至2026年12月31日，共约180个日历天，划分为四个实施阶段：')

# Update phase durations in work schedule
idx = find_para_idx('第一阶段（项目准备）：第1天至第15天', 280)
if idx > 0:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if '第1天至第15天' in run.text:
            run.text = '第一阶段（项目准备）：2026年7月6日至7月20日，共15天；'

idx = find_para_idx('第二阶段（试点验证）：第16天至第30天', 280)
if idx > 0:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if '第16天至第30天' in run.text:
            run.text = '第二阶段（试点验证）：2026年7月21日至8月4日，共15天；'

idx = find_para_idx('第三阶段（全面实施）：第31天至第75天', 280)
if idx > 0:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if '第31天至第75天' in run.text:
            run.text = '第三阶段（全面实施）：2026年8月5日至11月13日，共101天；'

idx = find_para_idx('第四阶段（验收收尾）：第76天至第90天', 280)
if idx > 0:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if '第76天至第90天' in run.text:
            run.text = '第四阶段（验收收尾）：2026年11月14日至12月31日，共48天。'

# Update Phase 1 detailed schedule
idx = find_para_idx('第一阶段工作计划（项目准备，第1-15天）', 280)
if idx > 0:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if '第1-15天' in run.text:
            run.text = run.text.replace('第一阶段工作计划（项目准备，第1-15天）', '第一阶段工作计划（项目准备，2026.7.6-7.20）')

idx = find_para_idx('第二阶段工作计划（试点验证，第16-30天）', 280)
if idx > 0:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if '第16-30天' in run.text:
            run.text = run.text.replace('第二阶段工作计划（试点验证，第16-30天）', '第二阶段工作计划（试点验证，2026.7.21-8.4）')

idx = find_para_idx('第三阶段工作计划（全面实施，第31-75天）', 280)
if idx > 0:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if '第31-75天' in run.text:
            run.text = run.text.replace('第三阶段工作计划（全面实施，第31-75天）', '第三阶段工作计划（全面实施，2026.8.5-11.13）')

idx = find_para_idx('第四阶段工作计划（验收收尾，第76-90天）', 280)
if idx > 0:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if '第76-90天' in run.text:
            run.text = run.text.replace('第四阶段工作计划（验收收尾，第76-90天）', '第四阶段工作计划（验收收尾，2026.11.14-12.31）')

# Update the "90天" reference in last milestone
idx = find_para_idx('第90天：配合招标方组织项目最终验收', 280)
if idx > 0:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if '第90天' in run.text:
            run.text = run.text.replace('第90天：配合招标方组织项目最终验收', '2026年12月31日前：配合招标方组织项目最终验收')

# Update milestone M8
idx = find_para_idx('M8（T+90天）', 280)
if idx > 0:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if 'M8（T+90天）' in run.text:
            run.text = run.text.replace('M8（T+90天）：项目最终验收完成', 'M8（2026年12月31日前）：项目最终验收完成')



# --- 21. Expand Part 2 项目服务目标 ---
idx = find_para_idx('文档交付：全套项目文档按时', 420)
if idx > 0:
    ref = doc.paragraphs[idx]
    texts_svc2 = [
        '为确保上述各项服务目标如期实现，项目团队将建立完善的目标管理和过程控制体系：',
        '（1）目标分解——将总体服务目标分解为各阶段、各批次、各站点的具体目标，明确每个阶段的交付标准和验收条件。',
        '（2）过程监控——建立关键绩效指标（KPI）日报制度，实时跟踪探针部署进度、策略配置合规率、告警测试通过率等核心指标，确保目标偏差能够被及时发现和纠正。',
        '（3）质量闭环——对于未达标的质量指标，建立"发现→分析→整改→验证→关闭"的闭环管理机制，确保每个质量问题都得到彻底解决。',
        '（4）风险预控——识别可能影响服务目标实现的风险因素，提前制定应对措施和预案，将风险影响降到最低。',
    ]
    current = ref._element
    for t in texts_svc2:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 22. Expand Part 2 项目服务内容 (after 验收交付服务) ---
idx = find_para_idx('项目最终验收配合', 420)
if idx > 0:
    # Find the content paragraph
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts_svc_content2 = [
        '八、项目团队组织与管理',
        '本项目设立以下组织架构保障项目顺利实施：',
        '（1）项目管理组——由项目经理牵头，负责项目整体进度管控、资源协调、对外沟通和重大问题决策。项目经理全程驻守现场，每日与招标方项目负责人进行工作对接。',
        '（2）技术支持组——由技术负责人牵头，负责技术方案制定、策略模板编制、疑难问题解决和施工质量把控。技术负责人需具备5年以上电力系统网络安全项目经验，熟悉各类电力监控系统设备和网络安全监测技术。',
        '（3）现场施工组——设置2个施工小组，每组配置组长1名、施工工程师2-3名。各组按照施工计划分区域并行作业，组长负责本组的施工组织、安全管理和质量自检。',
        '（4）安全监督组——由专职安全员负责，对施工全过程的安全措施落实情况进行监督检查，组织班前安全交底，开展安全隐患排查，处理安全相关问题。',
        '（5）后方技术保障——设置2-3名后方技术支持工程师，负责策略配置模板维护、技术问题远程协助、与设备厂家的技术沟通等工作。',
        '九、应急响应预案',
        '为有效应对项目实施过程中可能出现的各类突发事件，制定以下分级应急响应预案：',
        '一级响应（系统安全事件）：当施工操作导致电力监控系统功能异常或触发安全保护动作时，立即停止所有施工操作，启动系统回退流程，通知调度部门和运维部门，配合进行系统恢复和事件分析。项目经理第一时间向招标方报告。',
        '二级响应（设备故障事件）：当单台设备因探针安装或配置操作出现故障时，立即执行该设备的备份恢复操作，同时不影响其他设备的正常运行。记录故障现象和处理过程，分析原因后调整施工方案再行实施。',
        '三级响应（进度延误事件）：当实际进度落后计划进度超过5天时，启动进度追赶措施，包括但不限于增派施工人员、延长工作时间、优化工序安排等。项目经理召开专题分析会议，制定进度追赶计划并跟踪实施效果。',
        '四级响应（自然灾害和极端天气）：当遇到暴雪、冰冻等极端天气影响施工时，以人员安全为第一优先级，暂停受影响站点的施工工作。待天气好转后重新安排施工计划，必要时启用预留的缓冲时间。',
    ]
    current = ref._element
    for t in texts_svc_content2:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 23. Expand Part 2 work schedule (add detail for extended Phase 3 and 4) ---
idx = find_para_idx('第73-75天（第8批）', 280)
if idx > 0:
    ref = doc.paragraphs[idx]
    texts_schedule2 = [
        '第76-81天（第9批）：完成4座变电站施工；重点安排偏远地区站点。',
        '第82-87天（第10批）：完成4座变电站施工；对前期施工站点进行质量复查。',
        '第88-93天（第11批）：完成最后4座变电站施工；开始整理阶段性施工记录。',
        '第94-101天：集中处理施工过程中的遗留问题和返工整改项；完成所有站点的阶段性质量检查。',
        '注：由于项目总工期调整为2026年7月6日至12月31日（约180天），第三阶段全面实施的时间相应延长至101天，可将32座变电站分为11个批次从容推进，每批次间留有充足的转场和准备时间，有利于保障施工质量。',
    ]
    current = ref._element
    for t in texts_schedule2:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 24. Expand Part 2 Phase 4 acceptance details ---
idx = find_para_idx('配合招标方组织项目最终验收。', 640)
if idx > 0 and idx < 660:
    ref = doc.paragraphs[idx]
    texts_accept2 = [
        '由于验收收尾阶段时间延长至48天（2026年11月14日-12月31日），可以更加充分细致地开展验收工作：',
        '第102-115天（11月14日-11月27日）：分三批组织35座变电站的主站核查调阅工作，每批约12座站，确保每座站的核查调阅时间充裕。',
        '第116-130天（11月28日-12月12日）：集中处理核查中发现的问题和整改项，对整改完成的站点进行复验确认。',
        '第131-145天（12月13日-12月27日）：整理全套项目资料，编制项目竣工报告和总结报告。组织内部预验收，确认所有交付物符合要求。',
        '第146-180天（12月28日-12月31日）：向招标方提交全部项目资料，配合组织最终验收，签署验收报告。',
    ]
    current = ref._element
    for t in texts_accept2:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 25. Update milestones in Part 2 ---
idx = find_para_idx('M6（T+75天）：全部35座变电站施工完成', 280)
if idx > 0:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if 'M6（T+75天）' in run.text:
            run.text = 'M6（2026年11月13日）：全部35座变电站施工完成；'

idx = find_para_idx('M7（T+85天）', 280)
if idx > 0:
    p = doc.paragraphs[idx]
    for run in p.runs:
        if 'M7（T+85天）' in run.text:
            run.text = 'M7（2026年12月20日）：全部核查调阅完成，项目资料提交；'



# --- 26. Expand Part 1 项目服务内容 section (after 安全策略精细化配置) ---
idx = find_para_idx('板块六：告警测试与验收', 0)
if idx > 0 and idx < 170:
    ref = doc.paragraphs[idx]
    texts_svc_p1 = [
        '板块七：项目管理与协调服务——提供全程项目管理服务，包括进度管理、质量管理、安全管理、沟通协调和文档管理等。',
        '各板块工作之间存在逻辑先后关系和依赖关系：板块一（探针部署）是基础，板块四（策略配置）依赖板块一完成后进行，板块二（网络设备接入）和板块三（监测装置维护）可并行开展，板块五（资产核对）贯穿全程，板块六（告警测试与验收）是所有工作完成后的最终验证环节。合理安排各板块工作的时序关系，是确保项目高效推进的关键。',
    ]
    current = ref._element
    for t in texts_svc_p1:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 27. Expand Part 1 项目建设依据 (after 企业管理文件) ---
idx = find_para_idx('国网新疆奎屯供电公司安全生产管理规定', 0)
if idx > 0 and idx < 190:
    ref = doc.paragraphs[idx]
    texts_mgmt = [
        '（6）国网新疆电力有限公司2025-2026年网络安全工作要点',
        '（7）国网新疆奎屯供电公司变电运维管理规程',
        '（8）国家电网公司电力监控系统安全防护技术管理规范（2024年修订版）',
    ]
    current = ref._element
    for t in texts_mgmt:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 28. More expansion for Part 1 项目背景 (after 问题描述) ---
idx = find_para_idx('基于上述背景和现状，国网新疆奎屯供电公司决定实施220kV', 0)
if idx > 0 and idx < 35:
    ref = doc.paragraphs[idx]
    texts_bg1_more = [
        '本项目的实施不仅是解决当前突出问题的现实需求，更是面向未来新型电力系统建设的前瞻性布局。随着奎屯地区新能源发电的快速发展和电力市场化改革的深入推进，电力监控系统的网络架构将更加复杂，面临的安全威胁也将更加多样化。通过本项目建立的网络安全监测体系和运维管理机制，将为应对未来更加复杂的网络安全挑战奠定坚实基础。',
        '项目实施周期为2026年7月6日至2026年12月31日。在此时间范围内，项目团队将充分利用夏秋季节施工条件较好的有利时机，科学组织施工力量，合理安排施工进度，确保在规定时间内高质量完成全部64座变电站的网络安全探针接入服务工作。',
    ]
    current = ref._element
    for t in texts_bg1_more:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 29. Expand Part 2 项目服务内容 (探针安装流程后) ---
idx = find_para_idx('安装过程中全程记录操作步骤和', 420)
if idx > 0:
    ref = doc.paragraphs[idx]
    texts_install2 = [
        '探针安装过程中需特别注意以下技术要点：一是安装前必须确认设备硬盘剩余空间不低于2GB，系统内存剩余不低于512MB，以确保探针运行不影响业务系统性能；二是安装过程中需关闭设备上运行的杀毒软件或安全防护软件，避免其将探针安装包误判为恶意软件而阻止安装；三是安装完成后需在探针管理界面确认探针状态为"在线"，并检查监测装置侧能否正确接收探针上报的数据；四是安装后至少持续观察2小时，确认设备各项业务功能正常运行，CPU和内存占用率无明显上升。',
    ]
    current = ref._element
    for t in texts_install2:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 30. More expansion for Part 2 项目背景 (after 2022 notice) ---
idx = find_para_idx('调网安〔2022〕7号', 285)
if idx > 0 and idx < 310:
    ref = doc.paragraphs[idx]
    texts_notice2 = [
        '该通知的核心要求包括：一是厂站侧网络安全监测装置应覆盖安全I区和安全II区的所有电力监控系统设备；二是网络安全探针软件应部署于所有主机类设备上，实现主机层面的安全监测；三是安全策略配置应达到精细化标准，能够有效区分正常操作和异常行为；四是告警信息应能准确、及时地上报至主站网络安全管理平台，实现集中监控和统一管理。这些要求为本项目的实施目标和技术标准提供了明确的依据。',
    ]
    current = ref._element
    for t in texts_notice2:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 31. Expand Part 1 Service Content - 告警测试 details ---
idx = find_para_idx('板块五：资产信息完善与核对', 0)
if idx > 0 and idx < 170:
    ref = doc.paragraphs[idx]
    texts_asset = [
        '资产信息的完善和核对是确保网络安全监测系统正常运行的重要基础工作。完整准确的资产信息能够帮助安全运维人员快速定位告警设备、了解设备网络环境、评估安全风险影响范围。本板块的工作内容包括：逐站逐设备核查资产信息的准确性，补录缺失的设备名称、IP地址、MAC地址、操作系统版本、安装软件、网络连接关系等信息，建立与实际部署情况一致的数字化资产台账。',
    ]
    current = ref._element
    for t in texts_asset:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 32. More detail in Part 2 策略配置服务 ---
idx = find_para_idx('配置前需', 500)
if idx > 0:
    ref = doc.paragraphs[idx]
    texts_port = [
        '服务端口白名单的配置对于发现系统中的后门程序和非法服务具有重要作用。如果攻击者在系统中植入后门程序，该程序通常会开放一个非正常的网络端口用于远程连接。通过服务端口白名单的监测，一旦出现白名单以外的新开端口，系统将立即产生告警，帮助安全运维人员第一时间发现潜在的安全威胁。在实际配置中，需要特别注意排除一些临时性的合法端口（如系统更新时临时开放的端口），避免产生误报。',
    ]
    current = ref._element
    for t in texts_port:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 33. Expand Part 1 安全策略技术细则 - 白名单部分 ---
idx = find_para_idx('典型配置示例——SCADA服务器', 0)
if idx > 0 and idx < 270:
    ref = doc.paragraphs[idx]
    texts_wl = [
        '典型配置示例——保信子站：保信子站作为客户端连接调度保信主站，白名单配置为"TCP [保信主站IP] [主站端口]"；保信子站采集各间隔保护装置数据，作为服务端接受保护装置的数据上送，白名单配置为"TCP [保护装置IP] [通信端口]"。由于保信子站涉及的保护装置数量较多，其白名单条目数通常较多，需要逐一确认每条通信关系的正确性。',
        '典型配置示例——故障录波系统：故障录波处理单元通常作为数据采集端，接收各间隔故障录波器上送的波形数据；同时作为客户端向主站上送已处理的故障报告。其白名单配置需要覆盖与各间隔录波器的通信关系以及与主站的通信关系。',
        '白名单配置的常见问题与处理方法：（1）设备有多网卡的情况——需要为每个网卡分别配置白名单，注意区分管理网口和业务网口的通信关系；（2）设备存在周期性的临时通信——某些设备会定期与NTP服务器同步时间或与认证服务器验证身份，这些通信虽然不频繁但属于合法行为，需要加入白名单；（3）多播/广播通信——某些网络协议使用多播地址进行设备发现或状态同步，需要确认是否为合法业务需要后决定是否加入白名单。',
    ]
    current = ref._element
    for t in texts_wl:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 34. More expansion in Part 2 fully (after emergency response) ---
idx = find_para_idx('网络设备监测缺失', 280)
if idx > 0 and idx < 310:
    ref = doc.paragraphs[idx]
    texts_net2 = [
        '网络设备作为电力监控系统通信的基础承载平台，其安全状态直接影响上层业务系统的可用性和可靠性。交换机和防火墙承担着数据转发、访问控制、安全隔离等关键功能，一旦网络设备被攻击者控制，攻击者可以监听网络流量、篡改数据包、绕过安全防护措施，造成极其严重的安全后果。因此，将网络设备纳入网络安全监测范围，实现网络层面的全面可视化，是构建完整安全防护体系不可或缺的组成部分。',
    ]
    current = ref._element
    for t in texts_net2:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)



# --- 35. Expand Part 2 建设依据 ---
idx = find_para_idx('网络安全监测能力验证评估标准', 420)
if idx > 0:
    ref = doc.paragraphs[idx]
    texts_basis2 = [
        '五、相关技术参考标准',
        '（1）GB/T 25058-2019《信息安全技术 网络安全等级保护实施指南》，为网络安全等级保护工作的具体实施提供了方法论指导。',
        '（2）GB/T 28448-2019《信息安全技术 网络安全等级保护测评要求》，明确了网络安全等级保护测评的技术和管理要求。',
        '（3）DL/T 2569-2022《电力监控系统网络安全监测装置技术规范》，对网络安全监测装置的功能、性能、接口和测试方法提出了详细技术要求。',
        '以上标准规范构成了本项目实施的完整技术依据体系，确保项目实施的每个环节都有据可依、有标准可循。',
    ]
    current = ref._element
    for t in texts_basis2:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 36. Expand Part 1 - add content after 项目展望 ---
idx = find_para_idx('推动形成电力系统网络安全监测的标准化规范，为行业发展贡献力量', 120)
if idx > 0 and idx < 140:
    ref = doc.paragraphs[idx]
    texts_outlook1 = [
        '（6）探索电力系统网络安全保险机制，通过安全监测数据量化网络安全风险水平，为网络安全保险产品的开发和定价提供数据支撑。',
        '（7）推动网络安全监测与电力系统调度运行深度融合，将网络安全态势纳入电力系统调度决策的考量因素，实现电力业务安全与网络空间安全的协同保障。',
        '本项目的实施将为奎屯供电公司在网络安全领域树立标杆，通过220kV和35kV两个电压等级64座变电站的全面覆盖，构建起从骨干输电到终端配电的完整安全监测链条。这一成果不仅满足当前的合规要求，更为未来新型电力系统的安全运营提供了可靠的技术保障和管理基础。',
    ]
    current = ref._element
    for t in texts_outlook1:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 37. Expand Part 2 展望 ---
idx = find_para_idx('推动标准化和制度化建设', 410)
if idx > 0:
    ref = doc.paragraphs[idx]
    texts_outlook2 = [
        '（6）探索建立网络安全运营中心（SOC）',
        '以本项目建成的网络安全监测体系为基础，逐步建设区域级的网络安全运营中心。通过SOC实现安全事件的统一监控、分析、响应和处置，将分散的安全监测能力整合为体系化的安全运营能力。SOC的建设将使奎屯供电公司从"有监测能力"提升到"有运营能力"，实现网络安全管理的质的飞跃。',
        '（7）推动网络安全与业务运维的深度融合',
        '未来应推动网络安全监测与电力设备运维管理的深度融合，将网络安全指标纳入设备健康状态评估体系。当网络安全探针检测到设备异常行为时，不仅产生安全告警，还能够触发设备运维工单，促进安全团队与运维团队的协同工作，实现从"发现问题"到"解决问题"的全流程闭环管理。',
    ]
    current = ref._element
    for t in texts_outlook2:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 38. More expansion: Part 1 项目服务内容 (after 220kV网络架构) ---
idx = find_para_idx('220kV变电站的网络架构通常分为三层', 0)
if idx > 0 and idx < 220:
    ref = doc.paragraphs[idx]
    texts_arch = [
        '在安全分区方面，220kV变电站的电力监控系统设备严格按照"安全分区"原则划分为安全I区和安全II区。安全I区包含直接参与电力系统实时控制的设备（如远动装置、安全自动装置等），其安全防护等级最高；安全II区包含进行数据采集、分析和管理的设备（如保信子站、故障录波系统等），安全防护等级次之。两个安全大区之间通过横向隔离装置进行物理隔离，确保I区设备不受II区安全事件的影响。网络安全探针的部署需要分别在两个安全大区内独立进行，使用各自区域内的网络安全监测装置进行数据收集和上报。',
    ]
    current = ref._element
    for t in texts_arch:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 39. More expansion: Part 2 基线核查 ---
idx = find_para_idx('对所有主机设备执行安全基线核查', 500)
if idx > 0:
    ref = doc.paragraphs[idx]
    texts_baseline = [
        '安全基线核查是对主机操作系统安全配置状况的全面体检，是确保主机层面安全防护能力的重要手段。通过基线核查，能够发现系统中存在的配置缺陷和安全隐患，如默认密码未修改、不必要的服务未关闭、审计功能未开启等问题。这些配置缺陷虽然不是直接的安全漏洞，但会降低系统的安全防护能力，增加被攻击成功的风险。因此，基线加固是网络安全防护体系中"打好基础"的关键环节。',
        '基线加固过程中需要特别注意与业务系统的兼容性问题。电力监控系统的某些业务应用可能依赖特定的操作系统配置（如特定的服务、特定的端口、特定的用户权限等），如果盲目按照安全基线要求进行加固，可能导致业务应用无法正常运行。因此，每项加固操作前都必须充分评估对业务系统的潜在影响，必要时与设备原厂家确认后再行操作。',
    ]
    current = ref._element
    for t in texts_baseline:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 40. Expand Part 2 告警测试 ---
idx = find_para_idx('配合主站网络安全管理平台运维人员完成探针核查调阅', 500)
if idx > 0:
    ref = doc.paragraphs[idx]
    texts_alarm2 = [
        '核查调阅是项目验收的最关键环节，直接决定项目是否达标。核查调阅的标准包括：（1）主站能够正确展示每台设备的在线状态；（2）设备基本信息（名称、IP、系统类型等）显示正确；（3）安全策略配置内容能够在主站正确查看；（4）模拟触发的告警能够在主站及时展示（通常要求30秒内）；（5）告警内容完整准确，包含事件类型、时间戳、设备标识、事件详情等关键信息。对于核查中发现的任何问题，需要逐项排查原因并进行整改，直到所有核查项全部通过。',
    ]
    current = ref._element
    for t in texts_alarm2:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- 41. More content for Part 1 after 项目目标 section ---
idx = find_para_idx('完成主机安全基线加固', 0)
if idx > 0 and idx < 50:
    # Find the content after
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts_host = [
        '安全基线加固是提升设备自身抗攻击能力的重要措施。通过关闭不必要的服务和端口、强化账户和密码策略、开启安全审计日志等措施，可以显著缩小设备的攻击面，增加攻击者的入侵难度。64座变电站的主机设备涵盖多种操作系统版本，加固方案需要根据各操作系统的特点和业务应用的依赖关系进行差异化制定，确保加固措施既满足安全要求又不影响业务功能。',
    ]
    current = ref._element
    for t in texts_host:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

print("Content insertion completed successfully.")
