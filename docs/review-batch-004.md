# 原书审阅批次 004

- 来源：`Strategic Applications of Named Reactions in Organic Synthesis`
- PDF 页面：116–135
- 印刷页码：62–81
- 目录条目：KCC031–KCC040
- 审阅日期：2026-09-22

本批次先读取可选择文本，再对 PDF 116、120、132 页进行渲染核对。渲染页确认标题、反应箭头、条件和代表性示意图均可定位；其余页面保留 `rendered_pending_manual`，避免把文本抽取结果当作结构图验证。

## 条目记录

| ID | 反应 | 文字状态 | 视觉状态 | 备注 |
|---|---|---|---|---|
| KCC031 | Bischler–Napieralski isoquinoline synthesis | complete | complete | 酰化苯乙胺经脱水/环化；书中同时给出 α-羟基底物的进一步脱水 |
| KCC032 | Brook rearrangement | complete | rendered_pending_manual | 需区分硅迁移与底物取代模式，暂不生成精确规则 |
| KCC033 | Brown hydroboration reaction | complete | complete | 反应图显示烯烃逐步形成 mono-/di-/trialkylborane；区域/立体选择性和后续氧化属于额外步骤 |
| KCC034 | Buchner method of ring expansion | complete | rendered_pending_manual | 卡宾插入芳环并扩环，底物和重排选择性需图级确认 |
| KCC035 | Buchwald–Hartwig cross-coupling | complete | rendered_pending_manual | 胺化偶联；配体、碱、卤素/伪卤素范围需要结构级核对 |
| KCC036 | Burgess dehydration reaction | complete | rendered_pending_manual | 脱水条件依赖底物和试剂形式，暂不把通用箭头当作可执行映射 |
| KCC037 | Cannizzaro reaction | complete | rendered_pending_manual | 非烯醇化醛的歧化；产物计量与底物约束需保留 |
| KCC038 | Carroll rearrangement (Kimel–Cope) | complete | rendered_pending_manual | β-keto ester 烯丙基酯重排/脱羧，存在串联步骤 |
| KCC039 | Castro–Stephens coupling | complete | complete | 图示芳基/乙烯基卤化物与端炔的铜介导偶联；邻位双官能团实例还会继续环化 |
| KCC040 | Chichibabin amination reaction | complete | rendered_pending_manual | 杂芳环亲核胺化，区域选择性依赖环系和离去基 |

## 规则状态

本批次没有新增 `source_transcribed` 规则。现有 100 条 demo 规则仍是带有原书章节定位和文本哈希的 `source_general_scheme` 可执行 RDKit reaction SMARTS；只有在原书结构图、原子映射和产物边界能够逐项核对时才升级为 `source_transcribed`。本批次的图示足以确认反应身份和条件语境，但不足以安全地把复杂环化、多步串联或选择性依赖步骤压缩成单一模板。
