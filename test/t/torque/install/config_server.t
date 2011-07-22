#!/usr/bin/perl
use strict;
use warnings;

use TestLibFinder;
use lib test_lib_loc();

#* This test creates the server_priv/nodes file

use CRI::Test;
plan('no_plan'); 
setDesc('Configure Torque Server');

my %hostnameCommand = runCommand("hostname -s","Getting hostname IP address");
my $hostname = $hostnameCommand{'STDOUT'};
chomp($hostname);

my $nodeArgs = $props->get_property('torque.node.args');

# Create/edit the server_priv/nodes file for the server
ok(open(NODES, ">".$props->get_property('Torque.Home.Dir') ."/server_priv/nodes"),'Opening Torque server config file') or die("Couldn't open torque server config file");
print NODES << "EOF";
$hostname $nodeArgs
EOF

ok(close NODES,'Closing Torque server config file') or die("Couldn't close torque server config file");

runCommand("grep $hostname ".  $props->get_property('Torque.Home.Dir') ."/server_priv/nodes") && die("Server config is not correct!");
