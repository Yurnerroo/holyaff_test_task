from .models import Account, Transaction
from django.db import transaction


@transaction.atomic
def perform_deposit(user, amount):
    account = Account.objects.get(user=user)
    account.balance += amount
    account.save()

    transaction = Transaction.objects.create(
        account=account,
        transaction_type=Transaction.TRANSACTION_TYPE_DEPOSIT
    )

    return transaction


@transaction.atomic
def perform_withdrawal(user, amount):
    account = Account.objects.get(user=user)
    account.balance -= amount
    account.save()

    transaction = Transaction.objects.create(
        account=account,
        transaction_type=Transaction.TRANSACTION_TYPE_WITHDRAWAL
    )

    return transaction
