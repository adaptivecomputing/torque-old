#!/usr/bin/perl

use TestLibFinder;
use lib test_lib_loc();
 
use strict;
use warnings;
use CRI::Test;
plan('no_plan');
setDesc('Make Clean on Torque');

ok(-d $props->get_property('torque.build.dir'),"Checking if torque build dir exists")
    or die "Torque build dir doesn't exist";
ok(chdir $props->get_property('torque.build.dir'),"Changing to torque build dir")
    or die('Couldn\'t change to Torque build dir'); 

# Run make clean
ok(runCommand("make clean") == 0, "make clean on Torque")
    or die "Couldn't make clean Torque: $!"; 
