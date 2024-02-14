=============
CryptoTracker
=============



About
----------
It's an open source and free bot for tracking popular cryptocurrencies from the `Coinmarketcap`_


.. _Coinmarketcap: https://coinmarketcap.com/ru/

.. contents:: :depth: 3




Futures
--------

1. Overview of most cryptocurrencies.
2. Setting currencies for tracking.
3. Setting a date for the bot to send you data in messages.



Usage
------
To use you need to open telegram bot and start it:

`<https://t.me/cryptotracker_official_bot>`_



Available cryptocurrencies
--------------------------------

::

  Bitcoin
  Ethereum
  Tether USDt
  BNB
  Solana
  XRP
  USDC
  Cardano
  Dogecoin
  Avalanche
  TRON
  Chainlink
  Polkadot
  Toncoin
  Polygon
  Dai
  Shiba Inu
  Litecoin
  Internet Computer
  Bitcoin Cash


Basic commands
--------------
The bot has several basic commands for interacting with your tracking orders.

``/start``
~~~~~~~~~~
The very first button that activates the bot. It also outputs a greeting.

``/orders``
~~~~~~~~~~~
Shows confirmation of orders.

``/help``
~~~~~~~~~~~
Shows current moderators who can help you.

``/clear``
~~~~~~~~~~
This command clears the current order and back you to welcome message.

``/remove``
~~~~~~~~~~~
Removes all your orders for tracking.



For developers
---------------

docker-compose
~~~~~~~~~~~~~~~
Docker compose allow you to deploy this bot on any machine if **docker** is available.
Follow the following steps to create your image.

1. Create **.env** in **docker-compose.yaml**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Folder structure must be shown as:

::

  .
  ├── bot
  ├── docker-compose.yaml
  ├── .env
  ├── init.sql
  ├── LICENSE
  └── README.rst

  2 directories, 4 files


2. Fill following data
^^^^^^^^^^^^^^^^^^^^^^^
Open **.env** file, paste and fill that data on your own.
:: 

  DSN="postgresql+psycopg://postgres:password@localhost:5433/postgres" #stable for that version
  BOT_KEY=""
  KEY=""

3. Start docker-compose
To build finally write that commands in terminal in main folder.

:: 

  docker-compose up

After a few time, your own docker multiple image will was build and run.



About
---------
- Main author: `IvanIsak2000 <https://github.com/IvanIsak2000>`_. Also known as Ivan Isakharov.
- Tracking issue: You can see the current `issues <https://github.com/IvanIsak2000/CryptoTracker/issues/>`_  or create new issue `here <https://github.com/IvanIsak2000/CryptoTracker/issues/new>`_.
