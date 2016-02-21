import vdp_utils
import json
import nessie


BASE_URL = 'https://sandbox.api.visa.com'


def pullFunds(S):
    uri = '/visadirect/fundstransfer/v1/pullfundstransactions/'
    body = json.loads('''{
        "businessApplicationId": "AA",
        "merchantCategoryCode": 6012,
        "pointOfServiceCapability": {
            "posTerminalType": "4",
            "posTerminalEntryCapability": "2"
        },
        "feeProgramIndicator": "123",
        "systemsTraceAuditNumber": 300259,
        "retrievalReferenceNumber": "407509300259",
        "foreignExchangeFeeTransaction": "10.00",
        "cardAcceptor": {
            "name": "Acceptor 1",
            "terminalId": "365539",
            "idCode": "VMT200911026070",
            "address": {
                "state": "CA",
                "county": "081",
                "country": "USA",
                "zipCode": "94404"
            }
        },
        "magneticStripeData": {
            "track1Data": "1010101010101010101010101010"
        },
        "senderPrimaryAccountNumber": "4005520000011126",
        "senderCurrencyCode": "USD",
        "surcharge": "2.00",
        "localTransactionDateTime": "2016-02-21T21:32:52",
        "senderCardExpiryDate": "2013-03",
        "pinData": {
            "pinDataBlock": "1cd948f2b961b682",
            "securityRelatedControlInfo": {
                "pinBlockFormatCode": 1,
                "zoneKeyIndex": 1
            }
        },
        "cavv": "0000010926000071934977253000000000000000",
        "pointOfServiceData": {
            "panEntryMode": "90",
            "posConditionCode": "0",
            "motoECIIndicator": "0"
        },
        "acquiringBin": 409999,
        "acquirerCountryCode": "101",
        "amount": "112.00"
    }''')
    r = S.post(BASE_URL + uri, json=body)
    return r

def pushFunds(S):
    uri = '/visadirect/fundstransfer/v1/pushfundstransactions/'
    body = json.loads('''{
        "acquirerCountryCode": "840",
        "acquiringBin": "408999",
        "amount": "124.05",
        "businessApplicationId": "AA",
        "cardAcceptor": {
            "address": {
                "country": "USA",
                "county": "San Mateo",
                "state": "CA",
                "zipCode": "94404"
            },
        "idCode": "CA-IDCode-77765",
        "name": "Visa Inc. USA-Foster City",
        "terminalId": "TID-9999"
        },
        "localTransactionDateTime": "2016-02-20T21:07:28",
        "magneticStripeData": {
            "track2Data": "4957030420210496D130310191014085"
        },
        "merchantCategoryCode": "6012",
        "pinData": {
            "pinDataBlock": "dd6aa9d28517e7db",
        "securityRelatedControlInfo": {
            "pinBlockFormatCode": "01",
        "zoneKeyIndex": "01"
            }
        },
        "pointOfServiceCapability": {
            "posTerminalEntryCapability": "2",
        "posTerminalType": "3"
        },
        "pointOfServiceData": {
            "motoECIIndicator": "0",
            "panEntryMode": "90",
            "posConditionCode": "00"
        },
        "recipientName": "Target",
        "recipientPrimaryAccountNumber": "4957030420210496",
        "retrievalReferenceNumber": "412770451018",
        "senderAccountNumber": "4653459515756154",
        "senderAddress": "901 Metro Center Blvd",
        "senderCity": "Foster City",
        "senderCountryCode": "124",
        "senderName": "S Bala",
        "senderReference": "",
        "senderStateCode": "CA",
        "sourceOfFundsCode": "05",
        "systemsTraceAuditNumber": "451018",
        "transactionCurrencyCode": "USD",
        "transactionIdentifier": "381228649430015"
    }''')
    r = S.post(BASE_URL + uri, json=body)
    return r





# import vdp_utils


# BASE_URL = 'https://sandbox.api.visa.com'


# def get_payment_info(S, call_id, data_level='SUMMARY'):
#     uri = '/wallet-services-web/payment/data/' + call_id
#     params = {'dataLevel': data_level}
#     r = S.get(BASE_URL + uri, params=params)
#     return r


# def main():
#     call_id = '1105650383641652501'
#     api_key = 'UBYGU2DTGBMLJRUIIKV721kf4f9dTZ6UE0fHfTgNlvwqvHvSY'
#     shared_secret = '21F-e+fifjoRtYzmYi{tIzDTERE@W+sKv{TfQY8m'
#     with vdp_utils.XSession(api_key, shared_secret) as S:
#         S.headers.update({'content-type': 'application/json',
#                          'accept': 'application/json'})
#         r = get_payment_info(S, call_id)
#     print r.status_code
#     print r.content


# if __name__ == '__main__':
#     main()

x = 1100
print "cost of product: " + str(x)

def main():
    user_id = 'O9BAMP8XV1MQZ3FTYJ93216QeNA7E4jfr5Ttfoe08zet3YjX8'
    password = 'sNuMf1Rz5Loe3XMAzPDGo9ffKs0gh'
    cert = './cert.pem'
    key = './key_Instabuy2.pem'

    with vdp_utils.MSession(user_id, password, cert, key) as S:
        S.headers.update({'content-type': 'application/json',
                         'accept': 'application/json'})

        if nessie.checkBalance() > x:
            response_pull = pullFunds(S)
        else:
            raise ValueError('Account lacks funds to buy product!')
        response_push = pushFunds(S)

    print response_pull.status_code
    print response_pull.content
    print response_push.status_code
    print response_push.content





























if __name__ == '__main__':
    main()