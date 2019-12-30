import json, csv, datetime
from dateutil.parser import parse

string = """[{"id":"47131-002-0001","data":{"name":"Order 47131-002-0001","amount_paid":1000,"amount_total":690,"amount_tax":33,"amount_return":310,"lines":[[0,0,{"qty":1,"price_unit":690,"discount":0,"product_id":49064,"tax_ids":[[6,false,[1]]],"id":1,"pack_lot_ids":[[0,0,{"lot_name":"188714016073454","is_customer_return":false,"is_customer_claim":false}]],"sales_user_id":643}]],"statement_ids":[[0,0,{"name":"2019-12-08 06:04:17","statement_id":512250,"account_id":27,"journal_id":6,"amount":1000}]],"pos_session_id":47131,"partner_id":false,"disctype_id":false,"user_id":26,"uid":"47131-002-0001","sequence_number":1,"creation_date":"2019-12-08T06:04:17.000Z","fiscal_position_id":false,"location_id":[85,"43, ELEPHANT ROAD"],"foc_reference_info":null,"pos_mobile_no":null}}]"""
jdata = json.loads(string)
# print (type(jdata))

row_list = [["Shop", "Barcode", "Product ID", "Salesman", "Qty"]]

product_id = 0
barcode = 0
user_id = 0
qty = 0
shop_name = ''
date = ''
grand_total = 0.00

for var in jdata:

    data = var['data']

    amount_total = data['amount_total']
    grand_total += amount_total
    print(amount_total)

    creation_date = data['creation_date']
    dt = parse(creation_date)
    date = dt.date()
    order_date = date.strftime("%Y-%m-%d")
    if order_date == "2019-12-08":
        lists = data['lines']
        user_id = data['user_id']
        shop_name = data['location_id'][1]

        for item in lists:
            qty = item[2]['qty']
            product_id = item[2]['product_id']

            pack_lot_ids = item[2]['pack_lot_ids']
            for pack_lot_id in pack_lot_ids:
                barcode = pack_lot_id[2]['lot_name']

        row_list.append([shop_name, barcode, product_id, user_id, qty])

        print(product_id)
        print(barcode)
        print(user_id)
        print(qty)
        print(shop_name)
print(grand_total)
# row_list.append(['GRAND TOTAL', '', '', '', grand_total])

filename = shop_name+'.csv'

with open(filename, 'w', newline='') as csvfile:
    writer =  csv.writer(csvfile)
    # writer.writerow(["Shop", "Barcode", "Product ID", "Salesman", "Qty"])
    # writer.writerow(["43", barcode, product_id, user_id, qty])
    writer.writerows(row_list)

    # print(lists)
