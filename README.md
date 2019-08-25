service that notifies people about desirable foreign exchange rates

uses rates using API at this url: https://free.currencyconverterapi.com/

to initiate a worker: heroku ps:scale worker=1
to deactivate the worker: heroku ps:scale worker=0

in the Procfile, specify process type (worker) and the command you want to do
	- this has been set up already

personal notes:
- only include libraries that do not already exist within standard library
	- refer to this link: https://github.com/heroku/heroku-buildpack-python/issues/790
- after deploying successfully, all that needs to be done (currently) is to initiate a worker process
