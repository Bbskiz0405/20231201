# 定義營業額和獲利率數據
revenues = [1550000, 2000000, 2234000]  # 營業額
profit_margins = [3.09, 5.23, 5.47]  # 獲利率

# 使用 for 迴圈來格式化和印出每年的財務數據
for i in range(len(revenues)):
    formatted_revenue = f"{revenues[i]:,}"  # 格式化營業額加上千分位
    formatted_profit_margin = f"{profit_margins[i]:.2f}%"  # 格式化獲利率為百分比表示法
    print(f"年度: {105 + i}, 營業額: {formatted_revenue}, 獲利率: {formatted_profit_margin}")
