#!/bin/bash

#creates an entirely new config file

file { '/root/.ssh/config':
  ensure => present,
  owner => 'root',
  group => '0600',
  content => "Host *\n passwordAuthentication no\n identityFile ~/.ssh/school\n",
}