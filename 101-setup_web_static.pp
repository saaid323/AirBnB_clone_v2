# sets up your web servers for the deployment of web_static

exec {'apt':
  command => '/usr/bin/apt-get update',
} ->
package { 'nginx':
  ensure => installed,
} ->
exec { 'folders':
  command => '/usr/bin/mkdir -p "/data/web_static/releases/test/" "/data/web_static/shared/"',
} ->
exec { 'msg':
  command => '/usr/bin/echo "Hi!" | sudo tee /data/web_static/releases/test/index.html > /dev/null',
} ->
exec { 'remove':
  command => '/usr/bin/rm -rf /data/web_static/current',
} ->
exec { 'link':
  command => '/usr/bin/ln -s /data/web_static/releases/test/ /data/web_static/current',
} ->
exec { 'ownership':
  command => '/usr/bin/chown -R ubuntu:ubuntu /data/',
} ->
exec { 'static':
  command => 'sudo sed -i "/^server {/a \ \n\tlocation \/hbnb_static {alias /data/web_static/current/;index index.html;}" /etc/nginx/sites-enabled/default',
  provider => shell,
} ->
exec { 'restart':
  command => '/usr/sbin/service nginx restart',
}
