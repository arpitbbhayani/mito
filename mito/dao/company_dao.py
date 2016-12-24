from mito.entities import Company
from mito.errors import DuplicateDataError
from mito.distributed_db.api import index as index_api
from mito.distributed_db.api import data as data_api


class CompanyDao:
    @staticmethod
    def create(company):
        name = company.name
        existing_company = index_api.get_one(Company, 'name', name)
        if existing_company:
            raise DuplicateDataError("Company with name '%s' already exists!" % (name))

        return data_api.add(company)

    @staticmethod
    def update(company):
        print("Updating the company")

    @staticmethod
    def get_by_id(guid):
        return data_api.get(Company, guid)
