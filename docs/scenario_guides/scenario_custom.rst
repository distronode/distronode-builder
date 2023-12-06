.. _custom_usage:

Building EEs with environment variables for Galaxy configuration
================================================================

Distronode Builder version 3 schema allows users to perform complex scenarios
such as specifying custom Galaxy configurations.
You can use this approach to pass sensitive information, such as authentication tokens,
into the EE build without leaking them into the final EE image.

In the example below, we will take a look at

* Using Galaxy Server environment variables

.. literalinclude:: galaxy_ee.yml
   :language: yaml


You can provide environment variables such as ``DISTRONODE_GALAXY_SERVER_LIST``, ``DISTRONODE_GALAXY_SERVER_AUTOMATION_HUB_URL`` and ``DISTRONODE_GALAXY_SERVER_AUTOMATION_HUB_AUTH_URL`` using the ``ENV`` directive.
See `configuring Galaxy client <https://docs.distronode.khulnasoft.com/distronode/latest/galaxy/user_guide.html#configuring-the-distronode-galaxy-client>`_ for more details.

For security reason, we do not want to store sensitive information in this case `DISTRONODE_GALAXY_SERVER_AUTOMATION_HUB_TOKEN`.
You can use `ARG` directive in order to receive the sensitive information from the user as an input. `--build-args` can be used
to provide this information while invoking the `distronode-builder` command.

.. seealso::

   :ref:`Execution Environment Definition version 3 <version_3_format>`
      The detailed documentation about EE definition version 3
