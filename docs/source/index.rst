PyAxisVM - The official python package of **AxisVM**
====================================================


The **PyAxisVM** project offers a high-level interface to **AxisVM**, 
making its operations available directly from Python. It builds on top of 
Microsoft's COM technology and supports all the features of the original 
**AxisVM** COM type library, making you able to

* build, manipulate and analyse **AxisVM** models

* find better solutions with iterative methods

* combine the power of **AxisVM** with third-party Python libraries

* build extension modules

On top of that, **PyAxisVM** enhances the type library with Python's slicing 
mechanism, context management and more, that enables writing clean, concise, 
and readable code.

>>> from axisvm.com.client import start_AxisVM
>>> axapp = start_AxisVM(visible=True)

Contents
--------

.. toctree::
   :maxdepth: 3

   getting_started   
   tips_and_tricks
   api_python
   api_com
   
   

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`



