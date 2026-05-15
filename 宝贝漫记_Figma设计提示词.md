# 宝贝漫记 — Figma Make / AI设计工具提示词集

> 适用工具：Figma Make、Google Stitch、即时设计AI、Magic Patterns
> 使用策略：先用AI生成骨架 → 再手动注入"人味"（纹理/手写字/不对称装饰）
> 核心风格关键词：warm cream, picture book, hand-crafted, organic, soft rounded

---

## 一、全局风格设定（所有页面共用）

### 1.1 Figma Make 全局System Prompt

```
You are designing a WeChat mini-program for young mothers (age 25-35) to record their baby's funny/touching moments as AI-generated comic strips.

Design system rules:
- Background: warm cream (#FFFDF7), never pure white
- Primary color: warm coral (#FF8A65) for buttons
- Text color: dark brown (#3E2723) for titles, medium brown (#795548) for body
- Font: rounded sans-serif (similar to Nunito Rounded or 思源圆体)
- Border radius: 16-24px for cards, full rounded for buttons
- Shadows: very soft, warm-toned (rgba(0,0,0,0.06))
- Style: cozy picture book feel, NOT modern/techy/minimal
- Avoid: gradients, glassmorphism, neon colors, sharp corners, pure black text
- Include: subtle paper texture hints, hand-drawn style decorative elements
- Spacing: generous, breathing room, not cramped
- The app should feel like opening a warm handmade storybook
```

### 1.2 配色速查（复制到AI工具）

```
Background colors:
- Page bg: #FFFDF7 (cream white)
- Card bg: #FFF8EE (warm milk)  
- Section bg: #F9F5F0 (light warm gray)

Primary actions:
- Main button: #FF8A65 (warm coral)
- Secondary: #FFB74D (honey yellow)
- Accent: #F06292 (cherry pink)

Text:
- Title: #3E2723 (dark brown)
- Body: #795548 (medium brown)
- Hint/disabled: #BCAAA4 (light brown)

Success/info:
- Success: #81C784 (grass green)
- Link: #64B5F6 (sky blue)
- Special: #CE93D8 (lavender)
```

---

## 二、各页面设计Prompt

### 2.1 创作首页（Tab1 — 核心页面）

```
Design a mobile app home screen for a baby moment recording app.

Layout (top to bottom):
1. Status bar area (leave space)
2. A small decorative cloud illustration floating at top-right (hand-drawn style, very subtle)
3. Title: "记录宝贝的高光时刻" with a small star emoji, using rounded bold font, dark brown color
4. Large text input area with rounded corners (20px radius), cream background, with placeholder text "今天宝宝做了什么有趣的事？说了什么好玩的话？" in light brown
5. Inside input area bottom-left: a microphone icon button with "语音" label
6. Inside input area bottom-right: character count "200字以内" in very light text
7. Below input: a "💡今日灵感：宝宝今天模仿谁了？" text link in warm brown
8. Large full-width rounded button at bottom: "✨ 开始创作漫画" in white text on coral (#FF8A65) background
9. Bottom tab bar with 4 icons: pencil (创作), book (回忆), baby face (角色), person (我的)

Style notes:
- Overall feel: like a page from a children's picture book
- Background: cream white (#FFFDF7)
- No sharp edges anywhere
- The input area should feel like a paper notepad
- Tab bar is minimal, using warm brown icons
- The create tab icon should be slightly larger than others (it's the core function)
- Add very subtle paper grain texture to the background
```

### 2.2 风格选择页

```
Design a mobile screen for selecting comic art style.

Layout:
1. Top bar: "← 返回" on left, "跳过(用推荐)" on right in light text
2. Title: "选一种画风吧 🎨" in rounded bold font
3. Subtitle: "让AI用你喜欢的风格来画" in smaller light brown text
4. AI Recommendation card (featured, larger):
   - Label: "⭐ AI推荐" badge
   - Style name: "温馨绘本风" in bold
   - Reason: "适合这个温暖的故事" in small italic text
   - Preview image: a warm, soft comic panel preview (placeholder)
   - This card has a subtle golden glow border
5. Below: horizontal scrollable row of smaller style cards (4 visible):
   - Each card: square preview image + style name below
   - Style names: "日式治愈风", "搞笑漫画风", "Q版萌系风", "复古怀旧风"
   - Cards have 12px rounded corners and light shadow
6. Bottom: full-width coral button "✨ 用「温馨绘本风」画吧"

Style:
- Cards should look like collectible stickers or small paper cards
- The AI recommendation should stand out but not be aggressive
- Warm cream background throughout
- Preview images should have rounded corners matching the cards
```

### 2.3 生成等待页

```
Design a mobile loading/waiting screen for AI generating a comic.

Layout (centered, full-screen immersive):
1. No navigation bar (full immersion)
2. Center area:
   - An illustration of a pencil drawing wavy lines (suggesting "drawing in progress")
   - Text below: "AI正在画画中..." in medium brown
3. Below center: a progress bar at 72%, using coral color fill on cream track
   - Rounded ends on progress bar
4. Below progress: a card with "💡 创作小贴士：" header
   - Tip text: "试试多描述一些细节，比如宝宝当时的表情和动作，画面会更生动哦～"
   - Card has light warm background (#FFF8EE) with rounded corners
5. Bottom text: "小土豆的第 7 幅漫画即将诞生 🌱" in warm brown, centered

Style:
- This page should feel calm and anticipatory, like waiting for a gift to be unwrapped
- The pencil animation area should look playful and hand-drawn
- Background: warm cream
- No distracting elements - very focused
- The progress bar should feel gentle, not urgent
- Overall mood: cozy patience, not anxious waiting
```

### 2.4 作品展示页（生成完成）

```
Design a mobile screen showing a generated 4-panel comic result.

Layout:
1. Top: "← 返回" left, "⋯ 更多" right
2. Main area - a large card containing:
   - 4-panel comic grid (2x2), each panel is a placeholder image with rounded inner corners
   - Below the comic grid inside the card:
     - Quote marks with text: "妈妈！我是宇航员！我要飞到月亮上给你摘星星！"
     - Using a handwriting-style font
     - Divider line
     - "── 小土豆 · 2岁7个月 ──" centered
     - "2026年5月15日" in small light text
   - The entire card has 16px rounded corners and soft shadow
3. Below card - action buttons row:
   - Left: small gray "💾 保存" button
   - Right: large coral "📤 分享" button (2.5x wider than save)
4. Below buttons: centered text link "🔄 换一种画法" in light brown

Style:
- The card should look like a premium postcard or greeting card
- The quote area should feel handwritten and warm
- "分享" button must be visually dominant (larger, coral color, full rounded)
- "保存" button is intentionally understated (small, gray outline)
- Background: cream white
- The overall feel: "look at this beautiful thing I created"
```

### 2.5 回忆时间轴页（Tab2）

```
Design a mobile timeline/feed screen showing baby's comic history.

Layout:
1. Header area:
   - Title: "小土豆的成长漫画 📖" in bold rounded font
   - Subtitle: "已记录 47 个瞬间" in small warm text
   - A prominent button/card: "🎬 生成回忆视频" with subtitle "让47个瞬间动起来"
2. Timeline entries grouped by month:
   - Month header: "── 2026年5月 ──" with subtle line decorators
   - Each entry:
     - Date + age: "15日 · 2岁7个月" in small text
     - Row with: comic thumbnail (small square, rounded) + quote "我是宇航员！" + style badge "温馨绘本风"
   - Multiple entries per month
3. At the very bottom of the scroll: "🎂 2024年10月 · 出生" with a special milestone marker
4. Bottom tab bar (same as home page)

Style:
- This should feel like a scrapbook or diary
- Thumbnails are small and cozy, not clinical
- The timeline has a vertical line on the left connecting entries (optional, subtle)
- Month separators use a gentle decorative style
- Video button should feel exciting but not jarring
- Overall mood: nostalgia, growth, pride in accumulation
```

### 2.6 角色库页（Tab3）

```
Design a mobile screen showing a character/avatar library.

Layout:
1. Title: "我的角色 👶" in bold rounded font
2. Character selector row (horizontal scroll):
   - Character cards: avatar image + name + age
   - First card has a star badge (currently active): "🌟 小土豆, 2岁7月"
   - Second: "妈妈"
   - Last: "+ 新增" (add new) in dashed border style
3. Section title: "── 小土豆的角色卡 ──"
4. 3x3 grid of style cards:
   - Each card: character rendered in that art style (placeholder) + style name below
   - Style names: 日漫风, 美漫风, 韩漫风, 萌系风, Q版风, 3D渲染, 半写实, 水彩风, 像素风
   - Cards have equal spacing, rounded corners (12px)
5. Below grid: a text button "🔄 更新照片(宝宝长大了？)" in warm brown
6. Bottom tab bar

Style:
- The grid should feel like a sticker collection or trading card collection
- Each style card is like a mini portrait in different art styles
- The "active character" selector should have a subtle glow or border highlight
- The "add new" card uses dashed border to differentiate from content cards
- Feel: collectible, fun, pride in having multiple styles
```

### 2.7 分享卡片设计

```
Design a shareable card image (vertical, 9:16 ratio) for social media posting.

Layout (this is the image that gets shared to WeChat Moments):
1. Top 60%: 4-panel comic in 2x2 grid with small gaps between panels
2. Below comic: 
   - Quote in handwriting font: "妈妈！我是宇航员！我要飞到月亮上给你摘星星！"
   - Horizontal divider line (subtle, decorative)
   - "🌱 小土豆 · 2岁7个月"
   - "📅 2026年5月15日"
3. Bottom section (small, restrained):
   - Brand area with cream background
   - "📖 宝贝漫记" logo/text
   - "用AI记录宝贝的每个高光时刻" tagline
   - QR code (small, bottom right) with "长按识别体验 →" text

Style:
- This should look like a premium greeting card, NOT an advertisement
- The brand area must be subtle (occupies max 15% of height)
- QR code is small and doesn't dominate
- Overall feel: "I want to share this because it's beautiful and touching"
- Background: cream with very subtle paper texture
- The comic panels are the hero - everything else serves them
- Someone seeing this should think "how cute!" not "this is an ad"
```

### 2.8 视频创建页 — 选择模板

```
Design a mobile screen for choosing a video template to create a memory video.

Layout:
1. Top: "← 返回" + title "创建回忆视频"
2. Section title: "选一个故事模板 🎬" + subtitle "不同模板，不同的叙事节奏"
3. Featured AI recommendation card (larger):
   - Badge: "⭐ AI推荐"
   - Title: "🎂 生日回顾"
   - Subtitle: "小土豆下周就3岁啦！"
   - Info: "约60秒 · 精选10-20张"
   - A preview area showing subtle animation hint (film strip style)
4. Grid of other templates (2x2):
   - "📅 年度成长" - "2-3分钟 · 20-30张"
   - "🌙 月度精选" - "30-45秒 · 5-10张"
   - "🎬 自由编排" - "自定义 · 自选"
   - "🌟 里程碑集锦" - "60秒 · 自动选"
5. Bottom button: "✨ 用「生日回顾」开始" in coral

Style:
- Template cards should look like movie posters or DVD covers (but cute)
- The AI recommended card should feel special/exciting
- Each template card has a distinct small emoji icon
- Warm cream background
- The page should make the user feel "this is going to be amazing"
```

### 2.9 视频播放/结果页

```
Design a mobile screen showing a completed memory video with playback.

Layout:
1. Top: "← 返回" + "⋯ 更多"
2. Video player area (takes up top 50% of screen):
   - Rounded corners (16px)
   - Play button overlay in center
   - Progress bar at bottom: "▶ 00:32 / 01:05"
   - Dark overlay with subtle vignette
3. Below video - info card:
   - Title: "🎬 小土豆的3岁生日回顾" in bold
   - Meta: "📅 2025.10 → 2026.05 | 🖼️ 12张漫画 · 65秒 | 🎵 温馨钢琴曲"
4. Action buttons:
   - Row 1: "💾 保存" (small, gray) + "📤 分享给家人" (large, coral)
   - Row 2: "📺 发布到视频号" (full-width, special gradient or accent color)
5. Bottom text links: "🔄 重新生成" + "✏️ 修改设置"

Style:
- Video player area should feel cinematic (slightly dark background behind it)
- The "发布到视频号" button should have a special treatment (gradient or glow) since it's the growth lever
- Info card is clean and informative
- Overall feel: pride in creation, eagerness to share
- The share button should be the most prominent action
```

---

## 三、Midjourney配图Prompt（生成示例漫画素材）

### 3.1 温馨绘本风示例

```
A 4-panel comic strip about a toddler wearing a bowl as a space helmet, announcing "I'm an astronaut!" to their mom. Warm watercolor picture book style, soft cream and peach tones, rounded character designs, gentle expressions, cozy home interior background, hand-drawn quality, subtle paper texture, children's book illustration, warm lighting --ar 1:1 --style raw --v 7
```

### 3.2 搞笑漫画风示例

```
A 4-panel comic strip of a 2-year-old baby trying to feed their teddy bear with a spoon, making a huge mess, exaggerated funny expressions, bold dynamic lines, bright saturated colors, manga-style speed lines, comic sound effects in Chinese characters, playful and energetic, slightly imperfect hand-drawn style --ar 1:1 --style raw --v 7
```

### 3.3 Q版萌系风示例

```
A cute chibi-style 4-panel comic of a toddler imitating their father's serious work face, 2-head-body proportion, big sparkly eyes, rosy cheeks, pastel candy colors, kawaii aesthetic, soft rounded everything, tiny cute details, slightly imperfect line work to feel hand-drawn, warm cream background --ar 1:1 --style raw --v 7
```

### 3.4 角色卡示例（9种风格的同一个宝宝）

```
Portrait of a happy 2-year-old Chinese toddler with short hair and round cheeks, [STYLE] art style, bust shot, looking at viewer with a bright smile, clean background, high quality character design, suitable for avatar/profile picture --ar 1:1 --style raw --v 7

[STYLE] variations:
- "Japanese anime, big expressive eyes, Ghibli-inspired colors"
- "Marvel comic book style, bold lines, heroic pose"
- "Korean webtoon, soft lighting, delicate features"
- "chibi/super-deformed, 3-head body ratio, extremely cute"
- "Pixar 3D rendered, subsurface scattering, warm lighting"
- "semi-realistic digital painting, between photo and illustration"
- "watercolor, wet-on-wet technique, soft edges"
- "pixel art, 16-bit style, limited color palette"
- "kawaii/moe style, huge eyes, pink cheeks, soft pastel"
```

---

## 四、去AI味检查清单

在AI生成设计后，逐项手动调整：

| 检查项 | AI的坏习惯 | 手动修复 |
|--------|-----------|---------|
| 对称性 | 所有元素完美对称 | 把装饰云朵/星星往左偏移3-5px |
| 颜色一致 | 每个灰色都是同一个值 | 每个section的背景色差1-2个色号 |
| 字体大小 | 整齐划一的字号阶梯 | 标题手动调大/小1px制造"呼吸感" |
| 间距 | 数学上完美等间距 | 某些区块的上间距比下间距大4px |
| 圆角 | 所有卡片同一圆角 | 主卡片16px，小标签12px，按钮24px |
| 投影 | 完美均匀的box-shadow | 某些卡片投影偏下1px（模拟光源方向） |
| 图标风格 | 完美的几何图标 | 选择略带手绘感的图标，或手动加1px不规则 |
| 背景 | 纯色平涂 | 叠加5%透明度的纸质纹理图层 |
| 文案排版 | AI生成的整齐段落 | 加入手写字体标注、手绘箭头标注 |
| 色彩饱和度 | 所有颜色饱和度一致 | 背景色降饱和，重点色略提饱和 |

---

## 五、产品截图Mock-up Prompt

生成手机截图用于展示/汇报：

```
A realistic iPhone 15 Pro mockup showing a baby comic app screen, phone held at slight angle, warm natural lighting, soft shadow on cream marble surface, with small baby toys blurred in background, cozy morning light atmosphere, product photography style --ar 3:4 --v 7
```

---

> 使用建议：先用2.1-2.9的prompt在Figma Make/Google Stitch中生成页面骨架，然后按照第四节的检查清单逐项"去AI味"，最后用第三节的Midjourney prompt生成示例漫画填充到设计稿中。
