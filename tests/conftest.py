import pytest
from faker import Faker

fake = Faker()

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=10, type=int, help="number of records to generate")

@pytest.fixture(scope="session")
def num_records(request):
    return request.config.getoption("--num_records")

@pytest.fixture
def fake_data():
    a = fake.random_number()
    b = fake.random_number()
    operation = fake.random_element(elements=('add', 'subtract', 'multiply', 'divide'))
    expected_result = {
        'add': a + b,
        'subtract': a - b,
        'multiply': a * b,
        'divide': a / b if b != 0 else None
    }[operation]
    return a, b, operation, expected_result
