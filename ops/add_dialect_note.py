from pathlib import Path
p=Path('SKILL.md'); s=p.read_text(encoding='utf-8'); needle='立体中心应分别标注 retention、inversion、creation、loss 或 unspecified。'; s=s.replace(needle,needle+'\n\n运行 `ops/classify_dialect.py` 对反应物侧和产物侧 map 集合做结构 lint。存在被删除的 leaving-group map 时，规则可以继续作为 RDKit reaction SMARTS，但不得标为 `strict_smirks_eligible`。'); p.write_text(s,encoding='utf-8')
