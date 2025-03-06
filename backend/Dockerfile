# syntax=docker/dockerfile:1
ARG PLONE_VERSION=6.1.0
FROM plone/server-builder:${PLONE_VERSION} AS builder

WORKDIR /app


# Add local code
COPY scripts/ scripts/
COPY . src

# Install local requirements and pre-compile mo files
RUN <<EOT
    set -e
    sed -i 's/plone.autoinclude==1.0.1/plone.autoinclude==2.0.0/g' /app/constraints.txt
    bin/pip install uv hatch hatchling wheel
    cd /app/src
    ../bin/hatch build
    cd /app
    bin/uv pip install /app/src/dist/*.whl -c /app/constraints.txt
    bin/python /compile_mo.py
    rm -Rf src
EOT

FROM plone/server-prod-config:${PLONE_VERSION}

LABEL maintainer="Plone Foundation <admins@plone.org>" \
      org.label-schema.name="2025.ploneconf.org-backend" \
      org.label-schema.description="Plone Conference 2025 backend image." \
      org.label-schema.vendor="Plone Foundation"

# Copy /app from builder
COPY --from=builder /app /app

RUN <<EOT
    set -e
    ln -s /data /app/var
EOT
