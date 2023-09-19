# OverView

Code to pull statistics from the Yahoo Fantansy Football site.

## Structure

CurrywareStatHarvestor  
    |--.github/worflows  
    |-- *Build Actions for Github*  
    |  
    |-- classes  
    |  
    |---- authentication  
    |---- *Authentication to Firebase and FireStore*  
    |  
    |---- fantasy  
    |---- *Any calls to the Yahoo API*  
    |  
    |---- firebase  
    |---- *Calls that read or store information in the Google Realtime Database*  
    |  
    |---- firestore  
    |---- *Calls that read or store information in the Firestore Database*  
    |  
    |---- http  
    |---- *The REST API handler for all REST API calls  
    |  
    |---- settings  
    |---- *A handler class to pull values from the app_settings.yaml file*  
    |  
    |---- utilities  
    |---- *Currently a way to turn the team name into the Yahoo team ID and URL substitution for different teams*  
    |  
    |---- tests  

## Note

There is an authentication JSON file that is not stored in the repository.  The google_build_authentication.py uses
Github Actions secrets. If running locally it pulls the private key from a file.