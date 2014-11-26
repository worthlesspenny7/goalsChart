#### Goal:  Display the amount needed at any given time at 1 week resolution in order to pay for all of the goals in the input list
import datetime
import pylab as plt

def startBalance():
    '''Input current account balance'''
    return raw_input('What is the Starting Balance of the Account?: ')
    
#def goalEntry(goalTable):
#    '''Input goal information - Goal name, Estimated Goal Cost, Date of Goal Expenditure
#    
#    input - goalTable - list of lists containing goal attributes [goalName, goalCost, goalDate, dateEntered = datetime.date.today()]
#    returns - sorted (on name) goalTable with new goal lists to goalTable '''
#    while True:
#        goalEntry = raw_input('Would you like to add another goal? (y/n) ')
#        if goalEntry == 'y':
#            try:
#                goalName = str(raw_input('What is the name of the goal? '))
#                goalCost = float(raw_input('What is the cost of the goal? '))
#                goalDate = raw_input('When will you pay for this goal? Enter in MM/DD/YYY ') # need to format date as datetime format and manage exceptions
#                # test, the time tuple has the following items ...
#                # (year,month,day,hour,min,sec,weekday(Monday=0),yearday,dls-flag)
#                date_tuple = datetime.datetime.strptime(goalDate, "%m/%d/%Y")
#                #difference between goalDate and dateEntered (c.days = difference in days)
#                c = date_tuple - datetime.datetime.today()
#                # savings rate per day
#                r = goalCost / c.days
#                #goal list <goalName, goalCost, goalDate(datetime object), date entered(datetime object), difference in dates (days), savings rate per day>
#                goalTable.append([goalName, goalCost, date_tuple , datetime.datetime.today(), c.days, r])
#            except:
#                ValueError('Please enter the correct value type') # fix the behavior so this message prints
#        else:
#            break
#    return sorted(goalTable) # need to sort on date rather than name

class Goal(object):
    def __init__(self, goalName, goalCost, goalDate, goalStart):
        '''goalName == string
            goalCost == int or float
            goalDate == datetime tuple'''
        self.goalName = goalName
        self.goalCost = float(goalCost)
        self.goalDate = goalDate
        self.goalStart = goalStart
    def getGoalName(self):
        return self.goalName
    def getGoalCost(self):
        return self.goalCost
    def getGoalDate(self):
        return self.goalDate
    def getGoalStart(self):
        return self.goalStart
    def getDailySavingsRate(self):
        c = self.goalDate - self.goalStart
        return self.goalCost / c.days
        
class User(object):
    def __init__(self, goals):
        '''goals is a list of Goal objects'''
        self.goals = goals
        dateRangeStart = datetime.datetime(2014,1,1) #(yyyy, mm, dd)
        self.dateDict = {}
        #populating dateDict with key for each day (datetime tuple) for a year from 
        #dateRangeStart with a value of 0
        for i in range(365):
            self.dateDict[dateRangeStart+datetime.timedelta(days=i)] = 0
    def getGoals(self):
        return self.goals
    def calculateDailySums(self):
        '''for each date in dateDict, see if it falls between the start and end
        #date of each goal, if yes, add Daily Savings Rate to value
        
        returns dateDict - dict containg all dates in range and total daily savings rate'''
        for day in self.dateDict.keys():
            for goal in self.goals:
                if day >= goal.getGoalStart() and day <= goal.getGoalDate():
                    self.dateDict[day] += goal.getDailySavingsRate()
        return self.dateDict
        
        

#def generateData(goalTable):
#    '''Iterates over each list in the goalTable list and determines if each goal falls within a day of the year, 
#    if it does, adds the savings rate per day to that day's savings rate'''
#    #Generating a table of days for each day in 2014
#    dateTable = {}
#    for i in range(365):
#        startDate = datetime.datetime(2013,12,20)
#        dateTable[startDate+datetime.timedelta(days=i)] = 0
#    
#    #Looping over the goalTable add the daily savings rate to each day
#    for i in goalTable:
#        #print 'goal of interest: ' + str(i)
#        for j in dateTable:
#            #print D
#            #print j, ' is between ', i[3], ' and ', i[2], ' ', j >= i[3] and j <= i[2]
#            if j >= i[3] and j <= i[2]: #if the date in question from dateTable is between the goal's date entered and goalDate
#                dateTable[j] = dateTable.get(j) + i[5] # get the value associated with the date key and add the daily savings rate from the goal
#    #print the table with added daily savings rate
#    goalSum = 0A
#    daySumTable = {}
#    for i in sorted(dateTable):
#        goalSum += dateTable.get(i)
#        daySumTable[i] = goalSum
#        print i, ' ', dateTable.get(i), ' ', goalSum
#    return dateTable, daySumTable

###Calculate how much money will need to be saved each week for that goal for the next 52 weeks
###Sum the amount needed for each week for the next 52 weeks
###Display the summed amount needed for each week for the next 52 weeks plus the last 52 weeks with actual account balance info.
def plotSavings(dateDict):
    '''takes dateDict, plots ******TBD rethink how to add the daily sums so output is
    linear up and drops after each goal is spent'''
    dates = []
    goalSum = []
    daySum = 0
    for day in sorted(dateDict.keys()):
        dates.append(day)
        daySum += dateDict[day]
        goalSum.append(daySum)
        print 'day ' + str(day) + ' daySum ' + str(daySum)
    plt.plot(dates, goalSum)
    plt.title('Joshs Savings Graph!!!!')
    plt.xlabel('Week')
    plt.ylabel('Dollars')
    plt.show()
    
    
    
## Main
goals = [] 

#Test Code - uncomment when testing full program
#Goal(goalName, goalCost, goalDate, goalStart):

g1 = Goal('baby coming', 500.0, datetime.datetime(2014, 6, 14), datetime.datetime(2014, 2, 21))
g2 = Goal('anniversary', 1000.0, datetime.datetime(2014, 9, 6), datetime.datetime(2014, 5, 15))

goals = [g1, g2]

josh = User(goals)
   
plotSavings(josh.calculateDailySums())
