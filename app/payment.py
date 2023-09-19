import yookassa

def create_payment():
    yookassa.Configuration.account_id = '256605'
    yookassa.Configuration.secret_key = 'test_C7QrmrPH3wXboT8Jk9oGy6fzv42U1GsifazhytTXxjI'

    payment = yookassa.Payment.create({
        "amount": {
            "value": 100,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://t.me/tg121212_bot"
        },
        "description": "Покупка",
        "capture": True
    })

    url = payment.confirmation.confirmation_url

    return url, payment.id


def check_payment(id):
    id = id.split(':')[1]
    payment = yookassa.Payment.find_one(id)
    if payment.status == 'succeeded':
        return True
    else:
        return False



