import ape

def test_init(ERC20, owner):
    print(owner.balance)
    assert ERC20.balanceOf(owner) == 10 ** 18

def test_total_supply(ERC20):
    assert ERC20.totalSupply() == 10 ** 18