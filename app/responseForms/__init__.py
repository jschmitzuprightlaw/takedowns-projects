import gspread
from oauth2client.service_account import ServiceAccountCredentials


class Session:
    def __init__(self):
        scope = ['https://spreadsheets.google.com/feeds',
                 'https://www.googleapis.com/auth/drive']

        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            './responseForms/credentials.json', scope
        )

        self.gc = gspread.authorize(credentials)
        self.responseWks = self.gc.open_by_key("1JRcWGXM_KOfFOzNYdNrH71XbymgYNeiWCXHoi-6ST1U")
        self.responseSheet = self.responseWks.worksheet("Form Responses 1")

    def getResponses(self):
        responses = self.responseSheet.get_all_values()[1:]
        responses.reverse()
        responses_dict = {}
        for response in responses:
            if response[1] not in responses_dict.keys():
                responses_dict[response[1]] = response[1:]
        return list(responses_dict.values())

    def getPenalties(self):
        pass

if __name__ == "__main__":
    session = Session()
    print(session.sheet.get_all_values())