import MySQLdb
import sys
#import getpass
import time
#import prettytable
import datetime
from backup_utility import  *
from plugins import default_values
import css 

#/* **************** Variable Declarations ********************* */
i = 0 
#i = default_values.I
cnt_ok=0
cnt_warning=0
global cnt_error
no_of_admin=0
adminuser=""
adminlist=""
counter = 0

def run_db_checker():
	#print("\n\t\t%s*****************Database Details*****************%s\n")%(css.h3Start,css.br)
	#print("\t\t************ Using Information Schema ***************\n\n%s%s%s")%(css.h3End,css.br, css.br)

	s_hostname = "localhost"	#default_input("\nEnter the source hostname of the database ,"localhost")
	s_port     = 3306			#default_input("\nEnter the source port of the database serverr.","3306")
	s_username = "root"			#default_input("\nEnter the source username that connects.", 'root')
	s_password = "password"			#getpass.getpass("\nEnter the source password.")
	db1        = "" 			#default_input("\nEnter the source database name.",'')#Default only one if second is not given
	
	print("%s%s\nYour Database Credentials: %s%s\n")%(css.br,css.boldStart,css.boldEnd, css.br)

	enc = "***********"
	print("Host Name: %s%s")%(s_hostname, css.br)
	print("\nUser Name: %s%s")%(s_username, css.br)
	print("\nPassword: %s%s")%(enc, css.br)
	print("\nDB name: " + db1 + "\n\n%s%s")%(css.br, css.br)




	#sys.stderr.write("Enter how many admin users exist: ")
	#no_of_admin=1	#int(raw_input(""))
	#sys.stderr.write("Enter name of admin user1: \n")
	#adminuser="root"		#raw_input("")
	#pwd="root"		#getpass.getpass("Enter admin user\'s password: ")
	#adminlist="\'%s\'"%(adminuser)

	checker(s_hostname, s_username, s_password, db1)
		
	# for i in range(2,no_of_admin+1):
	# 	sys.stderr.write("Enter the name of admin user"+str(i)+" : \n")	
	# 	a=raw_input("")	
	# 	adminlist=adminlist+","+"\'"+a+"\'"




	#/****************** USER DETAILS ************************* */
	# -- Countings the  no of unique users and displaying

	nusers = ("Select COUNT(Distinct USER) FROM mysql.user;")
	nusersResult = executeQueryOne(s_hostname, s_username,s_password, db1, nusers)
	no_of_user = nusersResult

	print("%s<b>User Details:</b>%s%s")%(css.boldStart,css.boldEnd, css.br)
	print("<b>No of User:</b> %s%s%s") %(str(no_of_user),css.br,css.br)


	# -- Selecting the unique users and displaying
	print("<b>Distinct Users:</b>%s")%(css.br)
	usersQuery=("SELECT Distinct USER FROM mysql.user;")
	userResult = executeQueryAll(s_hostname,s_username, s_password, db1, usersQuery)
	#print userResult
	i = 0
	for rows in userResult:
		for row in rows:
			print("Users[%s" %(i)+ " ]:" + row + css.br)
		i = i + 1	


	# -- Checking if the database port  is default(3306) OR changed
	global cnt_ok
	print("%s<b>DB server port :</b>")%(css.br)
	portQuery="SHOW VARIABLES LIKE 'Port'"
	portQueryResult = executeQueryAll(s_hostname,s_username, s_password, db1, portQuery)
	portQueryCount = portQueryResult[0][1]
	if portQueryCount!="3306" :
		cnt_ok=cnt_ok+1
		print "%s<b>Default Port</b> Is <b>Closed<b>. %s %s"%(css.okStart,css.ok,css.okEnd)
	else:
		cnt_warning = 0
		print "%s<b>Default Port<b> Is Open :  <b>%s</b> %s %s"%(css.wrStart,portQueryCount,css.warning,css.wrEnd)
		print css.portRecom
		cnt_warning=cnt_warning+1




	# -- Checking if any of the users have blank password
	print("%s<b>Users with Blank Password :</b>")%(css.br)
	usPassQuery="SELECT count(1) FROM mysql.user WHERE Password = '';"
	userPass = executeQueryOne(s_hostname,s_username, s_password, db1, usPassQuery)
	blankpwdcount=userPass
	if (str(blankpwdcount)=="0") :
		cnt_ok=cnt_ok+1
		print ("%sNo Blank Passwords For Any User.%s%s")%(css.okStart,css.ok,css.okEnd)
	else:
		cnt_warning = 0
		print ("%sBlank password exists for database user. Blank password count is %d. %s%s")%(css.wrStart,blankpwdcount,css.warning,css.wrEnd)
		print css.blankPassRecom
		cnt_warning=cnt_warning+1


	# -- Checking whether 'root' user exists or not
	print("%s<b>Existence of Root user :</b>")%(css.br)
	rootUserRenamed="SELECT count(1) FROM mysql.user WHERE User = 'root'"
	rootUserRenamedResult=executeQueryOne(s_hostname,s_username, s_password, db1, rootUserRenamed)
	rootusercount=rootUserRenamedResult
	if rootusercount==0 :
		cnt_ok=cnt_ok+1
		print ("%sRoot user has been renamed which  is good.%s %s ")%(css.okStart,css.ok,css.okEnd)
	else:
		cnt_warning = 0
		print ("%s \"root\" user has not been renamed. root user allowed to access from %d different hosts.%s %s ")%(css.wrStart,rootusercount,css.warning,css.wrEnd)
		cnt_warning=cnt_warning+1
		print css.rootUserRecom
		cnt_warning=cnt_warning+1



	# -- Checking whether anonymous user i.e. '' users exist or not
	print("%s<b>Existence of Anonymous user :</b>")%(css.br)
	anoUser="SELECT count(1) FROM mysql.user WHERE User = ''"
	anoUserResult=executeQueryOne(s_hostname,s_username, s_password, db1, anoUser)
	anoUserCount=anoUserResult
	if anoUserCount==0 :
		cnt_ok=cnt_ok+1
		print ("%sNo Anonymous User Exists. %s %s")%(css.okStart,css.ok,css.okEnd)
	else:
		cnt_warning = 0
		print ("%sAnonymous database users exist . Anonymous users allowed to access from %d different hosts. %s %s")%(css.wrStart,anoUserCount,css.warning,css.wrEnd)
		cnt_warning=cnt_warning+1



	# -- Checking whether user have database access from any host or not 
	print("%s<b>Database Accessibility :</b>")%(css.br)
	userAccHost="SELECT count(1) FROM mysql.user WHERE Host LIKE '%\%%'"
	userAccHostResult = executeQueryOne(s_hostname,s_username, s_password, db1, anoUser)
	userAccHostCount = userAccHostResult
	if userAccHostCount==0 :
		cnt_ok=cnt_ok+1
		print "%sNo User can access from ANY hosts which  is a good practice to follow %s%s"%(css.okStart,css.ok,css.okEnd)
	else:
		cnt_warning = 0
		print ("%sUsers found to be having database access from ANY hosts. Number of such entries found is %d. %s %s")%(css.wrStart,userAccHostCount,css.warning,css.wrEnd)
		cnt_warning=cnt_warning+1



	# -- Checking whether SSL is ENABLED OR NOT

	print("%s<b>DB Connection Encyption :</b>")%(css.br)
	sslQuery="SHOW VARIABLES LIKE '%_openssl%'"
	sslQueryResult = executeQueryAll(s_hostname,s_username, s_password, db1, sslQuery)
	sslQueryCount = sslQueryResult[0][1]
	if sslQueryCount=="Enabled" :
		cnt_ok=cnt_ok+1
		print "%sSSL Is Enabled. %s%s"%(css.okStart,css.ok,css.okEnd)
	else:
		cnt_warning = 0
		print "%sWarning: SSL Is Disabled. %s %s"%(css.wrStart,css.warning,css.wrEnd)
		cnt_warning=cnt_warning+1


	# -- Checking if Binary Logging is ON or OFF
	print("%s<b>Binary log status :</b>")%(css.br)
	binQuery="SHOW VARIABLES LIKE '%\log_bin%'"
	binQueryResult = executeQueryAll(s_hostname,s_username, s_password, db1, binQuery)
	binQueryCount = binQueryResult[0][1]
	if binQueryCount=="ON" :
		cnt_ok=cnt_ok+1
		print "%sBinary Logging Is Enabled. %s%s"%(css.okStart,css.ok,css.okEnd)
	else:
		cnt_warning = 0
		print "%sBinary Logging Is Disabled. %s%s"%(css.wrStart,css.warning,css.wrEnd)
		cnt_warning=cnt_warning+1


	# -- Checking whether slow query logging is ON or OFF
	print("%s<b>Slow query status :</b>")%(css.br)
	slowQuery="SHOW VARIABLES LIKE '%\slow_query%'"
	slowQueryResult = executeQueryAll(s_hostname,s_username, s_password, db1, slowQuery)
	slowQueryCount = slowQueryResult[0][1]
	slowQueryFIle = slowQueryResult[1][1]
	#print(slowQueryFIle)
	#print(slowQueryCount)
	if slowQueryCount=="ON" :
		cnt_ok=cnt_ok+1
		print ("%sSlow Query Logging Is Enabled and the log file is %s %s %s") %(css.okStart,slowQueryFIle,css.ok,css.okEnd)
	else:
		cnt_warning = 0
		print ("%sWarning: Slow Query Logging Is Disabled %s %s")%(css.wrStart,css.warning,css.wrEnd)
		cnt_warning=cnt_warning+1


	# -- Checking whether LOAD DATA LOCAL INFILE command is executable  or not
	print("%s<b>Local Infile command status :</b>")%(css.br)
	loadQuery="SHOW VARIABLES LIKE '%\local_infile%'"
	loadQueryResult = executeQueryAll(s_hostname,s_username, s_password, db1, loadQuery)
	loadQueryCount = loadQueryResult[0][0]
	loadQueryFIle = loadQueryResult[0][1]
	if loadQueryFIle!="ON" :
		cnt_ok=cnt_ok+1
		print ("%s'LOAD DATA LOCAL INFILE' Disabled.%s%s")%(css.okStart,css.ok,css.okEnd)
	else:
		cnt_warning = 0
		print ("%s'LOAD DATA LOCAL INFILE' Is Enabled.%s%s ")%(css.wrStart,css.warning,css.wrEnd)
		cnt_warning=cnt_warning+1



	total_auditpoints=cnt_ok+cnt_warning+cnt_error
	print("<h3>Final Pointers :</h3>")
	print("Out of %d Audit Factors: %s")%(total_auditpoints,css.br)
	print("<b>%d</b> - %sPass%s. %s")%(cnt_ok,css.okStart,css.okEnd,css.br)
	print("<b>%d</b> - %sWarnings%s. %s")%(cnt_warning,css.wrStart,css.wrEnd,css.br)
	print("<b>%d</b> - %sErrors%s. %s")%(cnt_error,css.erStart,css.erEnd,css.br)
	print("\nChecked All areas from audit check list. Please Take necessary actions to secure database. \n\n")
	#db.close()


	#sys.stderr.write("\n\nPlease check audit result in log file.\n\n")

	print("%s Database Server Grade: C %s%s")%(css.h3Start, css.h3End, css.br)

	#f.close()