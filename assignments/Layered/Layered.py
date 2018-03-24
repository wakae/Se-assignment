

"""
LAYERED ARCHITECHTURE implmentation 3-tier
Separates presentation, application processing, and data management functions.
"""


class Data(object):
    """ Data Store Class """

    products = {
        'wetet': {'price': 1.50, 'quantity': 17},
        'enqulal': {'price': 0.20, 'quantity': 100},
        'Qibe': {'price': 2.00, 'quantity': 50}
    }

    def __get__(self, obj, klas):
        print("(Fetching from Data Store)")
        return {'products': self.products}


class BusinessLogic(object):
    """ Business logic holding data store instances """

    data = Data()

    def product_list(self):
        return self.data['products'].keys()

    def product_information(self, product):
        return self.data['products'].get(product, None)


class Ui(object):
    """ UI interaction class """

    def __init__(self):
        self.business_logic = BusinessLogic()

    def get_product_list(self):
        print('PRODUCT LIST:')
        for product in self.business_logic.product_list():
            print(product)
        print('')

    def get_product_information(self, product):
        product_info = self.business_logic.product_information(product)
        if product_info:
            print('PRODUCT INFORMATION:')
            print('Name: {0}, Price: {1:.2f}, Quantity: {2:}'.format(
                product.title(), product_info.get('price', 0),
                product_info.get('quantity', 0)))
        else:
            print('That product "{0}" does not exist in the records'.format(
                product))


def main():
    ui = Ui()
    ui.get_product_list()
    ui.get_product_information('Qibe')
    ui.get_product_information('enqulal')
    ui.get_product_information('wetet')
    ui.get_product_information('ergo')

if __name__ == '__main__':
    main()

