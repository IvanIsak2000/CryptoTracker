=============
CryptoTracker
=============

-------------------------------------------------------------------------------------------------------------------------------------------
This is an open source and completely free bot for tracking the most popular cryptocurrencies right in your telegram from `Coinmarketcap <https://coinmarketcap.com/>`_ .
-------------------------------------------------------------------------------------------------------------------------------------------

.. contents:: :depth: 2

Opportunities
-------------
1. Overview of most cryptocurrencies.
2. Setting currencies for tracking.
3. Setting a date for the bot to send you data in messages.

Usage
------
To the use you need to open telegram bot and start it:

`https://t.me/cryptotracker_official_bot`



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
~~~~~~~~~
The very first button that activates the bot. It also outputs a greeting.

``/orders``
~~~~~~~~~~
Shows confirmation of orders.

``/help``
~~~~~~~~
Shows current moderators who can help you.

``/clear``
~~~~~~
This command clears the current order and back you to welcome message.

``/remove``
~~~~~~~~~~
Removes all your orders for tracking.



For developers
---------------


Environment variables
~~~~~~~~~~~~~~~~~~~~~~
To make your own bot first create `.env` file and fill data:

::

  #.env
  KEY=""
  BOT_KEY=""
  DB_PORT=""
  DB_HOST=""
  DB_USER=""
  DB_NAME=""
  DB_PASS=""


Dependencies
~~~~~~~~~~~~
The next step is to install dependencies

::

  #terminal
  poetry shell
  poetry install


Start
~~~~~~
Final step is start your bot following command

:: 

  #terminal
  python3 bot/bot.py



About
---------
- Main author: `IvanIsak2000 <https://github.com/IvanIsak2000>`_. Also known as Ivan Isakharov.
- Tracking issue: You can see the current `issues <https://github.com/IvanIsak2000/CryptoTracker/issues/>`_  or create new issue `here <https://github.com/IvanIsak2000/CryptoTracker/issues/new>`_.
