'''
Created on Oct 10, 2014

@author: karav_000
'''
import csv
import sys

dict1 = {}
dict2 = {}
dict3 = {}

topstates =[]
toptitles = []

state_jobid_groupby = {}
country_title_groupby = {}

class A:
    
    def datacube(self,listdir1,listdir2,listdir3):
        
        """ Dictionary with UserID as Key and StateID,Country as the Value
                [UserID] -> (StateID,Country)  Value as stored as Tuple
        """
        
        i = 0
        for row in open(listdir1):
            rowval = row.strip().split('\t')
            
            Uid= rowval[0]
            loc = rowval[2]
            cou = rowval[3]
            
            dict1[Uid] = (loc,cou)
            
        """ Dictionary with JobID as Key and Title as Value
                [JobID] -> (Title)   Value as stored as Tuple
        """
        i = 0
        for row in open(listdir2):
        
            rowval = row.strip().split('\t')
            
            JobId= rowval[0]
            title = rowval[1]
            
            dict2[JobId] = (title)
                    
        """ Base Cuboid is created [JobID] -> [UserID,StateID,Country,Title]
                                                Value as stored as List
        """
        
        i = 0
        for row in open(listdir3):
                         
            rowval = row.strip().split('\t')
            
            UserId= rowval[0]
            JobId = rowval[2]
                           
            list_insert = [UserId,dict1.get(UserId, ("default state","default country")) ,dict2.get(JobId, "NULL")]
    
            dict3.setdefault(rowval[2],[]).append(list_insert)
            
        '''Slicing the Base Cuboid [(StateID,Country),JobID] -> [UserID] Values are stored in form of Lists '''    
        
        for item in dict3:
            for itemeach in dict3[item]:
                state_jobid_groupby.setdefault((itemeach[1],item),[]).append(itemeach[0])
        
        '''Sorting and Ranking the items in the Sliced Dictionary
           to get the Top 5 Count of StateID and JobID '''
        
        count_list = []
        
        for item in state_jobid_groupby:
            count_list.append([len(state_jobid_groupby.get(item)),item])            
        
        count_list.sort(reverse=True)
        topstates = count_list[:5]
        
        print"[Count,   Location,    UserID)]"
        
        for nested_list in topstates:
            print (nested_list)
            
        '''Slicing the Base Cuboid [(Country,Title)] -> [UserID] Values are stored in form of Lists '''
        
        for item in dict3:
            for itemeach in dict3[item]:
                    
                country_title_groupby.setdefault(((itemeach[1][1],itemeach[2])),[]).append(itemeach[0])
           
        count_list = []
        
        
        '''Sorting and Ranking the items in the Sliced Dictionary
           to get the Top 5 Count of TitleID and number of Applicants '''
        
        for item in country_title_groupby:
            if item[0]=='IN':
                count_list.append([len(country_title_groupby.get(item)),item[1]])            
        
        count_list.sort(reverse=True)
        toptitles = count_list[:5]
        
        
        print("\n")
        print"[Count,   TitleID]"
        
        for nested_list in toptitles:
            print (nested_list)
        
if __name__ == '__main__':
    a = A()
    Listdir = sys.argv
    a.datacube(Listdir[1],Listdir[2],Listdir[3])
