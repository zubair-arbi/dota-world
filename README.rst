Dota World App
==============

This repository contains application for providing helpful features for ``Dota 2`` game players. It's main feature is
to provide best hero suggestions in response to opponent team's heros.

This is an open source project. Feel free to contribute.

How do I run this project?
==========================

The ``dota-world`` project includes all the basic configurations necessary to get you starting.

**Setup Instructions:**

1. Create a python 3 virtual environment
.. code-block:: bash
    python3 -m venv dota_env

    source dota_env/bin/activate

2. Clone this project:
.. code-block:: bash
    git clone https://github.com/zubair-arbi/dota-world.git
    
    cd dota-world/

3. Install requirements:
.. code-block:: bash
    make requirements

4. Create database and run migrations:
.. code-block:: bash
    make migrate

5. Serve the dota-world app on localhost at port 4444
.. code-block:: bash
    make serve
