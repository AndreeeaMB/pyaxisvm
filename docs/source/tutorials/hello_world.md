# Hello World Example

This document is for those who are new to Python, but are willing to
do what is takes to learn it. It helps you to get going, set up a proven development enviroment and make your first steps. It also contains links to several useful references and learning materials, so you can bring your skills to the next level.

What do you gain?

* You can automate the boring stuff by wrapping up repetitive tasks into Python scripts. If you follow best practices, you can even create parametric, reusable macros.
* Not every strawberry ends up in Jogobella. Likewise, if you need domain specific functionality (which probably does not affect a lot of users), the Python ecosystem provides the batteries to customize your workflow.
* You can work with the latest and greatest. As of now, Python is the primary choice for data science applications including ML and AI, and the different distribution systems like PyPI or Conda are rich in libraries with bleeding-edge solutions. You can write high-performance, production-ready Python extensions with breeze.

## Installation

### Install Python

Go and wisit [http:\\python.org](https://www.python.org/) and download a version >= 3.6 and <3.10. We suggest to prioritize majority here, and stay below the curve a bit, except if you really are doing some bleeding edge stuff related the core funtionalities of Python as a language. In other cases, it is suggested to stay 2 major versions behing the latest distribution. If you already have an installed version compatible with the previous statements of this paragraph, then it should do the job. As of now, the suggested version is 3.8.

### Register AxisVM's Type Library

If this is not your first time using **AxisVM** through a COM interface on your machine, you should already have a registered type library and you can skip this step. Otherwise, follow the instructions at the beginning of the ***AxisVM API Reference Guide***.

### Create a Virtual Enviroment

It's optional, but hihgly recommended to create a dedicated virtual enviroment at all times to avoid conflicts with your other projects. Create a folder, open a command shell in that folder and use the following command

```console
>>> python -m venv venv_name
```

Once the enviroment is created, activate it via typing

```console
>>> .\venv_name\Scripts\activate
```

### Install PyAxisVM

The **AxisVM** python package can be installed (either in a virtual enviroment or globally) from PyPI using `pip` on Python >= 3.6:

```console
>>> pip install axisvm
```

## Hello World

To test your installation, start a new Python session in a terminal and execute the following code line by line.

```python
from axisvm.com.client import start_AxisVM
axapp = start_AxisVM(visible=True)
axapp.BringToFront()
```

## Recommendations

### Integrated Development Enviroments

If you plan to develop complex workflows, we suggest you to use Microsoft's *Visual Studio Code* to edit your code. It's a totally free and open-source IDE with excellent support for Jupyter Notebooks and a great developer community. Good alternatives are *PyCharm*, *Atom* and *Spyder*. 

For those who are familiar with *Matlab*, *Spyder* may be a good option as it offers similar look and feel. The suggested way of consumption here is to build it from source after cloning the project from GitHub.

## Useful Resources
