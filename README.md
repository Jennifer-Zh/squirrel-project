# Squirrel Tracker Project 
This is the squirrel tracker project for course E4501. 

## Contributors 
Wenxin Zhou      
Yujia Zhang  
Group Wenxin & Jennifer 
UNIs: [wz2551, yz3932] 

## Goal 
We are trying to keep track of the squirrels found in the Central Park in 2018, by showing their footprint on a map, and listing their occurences and characteristics, along with the options to update or add new squirrel record. 

## Data Source 
* For this project, we cleaned the dataset to include only squirrels with unique ID, which is the ```Squirrel.csv``` file in the repository.      
* Reference to the original dataset:      
  * creator: City of New York      
  * name: 2018 Central Park Squirrel Census - Squirrel Data     
  * link: https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw     

## Required Environments 
* Django 3.1.2 
* Pillow 8.0.0
* You may also run the following command to install: 
  ```
  $ pip install -r requirements.txt
  ``` 
  
## Management Commands 
#### ```import_squirrel_data```  
* This command could import a csv file to a database. The first argument should be the path of csv file.     
* The user should run the following command to import the squirrel data:       
  ``` 
  $ python manage.py import_squirrel_data Squirrel.csv 
  ``` 
  
#### ```export_squirrel_date```       
* This command could export database to a csv file. The first argument should be the path of csv file. 
* The user should run the following command to export the squirrel data:      
  ```
  $ python manage.py export_squirrel_data export_data.csv
  ```

## Different Views  
### 1. ```/map```
* Method: GET 
* Diplay a snapshot of squirrel locations on a map 

### 2. ```/sightings``` 
* Method: GET 
* Display a list of squirrels with their unique IDs and the date it was found     
* Each unique ID is clickable, and by clicking, one could make updates on this squirrel     

#### 2.1 ```/sightings/<unique_squirrel_id>``` 
* Method: GET & POST 
* Diplay different fields of a squirrel, such as latitude, longitude, ID, shift, date, and age 
* One could make updates by clicking the "Update" button at the end of the page 

#### 2.2 ```/sightings/add``` 
* Method: GET & POST 
* Add a new squirrel record to the database 
* Among all the fields, latitude, longitude, unique squirrel ID, and date are required 

#### 2.3 ```/sightings/stats``` 
* Method: GET 
* Display some statistics of the squirrels in the Central Park 

## License 
This Squirrel-project is made available under the Open Database License: http://opendatacommons.org/licenses/odbl/1.0/. Any rights in individual contents of the database are licensed under the Database Contents License: http://opendatacommons.org/licenses/dbcl/1.0/

