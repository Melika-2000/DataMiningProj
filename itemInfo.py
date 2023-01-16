
class ItemsInfo:
    inputPerYear = {}
    outputPerYear = {}
    operatedItemPerYear = {}
    topOperatedItemPerYear = {}

    # for each item in a year
    def __init__(self, item_id, consumer_id, create_year, operation_year):
        self.id = item_id
        self.item_count = 1
        self.create_year = create_year
        self.operation_year = operation_year
        self.consumers = {}
        self.top_consumer = consumer_id
        self.top_consumer_purchase_count = 1
        self.__add_new_consumer(consumer_id)
        self.update_output_per_year_counter(operation_year)
        self.update_input_per_year_counter(create_year)

    def add_item_count(self):
        self.item_count += 1

    def update_item_info(self, consumer_id, create_year, operation_year):
        if consumer_id not in self.consumers.keys():
            self.__add_new_consumer(consumer_id)
        else:
            self.__update_consumer_purchase(consumer_id)
        self.add_item_count()
        self.update_input_per_year_counter(create_year)
        self.update_output_per_year_counter(operation_year)

    def __add_new_consumer(self, consumer_id):
        self.consumers[consumer_id] = 1

    def __update_consumer_purchase(self, consumer_id):
        purchase_count = self.consumers[consumer_id]
        self.consumers[consumer_id] = purchase_count + 1

    def update_input_per_year_counter(self, create_year):
        if create_year not in ItemsInfo.inputPerYear.keys():
            ItemsInfo.inputPerYear[create_year] = 1
        else:
            item_count = ItemsInfo.inputPerYear[create_year]
            ItemsInfo.inputPerYear[create_year] = item_count + 1

    def update_output_per_year_counter(self, operation_year):
        # calculate overAll output
        if operation_year not in ItemsInfo.outputPerYear.keys():
            ItemsInfo.outputPerYear[operation_year] = 1
        else:
            item_count = ItemsInfo.outputPerYear[operation_year]
            ItemsInfo.outputPerYear[operation_year] = item_count + 1
        # calculate output per item
        key = str(self.operation_year) + "_" + str(self.id)
        if key not in ItemsInfo.operatedItemPerYear.keys():
            ItemsInfo.operatedItemPerYear[key] = 1
        else:
            item_count = ItemsInfo.operatedItemPerYear[key]
            ItemsInfo.operatedItemPerYear[key] = item_count + 1

    def update_top_consumer_per_year(self): #for each item
        max_count = 0
        for consumer_id in self.consumers.keys():
            purchase_count = self.consumers[consumer_id]
            if purchase_count > max_count:
                max_count = purchase_count
                self.top_consumer = consumer_id
                self.top_consumer_purchase_count = purchase_count

    def get_top_consumer_purchase_count(self):
        self.update_top_consumer_per_year()
        return self.top_consumer_purchase_count

    def get_top_consumer(self):
        self.update_top_consumer_per_year()
        return self.top_consumer

    def get_item_count(self):
        return self.item_count

    @staticmethod
    def get_top_operated_item_per_year(year):
        max_item_count = 0
        max_item_id = 0
        for key in ItemsInfo.operatedItemPerYear.keys():
            if str(year) in key:
                item_count = ItemsInfo.operatedItemPerYear[key]
                if item_count > max_item_count:
                    max_item_count = item_count
                    max_item_id = int(key.split("_")[1])  # extract id from key
        return max_item_id, max_item_count