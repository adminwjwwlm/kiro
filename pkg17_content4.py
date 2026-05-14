# Fourth batch - final ~15000+ chars to reach 80000+

# --- C1. Expand Part 1 between 项目服务目标 and 项目服务内容 more ---
idx = find_para_idx('项目实施过程中，将建立严格的过程管理制度', 0)
if idx > 0 and idx < 220:
    ref = doc.paragraphs[idx]
    texts = [
        '项目团队核心成员资质要求如下：项目经理应具有高级工程师职称或同等能力，具备8年以上电力系统工程项目管理经验，参与过3个以上同类规模项目管理工作；技术负责人应具有信息安全相关专业高级职称或CISP/CISSP等专业认证，精通电力监控系统网络安全防护技术，具备5年以上电力网络安全项目技术负责人经验；施工组长应具有中级工程师职称或同等能力，具备3年以上变电站网络安全项目现场施工经验；施工工程师应具有电力、计算机或信息安全相关专业本科以上学历，具备2年以上电力系统网络安全项目实施经验。',
        '项目管理工具和方法包括：（1）使用甘特图进行进度可视化管理，清晰展示64座变电站的施工安排和关键路径；（2）使用WBS（工作分解结构）将项目分解为可管理的工作包，便于任务分配和进度跟踪；（3）使用RACI矩阵明确各项工作的责任分工，避免职责不清和推诿扯皮；（4）使用风险登记册管理项目风险，定期评估风险状态并更新应对措施；（5）使用问题追踪表管理施工过程中发现的各类问题，确保问题闭环处理。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- C2. Expand Part 1 after 多方协调配合复杂度高 ---
idx = find_para_idx('多方协调配合复杂度高', 60)
if idx > 0 and idx < 75:
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts = [
        '从协调配合的实际操作层面分析，本项目需要协调的主要接口包括：（1）与奎屯供电公司调度部门的工作票审批接口——每座变电站进站施工前需提前3个工作日提交工作票，64座变电站至少需要申请60-70份工作票，审批工作量巨大；（2）与奎屯供电公司运维部门的现场配合接口——进站施工需要运维人员到场配合开门、引导、监护等工作；（3）与设备原厂家的技术支持接口——不同品牌设备的探针安装可能需要原厂家提供技术指导或特殊的安装权限；（4）与主站网络安全平台运维人员的联调验证接口——探针安装完成后需要主站侧配合进行数据接收验证和核查调阅。建立高效的多方协调机制，提前规划各方配合的时间和内容，是确保项目按计划推进的关键。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- C3. Expand Part 2 (after 保障地区经济社会发展) ---
idx = find_para_idx('保障地区经济社会发展', 395)
if idx > 0 and idx < 420:
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts = [
        '据统计，奎屯地区110kV变电站年均供电量约50亿千瓦时，服务用户超过30万户。如果因网络安全事件导致关键变电站保护系统误动作或失灵，最严重的情况可能造成大面积停电事故。以一座典型的110kV变电站为例，其供电范围通常覆盖1-3万户居民和数十家企业，一次停电事故的经济损失可能达到数百万元，对社会生活的影响更是难以估量。因此，投入资源加强网络安全防护，从经济角度来看是"用小投入防范大风险"的明智选择。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- C4. Expand Part 1 - 按电压等级分级管理 detail ---
idx = find_para_idx('按电压等级分级管理', 95)
if idx > 0 and idx < 110:
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts = [
        '分级管理的具体实施方案如下：一级管理（220kV变电站）——每站配备1名高级工程师作为技术主管，施工前编制专项技术方案并经技术负责人审批；施工过程实行双人操作和专人监护制度；每步操作后观察时间不少于15分钟；施工全程与调度保持即时通信；施工完成后进行48小时连续监测观察期。二级管理（35kV变电站）——按照标准化模板和作业指导书执行，施工人员按照既定流程操作；单人操作时需有组长远程确认；观察时间不少于10分钟；施工完成后进行24小时监测观察期。通过分级管理，既保证了高压等级变电站的施工安全，又不至于因过度保守而影响35kV变电站的施工效率。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- C5. Expand Part 2 after 精细化安全策略配置决定项目成效 ---
idx = find_para_idx('精细化配置是本项目成败的关键因素', 325)
if idx > 0 and idx < 340:
    ref = doc.paragraphs[idx]
    texts = [
        '精细化配置的技术实现路径为：首先通过设备配置文件和网络拓扑图进行静态分析，确定设备的理论通信关系；然后通过网络抓包工具（在确保安全的前提下）进行动态验证，确认实际通信行为与理论分析的一致性；最后综合静态分析和动态验证结果编写白名单规则，并经过观察期验证后正式启用。整个过程需要施工人员具备较强的网络协议分析能力和电力系统业务理解能力，这也是本项目对施工人员技术水平要求较高的重要原因。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- C6. More Part 2 service content details (关键目录) ---
idx = find_para_idx('关键目录配置', 560)
if idx > 0 and idx < 580:
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts = [
        '关键目录配置完成后的验证方法：（1）在被监控目录下创建一个测试文件，确认系统在规定时间内（通常30秒以内）产生文件创建告警；（2）修改被监控的关键配置文件（如在/etc/hosts中添加一行注释），确认系统产生文件修改告警；（3）删除测试文件，确认系统产生文件删除告警。三项验证全部通过后方可认定该设备的关键目录配置正确有效。验证完成后需及时撤销测试操作，将系统恢复至验证前状态。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- C7. Expand Part 1 more in 项目意义 section ---
idx = find_para_idx('保障地区电力供应安全', 115)
if idx > 0 and idx < 130:
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts = [
        '从供电安全角度进一步分析，奎屯地区地处新疆北疆核心经济带，是连接乌鲁木齐和伊犁的重要交通节点和经济中心。辖区内有石化、纺织、食品加工等多个重点工业企业，这些企业对供电连续性和电能质量有着极高的要求。64座变电站（6座220kV+58座35kV）构成的多层级供电网络，是保障这些企业正常生产和地区经济发展的生命线。加强网络安全防护，防范因网络攻击导致的电力设备误动作或异常停运，直接关系到地区的经济安全和社会稳定。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- C8. Expand Part 2 after 国家安全层面 ---
idx = find_para_idx('国家安全层面的战略意义', 395)
if idx > 0 and idx < 415:
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts = [
        '从国家安全战略高度来看，电力系统作为支撑经济社会运转的基础性命脉工程，其安全防护水平直接关系到国家安全大局。习近平总书记多次强调"没有网络安全就没有国家安全"，对关键信息基础设施保护作出系列重要指示。电力监控系统网络安全监测能力建设是贯彻落实总体国家安全观的具体实践，是维护电力领域关键信息基础设施安全的重要举措。本项目的实施将使奎屯地区35座110kV变电站具备实时化、精细化、体系化的网络安全监测能力，有效提升电力系统应对网络安全威胁的能力水平。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- C9. Expand Part 1 - add more after标准化模板提升35kV站效率 ---
idx = find_para_idx('标准化模板提升35kV站效率', 95)
if idx > 0 and idx < 110:
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts = [
        '标准化模板的具体内容和使用方法：以网络连接白名单模板为例，35kV变电站的典型设备通信关系相对固定——远动装置连接调度主站使用IEC104协议（端口2404）、SCADA服务器连接操作员工作站使用内部通信协议、保信子站连接保信主站等。将这些固定的通信关系模式形成模板文件，施工时只需将模板中的"调度主站IP"、"SCADA服务器IP"等变量替换为该站实际的IP地址即可完成白名单配置。对于58座35kV变电站，预计约70%的白名单规则可以直接从模板生成，仅有30%需要根据该站特殊设备或特殊通信关系单独配置。这种"模板+差异化"的配置方式可以大幅提升效率并降低人为配置错误的概率。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

# --- C10. Expand Part 2 策略精细化目标 ---
idx = find_para_idx('精细化安全策略配置', 310)
if idx > 0 and idx < 320:
    content_idx = idx + 1
    if content_idx < len(doc.paragraphs) and doc.paragraphs[content_idx].text.strip():
        ref = doc.paragraphs[content_idx]
    else:
        ref = doc.paragraphs[idx]
    texts = [
        '策略精细化配置的具体技术要求包括：关键目录方面，Linux系统需配置不少于15个关键监控目录/文件（涵盖系统核心目录、配置文件、用户信息文件等），Windows系统需配置不少于10个关键监控目录/文件（涵盖System32、注册表、驱动目录等）。危险命令方面，Linux系统需配置不少于30条危险命令监控规则（涵盖启停类、操作类、权限类三大类），Windows系统需配置不少于20条危险命令监控规则。网络白名单方面，每台设备的白名单规则数根据其实际通信关系确定，确保覆盖全部合法通信且无多余规则。服务端口白名单方面，每台设备需准确记录所有正在监听的服务端口及对应的服务名称。',
    ]
    current = ref._element
    for t in texts:
        current = insert_after_elem(type('P',(),{'_element':current})(), t, ref)

print("Fourth content batch (pkg17_content4) completed successfully.")
