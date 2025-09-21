import MyLinkedList

class Train:

    def __init__(self):
        self.wagons = MyLinkedList.MyLinkedList()

    def validate(self):

        if len(self.wagons) == 0:
            return False

        if self.wagons._size <= 10 and self.wagons.head.data.type != "Locomotive":
            return False

        if self.wagons._size > 10:
            if self.wagons.head.data.type != "Locomotive" or self.wagons.tail.data.type != "Locomotive":
                return False
        
        seen_goods = False
        seen_sleep_block = False
        sleep_block_done = False
        dining_seen = False
        seat_before_dining = False

        for wagon in self.wagons:

            parts = wagon.type.split(":", 1)
            category = parts[0]
            subtype = parts[1] if len(parts) > 1 else None


            if wagon.type == "Goods":
                seen_goods = True
            if seen_goods and category == "Passenger":
                return False

            if category == "Passenger" and subtype == "Sleep": 
                seen_sleep_block = True
                
            if subtype != "Sleep" and seen_sleep_block: 
                sleep_block_done = True
                
            if sleep_block_done and subtype == "Sleep":
                return False
            
            if category == "Passenger" and subtype == "Dining":
                dining_seen = True

            if category == "Passenger" and subtype == "Seat" and not dining_seen:
                seat_before_dining = True

            if category == "Passenger" and subtype == "Sleep":
                if seat_before_dining and not dining_seen:
                    return False
                
                
        return True



