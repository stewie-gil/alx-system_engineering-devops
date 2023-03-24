#Kills the killme now process

exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}