# 城市更新资料契约

全部楼宇、机构、居民群体、设备、交易及事件均为本地合成，不对应新闻所涉真实主体，不声称新闻中发生这些业务问题。seed.json及各同名Parquet保留完全相同的原始值；actions.json是尚未应用的后续资料。inventory.json仅记录物理大小、摘要及行数，不是业务结论。原始量纲、空值和时区按下文解释。

offers为CNY报价，unit=bag/tonne/m3，pack_kg为包装，含税/运费独立；属性不是预置质量系数。purchases为成交数量/单价/税运分项与offer_id。catalog给型号退出及技术属性，bridges为同月可比调查所见型号，不给价格比。basket_versions按合同/研究给base_month与fixed权重及可替范围，不能用新权重重写旧固定篮子。contract_terms区分公布月/适用工程月/可追溯截止/结清。work_quantities.completed与forecast分开。published_notices仅历史公布原件，actions更正一成交价；split留整月诊断，不用未来桥接支持早期。

work_quantities.base_value_cny是该月按合同基期计价的可调材料基值，不是实际采购金额；adjustable_share乘该基值的指数变化，其他款项不由本资料推导。C-fixed与C-closed保留基期固定篮子，C-flex仅可在同用途且品质可比支持成立时替换；未识别分项允许争议或区间，不能填0。published_notices仅供核对历史结清原依据。actions更正9月成交P102，可改变现行研究及有权追溯的合同，已结清范围保持。
