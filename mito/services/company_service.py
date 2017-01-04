from mito.dao import CompanyDao
from mito.errors import MitoError


def create_company(company):
    company, error = None, None
    try:
        company = CompanyDao.create(company)
    except MitoError as m:
        error = m
    return company, error


def update_company(company):
    company, error = None, None
    try:
        company = CompanyDao.update(company)
    except MitoError as m:
        error = m
    return company, error


def delete_company(company_name):
    is_deleted, error = False, None
    try:
        is_deleted = CompanyDao.delete_by_name(company_name)
    except MitoError as m:
        error = m
    return is_deleted, error


def get_all_active_companies():
    companies, error = None, None
    try:
        companies = CompanyDao.get_all_active()
    except MitoError as m:
        error = m
    return companies, error


def get_all_companies():
    companies, error = None, None
    try:
        companies = CompanyDao.get_all_active() + CompanyDao.get_all_inactive()
    except MitoError as m:
        error = m
    return companies, error


def get_by_name(company_name):
    companies, error = None, None
    try:
        companies = CompanyDao.get_by_name(company_name)
    except MitoError as m:
        error = m
    return companies, error


def get_by_id(company_id):
    company, error = None, None
    try:
        company = CompanyDao.get_by_id(company_id)
    except MitoError as m:
        error = m
    return company, error
