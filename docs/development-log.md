# Literature2SMIRKS 开发记录

## 2026-09-15 · 启动

- 按用户要求设立至少七小时的持续工作目标；七小时是最低时长，不替代交付验收。
- 输入为 Kürti 与 Czakó 的 *Strategic Applications of Named Reactions in Organic Synthesis*，816 页扫描 PDF，带有质量不均的 OCR 层。
- 全书主体为 250 个双页反应条目。正文印刷页 2 对应 PDF 第 56 页；必须保留两套页码。
- 本地 RDKit 版本 2026.03.5；主产物模板采用 `rdkit_reaction_smarts` 方言，不能声称等同于严格 Daylight SMIRKS。
- 全文 OCR、原始页图和本地路径留在被 git 忽略的 `private/`。公开产物使用独立编写的规则、测试、阅读笔记及页码引用。
- 初始阅读策略：OCR 用于正文，原生视觉核对反应结构；需要时再启用光学结构识别。
- 当前仅完成输入盘点与全文本地提取，尚未宣称全文阅读、任何反应验证或发布完成。

## 数据语义

每条模板绑定命名反应条目和源页。教学实例若为根据通式自行选取的小分子，必须标注为 `constructed_from_general_scheme`，不可称作书中真实底物回放。实际文献结构另设 `source_transcribed` 测试。规则的产品集合、歧义、选择性限制及未建模条件分别记录。

## 2026-09-22 · 恢复与第一轮 demo

- 从持久化状态恢复；未重新生成源 PDF 派生物。
- `data/book_index.json` 已生成 250 条条目，PDF 第 56 页对应印刷第 2 页。
- `data/rules/rules_demo.json` 已生成前 100 个条目，全部含 `dialect=rdkit_reaction_smarts`、书目页码和限制说明。
- `ops/validate_demo.py`：100/100 通过 `ReactionFromSmarts` 与至少一个 `RunReactants` product-set smoke test。RDKit 对未出现在产品侧的 mapped leaving groups 发出警告；该警告被保留为后续严格映射审查项，不计为文献验证通过。
- 已渲染并准备视觉核对 acetoacetic ester、acyloin、ene、aldol、alkene metathesis 前五个章节（PDF 56–65）。
- 规则抽取下一步是从这些页的 scheme 逐图转录至少一批 `source_transcribed` 实例，并替换相应 demo 条目。
