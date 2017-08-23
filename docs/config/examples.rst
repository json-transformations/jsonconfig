####################
JSON Config Examples
####################

=============================================
Storing & Retrieving Database Server Settings
=============================================

.. code:: 

  from jsonconfig import Config

  # Save the settings.

  with Conf('Mongo DB') as mongo:
    mongo.data = {"domain": "www.example.com",
      "mongodb": {"host": "localhost", "port": 27017}}

  # Retrieve the settings.

  with Conf('Mongo DB') as mongo:
      data = mongo.data

Retrieve the hostname & port from environments variables if they exist,
otherwise pull the information from the configuration file if it exists,
otherwise use default values.

.. code::

  from jsonconfig import Config

  with Conf('Mongo DB') as db:
      host = db.env['M_HOST'] or db.data['mongodb']['host'] or 'localhost'
      port = int(db.env['M_PORT'] or db.data['mongodb']['port'] or 27017)

================================================
Storing & Retrieving the Current State of a Game
================================================

.. code::

  from jsonconfig import BoxConfig, Config

  with Config('Chess Tournaments') as chess_match:
      chess_match.data = [
          {
              "Event": "Kramnik - Leko World Championship Match",
              "Site": "Brissago SUI",
              "Date": "2004.10.03",
              "EventDate": None,
              "Round": 6,
              "Result": None,
              "White": {"Name": "Vladimir Kramnik", "Elo": None},
              "Black": {"Name": "Peter Leko", "Elo": None},
              "ECO": "C88",
              "PlyCount": 40,
              "Moves": [
                  'e4 e5', 'Nf3 Nc6', 'Bb5 a6', 'Ba4 Nf6', 'O-O Be7',
                  'Re1 b5', 'Bb3 O-O', 'h3 Bb7', 'd3 d6', 'a3 Na5'
              ]
          }
      ]

  # Pick the game up where it left off and add new moves.

  with BoxConfig('Chess Tournaments') as chess_matches:
      match = chess_matches[0].data
      match.Moves.append([
          'Ba2 c5', 'Nbd2 Nc6', 'c3 Qd7', 'Nf1 d5', 'Bg5 dxe4',
          'dxe4 c4', 'Ne3 Rfd8', 'Nf5 Qe6', 'Qe2 Bf8', 'Bb1 h6'
      ])
      match.Result = '1/2-1/2'

  # Retrieve the data for all matches.

  with Config('Chess Tournaments') as chess_matches:
        match = chess_matches.data

=================================================
Making a Request from a Restful API Settings File
=================================================

.. code::

  from jsonconfig import Config

  api_info = {
      "headers": {"Authorization: Bearer {access_token}"}
      "parameters": {"includeAll": True}
      "resources": {"sheet": {"endpoint": "sheets/{sheetId}"}}
  )

  # example of saving both standard and enrypted data

  with Config('Sample API') as api:

      # save standard data
      api.data = api_info  

      # save encyrpted data
      api.pwd.access_token = 'll352u9jujauoqz4gstvsae05'

  # example of updating an existing configuration

  with Config('Sample API') as api:
      api.data['url'] = "https://api.smartsheet.com/2.0/"

Pull access token from environment variable if it exists, otherwise pull
it from the Keyring vault, it it doesn't exist there either prompt the
user for the password and mask the characters as they're typed in. 

.. code::

  import requests
  from jsonconfig import getpass, BoxConfig

  with BoxConfig('API Example') as api:
      endpoint = api.data.resources.sheet.endpoint
      access_token = api.env.ACCESS_TOKEN or api.pwd.access_token or getpass
      response = requests.get(
          api.data.url + endpoint.format(sheetId=4583173393803140),
          headers = api.data.headers.format(access_token),
          parameters = api.data.parameters
      )
