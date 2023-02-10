class Dad:
    basketball = 1
    # print(basketball)

class Son(Dad):
    dance = 1
    basketball = 10

    def isDance(self):
        return f"Yes I dance {self.dance} no of times"

class Grandson(Son):
    dance = 6

    def isDance(self):
        return f"Jackson yeah!" \
                f" Yes I dance vary awesomely {self.dance} no of times"

darry = Dad()
larry = Son()
Kkhan = Grandson()

# print(Kkhan.isDance())
# print(Kkhan.basketball)


# Quizs
# electronics device
# pocket gadget
# phone

class ElectronicsDevice:
    phone = "samsung"
    prize = 100000
    Brand = "Huwai"

class PocketGadget(ElectronicsDevice):
    phone = "Iphone"
    prize = 200000

    def sell(self):
        return f"This phone name is {self.phone} and this phone prize is {self.prize}"

class Phone(PocketGadget, ElectronicsDevice):
    specification = "8GB RAM 885Processors"

    def sell(self):
        return f"This phone name is {self.phone}, prize is {self.prize} and specification of this phone is {self.specification}"

device = Phone()
sell = device.sell()
print(sell)
print(device.Brand)

print(device.specification)