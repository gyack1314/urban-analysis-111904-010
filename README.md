# 材料换型后的工程价格指数与调差解释

本项目保留城市更新研究场景的本地合成原始资料和物理读取工具。统计分析应用尚未实现；没有预计算估计、分类、预测、风险排行或方案答案。资料能读取不代表其足以支持任意业务判断。

Python 3.11 与 requirements.txt 中固定的分析依赖配合使用。安装命令为 python -m pip install -r requirements.txt。运行 python -m materials inputs 校验摘要、大小、Parquet物理行数并经DuckDB实际读取。python -m unittest discover -s tests -v 核对JSON/Parquet值一致、损坏拒绝和领域原件引用。

容器用法为 docker build -t urban-materials .，再运行 docker run --rm urban-materials；输入测试使用 docker run --rm urban-materials python -m unittest discover -s tests -v。原件检查不连接真实业务系统。

inputs/保存原始观测及研究窗口，docs/input-contract.md说明语义。materials.build_inputs只重建同值Parquet与物理清单，不产生分析结果。actions.json内的新资料尚未处理；原件应保留，后续产品结果另存。实际分析接口、方法适用性和业务验证须在功能实现后补充，现有输入测试不替代未来产品验收。
