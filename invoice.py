class Invoice:

    

    def __init__(self, part_number , part_description , product_qty , product_price):
        self.part_number=part_number
        self.part_description=part_description
        self.product_qty=product_qty
        self.product_price=product_price


    def set_part_number(self,part_number):
        self.part_number=part_number

    def set_part_description(self,part_description):
        self.part_description=part_description

    def set_quantity(self,product_qty):
        self.product_qty=product_qty

    def set_price(self,price):
        self.price=price +20






    
    


