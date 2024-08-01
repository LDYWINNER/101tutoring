
class Attendee:
    def __init__(self, name, company, country, email):
        self.name = name
        self.company = company
        self.country = country
        self.email = email

    def getInfo(self):
        temp = {'Name':self.name, 'Company':self.company, 'Country':self.country,
                'Email' : self.email}
        return temp

class Conference:
    def __init__(self, name, location, dates):
        self.attend = []
        self.name = str(name)
        self.location = str(location)
        self.dates = str(dates)
        print('Conference '+'\"'+self.name+'\"'+' is created.')

    def addAttendee(self, Attendee):
        self.attend.append(Attendee)
        return 'Attendee ' + Attendee.name + ' is added to the list of conference participants'

    def removeAttendee(self, Attendee):
        self.attend.remove(Attendee)
        return 'Attendee ' + Attendee.name + ' is removed from the list of conference participants'

    def displayAttendees(self):
        print('_' * 50)
        print('Name' + ' ' * 4 + 'Company' + ' ' * 4 + 'Country' + ' ' * 4 + 'Email' + ' ' * 4)
        print('_' * 50)
        for person in self.attend:
            print(person.name + ' ' * 4 + person.company + ' ' * 4 + person.country
                  + ' ' * 4 + person.email + ' ' * 4)

    def checkAttendee(self, name):
        for person in self.attend:
            if person.name == name:
                return name + ' is attending the conference.'
            else:
                return name + ' is not attending the conference.'

    def displayAttendeesFromCountry(self, country):
        print('_' * 50)
        print('Name' + ' ' * 4 + 'Company' + ' ' * 4 + 'Country' + ' ' * 4 + 'Email' + ' ' * 4)
        print('_' * 50)
        for person in self.attend:
            if person.country == country:
                return person.name + ' ' * 4 + person.company + ' ' * 4 + person.country + ' ' * 4 + person.email + ' ' * 4
        else:
            pass


Attendee1 = Attendee("John", "ABC Pharma", "Barbados", "john@abcpharma.com")
Attendee2 = Attendee('Lisa', 'HealthTech Inc.', 'Malaysia', 'lisa@healthtech.inc')
print(Attendee1.getInfo())
print()
conference1 = Conference("National conference on computing", "Seoul", "22-25 December, 2020")
print()
print(conference1.addAttendee(Attendee1))
print(conference1.removeAttendee(Attendee1))
conference1.addAttendee(Attendee1)
conference1.addAttendee(Attendee2)
conference1.displayAttendees()
print(conference1.checkAttendee("John"))
print(conference1.checkAttendee("Seung"))
print( conference1.displayAttendeesFromCountry("Barbados"))