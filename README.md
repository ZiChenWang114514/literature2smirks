# Literature2SMIRKS

Literature2SMIRKS 是一个面向有机合成文献的反应规则抽取 skill：从论文、补充信息或反应书籍中定位反应图和文字通式，建立结构化证据，再输出带来源、适用范围和验证状态的 RDKit reaction SMARTS。

## 当前进度

- 已固定并哈希输入书籍：816 页，250 个命名反应条目。
- 已建立完整条目索引，保留 PDF 页码与印刷页码。
- 已建立前 100 条规则 demo scaffold；100/100 通过 RDKit 解析与正向 smoke test。
- 当前 100 条的状态是 `constructed_from_general_scheme`。这表示它们由书中通式和反应类别重建，用于开发验证，不等同于逐图转录或文献实例回放。
- 正式发布前仍需对源图结构进行视觉核对、补充 `source_transcribed` 实例、检查原子映射、立体化学和范围外匹配。

## 目录

```text
SKILL.md                       skill 入口
data/book_index.json           250 条书目索引
data/rules/rules_demo.json     100 条可执行 demo 规则
ops/prepare_source.py          固定输入并生成页级清单
ops/read_source.py             按页读取或渲染源文件
ops/validate_demo.py            RDKit 解析与回放 smoke test
docs/schema.md                 数据状态与证据语义
private/                       本地源派生物，已 gitignore
```

## 使用

```powershell
python ops/prepare_source.py "C:\path\to\book.pdf"
python ops/read_source.py 56-65 --render
python ops/validate_demo.py
```

规则字段中的 `dialect` 必须保留。RDKit reaction SMARTS 与严格 Daylight SMIRKS 有语义差异；本项目不会用名称替代方言声明，也不会把模板解析成功解释为实验可行性证明。

## 许可与来源

本仓库只提交索引、规则数据、测试和处理脚本，不提交用户提供的 PDF 或其大段可替代文本。书籍来源：Laszlo Kürti、Barbara Czakó，*Strategic Applications of Named Reactions in Organic Synthesis*（Academic Press/Elsevier，2005）。
