# Third batch of content additions for pkg17 expansion
# Target: add ~25000+ more characters

# --- B1. Major expansion in Part 1: Detailed work plan section ---
idx = find_para_idx('工作计划安排', 265)
if idx > 0 and idx < 280:
    ref = doc.paragraphs[idx]
    texts = [
        '根据项目技术规范书要求和64座变电站（6座220kV+58座35kV）的实际情况，结合本项目实施周期（2026年7月6日-2026年12月31日），制定以下详细工作计划安排：',
        '一、总体工期安排',
        '本项目计划实施周期为2026年7月6日至2026年12月31日，共约180个日历天（约26个工作周），划分为四个实施阶段：',
        '第一阶段（充分准备）：2026年7月6日至7月25日，共20天；',
        '第二阶段（分类试点）：2026年7月26日至8月14日，共20天；',
        '第三阶段（全面推进）：2026年8月15日至11月28日，共106天；',
        '第四阶段（验收收尾）：2026年11月29日至12月31日，共33天。',
        '二、第一阶段工作计划（充分准备，2026.7.6-7.25）',
        '第1-5天（7月6日-10日）：签订技术协议；组建项目团队并明确分工；收集64座变电站基础信息（设备清单、网络拓扑、IP地址分配表等）。',
        '第6-10天（7月11日-15日）：编制"三措一案"（分别为220kV和35kV变电站制定差异化方案）并提交招标方审核；取得设备原厂售后服务承诺书；准备施工设备和工具并完成安全加固。',
        '第11-15天（7月16日-20日）：组织全体施工人员学习"三措一案"；到招标方办理安全资质审核；参加入场安全教育和安全考试。',
        '第16-18天（7月21日-23日）：按地理区域制定64座变电站的详细施工进度计划表；划分施工批次和路线。',
        '第19-20天（7月24日-25日）：提前进场踏勘首批试点站（1座220kV+2座35kV）；确认施工条件；召开项目启动会。',
        '三、第二阶段工作计划（分类试点，2026.7.26-8.14）',
        '第21-23天（7月26日-28日）：选定试点站（220kV奎屯变、35kV承纵变、35kV古尔图变）并提交工作票申请；准备试点站施工所需材料。',
        '第24-30天（7月29日-8月4日）：完成220kV奎屯变电站的全部试点施工工作（作为220kV站的标杆站，每步操作都详细记录时间和注意事项）。',
        '第31-35天（8月5日-9日）：完成35kV承纵变电站（设备较新的代表站）的全部施工工作。',
        '第36-39天（8月10日-13日）：完成35kV古尔图变电站（设备较旧的代表站）的全部施工工作；配合主站进行试点站核查调阅。',
        '第40天（8月14日）：试点总结会议；分析问题优化方案；形成标准化施工流程和策略配置模板；确定全面实施阶段的详细计划。',
        '四、第三阶段工作计划（全面推进，2026.8.15-11.28）',
        '本阶段共106天，需完成剩余5座220kV变电站和56座35kV变电站的施工。安排3个施工小组并行作业：',
        '第41-50天（8月15日-24日）：A组完成剩余5座220kV变电站施工（每站约2天，技术负责人带队确保施工质量）；B组和C组开始第1批35kV变电站施工（每组2座）。',
        '第51-60天（8月25日-9月3日）：3组并行，完成6座35kV变电站施工。',
        '第61-70天（9月4日-13日）：3组并行，完成6座35kV变电站施工。',
        '第71-80天（9月14日-23日）：3组并行，完成6座35kV变电站施工。',
        '第81-90天（9月24日-10月3日）：3组并行，完成6座35kV变电站施工。重点安排国庆节前后的工作衔接。',
        '第91-100天（10月4日-13日）：3组并行，完成6座35kV变电站施工。国庆假期期间安排文档整理和质量复查工作。',
        '第101-110天（10月14日-23日）：3组并行，完成6座35kV变电站施工。',
        '第111-120天（10月24日-11月2日）：3组并行，完成6座35kV变电站施工。进入秋冬季节，注意偏远站点的交通安排。',
        '第121-130天（11月3日-12日）：3组并行，完成6座35kV变电站施工。',
        '第131-146天（11月13日-28日）：完成最后6座35kV变电站施工；集中处理施工过程中的遗留问题和整改项。',
        '五、第四阶段工作计划（验收收尾，2026.11.29-12.31）',
        '第147-155天（11月29日-12月7日）：分批配合主站平台进行全部64座变电站的集中核查调阅工作。',
        '第156-165天（12月8日-17日）：处理核查中发现的问题和整改项；对整改完成的站点进行复验确认。',
        '第166-175天（12月18日-27日）：整理全套项目资料（施工记录、调试报告、配置文档、验收报告等）；编制项目竣工报告。',
        '第176-180天（12月28日-31日）：向招标方提交全部项目资料；配合组织项目最终验收；签署验收报告。',
        '六、关键里程碑节点',
        'M1（7月15日）：三措一案编制完成并提交审核；',
        'M2（7月25日）：全体人员通过安全考试，获得施工许可；',
        'M3（8月14日）：试点站施工完成并通过验证，标准化模板确定；',
        'M4（9月23日）：累计完成30座变电站施工（约47%）；',
        'M5（10月23日）：累计完成48座变电站施工（约75%）；',
        'M6（11月28日）：全部64座变电站施工完成；',
        'M7（12月17日）：全部核查调阅完成，问题整改闭环；',
        'M8（12月31日）：项目最终验收完成，全部资料提交。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)



# --- B2. Major expansion Part 1 - Add project team description after 可行性建议 ---
idx = find_para_idx('利用项目间隙开展技术培训', 105)
if idx > 0 and idx < 140:
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts = [
        '（12）建立健全项目档案管理体系',
        '鉴于64座变电站项目规模较大，产生的文档资料量极为庞大（预计包括64份施工记录、64份调试报告、584份设备配置文档、64份告警测试记录等），建议从项目启动之初就建立完善的项目档案管理体系。采用统一的文档编号规则、统一的文件命名规范、统一的存储目录结构，并指定专人负责文档的收集、审核、归档和保管。建议采用电子化档案管理系统，便于文档的检索、查阅和批量打印。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- B3. Expand Part 2 detailed schedule (after the last milestone) ---
idx = find_para_idx('M8（2026年12月31日前）', 600)
if idx < 0:
    idx = find_para_idx('M8', 600)
if idx > 0:
    ref = doc.paragraphs[idx]
    texts = [
        '十、项目交付物清单',
        '本项目完成后，向招标方提交以下成果交付物：',
        '（1）项目管理类文档：项目实施方案、三措一案、施工组织设计、项目进度计划表、会议纪要、周报月报、项目竣工报告。',
        '（2）施工技术类文档：35座变电站施工记录（含每台设备的操作日志）、调试报告、策略配置文档（关键目录配置表、危险命令配置表、白名单配置表、端口白名单表）、网络设备接入配置文档。',
        '（3）测试验收类文档：告警测试记录、主站核查调阅记录、基线核查报告、资产核对报告。',
        '（4）资产管理类文档：35座变电站完整资产清单、设备配置信息表、网络拓扑图。',
        '（5）培训交付类文档：培训计划、培训教材、培训签到表和评估表。',
        '所有交付物按照招标方要求的格式编制，电子版和纸质版各提交一套，电子版光盘备份两份。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- B4. Expand Part 2 preparation section with more detail ---
idx = find_para_idx('信息收集与方案细化', 350)
if idx > 0 and idx < 370:
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts = [
        '信息收集的具体内容和方法包括：（1）设备清单采集——通过招标方提供的台账资料和现场确认相结合的方式，获取每座变电站内的设备完整清单，包括设备名称、型号、厂家、投运时间、操作系统类型和版本等关键信息；（2）网络拓扑采集——获取变电站站控层网络拓扑图，明确各设备的网络连接关系、VLAN划分情况、IP地址分配方案等；（3）现有监测状态——了解每座变电站当前网络安全监测系统的部署状态，包括已安装探针的设备、监测装置的软件版本、当前策略配置情况等；（4）通信关系梳理——预先通过配置文件分析梳理各设备的网络通信关系，为后续白名单配置提供基础数据。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- B5. More expansion Part 2 - project management section ---
idx = find_para_idx('项目建设依据', 420)
if idx > 0 and idx < 450:
    ref = doc.paragraphs[idx]
    texts = [
        '项目管理方法论',
        '本项目采用基于PMBOK项目管理知识体系的管理方法论，结合电力行业工程项目管理的特殊要求，建立覆盖项目全生命周期的管理体系。在项目启动阶段，明确项目章程、识别利益相关方、建立项目治理结构；在项目规划阶段，制定范围管理计划、进度管理计划、质量管理计划、资源管理计划、沟通管理计划、风险管理计划和采购管理计划；在项目执行阶段，严格按照各项计划执行并进行偏差分析和纠偏；在项目收尾阶段，完成正式验收、经验教训总结和项目关闭。',
        '项目治理结构方面，设立项目管理委员会（由招标方和投标方高层领导组成）负责项目重大事项决策和资源保障；设立项目管理办公室（由项目经理和各职能负责人组成）负责项目日常管理和执行层面的协调；设立技术评审组（由技术专家组成）负责技术方案审核和重大技术问题决策。三级管理架构确保项目的战略方向正确、执行过程可控、技术质量达标。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- B6. Expand Part 1 after 探针全覆盖部署（64站）---
idx = find_para_idx('工作量极为庞大。每台设备的探针安装', 45)
if idx > 0 and idx < 60:
    ref = doc.paragraphs[idx]
    texts = [
        '从施工效率角度分析，64座变电站的探针部署需要科学合理地规划施工节奏。根据试点阶段的实测数据，单台设备的探针安装和基本配置平均耗时约30-60分钟（视设备类型和操作系统而定），加上系统备份、安装后观察和记录填写的时间，单台设备的完整操作周期约90-120分钟。以此推算，每座220kV变电站（约20台设备）需要约3-4个工作日完成全部设备的探针安装，每座35kV变电站（约8台设备）需要约1.5-2个工作日完成探针安装。后续的策略精细化配置、告警测试等环节还需要额外的时间。因此，项目整体进度规划必须充分考虑每站实际工作量，合理安排资源和时间。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- B7. Major expansion Part 2 - after 项目实施规模 ---
idx = find_para_idx('项目实施规模、范围', 420)
if idx > 0 and idx < 450:
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts = [
        '一、项目实施规模',
        '本项目实施规模覆盖国网新疆奎屯供电公司辖区内35座110kV变电站，这些变电站构成了奎屯地区110kV电压等级供电网络的核心框架。35座变电站分布在奎屯市区、独山子区、乌苏市、沙湾县等多个行政区域，服务范围涵盖城市居民、工业企业、商业服务和农业生产等各类用电需求。',
        '35座110kV变电站名称如下：110kV长春变、110kV东苇湖变、110kV花园变、110kV霍果路变、110kV启航变、110kV三道坝变、110kV天北新区变、110kV乌尔禾变、110kV黄金变、110kV独山子变、110kV柳树沟变、110kV铁热克变、110kV芳草湖变、110kV建设变、110kV金沟河变、110kV乐土驿变、110kV莫乎尔变、110kV农六师变、110kV碧水变、110kV团结变、110kV城东变、110kV雀儿沟变、110kV四道河变、110kV塔西河变、110kV通达变、110kV头台变、110kV西戈壁变、110kV新安变、110kV车排子变、110kV皇宫变、110kV九间楼变、110kV八十四户变、110kV夹河子变、110kV北固城变、110kV库尔喀喇变。',
        '每座110kV变电站的典型设备配置包括：监控系统服务器/工作站1-3台、远动装置2台（I区和II区各1台或主备各1台）、五防系统1套、故障录波1-3套、保信子站1台、网络报文分析装置1台、在线监测系统1套（部分站点）。按照每站平均10台设备估算，35座变电站涉及设备总数约350台，项目工作量大、任务重。',
        '二、项目实施范围',
        '本项目实施范围涵盖七大工作板块：',
        '板块一：Agent网络安全探针软件安装与升级——对35座变电站内所有具备接入条件的设备完成探针安装或升级至最新版本。',
        '板块二：安全策略精细化配置——对所有安装探针的设备进行关键目录、危险命令、网络连接白名单、服务端口白名单等策略的精细化配置。',
        '板块三：网络设备监测接入——完成35座变电站站控层交换机、调度数据网交换机、防火墙等网络设备的安全监测功能接入。',
        '板块四：网络安全监测装置维护——完成I区、II区共70台监测装置的软件版本升级、双平面接入配置和对时整改。',
        '板块五：主机安全基线核查与加固——对所有主机类设备进行安全基线核查并整改不合规项。',
        '板块六：资产信息完善与核对——补录缺失资产信息，进行资产在线核对，建立完整的资产管理信息库。',
        '板块七：告警测试与验收——完成全部设备的告警测试和主站核查调阅工作，确保通过最终验收。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)



# --- B8. More expansion in Part 1 - after 精细化安全策略配置 goal ---
idx = find_para_idx('精细化安全策略配置', 30)
if idx > 0 and idx < 40:
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts = [
        '精细化策略配置的核心理念是"按需配置、最小授权"。即每台设备的安全监测策略严格根据该设备的实际业务功能和网络通信需求来配置，只将确认属于正常业务行为的操作和通信加入白名单，其余一律视为异常行为进行告警。这种配置方式虽然前期工作量大（需要对每台设备的业务行为进行深入分析），但能够最大程度地提高安全监测的灵敏度和准确性，实现"不放过任何一个真正的安全威胁"的目标。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- B9. Expand Part 2 safety measures (after safety section in schedule) ---
idx = find_para_idx('制定详细的应急预案，针对系统异常', 600)
if idx > 0:
    ref = doc.paragraphs[idx]
    texts = [
        '应急预案的具体内容包括：（1）系统异常应急处置——发现设备功能异常后，第一时间停止相关操作，执行备份恢复流程，10分钟内通知调度部门，30分钟内完成系统恢复；（2）人身安全应急处置——发生人身触电等安全事故时，立即切断电源、进行现场急救并拨打120急救电话，同时通知招标方安全管理部门；（3）信息安全事件处置——发现疑似网络攻击行为时，立即断开施工设备与站内网络的连接，保留相关日志和证据，通知网络安全管理部门进行分析研判。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- B10. Expand Part 1 more detail after 完善网络设备监测功能 goal ---
idx = find_para_idx('完善网络设备监测功能', 30)
if idx > 0 and idx < 40:
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts = [
        '网络设备监测功能的完善将使64座变电站的网络安全监测从"主机层"拓展到"网络层"，实现"端到端"的全栈安全监测。具体来说，通过交换机流量镜像可以监测站内设备间的数据通信行为是否符合预期模式；通过防火墙日志分析可以监测跨安全大区的通信是否存在违规行为；通过网络设备状态监测可以及时发现设备配置被非法修改、端口异常启停等潜在安全事件。这种多维度、多层次的监测手段相互配合，能够显著提高安全威胁的发现概率和定位精度。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- B11. More expansion after Part 2 第一阶段 details ---
idx = find_para_idx('现场踏勘。提前2天进场', 350)
if idx > 0 and idx < 370:
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and '第二阶段' in (doc.paragraphs[content_idx].text if content_idx < len(doc.paragraphs) else ''):
        ref = doc.paragraphs[idx]
    else:
        ref = doc.paragraphs[idx]
    texts = [
        '准备阶段的质量检查要点：（1）确认"三措一案"经过招标方审批并签字生效；（2）确认全体施工人员已通过安全考试并取得上岗许可；（3）确认施工设备和工具均已完成安全加固和检查；（4）确认设备原厂售后服务承诺书已取得；（5）确认64座变电站基础信息收集完整并经过核实；（6）确认首批试点站已完成现场踏勘并形成踏勘报告。以上各项均满足要求后，方可进入下一阶段施工。准备阶段的充分与否直接决定了后续施工的顺利程度，必须严格执行各项准备工作的质量标准。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- B12. Add售后服务 content for Part 2 ---
idx = find_para_idx('项目最终验收配合', 600)
if idx > 0:
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts = [
        '（4）售后技术服务',
        '项目验收合格后，提供为期12个月的免费售后技术服务。服务内容包括：探针运行异常的远程诊断和修复指导；安全策略优化建议（根据运行数据分析提出策略调整建议）；新增设备的探针接入技术咨询；监测装置运维问题的技术支持；新型安全威胁的策略更新建议。售后服务响应时间：一般问题24小时内响应，紧急问题4小时内响应。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

print("Third content batch (pkg17_content3) completed successfully.")
