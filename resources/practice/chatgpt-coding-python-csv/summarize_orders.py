import csv
from decimal import Decimal, InvalidOperation

total = Decimal('0')
paid_count = 0
with open('orders.csv', encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f)
    required = {'order_id', 'amount', 'status'}
    if not required.issubset(set(reader.fieldnames or [])):
        raise ValueError('缺少必要列')
    for line_number, row in enumerate(reader, start=2):
        try:
            amount = Decimal(row['amount'])
        except (InvalidOperation, TypeError):
            raise ValueError(f'第{line_number}行金额不是有效数字')
        if not amount.is_finite():
            raise ValueError(f'第{line_number}行金额不是有限数值')
        if row['status'].strip() == 'paid':
            total += amount
            paid_count += 1
print(f'已支付条数：{paid_count}')
print(f'已支付金额：{total:.2f}')
