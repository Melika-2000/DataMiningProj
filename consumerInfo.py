
class ConsumerInfo:

    #for each consumer in a year
    def __init__(self, consumer_id, item_id, created_year, operation_year):
        self.consumer_id = consumer_id
        self.purchase_count = 1
        self.mostPurchasedItem = item_id
        self.mostPurchasedItemCount = 1
        self.purchasedItems = {}
        self.inputPerYearCount = {}
        self.outputPerYearCount = {}
        self.__add_new_item(item_id)
        self.__update_input_per_year(created_year)
        self.__update_output_per_year(operation_year)

    def __add_new_item(self, item_id):
        self.purchasedItems[item_id] = 1

    def __update_item_purchase(self, item_id):
        purchase_count = self.purchasedItems[item_id]
        self.purchasedItems[item_id] = purchase_count + 1

    def update_consumer_info(self, item_id, create_year, operation_year):
        if item_id not in self.purchasedItems.keys():
            self.__add_new_item(item_id)
        else:
            self.__update_item_purchase(item_id)
        self.add_purchase_count()
        self.__update_input_per_year(create_year)
        self.__update_output_per_year(operation_year)

    def add_purchase_count(self):
        self.purchase_count += 1

    def __update_input_per_year(self, year):
        if year not in self.inputPerYearCount.keys():
            self.inputPerYearCount[year] = 1
        else:
            input_count = self.inputPerYearCount[year]
            self.inputPerYearCount[year] = input_count + 1

    def __update_output_per_year(self, year):
        if year not in self.outputPerYearCount.keys():
            self.outputPerYearCount[year] = 1
        else:
            output_count = self.outputPerYearCount[year]
            self.outputPerYearCount[year] = output_count + 1

    def get_most_purchased_item(self):
        for item_id in self.purchasedItems.keys():
            item_count = self.purchasedItems[item_id]
            if item_count > self.mostPurchasedItemCount:
                self.mostPurchasedItemCount = item_count
                self.mostPurchasedItem = item_id
        return self.mostPurchasedItem, self.mostPurchasedItemCount


