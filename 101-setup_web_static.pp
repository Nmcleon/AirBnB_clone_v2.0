# Configures a web server for deployment of web_static.

# Nginx configuration content
$nginx_conf = "
server {
    listen 80 default_server
    listen[::]: 80 default_server
    add_header X - Served - By ${hostname}
    root / var / www / html
    index  index.html index.htm

    # Configuration for serving static content
    location / hbnb_static {
        alias / data / web_static / current
        index index.html index.htm
    }

    # Redirect configuration
    location / redirect_me {
        return 301 http: // github.com / nmcleon /
    }

    # Error handling for 404
    error_page 404 / 404.html
    location / 404 {
        root / var / www / html
        internal
    }
}"

# Nginx package installation
package {'nginx':
         ensure = > 'present',
         provider = > 'apt',
         } ->

# Directory structure setup for deployment
file {'/data':
      ensure = > 'directory',
      } ->

file {'/data/web_static':
      ensure = > 'directory',
      } ->

file {'/data/web_static/releases':
      ensure = > 'directory',
      } ->

file {'/data/web_static/releases/test':
      ensure = > 'directory',
      } ->

file {'/data/web_static/shared':
      ensure = > 'directory',
      } ->

# Create a sample HTML file for testing purposes
file {'/data/web_static/releases/test/index.html':
      ensure = > 'present',
      content = > "Holberton School Puppet\n",
      } ->

# Create a symbolic link to the test release
file {'/data/web_static/current':
      ensure = > 'link',
      target = > '/data/web_static/releases/test',
      } ->

# Set ownership recursively for /data/ to ubuntu:ubuntu
exec {'chown -R ubuntu:ubuntu /data/':
      path = > ['/bin', '/usr/bin'],
      }

# Directory setup for default Nginx HTML pages
file {'/var/www':
      ensure = > 'directory',
      } ->

file {'/var/www/html':
      ensure = > 'directory',
      } ->

# Create default HTML files for Nginx
file {'/var/www/html/index.html':
      ensure = > 'present',
      content = > "Holberton School Nginx\n",
      } ->

file {'/var/www/html/404.html':
      ensure = > 'present',
      content = > "Ceci n'est pas une page\n",
      } ->

# Nginx configuration file setup
file {'/etc/nginx/sites-available/default':
      ensure = > 'present',
      content = > $nginx_conf,
      } ->

# Restart Nginx service for changes to take effect
exec {'nginx restart':
      path = > '/etc/init.d/',
      }
