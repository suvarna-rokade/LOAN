import pickle
import json
import numpy as np

class Loan_Prediction():

    def __init__(self,Age,Experience,Income,Family,CCAvg,Education,Mortgage,Securities_Account,CD_Account,Online,CreditCard):

       self.Age = Age
       self.Experience = Experience
       self.Income = Income
       self.Family = Family
       self.CCAvg = CCAvg
       self.Education = Education
       self.Mortgage = Mortgage
       self.Securities_Account = Securities_Account
       self.CD_Account = CD_Account
       self.Online = Online
       self.CreditCard = CreditCard
        

    def load_model(self):
        with open('Loan_approval.pkl', 'rb') as f:
            self.model = pickle.load(f)
        
        with open('project_data.json', 'r') as f:
            self.json_data = json.load(f)

    def get_loan_prediction(self):
        self.load_model()

        test_array = np.zeros(len(self.json_data['columns']))
        test_array[0] = self.Age
        test_array[1] = self.Experience
        test_array[2] = self.Income
        test_array[3] = self.Family
        test_array[4] = self.CCAvg
        test_array[5] = self.Education
        test_array[6] = self.Mortgage
        test_array[7] = self.Securities_Account
        test_array[8] = self.CD_Account
        test_array[9] = self.Online
        test_array[10] = self.CreditCard

    

        print('Test Array :', test_array)
        predicted_loan_status = self.model.predict([test_array])
        return predicted_loan_status
if __name__ == '__main__':
        Age = 25.0
        Experience = 1.0
        Income = 49.0
        Family = 4.0
        CCAvg = 1.6
        Education = 1.0
        Mortgage = 0.0
        Securities_Account = 1.0
        CD_Account = 0.0
        Online = 0.0
        CreditCard = 0.0
        # loan_ins = Loan_Prediction(Age,Experience,Income,Family,CCAvg,Education,Mortgage,Securities_Account,CD_Account,Online,CreditCard)
        # loan_ins.get_loan_prediction()