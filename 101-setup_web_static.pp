# sets up your web servers for the deployment of web_static
package { 'inginx':
  ensure   => 'present',
  provider => 'apt'
} ->
file { '/data':
  ensure  => 'directory'
} ->
file { '/data/web_static':
  ensure => 'directory'
} ->
file { '/data/web_static/releases':
  ensure => 'directory'
} ->
file { '/data/web_static/releases/test':
  ensure => 'directory'
} ->
file { '/data/web_static/shared':
  ensure => 'directory'
} ->
file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "Hello, web_static!/n"
} ->
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
} ->
exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => 's|server_name _;|server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}|'
} ->
exec { 'nginx restart':
  path => '/etc/init.d/'
}
