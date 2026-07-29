from breezypythongui import EasyFrame

class MonthlyBudgetPlanner(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self,title="Monthly Budget Planner")
        self.setBackground("lightblue")
        self.addLabel(text="Monthly Income", row=0, column=0, background="palegreen")
        self.incomeField = self.addFloatField(value=0.0, row=0, column=1)

        self.addLabel(text="Rent/Mortgage", row=1, column=0, background="lightpink")
        self.housingField = self.addFloatField(value=0.0, row=1, column=1)

        self.addLabel(text="Utilities", row=2, column=0, background="lightyellow")
        self.utilitiesField = self.addFloatField(value=0.0, row=2, column=1)

        self.addLabel(text="Food", row=3, column=0, background="lightcyan")
        self.foodField = self.addFloatField(value=0.0, row=3, column=1)

        self.addLabel(text="Transportation", row=4, column=0, background="lightgray")
        self.transportationField = self.addFloatField(value=0.0, row=4, column=1)

        self.addLabel(text="Entertainment", row=5, column=0, background="violet")
        self.entertainmentField = self.addFloatField(value=0.0, row=5, column=1)

        self.addLabel(text="Other Expenses", row=6, column=0, background="yellowgreen")
        self.otherField = self.addFloatField(value=0.0, row=6, column=1)

        self.addLabel(text="Savings Goal", row=7, column=0, background="palegoldenrod")
        self.savingsField = self.addFloatField(value=0.0, row=7, column=1)

        self.addLabel(text="Emergency Fund", row=8, column=0)
        self.emergencyField = self.addFloatField(value=0.0, row=8, column=1)

        self.addButton(text="Calculate Budget", row=9, column=0, columnspan=2, command=self.calculateBudget)
        self.addButton(text="Reset", row=9, column=2, columnspan=1, command=self.resetFields)
    
    def resetFields(self):
        self.incomeField = self.addFloatField(value=0.0, row=0, column=1)
        self.housingField = self.addFloatField(value=0.0, row=1, column=1)
        self.utilitiesField = self.addFloatField(value=0.0, row=2, column=1)
        self.foodField = self.addFloatField(value=0.0, row=3, column=1)
        self.transportationField = self.addFloatField(value=0.0, row=4, column=1)
        self.entertainmentField = self.addFloatField(value=0.0, row=5, column=1)
        self.otherField = self.addFloatField(value=0.0, row=6, column=1)
        self.savingsField = self.addFloatField(value=0.0, row=7, column=1)
        self.emergencyField = self.addFloatField(value=0.0, row=8, column=1)

    def calculateBudget(self):
        income = self.incomeField.getNumber()
        housing = self.housingField.getNumber()
        utilities = self.utilitiesField.getNumber()
        food = self.foodField.getNumber()
        transportation = self.transportationField.getNumber()
        entertainment = self.entertainmentField.getNumber()
        other = self.otherField.getNumber()

        totalExpenses = housing + utilities + food + transportation + entertainment + other
        remainingBudget = income - totalExpenses
        self.messageBox(title="Total Expenses", message=f"Total Expenses: ${totalExpenses:.2f}")
        self.messageBox(title="Remaining Balance", message=f"Remaining Balance: ${remainingBudget:.2f}")

        if remainingBudget < 0:
            self.messageBox(title="Over Budget", message="Warning: You are over budget!")
        elif remainingBudget == 0:
            self.messageBox(title="On Budget", message="You are exactly on budget.")
        else:
            self.messageBox(title="Under Budget", message="You are under budget. Muy bien!")

def main():
    MonthlyBudgetPlanner().mainloop()
main()
