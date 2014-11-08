Datacube
========
From the dataset collected from career website, a small data warehouse
is built by reading the information from input files .This data cubes
are build without using any databases such as SQL.

Data Structure used is Default Dictionary

Following functions have been implemented
1) Cuboid {StateID,JobID} is constructed from the Base Cuboid  [JobID]
-> [UserID,StateID,Country,Title]

Top 5 state-wise most popular job positions are calculated from the
constructed cuboid

2)Another cuboid is constructed from the base cuboid to perform the list
of top 5 most popular job titles in the given country
