# bta
Beating The Alternative: a tool for generating reports from health tracking data sources

# installation

## requirements
> pip install myfitnesspal 

# using

## usage
> mthome$ myfitnesspal store-password MYUSERNAME
> MyFitnessPal Password for MYUSERNAME: 
> 
> mthome$ ./bta.py MYUSERNAME

## glucose notes

> fasting [time]
> 7:15am 101
> 
> breakfast [8:30 [101]]
> 9:30 130 10:30 110 !awesome

The general form is:
> meal [time [glucose]
> time glucose [time2 glucose2 ...]

Where meal is one of fasting, breakfast, lunch, dinner, snack

# references
The basic access library is https://github.com/coddingtonbear/python-myfitnesspal

For excel output: https://openpyxl.readthedocs.org/en/2.3.3/

And I'll probably also add hsql and sqlalchemy to keep a local database of information and to aggregate from multiple services.

