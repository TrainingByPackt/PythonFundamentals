from functions import AccessApi as mws
import pytest

base_url: str = "https://raw.githubusercontent.com/TrainingByPackt/PythonFundamentals/master/Capstone/"
billing_end_point: str = "API/getBillingInfo.json"
customer_end_point: str = "API/getCustomers.json"
site_end_point: str = "API/getSites.json"

# TASK 2

# billing
def test_billing_status_code():
    api: mws.AccessApi = mws.AccessApi(base_url)
    status_code: int = api.get_status_code(billing_end_point)
    assert status_code == 200


def test_billing_validate_schema():
    api: mws.AccessApi = mws.AccessApi(base_url)
    billing: dict = api.get_end_point(billing_end_point)
    billing_schema : list = ['id', 'FirstName', 'LastName', 'city', 'state', 'Lang', 'SSN']
    assert billing_schema == list(billing.keys())


def test_billing_validate_ssn():
    api: mws.AccessApi = mws.AccessApi(base_url)
    billing: dict = api.get_end_point(billing_end_point)
    chunk: list = billing["SSN"].split('-')
    is_ssn: bool = False
    if len(chunk) ==3:
        if len(chunk[0]) == 3 and len(chunk[1]) == 2 and len(chunk[2]) == 4:
            is_ssn: bool = True
    assert is_ssn == True


def test_billing_validate_time():
    api: mws.AccessApi = mws.AccessApi(base_url)
    elapsed_time: float = api.get_elapsed_time(billing_end_point)
    assert elapsed_time <= 3


# customers


def test_customers_status_code():
    api: mws.AccessApi = mws.AccessApi(base_url)
    status_code: int = api.get_status_code(customer_end_point)
    assert status_code == 200


def test_customers_validate_schema():
    api: mws.AccessApi = mws.AccessApi(base_url)
    customers: dict = api.get_end_point(customer_end_point)
    customers_schema: list = ['id', 'first_name', 'last_name', 'email', 'ip_address', 'address']
    assert customers_schema == list(customers.keys())


def test_customers_validate_ssn():
    api: mws.AccessApi = mws.AccessApi(base_url)
    customers: dict = api.get_end_point(customer_end_point)
    chunk: list = customers["ip_address"].split('.')
    is_ip_address: bool = False
    if len(chunk) == 4:
        if len(chunk[0]) == 3 and len(chunk[1]) == 3 and len(chunk[2] ) == 3 and len(chunk[3] ) == 3:
            is_ip_address: bool = True
    assert is_ip_address == True


def test_customers_validate_time():
    api: mws.AccessApi = mws.AccessApi(base_url)
    elapsed_time: float = api.get_elapsed_time(customer_end_point)
    assert elapsed_time <= 3


# site

def test_site_status_code():
    api: mws.AccessApi = mws.AccessApi(base_url)
    status_code: int = api.get_status_code(site_end_point)
    assert status_code == 200


def test_site_validate_schema():
    api: mws.AccessApi = mws.AccessApi(base_url)
    site: dict = api.get_end_point(site_end_point)
    site_schema: list = ['id', 'address', 'ThirdParty', 'admin']
    assert site_schema == list(site.keys())


def test_site_validate_ssn():
    api: mws.AccessApi = mws.AccessApi(base_url)
    site: dict = api.get_end_point(site_end_point)
    id: int = site["id"]
    assert isinstance(id, int)


def test_site_validate_time():
    api: mws.AccessApi = mws.AccessApi(base_url)
    elapsed_time: float = api.get_elapsed_time(site_end_point)
    assert elapsed_time <= 3

    
# task 3


@pytest.mark.parametrize('base_url', [base_url])
@pytest.mark.parametrize('billing_end_point', [billing_end_point, customer_end_point, site_end_point])
def test_billing_status_code(base_url, billing_end_point):
    api: mws.AccessApi = mws.AccessApi(base_url)
    status_code: int = api.get_status_code(billing_end_point)
    assert status_code == 200


@pytest.mark.parametrize('base_url', [base_url])
@pytest.mark.parametrize('billing_end_point',[billing_end_point,customer_end_point,site_end_point])
def test_billing_validate_time(base_url,billing_end_point):
    api: mws.AccessApi = mws.AccessApi(base_url)
    elapsed_time: float = api.get_elapsed_time(billing_end_point)
    assert elapsed_time <= 3
