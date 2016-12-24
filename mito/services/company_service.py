from mito.dao import CompanyDao
from mito.errors import MitoError


def create_company(company):
    error = None
    try:
        company = CompanyDao.create(company)
    except MitoError as m:
        error = m
    return company, error


def delete_company(company_name):
    error = None
    try:
        is_deleted = CompanyDao.delete_by_name(company_name)
    except MitoError as m:
        error = m
    return is_deleted, error


def get_all_companies():
    error = None
    try:
        companies = CompanyDao.get_all_active()
    except MitoError as m:
        error = m
    return companies, error
