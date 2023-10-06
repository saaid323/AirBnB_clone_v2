# sets up your web servers for the deployment of web_static
exec { 'apt-update':
  command     => 'sudo apt-get update',
  provider    => shell,
  refreshonly => true,
}
package { 'nginx':
  ensure  => 'installed',
  require => Exec['apt-update'],
}
file { '/data/web_static/releases/test/':
  ensure => 'directory',
  before => File['/data/web_static/shared/'],
}
file { '/data/web_static/shared/':
  ensure => 'directory',
}
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => 'Static',
  require => File['/data/web_static/releases/test/'],
}
file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test',
  force  => true,
}

exec { 'set-ownership':
  command  => 'chown -R ubuntu:ubuntu /data/',
  provider => shell,
  require  => File['/data/web_static/current'],
}

file { '/etc/nginx/sites-enabled/default':
  content => "server {
    listen 80 default_server;
    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
    }

    location / {
        try_files \$uri \$uri/ =404;
    }
}",
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-enabled/default'],
}
