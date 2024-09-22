def salary(hours, hourly_pay, bonus=0):
    return hourly_pay * hours + bonus
# 詢問使用者輸入
hours_input = int(input("請輸入工作時數："))
hourly_pay_input = int(input("請輸入時薪："))
bonus_input = int(input("請輸入獎金："))

# 計算薪資
salary_total = salary(hours_input, hourly_pay_input, bonus_input)

# 輸出結果
print(f"工作時數{hours_input}、時薪{hourly_pay_input}、獎金{bonus_input}的薪資為 {salary_total}")
