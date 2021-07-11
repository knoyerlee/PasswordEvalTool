import random as r

class Password():
    def __init__(self):
        self.pass_aspects = [
            ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
            ['!', '*', '$', '&'],
        ]

    # This Function is used to assess that a password is strong
    def check_password(self, password):
        self.good_password = True
        self.i = 0
        while (self.i < len(self.pass_aspects[0]) - 1):
            if(self.pass_aspects[0][self.i] not in password):
                self.good_password = False
                self.i += 1
            else:
                self.good_password = True
                self.i = 0
                break
        while (self.i < len(self.pass_aspects[1]) - 1):
            if(self.pass_aspects[1][self.i] not in password):
                self.good_password = False
                self.i += 1
            else:
                self.good_password = True
                self.i = 0
                break
        while (self.i < len(self.pass_aspects[2]) - 1):
            if(self.pass_aspects[2][self.i] not in password):
                self.good_password = False
                self.i += 1
            else:
                self.good_password = True
                self.i = 0
                break
        while (self.i < len(self.pass_aspects[3]) - 1):
            if(self.pass_aspects[3][self.i] not in password):
                self.good_password = False
                self.i += 1
            else:
                self.good_password = True
                self.i = 0
                break
        if (len(password) < 15):
            self.good_password = False
        return self.good_password

    # This function generates a random password
    def generate_password(self):
        self.gen_password = ""
        while (len(self.gen_password) < 15):
            self.index1 = self.pass_aspects[r.randint(0,len(self.pass_aspects) - 1)]
            self.index2 = self.index1[r.randint(0, len(self.index1) - 1)]
            self.gen_password += self.index2
        return self.gen_password
    
    # Generate a strong password
    def generate_strong_password(self):
        self.password = self.generate_password()
        while (not self.check_password(self.password)):
            self.password = self.generate_password()
        return self.password
