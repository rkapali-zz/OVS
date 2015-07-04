from subprocess import PIPE, Popen
import MySQLdb
import datetime
import sys
import css

cnt_error = 0




#/* ************* function for executing system commands *************** */

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        stderr=PIPE,
        shell=True
    )
    return process.communicate()[0]


#/* *************** Creating a file to write into it ***************** */
'''
now = datetime.datetime.now()                           
date_stamp = now.strftime("%Y-%m-%d-%H-%M-%S")
filename = "db_audit_report_"
filepath = "./logs/"
f_filename = filepath + filename + date_stamp + ".html"
newline = "\n"
f = open(f_filename, 'w')
sys.stdout = f
'''

#/************************* Function for checking  db connection ************* */

def checker(h_name, username, passwd, db1):
    while True:    
        try:
            db = MySQLdb.connect(h_name, username, passwd, db1)
            cursor = db.cursor()
            cursor.execute("SELECT VERSION()")
            results = cursor.fetchone()
            #result1 = int(results)
            # Check if anything at all is returned
            if results:
                
                print("%sThe Credentials are correct to connect...%s%s%s")%(css.okStart,css.okEnd,css.br,css.br)
                return 1
            else:
                print("%sCredentials Mix-match...%s%s")%(css.erStart, css.erEnd, css.br)
                return 0
                break
        except MySQLdb.Error:
            print("%sCredentials Mix-match...%s%s")%(css.erStart, css.erEnd, css.br)
            return 0
            break    
#/************************* MySQLDB Function executing single result query ************* */

def executeQueryOne(h_name, username, passwd, db1, query):
    result1 = ''
    global cnt_error
    try:
        db = MySQLdb.connect(h_name, username, passwd, db1)
        cursor = db.cursor()        
        cursor.execute(query)
        results = cursor.fetchone()
        # Check if anything at all is returned
        #for row in results:
        result1 = results[0]
        return result1
        
    except:
        #print("\n\n\n ENtering Except block")
        print("%sError  : Unable to fetch data. %s%s%s")%(css.erStart,css.error, css.erEnd, css.br)
        cnt_error=cnt_error+1


#/************************* Function for hadling  multidimensional outputs  ************* */

		
def executeQueryAll(h_name, username, passwd, db1, query):
    #result1 = ''
    global cnt_error
    try:
        db = MySQLdb.connect(h_name, username, passwd, db1)
        cursor = db.cursor()        
        cursor.execute(query)
        results = cursor.fetchall()
        # Check if anything at all is returned
        #for row in results:
        result1 = results
        return result1
        
    except:
        #print("\n\n\n ENtering Except block")
        print("%sError  : Unable to fetch data. %s%s")%(css.erStart, css.error, css.erEnd)
        cnt_error=cnt_error+1



# /*************************** Function for user interactive input with default values *********** */

def default_input( message, defaultVal ):
    if defaultVal:
        return raw_input( "%s [%s]:" % (message,defaultVal) ) or defaultVal
    else:
        return raw_input( "%s " % (message) )

