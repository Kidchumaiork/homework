def vatcalculate(totalprice):
    result = totalprice+(totalprice*7/100)
    return result

print(vatcalculate(int(input("Price :"))))