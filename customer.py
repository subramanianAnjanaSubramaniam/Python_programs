'''#create base class
class Customer:
    def __init__(self,name,unitConsumed):
        self.name=name
        self.unitConsumed=unitConsumed
        def calculateBill(self):
            return unitConsumed*0.1
        def displayBill(self):
            print(f"consumer:{self.name}\n units consumed:{self.unitConsumed}\n Total Bill:{self.calculateBill}")

# create a subclass 
class ResidentialCustomer(Customer):
    def __init__(self,name,unitConsumed,familyMember):
        super().__init__(self,name,unitConsumed)
        self.familyMember=familyMember
    def calculateBill(self):
            base_rate=0.8
            discount_each_member=0.02
            discounted_rate=base_rate-(self.familyMember*discount_each_member)
            return self.unitConsumed*discounted_rate
        
#create another subclass
class CommercialCustomer(Customer):
    def __init__(self,name,unitConsumed,business_type)  :
        self.business_type=business_type
    def calculateBill(self):
             base_rate=0.12
            if self.business_type=="small":
                  base_rate*=0.9
            elif self.business_type=="large"  :
                 base_rate*=1.1
            return self.unitConsumed*base_rate
            
r1=ResidentialCustomer("Anjana",100,2)   
c1=CommercialCustomer("ABC Company",400,"large") 

r1.displayBill()
# c1.displayBil'''

class Customer:
    def __init__(self, name, units_consumed):
        self.name = name
        self.units_consumed = units_consumed

    def calculateBill(self):
        # Default rate for all customers
        return self.units_consumed * 0.1

    def displayBill(self):
        print(f"Customer: {self.name}\nUnits Consumed: {self.units_consumed}\nTotal Bill: ${self.calculateBill()}\n")


class ResidentialCustomer(Customer):
    def __init__(self, name, units_consumed, family_members):
        super().__init__(name, units_consumed)
        self.family_members = family_members

    def calculateBill(self):
        # Base rate for residential customers
        base_rate = 0.08

        # Discount for each family member
        discount_per_member = 0.02

        # Calculate discounted rate based on family members
        discounted_rate = base_rate - (self.family_members * discount_per_member)

        # Apply discounted rate to units consumed
        return self.units_consumed * discounted_rate


class CommercialCustomer(Customer):
    def __init__(self, name, units_consumed, business_type):
        super().__init__(name, units_consumed)
        self.business_type = business_type

    def calculateBill(self):
        # Base rate for commercial customers
        base_rate = 0.12

        # Adjust the rate based on business type
        if self.business_type == "Small":
            base_rate *= 0.9  # 10% discount for small businesses
        elif self.business_type == "Large":
            base_rate *= 1.1  # 10% surcharge for large businesses

        return self.units_consumed * base_rate


# Example Usage
residential_customer = ResidentialCustomer("John Doe", 150, 4)
commercial_customer = CommercialCustomer("ABC Corp", 300, "Large")

residential_customer.displayBill()
commercial_customer.displayBill()