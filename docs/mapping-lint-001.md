# 原子映射与方言审计 001

- **日期**：2026-10-03
- **脚本**：`ops/classify_dialect.py`
- **规则总数**：116
- **map 集合一致、可进入严格 SMIRKS 初筛**：49
- **存在离去基团或其他 map 差异、需要审阅**：67

脚本逐条从 reaction SMARTS 两侧提取原子 map 集合，并重写 `strict_smirks_lint` 字段。该初筛只检查映射集合一致性，不证明 Daylight 语法、键变化语义、立体化学或实验有效性。
