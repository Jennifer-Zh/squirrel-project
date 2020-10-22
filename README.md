# Squirrel Tracker Project 
This is the squirrel tracker project for course E4501. 

## Contributors 
Wenxin Zhou (wz2551)
Yujia Zhang (yz3932) 

## Data Source 
* creator: City of New York      
* name: 2018 Central Park Squirrel Census - Squirrel Data     
* link: https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw     

## Goal 
We are trying to keep track of the squirrels found in the Central Park. 

## Different Views  
### 1. '/map'
* Method: GET 
* Diplay a snapshot of squirrel locations on a map 

### 2. '/sightings' 
* Method: GET 
* Display a list of squirrels with their unique IDs and the date it was found 
* Each unique ID is clickable, and by clicking, one could make updates on this squirrel 

#### 2.1 '/sightings/<unique_squirrel_id>' 
* Method: GET & POST 
* Diplay different fields of a squirrel, such as latitude, longitude, ID, shift, date, and age 
* One could make updates by clicking the "Update" button at the end of the page 

#### 2.2 '/sightings/add' 
* Method: GET & POST 
* Add a new squirrel record to the database 
* Among all the fields, latitude, longitude, unique squirrel ID, and date are required 

#### 2.3 '/sightings/stats'  
* Method: GET 
* Display some statistics of the squirrels in the Central Park 

## Required Environments 
* Django 3.1.2
* Pillow 8.0.0 
* OpenStreetMaps 

## Management Commands 
* 'import_squirrel_data'     
  This command could import a csv file to a database. The first argument should be the path of csv file. 
  e.g. run 'python manage.py import_data Squirrel.csv' to add data file
* 'export_squirrel_date'      
  This command could export database to a csv file. The first argument should be the path of csv file. 

## License 
