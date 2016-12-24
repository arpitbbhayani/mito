from mito.dao import CompanyDao
from mito.errors import MitoError


def create_company(company):
    error = None
    try:
        company = CompanyDao.create(company)
    except MitoError as m:
        error = m
    return article, error
