import pytest
from wallet import Wallet,InsufficientAmount

@pytest.fixture
def empty_wallet():
    '''return the wallet instance with a 100 as balance'''
    return Wallet()

@pytest.fixture()
def wallet():
    '''return the wallet instance with a 100 as balance'''
    return Wallet(100)

@pytest.mark.parametrize("Earned,Spent,Expected",[(30,10,20),(20,2,18)])
def test_transactions(empty_wallet,Earned,Spent,Expected):
    empty_wallet.add_cash(Earned)
    empty_wallet.spend_cash(Spent)
    assert empty_wallet.balance==Expected

def test_default_initial_amount():
    #wallet=Wallet()
    assert wallet.balance==0

def test_setting_initial_amount():
    #wallet=Wallet(100)
    assert wallet.balance ==100

def test_wallet_add_cash():
    #wallet=Wallet(100)
    wallet.add_cash(10)
    assert wallet.balance==110

def test_wallet_spend_cash():
    #wallet=Wallet(100)
    wallet.spend_cash(10)
    assert wallet.balance==90

def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    #wallet=Wallet()
    with pytest.raises(InsufficientAmount):
        wallet.spend_cash(100)

