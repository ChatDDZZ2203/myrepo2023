import os
from flask import Flask, request, Response
from faker import Faker

fake = Faker()
app = Flask(__name__)

@app.before_request
def hand():
  credit_card_number = fake.credit_card_number()
  credit_card_cvv = fake.credit_card_security_code()
  credit_card_expire = fake.credit_card_expire()
  return f"{credit_card_number}\n{credit_card_cvv}\n{credit_card_expire}"

def main():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 3000)))


if __name__ == '__main__':
    main()



