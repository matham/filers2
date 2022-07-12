.. _install-filers2:

*************
Installation
*************

Filers2 can be found at https://github.com/matham/filers2. The following instructions is to install Filers2 from source.
You can find a compiled Filers2 executable for Windows on the
`release page <https://github.com/matham/filers2/releases>`_. To find the executable for the latest development
version of Filers2, download it from the `last action <https://github.com/matham/filers2/actions>`_ run.

Dependencies installation on Ubuntu
-----------------------------------

Following is a step by step example installation of Filers2 dependencies on Ubunutu 18.04.

Install the apt dependencies
****************************

* ``sudo apt update``.
* ``sudo apt install python3 python3-dev python3-pip``.

Make a virtual env for the project
**********************************

We'll make the virtual env in home:

* Install update pip/virtualenv ``python3 -m pip install --upgrade --user pip virtualenv``.
* ``cd ~``.
* Make the virtualenv ``python3 -m virtualenv filers2_venv``.
* Activate it ``source filers2_venv/bin/activate``. You'll have to do this every time you start a new terminal.

Install manual python dependencies
**********************************

* If using a **Flir camera**, on linux we must manually install its libraries

  * Get it from `here <https://www.flir.com/products/flycapture-sdk>`_, extract it and install by running ``install_flycapture.sh``.
  * Figure out your python version, find the appropriate linux wheel of the last release
    `here <https://github.com/matham/pyflycap2/releases>`_ and install e.g. with
    ``pip install https://github.com/matham/pyflycap2/releases/download/v0.3.0/pyflycap2-0.3.0-cp36-cp36m-linux_x86_64.whl``.
  * If successful, you should be able to run
    ``python3 -c 'from pyflycap2.interface import CameraContext; cc = CameraContext(); cc.rescan_bus(); print(cc.get_gige_cams())'``
    and it'll print a list of the serial numbers of all the connected cameras.

Dependencies installation on Windows
------------------------------------

Following is a step by step example installation of Filers2 dependencies on Windows 10.

Make a virtual env for the project
**********************************

Starting with Python and git available on the terminal, we'll first make the virtual env in the home
directory. The terminal should be in the home directory

* Install update pip/virtualenv ``python -m pip install --upgrade pip virtualenv``.
* Make the virtualenv ``python -m virtualenv filers2_venv``.
* Activate it ``filers2_venv\Scripts\activate``. You'll have to do this every time you start a new terminal.

Install manual python dependencies
**********************************

* If using a **Flir camera** install with ``pip install rotpy``.

  * If successful, you should be able to run
    ``python -c "from pyflycap2.interface import CameraContext; cc = CameraContext(); cc.rescan_bus(); print(cc.get_gige_cams())"``
    and it'll print a list of the serial numbers of all the connected cameras.
* If using a **Thor camera** install with ``pip install thorcam``.

Install Filers2
---------------

With the dependencies installed, you can simply install filter2 with::

    pip install filers2

Once installed, filers2 can be run either with the ``filers2`` command or by directly running
``python filers2/run_app.py``.
