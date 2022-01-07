Dockerfile not cache
=======================

- Use Cache

.. code-block:: Dockerfile
    :name: use cache dockerfile
    :caption: UseCacheDockerfile
    :linenos:

    FROM something
    RUN apt-get update && apt-get install foo bar baz ......
    CMD xxxx

.. code-block:: bash
    :name: docker build use cache
    :caption: docker build (use cache)
    :linenos:

    docker build .

- No Cache

.. code-block:: bash
    :name: docker build no cache
    :caption: docker build (no cache)
    :linenos:

    docker build .  --no-cache=true

- Part No Cache

If use two dockerfiles:

.. code-block:: bash
    :name: docker build part no cache
    :caption: docker build (part no cache)
    :linenos:

    docker build  -f xxxDockerfile .
    docker build  -f xxxDockerfile --no-cache=true .


If use one dockerfile:

.. code-block:: Dockerfile
    :name: use part cache dockerfile
    :caption: Use Part Cache Dockerfile
    :linenos:

    FROM something
    RUN apt-get update && apt-get install foo bar baz ......
    ARG CACHE_DATA=2021-01-01
    # Start now,no cache
    CMD xxxx

.. code-block:: bash
    :name: docker build use cache, use one dockerfile
    :caption: docker build (one dockerfile)
    :linenos:

    docker build  --build-arg CACHE_DATA="$(date +%Y-%m-%d:%H:%M:%S)"


References and Further Reading
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Availablity to have --no-cache=true for a single instruction in Dockerfile #22832 <https://github.com/moby/moby/issues/22832>`_
