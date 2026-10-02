# 规则证据与范围审计 011

- **日期**：2026-10-03
- **审计脚本**：`ops/audit_provenance.py`
- **结果文件**：`docs/provenance-audit-011.json`

本轮新增 Heck 烯烃芳基化的页面核对回放后，115 条规则全部具备来源页证据、通过的正向回放和通过的负向控制；其中 100 条为 `source_general_scheme`，15 条为 `source_transcribed`。`ops/audit_rules.py` 确认 115/115 条反应 SMARTS 可解析，15/15 条来源转录回放通过。严格 SMIRKS lint 统计为 45 条可通过、70 条需要审阅。

该审计证明的是数据记录完整性、回放控制和证据字段覆盖，不证明所有通式都等价于书中某个具体底物，也不证明实验条件、选择性或底物范围可直接外推。
