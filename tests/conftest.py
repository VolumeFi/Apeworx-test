import pytest

@pytest.fixture(scope="session")
def owner(accounts):
    return accounts[0]

@pytest.fixture(scope="session")
def receiver(accounts):
    return accounts[1]

@pytest.fixture(scope="session")
def ERC20(owner, project):
    return owner.deploy(project.ERC20, "My ERC20", "ERC", 18, 1)