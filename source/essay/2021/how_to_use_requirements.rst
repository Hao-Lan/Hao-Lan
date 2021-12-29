如何使用 `requirements.txt`
===============================

==============  =============
 Create
 Last Update     2021-12-29
==============  =============



`pip` 自带的 `-f` 参数，可以让我们很容易从零开始，搭建开发环境。

自动生成
-----------

当开发环境比较简单且单一时，如：

- 操作系统(开发和部署)都是 `windows` 或者 `linux`
- `python` 版本都是同一个，例如 `python:3.6` 或者 `python:3.9`

.. code-block:: bash
    :name: freeze
    :caption: freeze
    :linenos:

    pip freeze > requirements.txt

此种操作，会将开发环境(通常也是虚拟环境)中的所有依赖给存放进去。

手动生成
----------

如前面自动生成所述操作，不难看出，他是存在一些问题的：

- 开发环境和部署环境所需安装库种类不同

    比如开发环境通常需要提供 `pytest` 和 `sphinx` 这类工具库，而部署环境往往不需要。此时表现出来，开发环境所需要的库多于部署库。

- `windows` 和 `linux` 两种平台中，依赖库种类不同

    以 `django` 开发和部署为例。

    在 `linux` 的部署过程中，需要 `uwsgi` 或者 `uvicorn` 这类的部署工具。此时表现出来，部署环境需要的库多于开发环境。

    类推出去，也有可能一个库，它在 `windows` 和 `linux` 下的依赖不同，导致 `freeze` 冻结出来的环境，并不通用。


- 公司内部代码仓库中库引入

    冻结产生的依赖， `pip` 在安装时，会首先从官网中下载，然后会在我们为其配置的镜像网站中查找。

    但有时候，我们希望能够以 `git` 的形式，来安装一个内部仓库中维护的依赖。

    因为维护一个私有的 `PYPI` 新的成本。

基于种种原因，我们需要手动编写 `requirements.txt` 文件，甚至于，我们需要能编写逻辑判断多种多样的依赖文件。

记录依赖文件写法
-----------------

此处，每一行都表示依赖文件中的行。且仅仅用于记录一些特定用法，并未包含，将来也不会包含所有的示例。

- 依赖别的依赖文件

::

    -r xx/xxx/requirement.txt

- 多条件限制

::

    tornado;python_version>"2.7" and sys_platform=="win32"

- 引入 `git`

::

    git+https://xxxTokenxxx@github.com/tornadoweb/tornado.git@v6.1.0;python_version>"2.7" and sys_platform=="win32"


参考链接
-----------------

https://setuptools.pypa.io/en/latest/pkg_resources.html#requirement-objects

https://pip.pypa.io/en/stable/reference/requirements-file-format/?highlight=requirements

https://pip.pypa.io/en/stable/cli/pip_install/

https://www.python.org/dev/peps/pep-0440/#version-specifiers
