from utils import Loan_Prediction
import json
import pickle
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

##################################################################################
 ################################# Base API #####################################
##################################################################################

@app.route('/')
def Perdiction_model():
    print('Welcome to home loan Model')
    return render_template('home.html')


##################################################################################
 ################################# Test API #####################################
##################################################################################

@app.route('/check_status', methods = ['POST'])
def get_loan_prediction():
        print('We are using POST Method')
        data = request.form
        Age = int(data['Age'])
        Experience = int(data['Experience'])
        Income = int(data['Income'])
        Family = int(data['Family'])
        CCAvg = int(data['CCAvg'])
        Education = int(data['Education'])
        Mortgage = int(data['Mortgage'])
        Securities_Account = int(data['Securities_Account'])
        CD_Account = int(data['CD_Account'])
        Online = int(data['Online'])
        CreditCard = int(data['CreditCard'])
    

        print(f'Age >> {Age}, Experience >> {Experience}, Income >> {Income}, Family >> {Family}, CCAvg >> {CCAvg}, Education >> {Education}, Mortgage >> {Mortgage}, Securities_Account >> {Securities_Account}, CD_Account >> {CD_Account}, Online >> {Online}, CreditCard >> {CreditCard}')
        loan_ins = Loan_Prediction(Age,Experience, Income, Family,CCAvg, Education,Mortgage,Securities_Account,CD_Account,Online,CreditCard)
        status = loan_ins.get_loan_prediction()
        # return jsonify({'Result':f"Predicted Medical Insurance Charges are: RS.{charges}"})
        
        if status == 1:
            return ('CONGRATULATION .....! You Are Eligible For Home Loan')
        else:
            return ('SORRY .....! You Are not Eligible For Home Loan')
        return render_template('home.html', Output=status)
   


if __name__=='__main__':
    app.run( host="0.0.0.0",port=8055)