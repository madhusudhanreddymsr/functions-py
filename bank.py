class sbi:
    branch='palamaner'
    ifsc ='sbi00026'
    manager ='jagan'
    loc ='chittoor'
    def __init__(self,name,mob,acc,pan,bal):
        self.name=name
        self.mobile=mob
        self.accoun=acc
        self.pan=pan
        self.balance=bal
    def credit(self,amt):
        self.balance+=amt
    def debit(self,amt):
        self.balance-=amt
    def update_mob(self,mobile):
        self.mob=mobile
chandra=sbi('nara chandra',8184321012,76587658,'CBNT00000W',1)
lokesh=sbi('nara lokesh',9848321040,84765665,'CBNT00000Y',2)
        