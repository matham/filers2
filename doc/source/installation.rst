.. _install-filers2:

*************
Installation
*************

Filers2 can be found at https://github.com/matham/filers2. The following instructions is to install Filers2 from source. You can find a compiled Filers2 executable for Windows on the `release page <https://github.com/matham/filers2/releases>`_. To find the executable for the latest development version of Filers2, download it from the `last action <https://github.com/matham/filers2/actions>`_ run.

Dependencies
-------------

Following are the overall major dependencies. For exact instructions on how to install
Filers2 see below.

* Python 3.6+.
* Kivy 2.0.0+ and Kivy-garden widgets for the GUI.
* ffpyplayer for media control.
* base_kivy_app provides a basic Kivy app structure.
* cpl_media provides control over the various cameras.
* Optional dependencies that should be installed depending on the cameras to be used:
  * pyflycap2 if using Point Gray cameras.
  * thorcam if using Thor cameras (only supported on Windows).

Dependencies installation on Ubuntu
-----------------------------------

Following is a step by step example installation of Filers2 on Ubunutu 18.04.

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

* Install current **kivy** master

  * Install apt dependencies: ``sudo apt install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev zlib1g-dev``.
  * Install kivy: ``pip install https://github.com/kivy/kivy/archive/master.zip`` - it'll take a couple of minutes.
* If using a **PointGray camera**, on linux we must manually install its libraries

  * Get it from `here <https://www.flir.com/products/flycapture-sdk>`_, extract it and install by running ``install_flycapture.sh``.
  * Figure out your python version, find the appropriate linux wheel of the last release
    `here <https://github.com/matham/pyflycap2/releases>`_ and install e.g. with
    ``pip install https://github.com/matham/pyflycap2/releases/download/v0.3.0/pyflycap2-0.3.0-cp36-cp36m-linux_x86_64.whl``.
  * If successful, you should be able to run
    ``python3 -c 'from pyflycap2.interface import CameraContext; cc = CameraContext(); cc.rescan_bus(); print(cc.get_gige_cams())'``
    and it'll print a list of the serial numbers of all the connected cameras.

Dependencies installation on Windows
------------------------------------

Following is a step by step example installation of Filers2 on Windows 10.

Make a virtual env for the project
**********************************

Starting with Python and git available on the terminal, we'll first make the virtual env in the home
directory. The terminal should be in the home directory

* Install update pip/virtualenv ``python -m pip install --upgrade pip virtualenv``.
* Make the virtualenv ``python -m virtualenv filers2_venv``.
* Activate it ``filers2_venv\Scripts\activate``. You'll have to do this every time you start a new terminal.

Install manual python dependencies
**********************************

* Install current **kivy** master with ``pip install kivy[base] kivy_examples --pre --extra-index-url https://kivy.org/downloads/simple/``.
* If using a **PointGray camera** install with ``pip install pyflycap2``.

  * If successful, you should be able to run
    ``python -c "from pyflycap2.interface import CameraContext; cc = CameraContext(); cc.rescan_bus(); print(cc.get_gige_cams())"``
    and it'll print a list of the serial numbers of all the connected cameras.
* If using a **Thor camera** install with ``pip install thorcam``.

Install Filers2
---------------

To get the latest versions, manually install ``base_kivy_app`` and ``cpl_media`` from github with::

    pip install https://github.com/matham/base_kivy_app/archive/master.zip
    pip install https://github.com/matham/cpl_media/archive/master.zip

To use the latest release (if one has been made) instead, install with::

    pip install base_kivy_app cpl_media

Filers2 can be either cloned locally and installed, or simply installed (e.g. if it won't be edited in any way).
To simply install it, just do::

    pip install https://github.com/matham/filers2/archive/master.zip

Otherwise, clone Filers2 to the ``filers2`` directory with ``git clone https://github.com/matham/filers2.git``, followed by ``pip install -e filers2``.

Once installed, you can start Filers2 by simply typing ``filers2`` in the terminal.
Or, you can run it directly using ``python -m filers2.run_app``. Or from the
Filers2 directory (if cloned), just run ``python filers2/run_app.py``.
