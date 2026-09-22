---
name: literature2smirks
description: Extract traceable, executable reaction templates from a user-provided chemistry paper or book, preserving source locations, reaction instances, atom mapping, stereochemistry, conditions, applicability, and uncertainty. Use when the user asks to turn literature reaction schemes into SMIRKS or RDKit reaction SMARTS; do not treat a template smoke test as proof of literature fidelity.
metadata:
  short-description: 文献反应到可追溯 SMIRKS / RDKit reaction SMARTS
---

# Literature2SMIRKS

把文献中的反应图、文字通式和实例转化为可审计的反应规则。默认交付 **RDKit reaction SMARTS**，并在每条记录标明方言；只有满足 Daylight 约束时才称作严格 SMIRKS。规则必须能从结构变换追溯回源页，不能把催化剂、溶剂、收率或选择性假装编码进 SMIRKS。

## 工作边界

- 先建立全源文献索引，再选反应条目；保留 PDF 页码与印刷页码。
- 分开记录：源图转录的反应实例、由实例抽象的模板、由通式构造的 demo 例子。
- 反应物、试剂、催化剂和后处理分栏；结构变换与实验可行性分开判断。
- 不把 OCR 文本直接当作结构。含结构的图必须用原图视觉核对，必要时用结构识别或人工重建。
- 对每个模板检查结构解析、原子映射、键变化、正向回放、立体化学和越界匹配；失败底物应记录为反例或限制。
- 多步 one-pot 过程拆成单步规则；无法从证据拆分时输出 `multi_step_unresolved`，不要捏造中间体。

## 推荐流程

1. 固定输入文件哈希，提取文本并建立页级 source map。扫描 PDF 的 OCR 只用于定位，反应结构以渲染页图为准。
2. 定位命名反应标题、反应通式、反应实例和条件。记录 `pdf_page`、`printed_page`、scheme/figure 编号及正文锚点。
3. 逐个反应实例恢复结构，标准化电荷、芳香性、价态、氢和立体化学，给反应原子建立成对 map number。
4. 计算或人工复核断键、成键、键级和原子属性变化，再决定模板需要保留的局部环境。
5. 先写窄的 instance template，再根据同一文献给出的底物范围抽象 literature template。文献外推单独标 `hypothesis`。
6. 用 RDKit `ReactionFromSmarts` 解析并回放至少一个源转录实例；若只有通式，回放只能叫 `constructed_from_general_scheme`。
7. 生成 JSONL/CSV 与人工审阅报告，报告规则状态：`source_transcribed`、`constructed_from_general_scheme`、`hypothesis`、`rejected`。

## 最低记录字段

```json
{
  "rule_id": "LSM-001",
  "name": "named reaction",
  "dialect": "rdkit_reaction_smarts",
  "reaction_smarts": "reactants>>products",
  "source": {"pdf_pages": [56, 57], "printed_pages": [2, 3], "scheme": "general scheme"},
  "evidence_status": "source_transcribed",
  "reaction_center": {"formed": [], "broken": [], "order_changed": []},
  "conditions": {"reagents": [], "solvent": null, "temperature": null},
  "applicability": {"reported_scope": [], "exclusions": [], "selectivity": []},
  "tests": [{"kind": "literature_replay", "status": "pass"}],
  "limitations": []
}
```

## 方言与验证规则

RDKit 的反应语法是由 SMARTS 派生的 reaction SMARTS；它不等同于严格 SMIRKS。对需严格 SMIRKS 的交付，额外检查 mapped atoms、显式氢、变化键的 SMILES 原子表达式以及反应物/产物 map 成对关系。对 RDKit 规则，检查 `RunReactants` 产生的产物、sanitize 状态、重复匹配和手性结果。立体中心应分别标注 retention、inversion、creation、loss 或 unspecified。

## 输出组织

- `data/book_index.json`：全源条目索引。
- `data/rules/*.json`：规则与证据记录。
- `ops/`：提取、渲染、验证脚本。
- `docs/`：开发记录、方言说明和已知限制。
- `private/`：源 PDF 派生文本与页图，默认不提交版本库。

不要输出整本受版权保护的书籍文本；在聊天中只引用必要的短片段和页码，把审阅重点放在结构、规则和证据链上。
