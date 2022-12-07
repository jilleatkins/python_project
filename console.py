import pdb
from models.product import Product
from models.supplier import Supplier

import repositories.product_repository as product_repository
import repositories.supplier_repository as supplier_repository

product_repository.delete_all()
supplier_repository.delete_all()

supplier1 = Supplier("Buchanan's", "(Phone: 01475 722271), (Address: Fort Matilda Industrial Estate, Greenock, Inverclyde, Scotland)")
supplier_repository.save(supplier1)

supplier2 = Supplier("Northern Confectioners", "(Phone: 028 8772 351458), (Address: Old Eglish Road, Dungannon, Co Tyrone, Northern Ireland)")
supplier_repository.save(supplier2)

supplier3 = Supplier("Valeo Foods Group", "(Phone: +353 1 405 1500), (Address: Merrywell Industrial Estate, Ballymount, Dublin, Ireland)")
supplier_repository.save(supplier3)



product1 = Product("Iron Brew Pastilles", supplier1, "Soft sugar-coated iron brew flavoured pastilles", 55, 1, 2)
product_repository.save(product1)

product2 = Product("Chocolate Peppermint Creams", supplier1, "Smooth peppermint fondant, smothered in the finest dark chocolate with natural oil of peppermint", 43, 1, 2)
product_repository.save(product2)

product3 = Product("Forest Fruit Jellies", supplier1, "Deliciously soft and sweet berry-flavoured selection", 27, 1, 2)
product_repository.save(product3)


product4 = Product("Butter Toffees", supplier2, "Smooth soft-eating butter toffees. An exquisite classic-looking sweet", 14, 1, 2)
product_repository.save(product4)

product5 = Product("Edinburgh Rock", supplier2, "Delicious soft and crumbly candy sweet that really melts in your mouth", 17, 1, 2)
product_repository.save(product5)

product6 = Product("Millions Fizzy Cola Babies", supplier2, "Cola-flavoured jelly sweets", 56, 1, 2)
product_repository.save(product6)


product7 = Product("Barratt Wham Original Chew Bar", supplier3, "Raspberry flavour chew bar with sour crystals", 12, 1, 2)
product_repository.save(product7)

product8 = Product("Barratt Dip Dab", supplier3, "Lemon flavour sherbet dip with a strawberry flavour lolly", 43, 1, 2)
product_repository.save(product8)

product9 = Product("Barratt Refreshers Sweets", supplier3, "Hard tablet-formed fruit flavour fizzy sweets", 20, 1, 2)
product_repository.save(product9)