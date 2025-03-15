import pytest
from faker import Faker

fake = Faker()

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int, help="Number of test records")

@pytest.fixture(params=[(fake.random_int(), fake.random_int()) for _ in range(10)])
def random_numbers(request):
    return request.param
