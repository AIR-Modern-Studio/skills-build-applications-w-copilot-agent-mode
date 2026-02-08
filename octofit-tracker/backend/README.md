# OctoFit Tracker Backend

Django REST API backend for the OctoFit Tracker application.

## Environment Variables

The following environment variables can be used to configure the application:

### Required for Production

- **`DJANGO_SECRET_KEY`**: Secret key for Django. Must be set to a secure random string in production.
  - Default (development only): `'django-insecure-6jy92-q_0l8e*asyj97%smtcrrz0u*=y6r@l5!ykmk@5oq1g@d'`
  - Example: `export DJANGO_SECRET_KEY='your-very-secure-random-secret-key-here'`

- **`DJANGO_DEBUG`**: Enable/disable debug mode.
  - Default: `False` (production-safe)
  - Set to `'true'`, `'1'`, `'t'`, or `'yes'` to enable debug mode (case-insensitive)
  - Example: `export DJANGO_DEBUG='true'` (for local development only)

### Optional

- **`CODESPACE_NAME`**: Automatically set by GitHub Codespaces. Used to configure allowed hosts.

## Local Development

For local development, you can enable debug mode:

```bash
export DJANGO_DEBUG='true'
python manage.py runserver
```

## Production Deployment

For production, ensure these environment variables are properly set:

```bash
# Generate a secure secret key
export DJANGO_SECRET_KEY='your-secure-random-key-here'

# DEBUG defaults to False, so no need to set it explicitly
# But you can explicitly set it to ensure it's disabled:
export DJANGO_DEBUG='false'

python manage.py runserver
```

⚠️ **Security Warning**: Never commit the production `SECRET_KEY` to version control!
