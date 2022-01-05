cython 独立运行程序
===================


官方答疑
^^^^^^^^^^^^

https://github.com/cython/cython/wiki/FAQ#how-can-i-make-a-standalone-binary-from-a-python-program-using-cython


实操步骤
^^^^^^^^^^^^^

- cython 扩展文件

.. code-block:: python
    :name: cython示例
    :caption: t_x.pyx
    :linenos:

    # cython: language_level=3
    if __name__ == "__main__":
        print("Hello")


- 多阶段编译

.. code-block:: bash
    :name: cython 编译 t_x.pyx
    :caption: 编译
    :linenos:

    >>>cython  --embed t_x.pyx
    >>>gcc -I /usr/include/python3.10/ t_x.c -lpython3.10 -o t_x

- 执行

.. code-block:: bash
    :name: 执行输出
    :caption: 运行
    :linenos:

    >>>./t_x
    >>>Hello

