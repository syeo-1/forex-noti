service that notifies people about desirable foreign exchange rates

uses rates using API at this url: https://free.currencyconverterapi.com/

to initiate a worker: heroku ps:scale worker=1
to deactivate the worker: heroku ps:scale worker=0

in the Procfile, specify process type (worker) and the command you want to do
	- this has been set up already

personal notes:
- only include libraries that do not already exist within standard library for requirements.txt
	- refer to this link: https://github.com/heroku/heroku-buildpack-python/issues/790
- after deploying successfully, all that needs to be done (currently) is to initiate a worker process
- remember to be in the appropriate directory to run the code in the terminal
	- heroku login first and then do the worker initiation
