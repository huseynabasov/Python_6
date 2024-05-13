# class Account:
#     def __init__(self, name, surname, balance: int, amount: int):
#         self.name = name
#         self.surname = surname
#         self.balance = balance
#         self.amount = amount

#     def score_inc(self):
#         addition = int(input("Elave edilecekeblegi daxil edin: "))
#         if addition < 0:
#             print("Daxil edilen megleg 0-dan kicik ola bilmez!!!")
#         else:
#             self.balance += addition
#             print("\nElave edilen mebleg:", addition)

#     def whitdraw_money(self):
#         deductible = int(input("Cixilacaq meblegi daxil edin: "))
#         if deductible > self.balance:
#             print("Cekilen mebleg hesabdaki meglegden boyuk ola bilmez!!!")
#         else:
#             self.balance -= deductible
#             print("\nElave edilen mebleg:", deductible)

#     def show_balance(self):
#         print(f"\n{self.amount} nomreli hesabda faktiki olan mebleg : {self.balance}")


# class CreditAccount(Account):
#     def __init__(self, name, surname, balance, amount, loanAmount: int):
#         super().__init__(name, surname, balance, amount)
#         self.loanAmount = loanAmount

#     def give_credit(self):
#         self.loanAmount = int(input("Verilecek kredit meblegini qeyd edin: "))
#         self.balance += self.loanAmount
#         print(
#             f"\n{self.loanAmount} AZN məbləği hesabınıza əlavə edildi. Faktiki balansınız : {self.balance} AZN"
#         )

#     def loan_payment(self):
#         monthlyPayment = int(self.loanAmount / 12)
#         self.balance -= monthlyPayment
#         print(f"Ayliq {monthlyPayment} ödəniş edildi. Yeni balansınız: {self.balance}")


# amount1 = Account("Huseyn", "Abbasov", 500, 11200301)
# credit_amount = CreditAccount("Huseyn", "Abbasov", 500, 11200301, 1500)


# print(
#     f"Ilkin hesab : {amount1.name} {amount1.surname} : {amount1.balance} AZN : {amount1.amount}"
# )
# amount1.score_inc()
# print(
#     f"Elave edilen depositden sonraki hesab : {amount1.name} {amount1.surname} : {amount1.balance} AZN : {amount1.amount}"
# )
# amount1.whitdraw_money()
# print(
#     f"Çıxılan məbləğdən sonrakı sonraki hesab : {amount1.name} {amount1.surname} : {amount1.balance} AZN : {amount1.amount}"
# )
# amount1.show_balance()

# ------------------------------------------------------------------------------------------------------------
#Credit verilmesi ve kredit odenisinin gosterilmesi

# credit_amount.give_credit()
# print(
#     f"\nKredit aldiqdan sonraki hesab : {credit_amount.name} {credit_amount.surname} : {credit_amount.balance} AZN : {credit_amount.amount}\n"
# )
# credit_amount.loan_payment()

# print(
#     f"\nAyliq odenis edildikden sonraki qaliq hesab : {credit_amount.name} {credit_amount.surname} : {credit_amount.balance} AZN : {credit_amount.amount}"
# )

