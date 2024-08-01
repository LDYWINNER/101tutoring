# CSE 101 DongYoon Lee
# Email: DongYoon.Lee.1@stonybrook.edu

class Attendee:
    def __init__(self, N, Com, Coun, E):
        self._name = N
        self._company = Com
        self._country = Coun
        self._emailAddress = E

    def getInfo(self):
        info = {}
        info['Name'] = self._name
        info['Company'] = self._company
        info['Country'] = self._country
        info['Email'] = self._emailAddress
        return info

class Conference:

    def __init__(self, CN, L, D):
        if type(CN) == str and type(L) == str and type(D) == str:
            self._conferenceName = CN
            self._location = L
            self._dates = D
            self.attend = []
            print('Conference "', self._conferenceName, '"', "is created.")

    def addAttendee(self, Attendee):
        self.attend.append(Attendee.getInfo())
        print("Attendee", Attendee.Name, "is added to the list of conference participants." )


