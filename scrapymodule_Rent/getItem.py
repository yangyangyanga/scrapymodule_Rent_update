# 2018/02/08 修改表tmp_shool_major
def get_item(itemClass):
    item = itemClass()
    item["housing_type"] = ""
    item["available_time"] = ""
    item["house_name"] = ""
    item["room_type"] = ""
    item["car_spaces"] = ""
    item["lease"] = ""
    item["address"] = ""
    item["detaile_address"] = ""
    item["supporting_facilities"] = ""
    item["price"] = ""
    item["isRent"] = "1"
    item["postal_code"] = ""
    item["picture"] = ""
    item["housing_introduce"] = ""
    item["supplier_type"] = ""
    item["supplier_name"] = ""
    item["supplier_logo"] = ""
    item["country"] = ""
    item["city"] = ""
    item["contact_name"] = ""
    item["contact_phone"] = ""
    item["contact_email"] = ""
    item["url"] = ""
    return item