import json, csv, datetime
from dateutil.parser import parse

def processData(string, inputDate):
    jdata = json.loads(string)

    row_list = [["Shop", "Barcode", "Product ID", "Salesman", "Qty"]]

    product_id = 0
    barcode = 0
    user_id = 0
    qty = 0
    shop_name = ''
    date = ''

    for var in jdata:

        data = var['data']
        
        creation_date = data['creation_date']
        dt = parse(creation_date)
        date = dt.date()
        order_date = date.strftime("%Y-%m-%d")
        if order_date == inputDate:
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

    filename = shop_name+'.csv'

    return {'filename': filename, 'data': row_list}
