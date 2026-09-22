# 数据语义

`book_index.json` 是源条目清单，不代表规则已经完成。`rules_demo.json` 是第一轮规则抽象的可执行 scaffold，已绑定源章节证据：100 条记录与书中前 100 个条目关联，规则通过 RDKit smoke test，但 `evidence_status=source_general_scheme`，并带有源页、文本哈希和证据定位，不能当作书中某个底物实例的转录。

正式规则必须追加 `source_transcribed` 测试，包含原图中反应物和产物的 canonical SMILES、map 对应、结构图页码和期望产物比较。若规则无法唯一恢复，使用 `rejected` 或 `multi_step_unresolved`，不要填入猜测结构。
