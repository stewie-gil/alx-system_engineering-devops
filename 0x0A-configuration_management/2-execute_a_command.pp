#Kills the killme now process

exec {'killmenow':
command => 'pkill killmenow',
path => '/usr/local/bin/:/usr/bin:/bin/',
}