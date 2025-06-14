FROM netboxcommunity/netbox:latest-ldap

COPY ./phonebox_plugin /source/phonebox_plugin/phonebox_plugin/
COPY ./setup.py /source/phonebox_plugin/
COPY ./MANIFEST.in /source/phonebox_plugin/
COPY ./README.md /source/phonebox_plugin/
RUN /usr/local/bin/uv pip install --no-cache-dir /source/phonebox_plugin/
