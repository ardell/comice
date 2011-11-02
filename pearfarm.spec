<?php

$spec = Pearfarm_PackageSpec::create(array(Pearfarm_PackageSpec::OPT_BASEDIR => dirname(__FILE__)))
             ->setName('comice')
             ->setChannel('pearfarm.pearfarm.org')
             ->setSummary("A port of ruby's bundler for pear/php.")
             ->setDescription("A port of ruby's bundler for pear/php.")
             ->setReleaseVersion('0.0.5')
             ->setReleaseStability('alpha')
             ->setApiVersion('0.0.1')
             ->setApiStability('alpha')
             ->setLicense(Pearfarm_PackageSpec::LICENSE_MIT)
             ->setNotes('Initial release.')
             ->addMaintainer('lead', 'Jason Ardell', 'ardell', 'ardell@gmail.com')
             ->addMaintainer('lead', 'Alan Pinstein', 'apinstein', 'apinstein@mac.com')
             ->addGitFiles()
             ->addExecutable('comice')
             ->addPackageDependency('climax', 'apinstein.pearfarm.org')
             ;
