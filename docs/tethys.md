# Tethys

## Getting Started

These steps are based on the docs.tethysplatform.org [Developer Installation](http://docs.tethysplatform.org/en/stable/installation/developer_installation.html#developer-installation) documentation.

#### Install
```
$ curl https://raw.githubusercontent.com/tethysplatform/tethys/release/scripts/install_tethys.sh -o ./install_tethys.sh
$ bash install_tethys.sh -b release -t ~/Documents/Projects/python-visualization/.tethys/${CONDA_ENV_NAME}
```

#### Or Install as Submodule
```
$ git submodule add -b release git@github.com:tethysplatform/tethys.git tethys
$ bash scripts/install_tethys.sh
$ git submodule init
```
#### Configure
```
$ . ~/.bash_profile
```

#### Start server
```
$ t
$ tethys manage start
```

#### Access client
http://127.0.0.1:8000

#### Login
- User: admin
- Password: pass


## How to Startup Again

When you start up a new terminal, there are three steps to get the Tethys development server running again:
1. Activate the Tethys conda environment
2. Start the Tethys database server
3. Start the Tethys development server

Using the supplied aliases, starting the Tethys development server from a fresh terminal can be done with the following two commands:
```
$ t
$ tstart
```

## Important Paths

#### Project root
Note: The .tethys project root directory is hidden.

```
.tethys/
    miniconda.sh		
    portal_config.yml
    psql			
    tethys
```

#### Log
`.tethys/tethys-dev/psql/logfile`

## Remove Tethys
```
$ rm -rf /path/to/.tethys
$ rm -rf /Users/me/miniconda/envs/tethys-dev
```

## Troubleshooting
I have another instance of PostgreSQL running on my machine ($ brew services) listening to port 5432 for Metalnx.

I needed to update the /Users/me/.tethys/tethys-dev/psql/data/:
```
#------------------------------------------------------------------------------
# CONNECTIONS AND AUTHENTICATION
#------------------------------------------------------------------------------

# - Connection Settings -

#listen_addresses = 'localhost'		# what IP address(es) to listen on;
					# comma-separated list of addresses;
					# defaults to 'localhost'; use '*' for all
					# (change requires restart)
port = 5436				# (change requires restart)
```
Then I needed to restart my Tethys database:
```
pg_ctl -D '/Users/me/.tethys/tethys-dev/psql/data' -l logfile restart
```

## Resources
- https://github.com/tethysplatform/tethys
- http://www.tethysplatform.org/
- http://docs.tethysplatform.org/en/stable/installation/developer_installation.html#developer-installation
- https://www.vogella.com/tutorials/GitSubmodules/article.html