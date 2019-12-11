import json, csv, datetime
from dateutil.parser import parse

def processData(string, inputDate):
    jdata = json.loads(string)

    row_list = [["Date", "Shop", "Barcode", "Product ID", "Salesman", "Qty", "Price"]]

    product_id = 0
    barcode = 0
    user_id = 0
    qty = 0
    shop_name = ''
    date = ''
    price_unit = 0.00
    grand_total = 0.00

    for var in jdata:

        data = var['data']

        amount_total = data['amount_total']
        grand_total += amount_total

        creation_date = data['creation_date']
        dt = parse(creation_date)
        date = dt.date()
        order_date = date.strftime("%Y-%m-%d")
        if order_date: #== inputDate:
            lists = data['lines']
            user_id = data['user_id']
            shop_name = data['location_id'][1]

            if not lists:
                qty = 0
                price_unit = 0
                product_id = 0
                barcode = 0
                row_list.append([order_date, shop_name, barcode, product_id, user_id, qty, price_unit])

            else:
                for item in lists:
                    qty = item[2]['qty']
                    price_unit = item[2]['price_unit']
                    product_id = item[2]['product_id']

                    pack_lot_ids = item[2]['pack_lot_ids']
                    if not pack_lot_ids:
                        barcode = 0
                        row_list.append([order_date, shop_name, barcode, product_id, user_id, qty, price_unit])
                    for pack_lot_id in pack_lot_ids:
                        # if pack_lot_id != 0:
                        barcode = pack_lot_id[2]['lot_name']
                        row_list.append([order_date, shop_name, barcode, product_id, user_id, qty, price_unit])


    row_list.append(["Grand Total", "", "", "", "", "", grand_total])
    filename = shop_name+'.csv'

    return {'filename': filename, 'data': row_list}
