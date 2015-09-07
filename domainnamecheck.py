'''
    Python Script to check domain name available or not . 
''' 
import csv 
import urllib2 
import socket 
import httplib 

def write_data_to_file(filename,data):
    week_stock_data = open(filename, 'a')
    week_stock_data.write(data)
    week_stock_data.write('\n')
    week_stock_data.close() 

with open('domainnames5.csv','r') as cncsvfile:
    domain_name = csv.reader(cncsvfile, delimiter=',', quotechar='"')
    for row in domain_name:
        domain = 'http://' + str(row[0]) + '.com'
        try:
            response = urllib2.urlopen(domain)
            print domain,' is taken'
        except urllib2.HTTPError as e:
            print domain,' is available'
            write_data_to_file('availabledomains.txt',domain)
        except urllib2.URLError as e:
            print domain,' is available'
            write_data_to_file('availabledomains.txt',domain)
        except socket.error as e:
            print domain,' is taken'
        except httplib.BadStatusLine as e:
            print domain,' is taken'
            
