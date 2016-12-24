from flask import Blueprint, request, jsonify

from mito.entities import Company
from mito.services import company_service

mod = Blueprint('company_api', __name__, )


@mod.route('/create', methods=["POST"])
def create_company():
    company = Company(**request.json)
    company, error = company_service.create_company(company)
    if error:
        return jsonify(error.jsonify())
    return jsonify(company.__dict__)
