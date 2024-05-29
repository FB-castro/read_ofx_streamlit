from ofxparse import OfxParser

def getattr_safe(obj, attr):
    return getattr(obj, attr, None)

def parse_ofx_to_dict(file):
    try:
        ofx = OfxParser.parse(file)
        data = {
            "account_id": [],
            "number": [],
            "routing_number": [],
            "branch_id": [],
            "type": [],
            "organization": [],
            "fid": [],
            "start_date": [],
            "end_date": [],
            "balance": [],
            "payee": [],
            "transaction_type": [],
            "date": [],
            "user_date": [],
            "amount": [],
            "transaction_id": [],
            "transaction_memo": [],
            "sic": [],
            "mcc": [],
            "checknum": [],
            "security": [],
            "units": [],
            "unit_price": [],
            "market_value": [],
            "uniqueid": [],
            "security_name": [],
            "ticker": [],
            "security_memo": []
        }

        account = getattr_safe(ofx, 'account')
        if account:
            account_data = {
                "account_id": getattr_safe(account, 'account_id'),
                "number": getattr_safe(account, 'number'),
                "routing_number": getattr_safe(account, 'routing_number'),
                "branch_id": getattr_safe(account, 'branch_id'),
                "type": getattr_safe(account, 'type')
            }

            institution = getattr_safe(account, 'institution')
            if institution:
                institution_data = {
                    "organization": getattr_safe(institution, 'organization'),
                    "fid": getattr_safe(institution, 'fid')
                }
            else:
                institution_data = {"organization": None, "fid": None}

            statement = getattr_safe(account, 'statement')
            if statement:
                statement_data = {
                    "start_date": getattr_safe(statement, 'start_date'),
                    "end_date": getattr_safe(statement, 'end_date'),
                    "balance": getattr_safe(statement, 'balance')
                }

                transactions = getattr_safe(statement, 'transactions')
                if transactions:
                    for transaction in transactions:
                        transaction_data = {
                            "payee": getattr_safe(transaction, 'payee'),
                            "transaction_type": getattr_safe(transaction, 'type'),
                            "date": getattr_safe(transaction, 'date'),
                            "user_date": getattr_safe(transaction, 'user_date'),
                            "amount": getattr_safe(transaction, 'amount'),
                            "transaction_id": getattr_safe(transaction, 'id'),
                            "transaction_memo": getattr_safe(transaction, 'memo'),
                            "sic": getattr_safe(transaction, 'sic'),
                            "mcc": getattr_safe(transaction, 'mcc'),
                            "checknum": getattr_safe(transaction, 'checknum'),
                            "security": None,
                            "units": None,
                            "unit_price": None,
                            "market_value": None,
                            "uniqueid": None,
                            "security_name": None,
                            "ticker": None,
                            "security_memo": None
                        }

                        row = {**account_data, **institution_data, **statement_data, **transaction_data}
                        for key in row:
                            data[key].append(row[key])

                positions = getattr_safe(statement, 'positions')
                if positions:
                    for position in positions:
                        position_data = {
                            "security": getattr_safe(position, 'security'),
                            "units": getattr_safe(position, 'units'),
                            "unit_price": getattr_safe(position, 'unit_price'),
                            "market_value": getattr_safe(position, 'market_value'),
                            "payee": None,
                            "transaction_type": None,
                            "date": None,
                            "user_date": None,
                            "amount": None,
                            "transaction_id": None,
                            "transaction_memo": None,
                            "sic": None,
                            "mcc": None,
                            "checknum": None,
                            "uniqueid": None,
                            "security_name": None,
                            "ticker": None,
                            "security_memo": None
                        }

                        row = {**account_data, **institution_data, **statement_data, **position_data}
                        for key in row:
                            data[key].append(row[key])

                security = getattr_safe(statement.transactions[0], 'security') if transactions else None
                if not security:
                    security = getattr_safe(statement.positions[0], 'security') if positions else None

                if security:
                    security_data = {
                        "uniqueid": getattr_safe(security, 'uniqueid'),
                        "security_name": getattr_safe(security, 'name'),
                        "ticker": getattr_safe(security, 'ticker'),
                        "security_memo": getattr_safe(security, 'memo'),
                        "payee": None,
                        "transaction_type": None,
                        "date": None,
                        "user_date": None,
                        "amount": None,
                        "transaction_id": None,
                        "transaction_memo": None,
                        "sic": None,
                        "mcc": None,
                        "checknum": None,
                        "security": None,
                        "units": None,
                        "unit_price": None,
                        "market_value": None
                    }

                    row = {**account_data, **institution_data, **statement_data, **security_data}
                    for key in row:
                        data[key].append(row[key])

        return data
    except Exception as e:
        return {"error": str(e)}
