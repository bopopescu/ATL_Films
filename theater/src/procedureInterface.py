from theater import app
import mysql.connector

#db connection info
user = "team50"
password = "Columns1!"
host = "127.0.0.1"
db = 'team50'

def connect():
    connection = mysql.connector.connect(user=user, password=password, host=host, db=db)
    return connection

def prep(query):
    query = list(query)
    aposts = []
    
    for i, e in enumerate(query):
        if e == "'":
            aposts.append(i)
    for i in aposts:
        query.insert(i, "'")
    query = ''.join(query)
    return query

def query(sql):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

### Executes Stored Percedures
#screen 1
def userLogin(user, password):
    connection = connect()
    cursor = connection.cursor()
    sql = "use `Team50`;"
    cursor.execute(sql)
    sql = "call user_login('{}', '{}');".format(user, password)
    cursor.execute(sql)
    sql = "select * from UserLogin;"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data


#screen 3
def userRegister(user, password, first, last):
    user = prep(user)
    password = prep(password)
    connection = connect()
    cursor = connection.cursor()
    sql = "call user_register('{}','{}','{}','{}');".format(user, password, first, last)
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()

#screen 4
def custRegister(user, password, first, last):
    user = prep(user)
    password = prep(password)
    connection = connect()
    cursor = connection.cursor()
    sql = "call customer_only_register('{}', '{}', '{}', \
           '{}');".format(user, password, first, last)
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()

#screen 4
def custAddCC(user, cc):
    user = prep(user)
    connection = connect()
    cursor = connection.cursor()
    sql = "call customer_add_creditcard('{}', \
           '{}');".format(user, cc)
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()

#screen 5
def manRegister(user, password, first, last, company, street, 
                city, state, zipcode):
    user = prep(user)
    password = prep(password)
    company = prep(company)
    street = prep(street)
    connection = connect()
    cursor = connection.cursor()
    sql = "call manager_only_register('{}', '{}', '{}', '{}',\
           '{}','{}', '{}', '{}', '{}');".format(user, password, first, last, 
           company, street, city, state, zipcode)
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()

#screen 6
def manCustRegister(user, password, first, last, company, street, 
                city, state, zipcode):
    user = prep(user)
    password = prep(password)
    company = prep(company)
    street = prep(street)
    connection = connect()
    cursor = connection.cursor()
    sql = "call manager_customer_register('{}', '{}', '{}', '{}', '{}',\
           '{}', '{}', '{}', '{}');".format(user, password, first, last, 
           company, street, city, state, zipcode)
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()

#screen 6
def manCustAddCC(user, cc):
    user = prep(user)
    connection = connect()
    cursor = connection.cursor()
    sql = "call manager_customer_add_creditcard('{}','{}');".format(user, cc)
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()

#screen 13
def adminApproveUser(user):
    connection = connect()
    cursor = connection.cursor()
    sql = "call admin_approve_user('{}');".format(user)
    cursor.execute(sql)
    cursor.close()
    connection.close()

#screen 13
def adminDeclineUser(user):
    connection = connect()
    cursor = connection.cursor()
    sql = "call admin_decline_user('{}');".format(user)
    cursor.execute(sql)
    cursor.close()
    connection.close()

#screen 13
def adminFilterUser(user, status, sortBy, sortDirection):
    connection = connect()
    cursor = connection.cursor()
    sql = "call admin_filter_user('{}', '{}', '{}', '{}');".format(
        user, status, sortBy, sortDirection)
    cursor.execute(sql)
    sql = "select * from AdFilterUser;"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data
    
#screen 14    
def adminFilterCompany(comName, minCity, maxCity, minTheater,  
            maxTheater, minEmp, maxEmp, sortBy, sortDirection):
    connection = connect()
    cursor = connection.cursor()
    sql = "call admin_filter_company('{}', {}, {}, {}, {}, {}, {}, '{}', '{}');".format(comName, minCity, maxCity, 
           minTheater, maxTheater, minEmp, maxEmp, sortBy, sortDirection)
    cursor.execute(sql)
    sql = "select * from AdFilterCom;"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

#screen 15
def adminCreateTheater(theaterName, comName, street, city, state, 
                        zipcode, cap, manUser):
    theaterName = prep(theaterName)
    comName = prep(comName)
    street = prep(street)
    city = prep(city)
    connection = connect()
    cursor = connection.cursor()
    sql = "call admin_create_theater('{}', '{}',\
           '{}', '{}', '{}', \
           '{}', {}, '{}');".format(theaterName, comName, street, city, state, 
           zipcode, cap, manUser)
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()

#screen 16                
def adminViewComDetail_emp(company):
    connection = connect()
    cursor = connection.cursor()
    sql = "call admin_view_comDetail_emp('{}');".format(company)
    cursor.execute(sql)
    sql = "select * from AdComDetailEmp"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

#screen 16
def adminViewComDetail_th(company):
    connection = connect()
    cursor = connection.cursor()
    sql = "call admin_view_comDetail_th('{}');".format(company)
    cursor.execute(sql)
    sql = "select * from AdComDetailTh;"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

#screen 17
def adminCreateMovie(movie, duration, releaseDate):
    movie = prep(movie)
    connection = connect()
    cursor = connection.cursor()
    sql = "call admin_create_mov('{}', {}, \
           '{}');".format(movie, duration, releaseDate)
    try:
        cursor.execute(sql)
        connection.commit()
        cursor.close()
        connection.close()
        return None
    except:
        message = "Cannot create duplicate movies"
        connection.commit()
        cursor.close()
        connection.close()
        return message


#screen 18
def manageFilterTheater(manUser, movie, minDur, maxDur, minMovRD, 
             maxMovRD, minMovPD, maxMovPD, includeNotPlayed):
    connection = connect()
    cursor = connection.cursor()
    if minMovRD != 'NULL':
        minMovRD = "'" + minMovRD + "'"
    if maxMovRD != 'NULL':
        maxMovRD = "'" + maxMovRD + "'"
    if minMovPD != 'NULL':
        minMovPD = "'" + minMovPD + "'"
    if maxMovPD != 'NULL':
        maxMovPD = "'" + maxMovPD + "'"
    
    sql = "call manager_filter_th('{}', '{}', {}, {}, \
           {}, {}, {}, {}, {});".format(manUser, movie, minDur, maxDur, minMovRD, 
           maxMovRD, minMovPD, maxMovPD, includeNotPlayed)
    cursor.execute(sql)
    sql = "select * from ManFilterTh;"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data 

#screen 19
def managerScheduleMovie(manUser, movie, movRD, movPD):
    manUser = prep(manUser)
    movie = prep(movie)
    connection = connect()
    cursor = connection.cursor()
    sql = "call manager_schedule_mov('{}', '{}', \
           '{}', '{}');".format(manUser, movie, movRD, movPD)
    try:
        cursor.execute(sql)
        data = "Movie Scheduled"
        connection.commit()
    except:
        data = "An Error Occured"
    cursor.close()
    connection.close()
    return data

#screen 20
def customerFilterMovie(movName, comName, city, state, 
            minMovPlayDate, maxMovPlayDate):
    connection = connect()
    cursor = connection.cursor()
    if minMovPlayDate != 'NULL':
        minMovPlayDate = "'" + minMovPlayDate + "'"
    if maxMovPlayDate != 'NULL':
        maxMovPlayDate = "'" + maxMovPlayDate + "'"

    sql = "call customer_filter_mov('{}', '{}',\
           '{}', '{}', {}, {});".format(movName, comName, city, state, 
            minMovPlayDate, maxMovPlayDate)
    cursor.execute(sql)
    sql = "select * from CosFilterMovie;"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

#screen 20
def customerViewMovie(i_creditCardNum, i_movName, i_movReleaseDate, i_thName, 
                i_comName, i_movPlayDate):
    i_movName = prep(i_movName)
    i_thName = prep(i_thName)
    i_comName = prep(i_comName)
    connection = connect()
    cursor = connection.cursor()
    sql = "call customer_view_mov('{}', '{}', '{}', '{}', '{}', '{}');".format(i_creditCardNum, 
           i_movName, i_movReleaseDate, i_thName, i_comName, i_movPlayDate)
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()

#screen 21
def customerViewHistory(user):
    connection = connect()
    cursor = connection.cursor()
    sql = "call customer_view_history('{}');".format(user)
    cursor.execute(sql)
    sql = "select * from CosViewHistory;"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

#screen 22
def userFilterTheater(i_thName, i_comName, i_city, i_state):
    i_thName = prep(i_thName)
    i_comName = prep(i_comName)
    connection = connect()
    cursor = connection.cursor()
    sql = "call user_filter_th('{}', '{}', '{}',\
           '{}');".format(i_thName, i_comName, i_city, i_state)
    cursor.execute(sql)
    sql = "select * from UserFilterTh;"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

#screen 22
def userVisitTheater(i_thName, i_comName, i_visitDate, i_username):
    i_thName = prep(i_thName)
    i_comName = prep(i_comName)
    i_username = prep(i_username)
    connection = connect()
    cursor = connection.cursor()
    sql = "call user_visit_th('{}','{}','{}','{}');".format(i_thName, i_comName, i_visitDate, i_username)
    cursor.execute(sql)
    connection.commit()
    cursor.close()
    connection.close()

#screen 23
def userFilterVisitHistory(i_username, i_minVisitDate, i_maxVisitDate):
    connection = connect()
    cursor = connection.cursor()
    if i_minVisitDate != 'NULL':
        i_minVisitDate = "'" + i_minVisitDate + "'"
    if i_maxVisitDate != 'NULL':
        i_maxVisitDate = "'" + i_maxVisitDate + "'"
    sql = "call user_filter_visitHistory('{}', {},\
        {});".format(i_username, i_minVisitDate, i_maxVisitDate)
    cursor.execute(sql)
    sql = "select * from UserVisitHistory"
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data